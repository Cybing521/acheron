# Source Generated with Decompyle++
# File: tmpeb0afn3z.marshal (Python 3.11)


def __init__(self = None, setting_name = None):
    self.setting_name = setting_name


def __get__(self = None, obj = None, objtype = None):
    s = obj.settings.value(self.setting_name)
# WARNING: Decompyle incomplete


def __set__(self = None, obj = None, val = None):
    obj.settings.setValue(self.setting_name, val.strip())

