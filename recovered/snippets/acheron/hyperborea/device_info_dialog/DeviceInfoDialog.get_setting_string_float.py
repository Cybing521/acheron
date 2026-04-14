# Source Generated with Decompyle++
# File: tmpomf2ca16.marshal (Python 3.11)

lines = []
if len(default_bytes) == 4:
    default = struct.unpack_from('>f', default_bytes, 0)[0]
    scaled = default * s.scale + s.offset
    lines.append('    default={}'.format(scaled))
else:
    lines.append('    default=<ERROR>')

try:
    n = asphodel.unit_type_names[s.unit_type]
    unit_type_str = '{} ({})'.format(s.unit_type, n)
except IndexError:
    unit_type_str = str(s.unit_type)

lines.append('    unit_type={}'.format(unit_type_str))
value_float = struct.unpack_from('>f', self.device_info.nvm, s.nvm_word * 4)[0]
scaled_value = value_float * s.scale + s.offset
lines.append('    value={}'.format(scaled_value))
return lines
