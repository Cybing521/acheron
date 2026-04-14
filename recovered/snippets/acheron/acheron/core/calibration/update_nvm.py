# Source Generated with Decompyle++
# File: tmpx8t06le1.marshal (Python 3.11)

nvm = bytearray(nvm)
for setting_index, value in unit_settings.items():
    setting = settings[setting_index]
    if setting.setting_type != asphodel.SETTING_TYPE_UNIT_TYPE:
        msg = 'Setting {} is not a unit type'.format(setting_index)
        logger.error(msg)
    s = setting.u.byte_setting
    byte_offset = s.nvm_word * 4 + s.nvm_word_byte
    struct.pack_into('>B', nvm, byte_offset, value)
    for setting_index, f in float_settings.items():
        setting = settings[setting_index]
        if setting.setting_type == asphodel.SETTING_TYPE_INT32_SCALED:
            s_scaled = setting.u.int32_scaled_setting
            unscaled_i = int(round((f - s_scaled.offset) / s_scaled.scale))
            unscaled_i = max(unscaled_i, s_scaled.minimum)
            unscaled_i = min(unscaled_i, s_scaled.maximum)
            struct.pack_into('>i', nvm, s_scaled.nvm_word * 4, unscaled_i)
            continue
        if setting.setting_type == asphodel.SETTING_TYPE_FLOAT:
            s_float = setting.u.float_setting
            unscaled_f = (f - s_float.offset) / s_float.scale
            unscaled_f = max(unscaled_f, s_float.minimum)
            unscaled_f = min(unscaled_f, s_float.maximum)
            struct.pack_into('>f', nvm, s_float.nvm_word * 4, unscaled_f)
            continue
        msg = 'Setting {} is not a float type'.format(setting_index)
        logger.error(msg)
        return nvm
