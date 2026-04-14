# Source Generated with Decompyle++
# File: tmphy9zcts8.marshal (Python 3.11)

wrapped = object.__getattribute__(self, '_wrapped')
name = object.__getattribute__(self, '_name')
cmd_list = object.__getattribute__(self, '_cmd_list')
new_name = GetItemCommand(cmd_list, name, key)
value = wrapped.__getitem__(key)
if is_ignored_type(value):
    return value
return None(value, new_name, cmd_list)
