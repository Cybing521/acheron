# Source Generated with Decompyle++
# File: tmpylennh5w.marshal (Python 3.11)

lines = []
if len(default_bytes) == 1:
    
    try:
        n = asphodel.unit_type_names[default_bytes[0]]
        unit_type_str = '{} ({})'.format(default_bytes[0], n)
    except IndexError:
        unit_type_str = str(default_bytes[0])

    lines.append('    default={}'.format(unit_type_str))
else:
    lines.append('    default=<ERROR>')
byte_offset = s.nvm_word * 4 + s.nvm_word_byte
value_int = struct.unpack_from('>B', self.device_info.nvm, byte_offset)[0]

try:
    n = asphodel.unit_type_names[value_int]
    unit_type_str = '{} ({})'.format(value_int, n)
except IndexError:
    unit_type_str = str(value_int)

lines.append('    value={}'.format(unit_type_str))
return lines
