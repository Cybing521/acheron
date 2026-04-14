# Source Generated with Decompyle++
# File: gui_log.pyc (Python 3.11)

from collections import deque
import logging
import logging.handlers
import threading
from typing import Any, Optional, Union
from PySide6 import QtCore
logger = logging.getLogger(__name__)
GUI_LOG_SIZE = 1000
_models: dict[str | None, "GUILogModel"] = {}
_global_deque: deque[str] = deque(maxlen=GUI_LOG_SIZE)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class GUILogModel(QtCore.QAbstractListModel):

    def __init__(self, global_deque):
        super().__init__()
        self.list = list(global_deque)
        self.deque = deque(maxlen=GUI_LOG_SIZE)
        self.lock = threading.Lock()

    def log_message(self, message):
        with self.lock:
            self.deque.append(message)

    def update_messages(self):
        with self.lock:
            new_messages = list(self.deque)
            if not new_messages:
                return None
            self.deque.clear()

        messages_len = len(new_messages)
        remove_count = len(self.list) + messages_len - GUI_LOG_SIZE
        if remove_count > 0:
            self.beginRemoveRows(QtCore.QModelIndex(), 0, remove_count - 1)
            del self.list[:remove_count]
            self.endRemoveRows()

        insert_start = len(self.list)
        insert_end = insert_start + messages_len - 1
        self.beginInsertRows(QtCore.QModelIndex(), insert_start, insert_end)
        self.list.extend(new_messages)
        self.endInsertRows()
        return None

    def rowCount(self, parent):
        return len(self.list)

    def data(self, index, role):
        row = index.row()
        if row < 0 or row >= len(self.list):
            return ""
        if role in (
            QtCore.Qt.ItemDataRole.DisplayRole,
            QtCore.Qt.ItemDataRole.EditRole,
        ):
            return self.list[row]
        return None

class GUILogHandler(logging.Handler):

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_cb)
        self.timer.start(20)

    def emit(self, record):
        message = self.format(record)
        try:
            serial_number = record.serial_number
            model = _models[serial_number]
        except KeyError:
            serial_number = getattr(record, "serial_number", None)
            model = GUILogModel(_global_deque)
            _models[serial_number] = model
        except AttributeError:
            _global_deque.append(message)
            for model in _models.values():
                model.log_message(message)
            return None

        model.log_message(message)
        return None

    def timer_cb(self):
        for serial_number, model in _models.items():
            model.update_messages()

def get_log_list_model(serial_number):
    try:
        model = _models[serial_number]
    except KeyError:
        model = GUILogModel(_global_deque)
        _models[serial_number] = model

    return model
