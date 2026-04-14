# Source Generated with Decompyle++
# File: tmpvhtbbwmu.marshal (Python 3.11)


def __init__(self = None, setting_name = None, default = None):
    self.setting_name = setting_name
    self.default = default


def __get__(self = None, obj = None, objtype = None):
    return read_bool_setting(obj.settings, self.setting_name, self.default)


def __set__(self = None, obj = None, value = None):
    write_bool_setting(obj.settings, self.setting_name, value)

