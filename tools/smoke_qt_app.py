#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import bootstrap_recovered_app as bootstrap


def _patch_message_boxes(QtWidgets) -> None:
    def _log_message(kind: str):
        def _handler(parent, title, text, *args, **kwargs):
            payload = {
                "event": "message_box",
                "kind": kind,
                "title": str(title),
                "text": str(text),
            }
            print(json.dumps(payload, ensure_ascii=False), flush=True)
            return QtWidgets.QMessageBox.StandardButton.Ok

        return staticmethod(_handler)

    QtWidgets.QMessageBox.information = _log_message("information")
    QtWidgets.QMessageBox.warning = _log_message("warning")
    QtWidgets.QMessageBox.critical = _log_message("critical")
    QtWidgets.QMessageBox.question = _log_message("question")


def _patch_exec(QtCore, QtWidgets, timeout_ms: int, snapshot_delay_ms: int) -> None:
    original_exec = QtWidgets.QApplication.exec

    def patched_exec(self):
        def emit_snapshot() -> None:
            widgets = []
            for widget in self.topLevelWidgets():
                widgets.append(
                    {
                        "class": type(widget).__name__,
                        "title": widget.windowTitle(),
                        "visible": widget.isVisible(),
                        "enabled": widget.isEnabled(),
                    }
                )
            payload = {
                "event": "snapshot",
                "widget_count": len(widgets),
                "widgets": widgets,
            }
            print(json.dumps(payload, ensure_ascii=False), flush=True)

        QtCore.QTimer.singleShot(snapshot_delay_ms, emit_snapshot)
        QtCore.QTimer.singleShot(timeout_ms, self.quit)
        return original_exec()

    QtWidgets.QApplication.exec = patched_exec


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test a recovered Qt app by auto-quitting its event loop.")
    parser.add_argument("app", choices=sorted(bootstrap.ENTRY_MODULES))
    parser.add_argument("--module", help="Optional module override.")
    parser.add_argument("--timeout-ms", type=int, default=2000)
    parser.add_argument("--snapshot-delay-ms", type=int, default=500)
    args = parser.parse_args()

    target_module = args.module or bootstrap.ENTRY_MODULES[args.app]
    paths = bootstrap.bootstrap(args.app, target_module)
    from PySide6 import QtCore, QtWidgets

    _patch_message_boxes(QtWidgets)
    _patch_exec(QtCore, QtWidgets, args.timeout_ms, args.snapshot_delay_ms)
    print(
        json.dumps(
            {
                "event": "bootstrap",
                "app": args.app,
                "module": target_module,
                "paths": [str(path) for path in paths],
            },
            ensure_ascii=False,
        ),
        flush=True,
    )

    try:
        module = importlib.import_module(target_module)
        print(json.dumps({"event": "imported", "module": target_module}), flush=True)
        result = module.main()
        print(json.dumps({"event": "exit", "result": result}), flush=True)
        return int(result or 0)
    except BaseException as exc:
        print(
            json.dumps(
                {
                    "event": "exception",
                    "type": type(exc).__name__,
                    "message": str(exc),
                    "traceback": traceback.format_exc(),
                },
                ensure_ascii=False,
            ),
            flush=True,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
