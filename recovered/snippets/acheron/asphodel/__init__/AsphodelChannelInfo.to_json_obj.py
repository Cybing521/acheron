# Source Generated with Decompyle++
# File: tmp5a4f4y2u.marshal (Python 3.11)


def to_hex(b):
    return binascii.b2a_hex(b).decode('ascii')

d = self.__getstate__()
d['_name_array'] = to_hex(d['_name_array'])
return d
