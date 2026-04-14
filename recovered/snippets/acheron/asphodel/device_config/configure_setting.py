# Source Generated with Decompyle++
# File: tmpchcn390p.marshal (Python 3.11)

if setting.setting_type in (asphodel.SETTING_TYPE_BYTE, asphodel.SETTING_TYPE_CHANNEL_TYPE, asphodel.SETTING_TYPE_UNIT_TYPE):
    s_byte = setting.u.byte_setting
    byte_offset = s_byte.nvm_word * 4 + s_byte.nvm_word_byte
    struct.pack_into('>B', nvm, byte_offset, value)
    return None
if None.setting_type == asphodel.SETTING_TYPE_BOOLEAN:
    s_byte = setting.u.byte_setting
    byte_offset = s_byte.nvm_word * 4 + s_byte.nvm_word_byte
    struct.pack_into('>?', nvm, byte_offset, value)
    return None
if None.setting_type == asphodel.SETTING_TYPE_BYTE_ARRAY:
    s_barray = setting.u.byte_array_setting
    length_byte_offset = s_barray.length_nvm_word * 4 + s_barray.length_nvm_word_byte
    b = binascii.a2b_hex(value.replace(',', ''))
    if len(b) > s_barray.maximum_length:
        b = b[0:s_barray.maximum_length]
    struct.pack_into('>B', nvm, length_byte_offset, len(b))
    fmt = '>{}s'.format(len(b))
    struct.pack_into(fmt, nvm, s_barray.nvm_word * 4, b)
    return None
if None.setting_type == asphodel.SETTING_TYPE_STRING:
    s_str = setting.u.string_setting
    fmt = '>{}s'.format(s_str.maximum_length)
    b = value.encode('UTF-8')
    struct.pack_into(fmt, nvm, s_str.nvm_word * 4, b)
    return None
if None.setting_type == asphodel.SETTING_TYPE_INT32:
    s_int32 = setting.u.int32_setting
    struct.pack_into('>i', nvm, s_int32.nvm_word * 4, value)
    return None
if None.setting_type == asphodel.SETTING_TYPE_INT32_SCALED:
    s_scaled = setting.u.int32_scaled_setting
    struct.pack_into('>i', nvm, s_scaled.nvm_word * 4, value)
    return None
if None.setting_type == asphodel.SETTING_TYPE_FLOAT:
    s = setting.u.float_setting
    struct.pack_into('>f', nvm, s.nvm_word * 4, value)
    return None
# WARNING: Decompyle incomplete
