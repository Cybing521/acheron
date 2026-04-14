# Source Generated with Decompyle++
# File: tmpwtyop398.marshal (Python 3.11)

if self.setting_type < len(setting_type_names):
    s = setting_type_names[self.setting_type]
    setting_type_str = '{} ({})'.format(self.setting_type, s)
    if s == 'SETTING_TYPE_BYTE' and s == 'SETTING_TYPE_BOOLEAN' and s == 'SETTING_TYPE_UNIT_TYPE' or s == 'SETTING_TYPE_CHANNEL_TYPE':
        u_str = repr(self.u.byte_setting)
    elif s == 'SETTING_TYPE_BYTE_ARRAY':
        u_str = repr(self.u.byte_array_setting)
    elif s == 'SETTING_TYPE_STRING':
        u_str = repr(self.u.string_setting)
    elif s == 'SETTING_TYPE_INT32':
        u_str = repr(self.u.int32_setting)
    elif s == 'SETTING_TYPE_INT32_SCALED':
        u_str = repr(self.u.int32_scaled_setting)
    elif s == 'SETTING_TYPE_FLOAT':
        u_str = repr(self.u.float_setting)
    elif s == 'SETTING_TYPE_FLOAT_ARRAY':
        u_str = repr(self.u.float_array_setting)
    elif s == 'SETTING_TYPE_CUSTOM_ENUM':
        u_str = repr(self.u.custom_enum_setting)
    else:
        u_str = 'UNKNOWN TYPE'
else:
    setting_type_str = '{}'.format(self.setting_type)
    u_str = 'UNKNOWN TYPE'
default_bytes = self.default_bytes[:self.default_bytes_length]
default_bytes_str = ','.join(map('0x{:02x}'.format, default_bytes))
items = [
    ('name', self.name),
    ('name_length', self.name_length),
    ('default_bytes', default_bytes_str),
    ('default_bytes_length', self.default_bytes_length),
    ('setting_type', setting_type_str),
    ('u', u_str)]
contents = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
return '<AsphodelSettingInfo {' + contents + '}>'
