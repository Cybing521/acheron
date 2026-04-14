# Source Generated with Decompyle++
# File: tmpxzvwgwry.marshal (Python 3.11)

lines = []

try:
    default_str = default_bytes.decode('UTF-8')
except UnicodeDecodeError:
    default_str = '<ERROR>'

lines.append('    default={}'.format(default_str))
fmt = '>{}s'.format(s.maximum_length)
raw = struct.unpack_from(fmt, self.device_info.nvm, s.nvm_word * 4)[0]
raw = raw.split(b'\x00', 1)[0]
raw = raw.split(b'\xff', 1)[0]

try:
    value_str = raw.decode('UTF-8')
except UnicodeDecodeError:
    value_str = '<ERROR>'

lines.append('    value={}'.format(value_str))
return lines
