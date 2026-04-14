# Source Generated with Decompyle++
# File: tmpff981tar.marshal (Python 3.11)

lines = []

try:
    enum = self.device_info.custom_enums[s.custom_enum_index]
except KeyError:
    enum = []

if len(default_bytes) == 1:
    default_value = default_bytes[0]
    
    try:
        default_str = enum[default_value]
    except IndexError:
        default_str = 'unknown ({})'.format(default_value)
    except:
        default_str = '<ERROR>'

    lines.append('    default={}'.format(default_str))
    byte_offset = s.nvm_word * 4 + s.nvm_word_byte
    value_int = struct.unpack_from('>B', self.device_info.nvm, byte_offset)[0]
    
    try:
        value_str = enum[value_int]
    except IndexError:
        value_str = 'unknown ({})'.format(value_int)

    lines.append('    value={}'.format(value_str))
    return lines
