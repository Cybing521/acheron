# Source Generated with Decompyle++
# File: device_info_dialog.pyc (Python 3.11)

import logging
import os
import struct
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from .ui.ui_device_info_dialog import Ui_DeviceInfoDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def format_bitrate(bitrate):
    scales = [
        (1, 'bit/s'),
        (1000, 'kbit/s'),
        (1e+06, 'Mbit/s'),
        (1e+09, 'Gbit/s')]
    for factor, suffix in scales:
        if bitrate < factor * 1000:
            
            return None, f'''{bitrate / factor:.1f} {suffix}'''
        return f'''{bitrate / 1e+09:.3f} Gbit/s'''

class DeviceInfoDialog(Ui_DeviceInfoDialog, QtWidgets.QDialog):

    def __init__(self, device_info, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST parent
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST device_info
        #   72 LOAD_FAST self
        #   74 STORE_ATTR device_info
        #   84 LOAD_FAST self
        #   86 LOAD_METHOD setupUi
        #  108 LOAD_FAST self
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR plainTextEdit
        #  138 LOAD_METHOD setFont
        #  160 LOAD_GLOBAL QtGui
        #  172 LOAD_ATTR QFontDatabase
        #  182 LOAD_METHOD systemFont
        #  204 LOAD_GLOBAL QtGui
        #  216 LOAD_ATTR QFontDatabase
        #  226 LOAD_ATTR SystemFont
        #  236 LOAD_ATTR FixedFont
        #  246 PRECALL
        #  250 CALL
        #  260 PRECALL
        #  264 CALL
        #  274 POP_TOP
        #  276 LOAD_FAST self
        #  278 LOAD_METHOD create_device_info_string
        #  300 PRECALL
        #  304 CALL
        #  314 LOAD_FAST self
        #  316 STORE_ATTR device_info_str
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR plainTextEdit
        #  338 LOAD_METHOD setPlainText
        #  360 LOAD_FAST self
        #  362 LOAD_ATTR device_info_str
        #  372 PRECALL
        #  376 CALL
        #  386 POP_TOP
        #  388 LOAD_FAST self
        #  390 LOAD_ATTR saveButton
        #  400 LOAD_ATTR clicked
        #  410 LOAD_METHOD connect
        #  432 LOAD_FAST self
        #  434 LOAD_ATTR save
        #  444 PRECALL
        #  448 CALL
        #  458 POP_TOP
        #  460 LOAD_CONST None
        #  462 RETURN_VALUE
        pass

    def create_device_info_string(self):
        d = self.device_info
        s = ''
        s += 'Serial Number: {}\n'.format(d.serial_number)
        s += 'User Tag 1: {}\n'.format(d.user_tag_1)
        s += 'User Tag 2: {}\n'.format(d.user_tag_2)
        s += 'Location String: {}\n'.format(d.location_string)
        s += 'Max Outgoing Param Len: {}\n'.format(d.max_outgoing_param_length)
        s += 'Max Incoming Param Len: {}\n'.format(d.max_incoming_param_length)
        s += 'Stream Packet Length: {}\n'.format(d.stream_packet_length)
        s += 'Protocol Version: {}\n'.format(d.protocol_version)

    def get_setting_string(self, setting_id, setting):
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

    def get_setting_string_bytes(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 1:
            lines.append('    default={}'.format(default_bytes[0]))
        else:
            lines.append('    default=<ERROR>')
        byte_offset = s.nvm_word * 4 + s.nvm_word_byte
        value_int = struct.unpack_from('>B', self.device_info.nvm, byte_offset)[0]
        lines.append('    value={}'.format(value_int))
        return lines

    def get_setting_string_bool(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 1:
            lines.append('    default={}'.format(bool(default_bytes[0])))
        else:
            lines.append('    default=<ERROR>')
        byte_offset = s.nvm_word * 4 + s.nvm_word_byte
        value_bool = struct.unpack_from('>?', self.device_info.nvm, byte_offset)[0]
        lines.append('    value={}'.format(value_bool))
        return lines

    def get_setting_string_unit_type(self, s, default_bytes):
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

    def get_setting_string_channel_type(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 1:
            
            try:
                n = asphodel.channel_type_names[default_bytes[0]]
                channel_type_str = '{} ({})'.format(default_bytes[0], n)
            except IndexError:
                channel_type_str = str(default_bytes[0])

            lines.append('    default={}'.format(channel_type_str))
        else:
            lines.append('    default=<ERROR>')
        byte_offset = s.nvm_word * 4 + s.nvm_word_byte
        value_int = struct.unpack_from('>B', self.device_info.nvm, byte_offset)[0]

        try:
            n = asphodel.channel_type_names[value_int]
            channel_type_str = '{} ({})'.format(value_int, n)
        except IndexError:
            channel_type_str = str(value_int)

        lines.append('    value={}'.format(channel_type_str))
        return lines

    def get_setting_string_byte_array(self, s, default_bytes):
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

    def get_setting_string_string(self, s, default_bytes):
        lines = []

        try:
            default_str = default_bytes.decode('UTF-8')
        except UnicodeDecodeError:
            default_str = '<ERROR>'

        lines.append('    default={}'.format(default_str))
        fmt = '>{}s'.format(s.maximum_length)
        raw = struct.unpack_from(fmt, self.device_info.nvm, s.nvm_word * 4)[0]
        raw = raw.split(b'\x00', 1)[0]
        raw = raw.split(b'\xff', 1)[0]

        try:
            value_str = raw.decode('UTF-8')
        except UnicodeDecodeError:
            value_str = '<ERROR>'

        lines.append('    value={}'.format(value_str))
        return lines

    def get_setting_string_int32(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 4:
            default = struct.unpack_from('>i', default_bytes, 0)[0]
            lines.append('    default={}'.format(default))
        else:
            lines.append('    default=<ERROR>')
        value_int = struct.unpack_from('>i', self.device_info.nvm, s.nvm_word * 4)[0]
        lines.append('    value={}'.format(value_int))
        return lines

    def get_setting_string_int32_scaled(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 4:
            default = struct.unpack_from('>i', default_bytes, 0)[0]
            scaled = default * s.scale + s.offset
            lines.append('    default={}'.format(scaled))
        else:
            lines.append('    default=<ERROR>')

        try:
            n = asphodel.unit_type_names[s.unit_type]
            unit_type_str = '{} ({})'.format(s.unit_type, n)
        except IndexError:
            unit_type_str = str(s.unit_type)

        lines.append('    unit_type={}'.format(unit_type_str))
        value_int = struct.unpack_from('>i', self.device_info.nvm, s.nvm_word * 4)[0]
        scaled_value = value_int * s.scale + s.offset
        lines.append('    value={}'.format(scaled_value))
        return lines

    def get_setting_string_float(self, s, default_bytes):
        lines = []
        if len(default_bytes) == 4:
            default = struct.unpack_from('>f', default_bytes, 0)[0]
            scaled = default * s.scale + s.offset
            lines.append('    default={}'.format(scaled))
        else:
            lines.append('    default=<ERROR>')

        try:
            n = asphodel.unit_type_names[s.unit_type]
            unit_type_str = '{} ({})'.format(s.unit_type, n)
        except IndexError:
            unit_type_str = str(s.unit_type)

        lines.append('    unit_type={}'.format(unit_type_str))
        value_float = struct.unpack_from('>f', self.device_info.nvm, s.nvm_word * 4)[0]
        scaled_value = value_float * s.scale + s.offset
        lines.append('    value={}'.format(scaled_value))
        return lines

    def get_setting_string_float_array(self, s, default_bytes):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL s
        #    2 RESUME
        #    4 BUILD_LIST
        #    6 STORE_FAST lines
        #    8 LOAD_GLOBAL NULL + len
        #   20 LOAD_FAST default_bytes
        #   22 PRECALL
        #   26 CALL
        #   36 LOAD_CONST 4
        #   38 BINARY_OP %
        #   42 LOAD_CONST 0
        #   44 COMPARE_OP ==
        #   50 POP_JUMP_FORWARD_IF_FALSE to 440
        #   52 LOAD_CONST '>{}f'
        #   54 LOAD_METHOD format
        #   76 LOAD_GLOBAL NULL + len
        #   88 LOAD_FAST default_bytes
        #   90 PRECALL
        #   94 CALL
        #  104 LOAD_CONST 4
        #  106 BINARY_OP //
        #  110 PRECALL
        #  114 CALL
        #  124 STORE_FAST fmt
        #  126 LOAD_GLOBAL NULL + struct
        #  138 LOAD_ATTR unpack_from
        #  148 LOAD_FAST fmt
        #  150 LOAD_FAST default_bytes
        #  152 LOAD_CONST 0
        #  154 PRECALL
        #  158 CALL
        #  168 STORE_FAST values
        #  170 LOAD_CLOSURE s
        #  172 BUILD_TUPLE
        #  174 LOAD_CONST <code object <listcomp> at 0x105abff00, file "hyperborea\device_info_dialog.py", line 471>
        #  176 MAKE_FUNCTION closure
        #  178 LOAD_FAST values
        #  180 GET_ITER
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST scaled_values
        #  198 LOAD_CONST ', '
        #  200 LOAD_METHOD join
        #  222 LOAD_GLOBAL NULL + map
        #  234 LOAD_GLOBAL str
        #  246 LOAD_FAST values
        #  248 PRECALL
        #  252 CALL
        #  262 PRECALL
        #  266 CALL
        #  276 STORE_FAST values_str
        #  278 LOAD_CONST ', '
        #  280 LOAD_METHOD join
        #  302 LOAD_GLOBAL NULL + map
        #  314 LOAD_GLOBAL str
        #  326 LOAD_FAST scaled_values
        #  328 PRECALL
        #  332 CALL
        #  342 PRECALL
        #  346 CALL
        #  356 STORE_FAST scaled_values_str
        #  358 LOAD_FAST lines
        #  360 LOAD_METHOD append
        #  382 LOAD_CONST '    default=[{}]'
        #  384 LOAD_METHOD format
        #  406 LOAD_FAST scaled_values_str
        #  408 PRECALL
        #  412 CALL
        #  422 PRECALL
        #  426 CALL
        #  436 POP_TOP
        #  438 JUMP_FORWARD to 482
        #  440 LOAD_FAST lines
        #  442 LOAD_METHOD append
        #  464 LOAD_CONST '    default=<ERROR>'
        #  466 PRECALL
        #  470 CALL
        #  480 POP_TOP
        #  482 NOP
        #  484 LOAD_GLOBAL asphodel
        # ... bytecode truncated ...
        pass

    def get_setting_string_custom_enum(self, s, default_bytes):
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

    def get_save_path(self):
        serial_number = self.device_info.serial_number
        default_name = f'''{serial_number}.txt'''
        settings = QtCore.QSettings()
        directory = settings.value('infoSaveDirectory')
        if not directory or isinstance(directory, str):
            directory = None
        elif not os.path.isdir(directory):
            directory = None
        if not directory:
            directory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
        file_and_dir = os.path.join(directory, default_name)
        caption = self.tr('Save Device Information')
        file_filter = self.tr('Text Files (*.txt);;All Files (*.*)')
        val = QtWidgets.QFileDialog.getSaveFileName(self, caption, file_and_dir, file_filter)
        output_path = val[0]
        if output_path:
            output_dir = os.path.dirname(output_path)
            settings.setValue('infoSaveDirectory', output_dir)
            return os.path.abspath(output_path)

    def save(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD get_save_path
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST path
        #   42 LOAD_FAST path
        #   44 POP_JUMP_FORWARD_IF_FALSE to 472
        #   46 NOP
        #   48 LOAD_GLOBAL NULL + open
        #   60 LOAD_FAST path
        #   62 LOAD_CONST 'wt'
        #   64 LOAD_CONST 'utf-8'
        #   66 KW_NAMES
        #   68 PRECALL
        #   72 CALL
        #   82 BEFORE_WITH
        #   84 STORE_FAST f
        #   86 LOAD_FAST f
        #   88 LOAD_METHOD write
        #  110 LOAD_FAST self
        #  112 LOAD_ATTR device_info_str
        #  122 PRECALL
        #  126 CALL
        #  136 POP_TOP
        #  138 LOAD_FAST f
        #  140 LOAD_METHOD write
        #  162 LOAD_CONST '\n'
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_CONST None
        #  182 LOAD_CONST None
        #  184 LOAD_CONST None
        #  186 PRECALL
        #  190 CALL
        #  200 POP_TOP
        #  202 LOAD_CONST None
        #  204 RETURN_VALUE
        #  206 PUSH_EXC_INFO
        #  208 WITH_EXCEPT_START
        #  210 POP_JUMP_FORWARD_IF_TRUE to 220
        #  212 RERAISE
        #  214 COPY
        #  216 POP_EXCEPT
        #  218 RERAISE
        #  220 POP_TOP
        #  222 POP_EXCEPT
        #  224 POP_TOP
        #  226 POP_TOP
        #  228 LOAD_CONST None
        #  230 RETURN_VALUE
        #  232 PUSH_EXC_INFO
        #  234 LOAD_GLOBAL Exception
        #  246 CHECK_EXC_MATCH
        #  248 POP_JUMP_FORWARD_IF_FALSE to 464
        #  250 POP_TOP
        #  252 LOAD_CONST 'Error writing file '
        #  254 LOAD_FAST path
        #  256 FORMAT_VALUE
        #  258 LOAD_CONST '.'
        #  260 BUILD_STRING
        #  262 STORE_FAST msg
        #  264 LOAD_GLOBAL logger
        #  276 LOAD_METHOD exception
        #  298 LOAD_FAST msg
        #  300 PRECALL
        #  304 CALL
        #  314 POP_TOP
        #  316 LOAD_GLOBAL QtWidgets
        #  328 LOAD_ATTR QMessageBox
        #  338 LOAD_METHOD critical
        #  360 LOAD_FAST self
        #  362 LOAD_FAST self
        #  364 LOAD_METHOD tr
        #  386 LOAD_CONST 'Error'
        #  388 PRECALL
        #  392 CALL
        #  402 LOAD_FAST self
        #  404 LOAD_METHOD tr
        # ... bytecode truncated ...
        pass
