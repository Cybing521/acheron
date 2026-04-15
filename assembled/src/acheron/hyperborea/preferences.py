# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

from typing import TypeVar, Union
from PySide6 import QtCore
T = TypeVar('T')

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def read_bool_setting(settings, setting_name, default):
    try:
        s = settings.value(setting_name)
        if s is not None:
            return int(s) != 0
        return default
    except ValueError:
        return default

def read_int_setting(settings, setting_name, default):
    try:
        s = settings.value(setting_name)
        if s is not None:
            return int(s)
        return default
    except ValueError:
        return default

def write_bool_setting(settings, setting_name, value):
    settings.setValue(setting_name, 1 if value else 0)
