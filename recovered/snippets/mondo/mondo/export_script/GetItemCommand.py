# Source Generated with Decompyle++
# File: tmpagjbrz7z.marshal (Python 3.11)


def __init__(self, cmd_list, base, key):
    self.cmd_list = cmd_list
    self.base = base
    self.key = key


def __repr__(self):
    return '{}[{}]'.format(self.base, self.cmd_list.get_string(self.key))

