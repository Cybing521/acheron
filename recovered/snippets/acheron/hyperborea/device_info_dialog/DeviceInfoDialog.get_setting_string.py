# Source Generated with Decompyle++
# File: tmpzzuxx58p.marshal (Python 3.11)

lines = []
lines.append(f'''  Setting {setting_id}''')
setting_name = setting.name.decode('UTF-8')
lines.append(f'''    name: {setting_name}''')

try:
    t = asphodel.setting_type_names[setting.setting_type]
except IndexError:
    t = None

length = setting.default_bytes_length
default_bytes = bytes(setting.default_bytes[0:length])
if t == 'SETTING_TYPE_BYTE':
    lines.extend(self.get_setting_string_bytes(setting.u.byte_setting, default_bytes))
elif t == 'SETTING_TYPE_BOOLEAN':
    lines.extend(self.get_setting_string_bool(setting.u.byte_setting, default_bytes))
elif t == 'SETTING_TYPE_UNIT_TYPE':
    lines.extend(self.get_setting_string_unit_type(setting.u.byte_setting, default_bytes))
elif t == 'SETTING_TYPE_CHANNEL_TYPE':
    lines.extend(self.get_setting_string_channel_type(setting.u.byte_setting, default_bytes))
elif t == 'SETTING_TYPE_BYTE_ARRAY':
    lines.extend(self.get_setting_string_byte_array(setting.u.byte_array_setting, default_bytes))
elif t == 'SETTING_TYPE_STRING':
    lines.extend(self.get_setting_string_string(setting.u.string_setting, default_bytes))
elif t == 'SETTING_TYPE_INT32':
    lines.extend(self.get_setting_string_int32(setting.u.int32_setting, default_bytes))
elif t == 'SETTING_TYPE_INT32_SCALED':
    lines.extend(self.get_setting_string_int32_scaled(setting.u.int32_scaled_setting, default_bytes))
elif t == 'SETTING_TYPE_FLOAT':
    lines.extend(self.get_setting_string_float(setting.u.float_setting, default_bytes))
elif t == 'SETTING_TYPE_FLOAT_ARRAY':
    lines.extend(self.get_setting_string_float_array(setting.u.float_array_setting, default_bytes))
elif t == 'SETTING_TYPE_CUSTOM_ENUM':
    lines.extend(self.get_setting_string_custom_enum(setting.u.custom_enum_setting, default_bytes))
else:
    lines.append('    unknown setting type!')
lines.append('')
return '\n'.join(lines)
