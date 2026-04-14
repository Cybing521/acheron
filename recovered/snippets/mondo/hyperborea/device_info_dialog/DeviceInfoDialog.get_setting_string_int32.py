# Source Generated with Decompyle++
# File: tmpa0v5gd3m.marshal (Python 3.11)

lines = []
if len(default_bytes) == 4:
    default = struct.unpack_from('>i', default_bytes, 0)[0]
    lines.append('    default={}'.format(default))
else:
    lines.append('    default=<ERROR>')
value_int = struct.unpack_from('>i', self.device_info.nvm, s.nvm_word * 4)[0]
lines.append('    value={}'.format(value_int))
return lines
