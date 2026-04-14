# Source Generated with Decompyle++
# File: tmpt4f0benz.marshal (Python 3.11)

wrapped = object.__getattribute__(self, '_wrapped')
name = object.__getattribute__(self, '_name')
cmd_list = object.__getattribute__(self, '_cmd_list')
cmd_list.append(SetItemCommand(cmd_list, name, key, value))
return wrapped.__setitem__(key, value)
