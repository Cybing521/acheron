#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import importlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSEMBLED_SRC_ROOT = ROOT / "assembled" / "src"
RUNTIME_SUPPORT_ROOT = ROOT / "runtime_support"
QT_RUNTIME_ROOT = ROOT / "qt-runtime"

ENTRY_MODULES = {
    "acheron": "acheron.gui.__main__",
    "mondo": "mondo.__main__",
}

INNER_SUBDIRS = {
    "acheron": ["gui", "core", "device_process", "connectivity", "disk"],
    "mondo": [],
}


def build_sys_path(app: str) -> tuple[list[Path], list[Path]]:
    app_root = ASSEMBLED_SRC_ROOT / app
    inner_root = app_root / app
    base_paths: list[Path] = [app_root]
    legacy_paths: list[Path] = [inner_root]

    for package_name in ("asphodel", "hyperborea", "setproctitle"):
        package_dir = app_root / package_name
        if package_dir.exists():
            base_paths.append(package_dir)

    for subdir in INNER_SUBDIRS.get(app, []):
        candidate = inner_root / subdir
        if candidate.exists():
            legacy_paths.append(candidate)

    seen: set[Path] = set()
    ordered_base: list[Path] = []
    ordered_legacy: list[Path] = []

    for path in base_paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        ordered_base.append(resolved)

    for path in legacy_paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        ordered_legacy.append(resolved)

    return (ordered_base, ordered_legacy)


def configure_runtime_environment(app: str) -> None:
    runtime_root = RUNTIME_SUPPORT_ROOT / app
    botodata = runtime_root / "botodata"
    cacert = botodata / "cacert.pem"
    if botodata.exists() and "AWS_DATA_PATH" not in os.environ:
        os.environ["AWS_DATA_PATH"] = str(botodata)
    if cacert.exists() and "AWS_CA_BUNDLE" not in os.environ:
        os.environ["AWS_CA_BUNDLE"] = str(cacert)


def configure_qt_environment() -> None:
    try:
        import PySide6
    except ImportError:
        return

    qt_root = Path(PySide6.__file__).resolve().parent / "Qt"
    plugins_dir = qt_root / "plugins"
    platforms_dir = plugins_dir / "platforms"
    visible_plugins_dir = QT_RUNTIME_ROOT / "plugins"
    visible_platforms_dir = visible_plugins_dir / "platforms"

    plugin_root = plugins_dir
    platform_root = platforms_dir

    if sys.platform == "darwin" and visible_platforms_dir.exists():
        plugin_root = visible_plugins_dir
        platform_root = visible_platforms_dir

    if plugin_root.exists() and "QT_PLUGIN_PATH" not in os.environ:
        os.environ["QT_PLUGIN_PATH"] = str(plugin_root)
    if platform_root.exists() and "QT_QPA_PLATFORM_PLUGIN_PATH" not in os.environ:
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(platform_root)


def prepend_paths(paths: list[Path]) -> None:
    for path in reversed(paths):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))


def bootstrap(app: str, target_module: str) -> list[Path]:
    base_paths, legacy_paths = build_sys_path(app)
    prepend_paths(base_paths)
    configure_runtime_environment(app)
    configure_qt_environment()

    package_name = app
    if target_module == package_name or target_module.startswith(f"{package_name}."):
        importlib.import_module(package_name)

    prepend_paths(legacy_paths)
    return base_paths + legacy_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap the reconstructed Acheron or Mondo source tree.")
    parser.add_argument("app", choices=sorted(ENTRY_MODULES))
    parser.add_argument(
        "--module",
        help="Import this module instead of the default application entry module.",
    )
    parser.add_argument(
        "--probe-import",
        action="store_true",
        help="Only import the module and print the resolved sys.path entries.",
    )
    args = parser.parse_args()

    target_module = args.module or ENTRY_MODULES[args.app]
    paths = bootstrap(args.app, target_module)
    module = importlib.import_module(target_module)

    if args.probe_import:
        print(f"imported={target_module}")
        for path in paths:
            print(path)
        return 0

    entrypoint = getattr(module, "main")
    result = entrypoint()
    return int(result or 0)


if __name__ == "__main__":
    raise SystemExit(main())
