#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from PySide6 import QtCore

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import bootstrap_recovered_app as bootstrap


def emit(event: str, **payload) -> None:
    message = {"event": event, **payload}
    print(json.dumps(message, ensure_ascii=False), flush=True)


def main() -> int:
    paths = bootstrap.bootstrap("acheron", "acheron.gui.__main__")
    emit("bootstrap", paths=[str(path) for path in paths])

    app = QtCore.QCoreApplication.instance() or QtCore.QCoreApplication([])

    from acheron.core.preferences import Preferences, create_empty_settings
    from acheron.core.dispatcher import Dispatcher
    from acheron.device_process.proxy import DeviceProxyManager

    create_empty_settings()
    preferences = Preferences()
    proxy_manager = DeviceProxyManager("acheron-device-backend-smoke")
    dispatcher = Dispatcher(proxy_manager, preferences, "acheron-calc-backend-smoke")
    emit("dispatcher_created")

    dispatcher.stop()
    emit("dispatcher_stopped")
    dispatcher.join()
    emit("dispatcher_joined")

    proxy_manager.stop()
    emit("proxy_stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
