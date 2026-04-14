#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
from pathlib import Path

from refinery.lib.inno.archive import InnoArchive

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_SUPPORT_ROOT = ROOT / "runtime_support"

INSTALLERS = {
    "acheron": ROOT / "Acheron_Setup_Win64_c7f9da5e7a33a154d737fdffa9887c9ba5033f67.exe",
    "mondo": ROOT / "Mondo_Setup_Win64_d41532fd318d2606311f9b169dedecb482f24507.exe",
}

INCLUDE_RULES = {
    "acheron": (
        "data/{app}/build_info.txt",
        "data/{app}/botodata/",
        "data/{app}/lib/asphodel/lib64/",
        "data/{app}/lib/setproctitle._setproctitle.cp311-win_amd64.pyd",
    ),
    "mondo": (
        "data/{app}/build_info.txt",
        "data/{app}/lib/asphodel/lib64/",
    ),
}


def should_extract(archive_path: str, rules: tuple[str, ...]) -> bool:
    for rule in rules:
        if rule.endswith("/"):
            if archive_path.startswith(rule):
                return True
        elif archive_path == rule:
            return True
    return False


def extract_assets(app: str) -> int:
    archive = InnoArchive(bytearray(INSTALLERS[app].read_bytes()))
    out_root = RUNTIME_SUPPORT_ROOT / app
    out_root.mkdir(parents=True, exist_ok=True)
    count = 0
    for file in archive.files:
        if file.dupe or not should_extract(file.path, INCLUDE_RULES[app]):
            continue
        relative = file.path.removeprefix("data/{app}/")
        out_path = out_root / relative
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(archive.read_file_and_check(file))
        count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract runtime DLLs and support assets from the original installers.")
    parser.add_argument("apps", nargs="+", choices=sorted(INSTALLERS))
    args = parser.parse_args()

    for app in args.apps:
        count = extract_assets(app)
        print(f"{app}: extracted {count} files into {RUNTIME_SUPPORT_ROOT / app}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
