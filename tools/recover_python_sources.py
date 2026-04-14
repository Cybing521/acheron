#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import json
import marshal
import re
import shutil
import subprocess
import tempfile
import types
import zipfile
from dataclasses import dataclass
from pathlib import Path

from refinery.lib.inno.archive import InnoArchive

PYC_HEADER_SIZE = 16
ROOT = Path(__file__).resolve().parents[1]
PYCDC = Path("/tmp/pycdc/build/pycdc")

ACHERON_INSTALLER = ROOT / "Acheron_Setup_Win64_c7f9da5e7a33a154d737fdffa9887c9ba5033f67.exe"
ACHERON_LIBRARY_ZIP = ROOT / "analysis" / "acheron" / "library.zip"
MONDO_INSTALLER = ROOT / "Mondo_Setup_Win64_d41532fd318d2606311f9b169dedecb482f24507.exe"
MONDO_LIBRARY_ZIP = ROOT / "analysis" / "mondo" / "library.zip"

RECOVERED_ROOT = ROOT / "recovered"
PYC_ROOT = RECOVERED_ROOT / "pyc"
SRC_ROOT = RECOVERED_ROOT / "src"
SNIPPET_ROOT = RECOVERED_ROOT / "snippets"
MANIFEST_PATH = RECOVERED_ROOT / "manifest.json"

QUALNAME_CLEAN_RE = re.compile(r"[^A-Za-z0-9_.-]+")


@dataclass
class DecompiledFile:
    package: str
    pyc_path: Path
    source_path: Path
    snippet_dir: Path
    source_size: int
    snippet_count: int
    stderr: str


def run(cmd: list[str], *, input_bytes: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        cmd,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def load_code(path: Path) -> types.CodeType:
    data = path.read_bytes()
    return marshal.loads(data[PYC_HEADER_SIZE:])


def iter_code_objects(code: types.CodeType) -> list[types.CodeType]:
    seen: set[int] = set()
    out: list[types.CodeType] = []

    def walk(obj: types.CodeType) -> None:
        if id(obj) in seen:
            return
        seen.add(id(obj))
        out.append(obj)
        for const in obj.co_consts:
            if isinstance(const, types.CodeType):
                walk(const)

    walk(code)
    return out


def sanitize_qualname(name: str) -> str:
    return QUALNAME_CLEAN_RE.sub("_", name).strip("._") or "code"


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def extract_from_installer(
    installer_path: Path,
    out_root: Path,
    prefixes: tuple[str, ...],
) -> list[Path]:
    archive = InnoArchive(bytearray(installer_path.read_bytes()))
    extracted: list[Path] = []
    for file in archive.files:
        if file.dupe or not file.path.endswith(".pyc"):
            continue
        if not any(file.path.startswith(prefix) for prefix in prefixes):
            continue
        relative = file.path.removeprefix("data/{app}/lib/")
        out_path = out_root / relative
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(archive.read_file_and_check(file))
        extracted.append(out_path)
    return extracted


def extract_from_zip(
    archive_path: Path,
    out_root: Path,
    prefixes: tuple[str, ...],
) -> list[Path]:
    extracted: list[Path] = []
    with zipfile.ZipFile(archive_path) as archive:
        for name in archive.namelist():
            if not name.endswith(".pyc"):
                continue
            if not any(name.startswith(prefix) for prefix in prefixes):
                continue
            out_path = out_root / name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(archive.read(name))
            extracted.append(out_path)
    return extracted


def extract_acheron() -> list[Path]:
    out_root = PYC_ROOT / "acheron"
    ensure_clean_dir(out_root)
    extracted = extract_from_installer(
        ACHERON_INSTALLER,
        out_root,
        (
            "data/{app}/lib/acheron/",
            "data/{app}/lib/asphodel/",
        ),
    )
    extracted.extend(
        extract_from_zip(
            ACHERON_LIBRARY_ZIP,
            out_root,
            (
                "hyperborea/",
                "setproctitle/",
            ),
        )
    )
    return sorted(extracted)


def extract_mondo() -> list[Path]:
    out_root = PYC_ROOT / "mondo"
    ensure_clean_dir(out_root)
    extracted = extract_from_zip(
        MONDO_LIBRARY_ZIP,
        out_root,
        (
            "mondo/",
            "hyperborea/",
        ),
    )
    extracted.extend(
        extract_from_installer(
            MONDO_INSTALLER,
            out_root,
            ("data/{app}/lib/asphodel/",),
        )
    )
    return sorted(extracted)


def decompile_module(package: str, pyc_path: Path) -> DecompiledFile:
    rel = pyc_path.relative_to(PYC_ROOT / package)
    source_path = SRC_ROOT / package / rel.with_suffix(".py")
    source_path.parent.mkdir(parents=True, exist_ok=True)

    result = run([str(PYCDC), str(pyc_path)])
    source_path.write_bytes(result.stdout)

    snippet_dir = SNIPPET_ROOT / package / rel.with_suffix("")
    snippet_dir.mkdir(parents=True, exist_ok=True)

    snippet_count = 0
    for code in iter_code_objects(load_code(pyc_path)):
        qualname = code.co_qualname or code.co_name or "code"
        snippet_name = sanitize_qualname(qualname)
        if snippet_name == "<module>":
            continue
        with tempfile.NamedTemporaryFile(suffix=".marshal", delete=False) as tmp:
            tmp.write(marshal.dumps(code))
            tmp_path = Path(tmp.name)
        try:
            snippet = run([str(PYCDC), "-c", "-v", "3.11", str(tmp_path)])
        finally:
            tmp_path.unlink(missing_ok=True)
        snippet_path = snippet_dir / f"{snippet_name}.py"
        snippet_path.write_bytes(snippet.stdout)
        snippet_count += 1

    return DecompiledFile(
        package=package,
        pyc_path=pyc_path,
        source_path=source_path,
        snippet_dir=snippet_dir,
        source_size=source_path.stat().st_size,
        snippet_count=snippet_count,
        stderr=result.stderr.decode("utf-8", "ignore"),
    )


def build_manifest(results: list[DecompiledFile]) -> None:
    payload = []
    for item in results:
        payload.append(
            {
                "package": item.package,
                "pyc_path": str(item.pyc_path.relative_to(ROOT)),
                "source_path": str(item.source_path.relative_to(ROOT)),
                "snippet_dir": str(item.snippet_dir.relative_to(ROOT)),
                "source_size": item.source_size,
                "snippet_count": item.snippet_count,
                "stderr": item.stderr,
            }
        )
    RECOVERED_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract and decompile Acheron / Mondo Python bytecode.")
    parser.add_argument(
        "--packages",
        nargs="+",
        choices=["acheron", "mondo"],
        default=["acheron", "mondo"],
        help="Packages to recover.",
    )
    parser.add_argument(
        "--skip-extract",
        action="store_true",
        help="Reuse already extracted .pyc files under recovered/pyc.",
    )
    args = parser.parse_args()

    RECOVERED_ROOT.mkdir(parents=True, exist_ok=True)
    ensure_clean_dir(SRC_ROOT)
    ensure_clean_dir(SNIPPET_ROOT)

    package_files: dict[str, list[Path]] = {}
    for package in args.packages:
        if args.skip_extract:
            package_root = PYC_ROOT / package
            package_files[package] = sorted(package_root.rglob("*.pyc"))
            continue
        if package == "acheron":
            package_files[package] = extract_acheron()
        elif package == "mondo":
            package_files[package] = extract_mondo()

    results: list[DecompiledFile] = []
    for package, files in package_files.items():
        for pyc_path in sorted(files):
            results.append(decompile_module(package, pyc_path))

    build_manifest(results)
    print(f"recovered_modules={len(results)} manifest={MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
