# Source Generated with Decompyle++
# File: tmpxn9w11sd.marshal (Python 3.11)

_fields_ = [
    ('name', c_char_p),
    ('name_length', c_uint8),
    ('default_bytes', POINTER(c_uint8)),
    ('default_bytes_length', c_uint8),
    ('setting_type', c_uint8),
    ('u', AsphodelSettingUnion)]
__reduce__ = object.__reduce__

def __repr__(self):
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


def __getstate__(self):
    default_bytes = self.default_bytes[:self.default_bytes_length]
    return {
        '_name_array': self.name,
        'name_length': self.name_length,
        '_default_bytes': default_bytes,
        'default_bytes_length': self.default_bytes_length,
        'setting_type': self.setting_type,
        'u': self.u }


def __setstate__(self, state):
    pass
# WARNING: Decompyle incomplete

from_str = (lambda cls, s: 
def trim_prefix(s, prefix):
if not s.startswith(prefix):
raise AsphodelError('Invalid string prefix "{}"'.format(prefix))s[len(prefix):]
def trim_suffix(s, suffix):
if not s.endswith(suffix):
raise AsphodelError('Invalid string suffix "{}"'.format(suffix))s[:-len(suffix)]s = trim_prefix(s, '<AsphodelSettingInfo {')s = trim_suffix(s, '}>')u = AsphodelSettingUnion()if not s.endswith('UNKNOWN TYPE'):
s = trim_suffix(s, '}>')(s, u_vals) = s.rsplit(' {', 1)(s, u_type) = s.rsplit(', u=<')u_dict = dict(map((lambda s: s.split('=', 1)), u_vals.split(', ')))
        if 'unit_type' in u_dict:
            u_dict['unit_type'] = u_dict['unit_type'].split(' ', 1)[0]
        for k, v in u_dict.items():
            u_dict[k] = int(v)
            except ValueError:
                u_dict[k] = float(v)
                continue
            for field_name, field_type in AsphodelSettingUnion._fields_:
                if field_type.__name__ == u_type:
                    u_struct = getattr(u, field_name)
                    for name, value in u_dict.items():
                        setattr(u_struct, name, value)
                (s, setting_type_str) = s.rsplit(', setting_type=', 1)
                setting_type = int(setting_type_str.split(' (', 1)[0])
                (s, default_bytes_length_str) = s.rsplit(', default_bytes_length=', 1)
                default_bytes_length = int(default_bytes_length_str)
                (s, default_bytes_str) = s.rsplit(', default_bytes=', 1)
                b = ''.join(map((lambda x: x[2:]), default_bytes_str.split(',')))
                default_bytes = binascii.a2b_hex(b)
                if len(default_bytes) != default_bytes_length:
                    raise AsphodelError('Bad default_bytes_length')
                (s, name_length_str) = s.rsplit(', name_length=', 1)
                name_length = int(name_length_str)
                name_str = trim_prefix(s, 'name=')
                name = ast.literal_eval(name_str)
                if not isinstance(name, bytes):
                    raise AsphodelError('Bad name')
                if len(name) != name_length:
                    raise AsphodelError('Bad name_length')
                instance = cls.__new__(cls)
                instance.__setstate__({
                    '_name_array': name,
                    'name_length': name_length,
                    '_default_bytes': default_bytes,
                    'default_bytes_length': default_bytes_length,
                    'setting_type': setting_type,
                    'u': u })
                return instance
)()
