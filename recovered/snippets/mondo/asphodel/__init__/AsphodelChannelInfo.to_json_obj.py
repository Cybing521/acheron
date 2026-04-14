# Source Generated with Decompyle++
# File: tmpbzb11p70.marshal (Python 3.11)


def to_hex(b):
    return binascii.b2a_hex(b).decode('ascii')

d = self.__getstate__()
d['_name_array'] = to_hex(d['_name_array'])
return d
