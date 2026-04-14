# Source Generated with Decompyle++
# File: tmprw57emu7.marshal (Python 3.11)


def from_hex(h):
    return binascii.a2b_hex(h)

d = obj.copy()
d['_name_array'] = from_hex(d['_name_array'])
instance = cls.__new__(cls)
instance.__setstate__(d)
return instance
