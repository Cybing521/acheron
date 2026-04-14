# Source Generated with Decompyle++
# File: tmptly4tmtg.marshal (Python 3.11)


def __init__(self = None, setting_name = None, default = None):
    self.setting_name = setting_name
    self.default = default


def __get__(self = None, obj = None, objtype = None):
    return read_int_setting(obj.settings, self.setting_name, self.default)


def __set__(self = None, obj = None, val = None):
    obj.settings.setValue(self.setting_name, val)

