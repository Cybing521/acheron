# Source Generated with Decompyle++
# File: tmpcounym13.marshal (Python 3.11)

from collections import deque
import logging
import logging.handlers as logging
import threading
from typing import Any, Optional, Union
from PySide6 import QtCore
logger = logging.getLogger(__name__)
GUI_LOG_SIZE = 1000

class GUILogModel(QtCore.QAbstractListModel):
    pass
# WARNING: Decompyle incomplete

_models: dict[(str, GUILogModel)] = { }
_global_deque: deque[str] = deque(maxlen = GUI_LOG_SIZE)

class GUILogHandler(logging.Handler):
    pass
# WARNING: Decompyle incomplete


def get_log_list_model(serial_number = None):
    
    try:
        model = _models[serial_number]
    except KeyError:
        model = GUILogModel(_global_deque)
        _models[serial_number] = model

    return model

