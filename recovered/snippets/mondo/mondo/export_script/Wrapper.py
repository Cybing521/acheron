# Source Generated with Decompyle++
# File: tmpitqunor5.marshal (Python 3.11)


def __init__(self = None, wrapped = None, name = None, cmd_list = ('cmd_list', CommandList)):
    self._wrapped = wrapped
    self._name = name
    self._cmd_list = cmd_list


def __getattribute__(self, attr):
    pass
# WARNING: Decompyle incomplete


def __getitem__(self, key):
    wrapped = object.__getattribute__(self, '_wrapped')
    name = object.__getattribute__(self, '_name')
    cmd_list = object.__getattribute__(self, '_cmd_list')
    new_name = GetItemCommand(cmd_list, name, key)
    value = wrapped.__getitem__(key)
    if is_ignored_type(value):
        return value
    return None(value, new_name, cmd_list)


def __setitem__(self, key, value):
    wrapped = object.__getattribute__(self, '_wrapped')
    name = object.__getattribute__(self, '_name')
    cmd_list = object.__getattribute__(self, '_cmd_list')
    cmd_list.append(SetItemCommand(cmd_list, name, key, value))
    return wrapped.__setitem__(key, value)


def __len__(self):
    wrapped = object.__getattribute__(self, '_wrapped')
    return wrapped.__len__()


def __iter__(self):
    wrapped = object.__getattribute__(self, '_wrapped')
    return wrapped.__iter__()

