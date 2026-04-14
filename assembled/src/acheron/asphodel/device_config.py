# Source Generated with Decompyle++
# File: device_config.pyc (Python 3.11)

import binascii
import struct
from typing import Any, Iterable
import asphodel
from device_info import DeviceInfo

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def convert_unit_type(unit_type):
    try:
        return asphodel.unit_type_names[unit_type]
    except IndexError:
        return 

def convert_setting(setting, nvm):
    try:
        t = asphodel.setting_type_names[setting.setting_type]
    except IndexError:
        t = str(setting.setting_type)

    result = {
        'name': setting.name.decode('UTF-8'),
        'setting_type': t }
    length = setting.default_bytes_length
    default_bytes = bytes(setting.default_bytes[0:length])
    if t in ('SETTING_TYPE_BYTE', 'SETTING_TYPE_CHANNEL_TYPE', 'SETTING_TYPE_UNIT_TYPE'):
        s_byte = setting.u.byte_setting
        if len(default_bytes) == 1:
            result['default'] = default_bytes[0]
        else:
            result['default'] = None
        byte_offset = s_byte.nvm_word * 4 + s_byte.nvm_word_byte
        result['value'] = struct.unpack_from('>B', nvm, byte_offset)[0]
    elif t == 'SETTING_TYPE_BOOLEAN':
        s_byte = setting.u.byte_setting
        if len(default_bytes) == 1:
            result['default'] = bool(default_bytes[0])
        else:
            result['default'] = None
        byte_offset = s_byte.nvm_word * 4 + s_byte.nvm_word_byte
        result['value'] = struct.unpack_from('>?', nvm, byte_offset)[0]
    elif t == 'SETTING_TYPE_BYTE_ARRAY':
        s_barray = setting.u.byte_array_setting
        result['default'] = default_bytes.hex(sep = ',')
        length_byte_offset = s_barray.length_nvm_word * 4 + s_barray.length_nvm_word_byte
        length = struct.unpack_from('>B', nvm, length_byte_offset)[0]
        if length > s_barray.maximum_length:
            length = s_barray.maximum_length
        result['maximum_length'] = s_barray.maximum_length
        fmt = '>{}s'.format(length)
        value = struct.unpack_from(fmt, nvm, s_barray.nvm_word * 4)[0]
        result['value'] = value.hex(sep = ',')
    elif t == 'SETTING_TYPE_STRING':
        s_str = setting.u.string_setting
        
        try:
            result['default'] = default_bytes.decode('UTF-8')
        except UnicodeDecodeError:
            result['default'] = None

        result['maximum_length'] = s_str.maximum_length
        fmt = '>{}s'.format(s_str.maximum_length)
        raw = struct.unpack_from(fmt, nvm, s_str.nvm_word * 4)[0]
        raw = raw.split(b'\x00', 1)[0]
        raw = raw.split(b'\xff', 1)[0]
        
        try:
            result['value'] = raw.decode('UTF-8')
        except UnicodeDecodeError:
            result['value'] = None
        except:
            if t == 'SETTING_TYPE_INT32':
                s_int32 = setting.u.int32_setting
                result['minimum'] = s_int32.minimum
                result['maximum'] = s_int32.maximum
                result['value'] = struct.unpack_from('>i', nvm, s_int32.nvm_word * 4)[0]
            elif t == 'SETTING_TYPE_INT32_SCALED':
                s_scaled = setting.u.int32_scaled_setting
                result['minimum'] = s_scaled.minimum
                result['maximum'] = s_scaled.maximum
                result['unit_type'] = convert_unit_type(s_scaled.unit_type)
                result['scale'] = s_scaled.scale
                result['offset'] = s_scaled.offset
                result['value'] = struct.unpack_from('>i', nvm, s_scaled.nvm_word * 4)[0]
            elif t == 'SETTING_TYPE_FLOAT':
                s_float = setting.u.float_setting
                result['minimum'] = s_float.minimum
                result['maximum'] = s_float.maximum
                result['unit_type'] = convert_unit_type(s_float.unit_type)
                result['scale'] = s_float.scale
                result['offset'] = s_float.offset
                result['value'] = struct.unpack_from('>f', nvm, s_float.nvm_word * 4)[0]
            elif t == 'SETTING_TYPE_FLOAT_ARRAY':
                s_farray = setting.u.float_array_setting
                result['minimum'] = s_farray.minimum
                result['maximum'] = s_farray.maximum
                result['unit_type'] = convert_unit_type(s_farray.unit_type)
                result['scale'] = s_farray.scale
                result['offset'] = s_farray.offset
                length_byte_offset = s_farray.length_nvm_word * 4 + s_farray.length_nvm_word_byte
                length = struct.unpack_from('>B', nvm, length_byte_offset)[0]
                if length > s_farray.maximum_length:
                    length = s_farray.maximum_length
                result['maximum_length'] = s_farray.maximum_length
                fmt = '>{}f'.format(length)
                result['value'] = struct.unpack_from(fmt, nvm, s_farray.nvm_word * 4)
            elif t == 'SETTING_TYPE_CUSTOM_ENUM':
                s_ce = setting.u.custom_enum_setting
                byte_offset = s_ce.nvm_word * 4 + s_ce.nvm_word_byte
                result['value'] = struct.unpack_from('>B', nvm, byte_offset)[0]
                result['custom_enum_index'] = s_ce.custom_enum_index
            else:
                result['default'] = default_bytes.hex(sep = ',')

    return result

def convert_ctrl_var(name, ctrl_var, value):
    return {
        'name': name,
        'unit_type': convert_unit_type(ctrl_var.unit_type),
        'minimum': ctrl_var.minimum,
        'maximum': ctrl_var.maximum,
        'scale': ctrl_var.scale,
        'offset': ctrl_var.offset,
        'value': value }

def configure_setting(setting, value, device_info, nvm):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_FAST setting
    #    4 LOAD_ATTR setting_type
    #   14 LOAD_GLOBAL asphodel
    #   26 LOAD_ATTR SETTING_TYPE_BYTE
    #   36 LOAD_GLOBAL asphodel
    #   48 LOAD_ATTR SETTING_TYPE_CHANNEL_TYPE
    #   58 LOAD_GLOBAL asphodel
    #   70 LOAD_ATTR SETTING_TYPE_UNIT_TYPE
    #   80 BUILD_TUPLE
    #   82 CONTAINS_OP
    #   84 POP_JUMP_FORWARD_IF_FALSE to 196
    #   86 LOAD_FAST setting
    #   88 LOAD_ATTR u
    #   98 LOAD_ATTR byte_setting
    #  108 STORE_FAST s_byte
    #  110 LOAD_FAST s_byte
    #  112 LOAD_ATTR nvm_word
    #  122 LOAD_CONST 4
    #  124 BINARY_OP *
    #  128 LOAD_FAST s_byte
    #  130 LOAD_ATTR nvm_word_byte
    #  140 BINARY_OP +
    #  144 STORE_FAST byte_offset
    #  146 LOAD_GLOBAL NULL + struct
    #  158 LOAD_ATTR pack_into
    #  168 LOAD_CONST '>B'
    #  170 LOAD_FAST nvm
    #  172 LOAD_FAST byte_offset
    #  174 LOAD_FAST value
    #  176 PRECALL
    #  180 CALL
    #  190 POP_TOP
    #  192 LOAD_CONST None
    #  194 RETURN_VALUE
    #  196 LOAD_FAST setting
    #  198 LOAD_ATTR setting_type
    #  208 LOAD_GLOBAL asphodel
    #  220 LOAD_ATTR SETTING_TYPE_BOOLEAN
    #  230 COMPARE_OP ==
    #  236 POP_JUMP_FORWARD_IF_FALSE to 348
    #  238 LOAD_FAST setting
    #  240 LOAD_ATTR u
    #  250 LOAD_ATTR byte_setting
    #  260 STORE_FAST s_byte
    #  262 LOAD_FAST s_byte
    #  264 LOAD_ATTR nvm_word
    #  274 LOAD_CONST 4
    #  276 BINARY_OP *
    #  280 LOAD_FAST s_byte
    #  282 LOAD_ATTR nvm_word_byte
    #  292 BINARY_OP +
    #  296 STORE_FAST byte_offset
    #  298 LOAD_GLOBAL NULL + struct
    #  310 LOAD_ATTR pack_into
    #  320 LOAD_CONST '>?'
    #  322 LOAD_FAST nvm
    #  324 LOAD_FAST byte_offset
    #  326 LOAD_FAST value
    #  328 PRECALL
    #  332 CALL
    #  342 POP_TOP
    #  344 LOAD_CONST None
    #  346 RETURN_VALUE
    #  348 LOAD_FAST setting
    #  350 LOAD_ATTR setting_type
    #  360 LOAD_GLOBAL asphodel
    #  372 LOAD_ATTR SETTING_TYPE_BYTE_ARRAY
    #  382 COMPARE_OP ==
    #  388 POP_JUMP_FORWARD_IF_FALSE to 814
    #  390 LOAD_FAST setting
    #  392 LOAD_ATTR u
    #  402 LOAD_ATTR byte_array_setting
    #  412 STORE_FAST s_barray
    #  414 LOAD_FAST s_barray
    #  416 LOAD_ATTR length_nvm_word
    #  426 LOAD_CONST 4
    #  428 BINARY_OP *
    #  432 LOAD_FAST s_barray
    #  434 LOAD_ATTR length_nvm_word_byte
    # ... bytecode truncated ...
    pass

def configure_nvm(device_config, device_info, nvm):
    nvm_array = bytearray(nvm)
    for key, value in device_config:
        setting_name = key.encode('UTF-8')
        for setting in device_info.settings:
            if setting.name == setting_name:
                configure_setting(setting, value, device_info, nvm_array)
            raise KeyError('No setting {}'.format(key))
            return bytes(nvm_array)
