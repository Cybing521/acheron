# Source Generated with Decompyle++
# File: tmp655bomg8.marshal (Python 3.11)

lines = []
default_str = default_bytes.hex(sep = ',')
lines.append('    default=[{}]'.format(default_str))
length_byte_offset = s.length_nvm_word * 4 + s.length_nvm_word_byte
length = struct.unpack_from('>B', self.device_info.nvm, length_byte_offset)[0]
if length > s.maximum_length:
    length = s.maximum_length
fmt = '>{}s'.format(length)
value_bytes = struct.unpack_from(fmt, self.device_info.nvm, s.nvm_word * 4)[0]
value_str = value_bytes.hex(sep = ',')
lines.append('    value={}'.format(value_str))
return lines
