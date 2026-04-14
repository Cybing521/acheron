# Source Generated with Decompyle++
# File: tmp9c7bitjv.marshal (Python 3.11)

lines = []
if len(default_bytes) == 1:
    lines.append('    default={}'.format(default_bytes[0]))
else:
    lines.append('    default=<ERROR>')
byte_offset = s.nvm_word * 4 + s.nvm_word_byte
value_int = struct.unpack_from('>B', self.device_info.nvm, byte_offset)[0]
lines.append('    value={}'.format(value_int))
return lines
