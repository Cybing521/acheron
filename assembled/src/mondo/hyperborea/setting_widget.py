# Source Generated with Decompyle++
# File: setting_widget.pyc (Python 3.11)

import struct
from typing import Optional, Union
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from .unit_formatter_spinbox import UnitFormatterSpinBox
from .unit_formatter_spinbox import UnitFormatterDoubleSpinBox

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class StringLengthValidator(QtGui.QValidator):

    def __init__(self, max_length, parent):
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
        #   70 LOAD_FAST max_length
        #   72 LOAD_FAST self
        #   74 STORE_ATTR max_length
        #   84 LOAD_CONST None
        #   86 RETURN_VALUE
        pass

    def fixup(self, input_text):
        return input_text

    def validate(self, input_text, pos):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST input_text
        #    6 LOAD_METHOD encode
        #   28 LOAD_CONST 'UTF-8'
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST utf_bytes
        #   46 JUMP_FORWARD to 130
        #   48 PUSH_EXC_INFO
        #   50 LOAD_GLOBAL Exception
        #   62 CHECK_EXC_MATCH
        #   64 POP_JUMP_FORWARD_IF_FALSE to 122
        #   66 POP_TOP
        #   68 LOAD_GLOBAL QtGui
        #   80 LOAD_ATTR QValidator
        #   90 LOAD_ATTR State
        #  100 LOAD_ATTR Invalid
        #  110 LOAD_FAST input_text
        #  112 LOAD_FAST pos
        #  114 BUILD_TUPLE
        #  116 SWAP
        #  118 POP_EXCEPT
        #  120 RETURN_VALUE
        #  122 RERAISE
        #  124 COPY
        #  126 POP_EXCEPT
        #  128 RERAISE
        #  130 LOAD_GLOBAL NULL + len
        #  142 LOAD_FAST utf_bytes
        #  144 PRECALL
        #  148 CALL
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR max_length
        #  170 COMPARE_OP <=
        #  176 POP_JUMP_FORWARD_IF_FALSE to 228
        #  178 LOAD_GLOBAL QtGui
        #  190 LOAD_ATTR QValidator
        #  200 LOAD_ATTR State
        #  210 LOAD_ATTR Acceptable
        #  220 LOAD_FAST input_text
        #  222 LOAD_FAST pos
        #  224 BUILD_TUPLE
        #  226 RETURN_VALUE
        #  228 LOAD_GLOBAL QtGui
        #  240 LOAD_ATTR QValidator
        #  250 LOAD_ATTR State
        #  260 LOAD_ATTR Invalid
        #  270 LOAD_FAST input_text
        #  272 LOAD_FAST pos
        #  274 BUILD_TUPLE
        #  276 RETURN_VALUE
        pass

class SettingWidget(QtWidgets.QWidget):

    def __init__(self, setting, nvm_bytes, custom_enums, parent):
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
        #   70 LOAD_FAST setting
        #   72 LOAD_FAST self
        #   74 STORE_ATTR setting
        #   84 LOAD_FAST nvm_bytes
        #   86 LOAD_FAST self
        #   88 STORE_ATTR nvm_bytes
        #   98 LOAD_FAST custom_enums
        #  100 LOAD_FAST self
        #  102 STORE_ATTR custom_enums
        #  112 LOAD_FAST self
        #  114 POP_TOP
        #  116 LOAD_FAST self
        #  118 POP_TOP
        #  120 LOAD_FAST self
        #  122 POP_TOP
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR setting
        #  136 POP_JUMP_FORWARD_IF_NONE to 238
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR setting
        #  150 LOAD_ATTR default_bytes_length
        #  160 STORE_FAST length
        #  162 LOAD_GLOBAL NULL + bytes
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR setting
        #  186 LOAD_ATTR default_bytes
        #  196 LOAD_CONST 0
        #  198 LOAD_FAST length
        #  200 BUILD_SLICE
        #  202 BINARY_SUBSCR
        #  212 PRECALL
        #  216 CALL
        #  226 LOAD_FAST self
        #  228 STORE_ATTR default_bytes
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR setting
        #  250 POP_JUMP_FORWARD_IF_NOT_NONE to 296
        #  252 LOAD_FAST self
        #  254 LOAD_METHOD setup_unknown_setting_type
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        #  296 LOAD_FAST self
        #  298 LOAD_ATTR setting
        #  308 LOAD_ATTR setting_type
        #  318 LOAD_GLOBAL asphodel
        #  330 LOAD_ATTR SETTING_TYPE_BYTE
        #  340 COMPARE_OP ==
        #  346 POP_JUMP_FORWARD_IF_FALSE to 392
        #  348 LOAD_FAST self
        #  350 LOAD_METHOD setup_byte
        #  372 PRECALL
        #  376 CALL
        #  386 POP_TOP
        #  388 LOAD_CONST None
        #  390 RETURN_VALUE
        #  392 LOAD_FAST self
        #  394 LOAD_ATTR setting
        #  404 LOAD_ATTR setting_type
        #  414 LOAD_GLOBAL asphodel
        #  426 LOAD_ATTR SETTING_TYPE_BOOLEAN
        #  436 COMPARE_OP ==
        #  442 POP_JUMP_FORWARD_IF_FALSE to 488
        #  444 LOAD_FAST self
        #  446 LOAD_METHOD setup_boolean
        #  468 PRECALL
        #  472 CALL
        #  482 POP_TOP
        # ... bytecode truncated ...
        pass

    def restore_defaults(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def create_setting_label(self):
        setting_name = self.setting.name.decode('UTF-8')
        setting_label = QtWidgets.QLabel(self)
        setting_label.setText(setting_name)
        return setting_label

    def setup_unknown_setting_type(self):
        self.setting_label = self.create_setting_label()
        self.unknown_label = QtWidgets.QLabel(self)
        self.unknown_label.setText('Unknown Setting Type!')
        style = 'QLabel { font-weight: bold; color : red; }'
        self.unknown_label.setStyleSheet(style)

        def update_nvm(nvm_bytes = None):
            pass

        self.update_nvm = update_nvm
        self.widgets = (self.setting_label, self.unknown_label)

    def setup_byte(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL byte_offset
        #    4 MAKE_CELL default_value
        #    6 RESUME
        #    8 LOAD_DEREF self
        #   10 LOAD_ATTR setting
        #   20 LOAD_ATTR u
        #   30 LOAD_ATTR byte_setting
        #   40 STORE_FAST s
        #   42 LOAD_DEREF self
        #   44 LOAD_METHOD create_setting_label
        #   66 PRECALL
        #   70 CALL
        #   80 LOAD_DEREF self
        #   82 STORE_ATTR setting_label
        #   92 LOAD_GLOBAL NULL + QtWidgets
        #  104 LOAD_ATTR QSpinBox
        #  114 LOAD_DEREF self
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_DEREF self
        #  132 STORE_ATTR spinbox
        #  142 LOAD_FAST s
        #  144 LOAD_ATTR nvm_word
        #  154 LOAD_CONST 4
        #  156 BINARY_OP *
        #  160 LOAD_FAST s
        #  162 LOAD_ATTR nvm_word_byte
        #  172 BINARY_OP +
        #  176 STORE_DEREF byte_offset
        #  178 LOAD_GLOBAL NULL + struct
        #  190 LOAD_ATTR unpack_from
        #  200 LOAD_CONST '>B'
        #  202 LOAD_DEREF self
        #  204 LOAD_ATTR nvm_bytes
        #  214 LOAD_DEREF byte_offset
        #  216 PRECALL
        #  220 CALL
        #  230 LOAD_CONST 0
        #  232 BINARY_SUBSCR
        #  242 STORE_FAST initial
        #  244 LOAD_DEREF self
        #  246 LOAD_ATTR spinbox
        #  256 LOAD_METHOD setMinimum
        #  278 LOAD_CONST 0
        #  280 PRECALL
        #  284 CALL
        #  294 POP_TOP
        #  296 LOAD_DEREF self
        #  298 LOAD_ATTR spinbox
        #  308 LOAD_METHOD setMaximum
        #  330 LOAD_CONST 255
        #  332 PRECALL
        #  336 CALL
        #  346 POP_TOP
        #  348 LOAD_DEREF self
        #  350 LOAD_ATTR spinbox
        #  360 LOAD_METHOD setValue
        #  382 LOAD_FAST initial
        #  384 PRECALL
        #  388 CALL
        #  398 POP_TOP
        #  400 LOAD_GLOBAL NULL + len
        #  412 LOAD_DEREF self
        #  414 LOAD_ATTR default_bytes
        #  424 PRECALL
        #  428 CALL
        #  438 LOAD_CONST 1
        #  440 COMPARE_OP ==
        #  446 POP_JUMP_FORWARD_IF_FALSE to 546
        #  448 LOAD_DEREF self
        #  450 LOAD_ATTR default_bytes
        #  460 LOAD_CONST 0
        #  462 BINARY_SUBSCR
        #  472 STORE_DEREF default_value
        #  474 LOAD_CONST '{}'
        #  476 LOAD_METHOD format
        #  498 LOAD_DEREF default_value
        #  500 PRECALL
        #  504 CALL
        # ... bytecode truncated ...
        pass

    def setup_boolean(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL byte_offset
        #    4 MAKE_CELL default_value
        #    6 RESUME
        #    8 LOAD_DEREF self
        #   10 LOAD_ATTR setting
        #   20 LOAD_ATTR u
        #   30 LOAD_ATTR byte_setting
        #   40 STORE_FAST s
        #   42 LOAD_GLOBAL NULL + QtWidgets
        #   54 LOAD_ATTR QCheckBox
        #   64 LOAD_DEREF self
        #   66 PRECALL
        #   70 CALL
        #   80 LOAD_DEREF self
        #   82 STORE_ATTR check_box
        #   92 LOAD_DEREF self
        #   94 LOAD_ATTR setting
        #  104 LOAD_ATTR name
        #  114 LOAD_METHOD decode
        #  136 LOAD_CONST 'UTF-8'
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST setting_name
        #  154 LOAD_DEREF self
        #  156 LOAD_ATTR check_box
        #  166 LOAD_METHOD setText
        #  188 LOAD_FAST setting_name
        #  190 PRECALL
        #  194 CALL
        #  204 POP_TOP
        #  206 LOAD_FAST s
        #  208 LOAD_ATTR nvm_word
        #  218 LOAD_CONST 4
        #  220 BINARY_OP *
        #  224 LOAD_FAST s
        #  226 LOAD_ATTR nvm_word_byte
        #  236 BINARY_OP +
        #  240 STORE_DEREF byte_offset
        #  242 LOAD_GLOBAL NULL + struct
        #  254 LOAD_ATTR unpack_from
        #  264 LOAD_CONST '>?'
        #  266 LOAD_DEREF self
        #  268 LOAD_ATTR nvm_bytes
        #  278 LOAD_DEREF byte_offset
        #  280 PRECALL
        #  284 CALL
        #  294 LOAD_CONST 0
        #  296 BINARY_SUBSCR
        #  306 STORE_FAST initial
        #  308 LOAD_DEREF self
        #  310 LOAD_ATTR check_box
        #  320 LOAD_METHOD setChecked
        #  342 LOAD_FAST initial
        #  344 PRECALL
        #  348 CALL
        #  358 POP_TOP
        #  360 LOAD_GLOBAL NULL + len
        #  372 LOAD_DEREF self
        #  374 LOAD_ATTR default_bytes
        #  384 PRECALL
        #  388 CALL
        #  398 LOAD_CONST 1
        #  400 COMPARE_OP ==
        #  406 POP_JUMP_FORWARD_IF_FALSE to 532
        #  408 LOAD_GLOBAL NULL + bool
        #  420 LOAD_DEREF self
        #  422 LOAD_ATTR default_bytes
        #  432 LOAD_CONST 0
        #  434 BINARY_SUBSCR
        #  444 PRECALL
        #  448 CALL
        #  458 STORE_DEREF default_value
        #  460 LOAD_CONST '{}'
        #  462 LOAD_METHOD format
        #  484 LOAD_DEREF default_value
        #  486 PRECALL
        #  490 CALL
        #  500 STORE_FAST default_str
        #  502 LOAD_CONST ('return', None)
        # ... bytecode truncated ...
        pass

    def setup_unit_type(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL byte_offset
        #    4 MAKE_CELL default_index
        #    6 MAKE_CELL option_values
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR byte_setting
        #   42 STORE_FAST s
        #   44 LOAD_GLOBAL NULL + len
        #   56 LOAD_DEREF self
        #   58 LOAD_ATTR default_bytes
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_CONST 1
        #   84 COMPARE_OP ==
        #   90 POP_JUMP_FORWARD_IF_FALSE to 158
        #   92 LOAD_CONST '{}'
        #   94 LOAD_METHOD format
        #  116 LOAD_DEREF self
        #  118 LOAD_ATTR default_bytes
        #  128 LOAD_CONST 0
        #  130 BINARY_SUBSCR
        #  140 PRECALL
        #  144 CALL
        #  154 STORE_FAST default_str
        #  156 JUMP_FORWARD to 162
        #  158 LOAD_CONST 'unknown'
        #  160 STORE_FAST default_str
        #  162 LOAD_DEREF self
        #  164 LOAD_METHOD create_setting_label
        #  186 PRECALL
        #  190 CALL
        #  200 LOAD_DEREF self
        #  202 STORE_ATTR setting_label
        #  212 BUILD_LIST
        #  214 STORE_DEREF option_values
        #  216 LOAD_GLOBAL NULL + QtWidgets
        #  228 LOAD_ATTR QComboBox
        #  238 LOAD_DEREF self
        #  240 PRECALL
        #  244 CALL
        #  254 LOAD_DEREF self
        #  256 STORE_ATTR combo_box
        #  266 LOAD_GLOBAL NULL + enumerate
        #  278 LOAD_GLOBAL asphodel
        #  290 LOAD_ATTR unit_type_names
        #  300 PRECALL
        #  304 CALL
        #  314 GET_ITER
        #  316 FOR_ITER to 466
        #  318 UNPACK_SEQUENCE
        #  322 STORE_FAST i
        #  324 STORE_FAST name
        #  326 LOAD_GLOBAL NULL + getattr
        #  338 LOAD_GLOBAL asphodel
        #  350 LOAD_FAST name
        #  352 PRECALL
        #  356 CALL
        #  366 STORE_FAST value
        #  368 LOAD_DEREF option_values
        #  370 LOAD_METHOD append
        #  392 LOAD_FAST value
        #  394 PRECALL
        #  398 CALL
        #  408 POP_TOP
        #  410 LOAD_DEREF self
        #  412 LOAD_ATTR combo_box
        #  422 LOAD_METHOD insertItem
        #  444 LOAD_FAST i
        #  446 LOAD_FAST name
        #  448 PRECALL
        #  452 CALL
        #  462 POP_TOP
        #  464 JUMP_BACKWARD to 316
        #  466 LOAD_FAST s
        #  468 LOAD_ATTR nvm_word
        #  478 LOAD_CONST 4
        #  480 BINARY_OP *
        # ... bytecode truncated ...
        pass

    def setup_channel_type(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL byte_offset
        #    4 MAKE_CELL default_index
        #    6 MAKE_CELL option_values
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR byte_setting
        #   42 STORE_FAST s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 BUILD_LIST
        #   96 STORE_DEREF option_values
        #   98 LOAD_GLOBAL NULL + QtWidgets
        #  110 LOAD_ATTR QComboBox
        #  120 LOAD_DEREF self
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_DEREF self
        #  138 STORE_ATTR combo_box
        #  148 LOAD_GLOBAL NULL + enumerate
        #  160 LOAD_GLOBAL asphodel
        #  172 LOAD_ATTR channel_type_names
        #  182 PRECALL
        #  186 CALL
        #  196 GET_ITER
        #  198 FOR_ITER to 348
        #  200 UNPACK_SEQUENCE
        #  204 STORE_FAST i
        #  206 STORE_FAST name
        #  208 LOAD_GLOBAL NULL + getattr
        #  220 LOAD_GLOBAL asphodel
        #  232 LOAD_FAST name
        #  234 PRECALL
        #  238 CALL
        #  248 STORE_FAST value
        #  250 LOAD_DEREF option_values
        #  252 LOAD_METHOD append
        #  274 LOAD_FAST value
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_DEREF self
        #  294 LOAD_ATTR combo_box
        #  304 LOAD_METHOD insertItem
        #  326 LOAD_FAST i
        #  328 LOAD_FAST name
        #  330 PRECALL
        #  334 CALL
        #  344 POP_TOP
        #  346 JUMP_BACKWARD to 198
        #  348 LOAD_FAST s
        #  350 LOAD_ATTR nvm_word
        #  360 LOAD_CONST 4
        #  362 BINARY_OP *
        #  366 LOAD_FAST s
        #  368 LOAD_ATTR nvm_word_byte
        #  378 BINARY_OP +
        #  382 STORE_DEREF byte_offset
        #  384 LOAD_GLOBAL NULL + struct
        #  396 LOAD_ATTR unpack_from
        #  406 LOAD_CONST '>B'
        #  408 LOAD_DEREF self
        #  410 LOAD_ATTR nvm_bytes
        #  420 LOAD_DEREF byte_offset
        #  422 PRECALL
        #  426 CALL
        #  436 LOAD_CONST 0
        #  438 BINARY_SUBSCR
        #  448 STORE_FAST initial
        #  450 NOP
        #  452 LOAD_DEREF option_values
        #  454 LOAD_METHOD index
        #  476 LOAD_FAST initial
        #  478 PRECALL
        # ... bytecode truncated ...
        pass

    def setup_byte_array(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_str
        #    4 MAKE_CELL len_offset
        #    6 MAKE_CELL s
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR byte_array_setting
        #   42 STORE_DEREF s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 LOAD_GLOBAL NULL + QtWidgets
        #  106 LOAD_ATTR QLineEdit
        #  116 LOAD_DEREF self
        #  118 PRECALL
        #  122 CALL
        #  132 LOAD_DEREF self
        #  134 STORE_ATTR lineedit
        #  144 LOAD_GLOBAL NULL + QtCore
        #  156 LOAD_ATTR QRegularExpression
        #  166 LOAD_CONST '[1-9, ]?'
        #  168 PRECALL
        #  172 CALL
        #  182 LOAD_DEREF self
        #  184 STORE_ATTR regexp
        #  194 LOAD_GLOBAL NULL + QtGui
        #  206 LOAD_ATTR QRegularExpressionValidator
        #  216 LOAD_DEREF self
        #  218 LOAD_ATTR regexp
        #  228 PRECALL
        #  232 CALL
        #  242 LOAD_DEREF self
        #  244 STORE_ATTR validator
        #  254 LOAD_DEREF self
        #  256 LOAD_ATTR lineedit
        #  266 LOAD_METHOD setValidator
        #  288 LOAD_DEREF self
        #  290 LOAD_ATTR validator
        #  300 PRECALL
        #  304 CALL
        #  314 POP_TOP
        #  316 LOAD_DEREF s
        #  318 LOAD_ATTR length_nvm_word
        #  328 LOAD_CONST 4
        #  330 BINARY_OP *
        #  334 LOAD_DEREF s
        #  336 LOAD_ATTR length_nvm_word_byte
        #  346 BINARY_OP +
        #  350 STORE_DEREF len_offset
        #  352 LOAD_GLOBAL NULL + struct
        #  364 LOAD_ATTR unpack_from
        #  374 LOAD_CONST '>B'
        #  376 LOAD_DEREF self
        #  378 LOAD_ATTR nvm_bytes
        #  388 LOAD_DEREF len_offset
        #  390 PRECALL
        #  394 CALL
        #  404 LOAD_CONST 0
        #  406 BINARY_SUBSCR
        #  416 STORE_FAST initial_len
        #  418 LOAD_GLOBAL NULL + min
        #  430 LOAD_FAST initial_len
        #  432 LOAD_DEREF s
        #  434 LOAD_ATTR maxiumum_length
        #  444 PRECALL
        #  448 CALL
        #  458 STORE_FAST initial_len
        #  460 LOAD_CONST '>{}B'
        #  462 LOAD_METHOD format
        #  484 LOAD_FAST initial_len
        #  486 PRECALL
        #  490 CALL
        #  500 STORE_FAST fmt
        #  502 LOAD_GLOBAL NULL + struct
        #  514 LOAD_ATTR unpack_from
        # ... bytecode truncated ...
        pass

    def setup_string(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_str
        #    4 MAKE_CELL fmt
        #    6 MAKE_CELL s
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR string_setting
        #   42 STORE_DEREF s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 LOAD_GLOBAL NULL + QtWidgets
        #  106 LOAD_ATTR QLineEdit
        #  116 LOAD_DEREF self
        #  118 PRECALL
        #  122 CALL
        #  132 LOAD_DEREF self
        #  134 STORE_ATTR lineedit
        #  144 LOAD_GLOBAL NULL + StringLengthValidator
        #  156 LOAD_DEREF s
        #  158 LOAD_ATTR maximum_length
        #  168 LOAD_DEREF self
        #  170 PRECALL
        #  174 CALL
        #  184 LOAD_DEREF self
        #  186 STORE_ATTR validator
        #  196 LOAD_DEREF self
        #  198 LOAD_ATTR lineedit
        #  208 LOAD_METHOD setValidator
        #  230 LOAD_DEREF self
        #  232 LOAD_ATTR validator
        #  242 PRECALL
        #  246 CALL
        #  256 POP_TOP
        #  258 LOAD_CONST '>{}s'
        #  260 LOAD_METHOD format
        #  282 LOAD_DEREF s
        #  284 LOAD_ATTR maximum_length
        #  294 PRECALL
        #  298 CALL
        #  308 STORE_DEREF fmt
        #  310 LOAD_GLOBAL NULL + struct
        #  322 LOAD_ATTR unpack_from
        #  332 LOAD_DEREF fmt
        #  334 LOAD_DEREF self
        #  336 LOAD_ATTR nvm_bytes
        #  346 LOAD_DEREF s
        #  348 LOAD_ATTR nvm_word
        #  358 LOAD_CONST 4
        #  360 BINARY_OP *
        #  364 PRECALL
        #  368 CALL
        #  378 LOAD_CONST 0
        #  380 BINARY_SUBSCR
        #  390 STORE_FAST raw
        #  392 LOAD_FAST raw
        #  394 LOAD_METHOD split
        #  416 LOAD_CONST b'\x00'
        #  418 LOAD_CONST 1
        #  420 PRECALL
        #  424 CALL
        #  434 LOAD_CONST 0
        #  436 BINARY_SUBSCR
        #  446 STORE_FAST raw
        #  448 LOAD_FAST raw
        #  450 LOAD_METHOD split
        #  472 LOAD_CONST b'\xff'
        #  474 LOAD_CONST 1
        #  476 PRECALL
        #  480 CALL
        #  490 LOAD_CONST 0
        #  492 BINARY_SUBSCR
        #  502 STORE_FAST raw
        #  504 NOP
        #  506 LOAD_FAST raw
        # ... bytecode truncated ...
        pass

    def setup_int32(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_value
        #    4 MAKE_CELL s
        #    6 RESUME
        #    8 LOAD_DEREF self
        #   10 LOAD_ATTR setting
        #   20 LOAD_ATTR u
        #   30 LOAD_ATTR int32_setting
        #   40 STORE_DEREF s
        #   42 LOAD_DEREF self
        #   44 LOAD_METHOD create_setting_label
        #   66 PRECALL
        #   70 CALL
        #   80 LOAD_DEREF self
        #   82 STORE_ATTR setting_label
        #   92 LOAD_GLOBAL NULL + QtWidgets
        #  104 LOAD_ATTR QSpinBox
        #  114 LOAD_DEREF self
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_DEREF self
        #  132 STORE_ATTR spinbox
        #  142 LOAD_GLOBAL NULL + struct
        #  154 LOAD_ATTR unpack_from
        #  164 LOAD_CONST '>i'
        #  166 LOAD_DEREF self
        #  168 LOAD_ATTR nvm_bytes
        #  178 LOAD_DEREF s
        #  180 LOAD_ATTR nvm_word
        #  190 LOAD_CONST 4
        #  192 BINARY_OP *
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_CONST 0
        #  212 BINARY_SUBSCR
        #  222 STORE_FAST initial
        #  224 LOAD_DEREF self
        #  226 LOAD_ATTR spinbox
        #  236 LOAD_METHOD setMinimum
        #  258 LOAD_DEREF s
        #  260 LOAD_ATTR minimum
        #  270 PRECALL
        #  274 CALL
        #  284 POP_TOP
        #  286 LOAD_DEREF self
        #  288 LOAD_ATTR spinbox
        #  298 LOAD_METHOD setMaximum
        #  320 LOAD_DEREF s
        #  322 LOAD_ATTR maximum
        #  332 PRECALL
        #  336 CALL
        #  346 POP_TOP
        #  348 LOAD_DEREF self
        #  350 LOAD_ATTR spinbox
        #  360 LOAD_METHOD setValue
        #  382 LOAD_FAST initial
        #  384 PRECALL
        #  388 CALL
        #  398 POP_TOP
        #  400 LOAD_GLOBAL NULL + len
        #  412 LOAD_DEREF self
        #  414 LOAD_ATTR default_bytes
        #  424 PRECALL
        #  428 CALL
        #  438 LOAD_CONST 4
        #  440 COMPARE_OP ==
        #  446 POP_JUMP_FORWARD_IF_FALSE to 586
        #  448 LOAD_GLOBAL NULL + struct
        #  460 LOAD_ATTR unpack_from
        #  470 LOAD_CONST '>i'
        #  472 LOAD_DEREF self
        #  474 LOAD_ATTR default_bytes
        #  484 LOAD_CONST 0
        #  486 PRECALL
        #  490 CALL
        #  500 LOAD_CONST 0
        #  502 BINARY_SUBSCR
        #  512 STORE_DEREF default_value
        #  514 LOAD_CONST '{}'
        #  516 LOAD_METHOD format
        # ... bytecode truncated ...
        pass

    def setup_int32_scaled(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_value
        #    4 MAKE_CELL inverted
        #    6 MAKE_CELL s
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR int32_scaled_setting
        #   42 STORE_DEREF s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 LOAD_DEREF s
        #   96 LOAD_ATTR minimum
        #  106 LOAD_DEREF s
        #  108 LOAD_ATTR scale
        #  118 BINARY_OP *
        #  122 LOAD_DEREF s
        #  124 LOAD_ATTR offset
        #  134 BINARY_OP +
        #  138 STORE_FAST scaled_min
        #  140 LOAD_DEREF s
        #  142 LOAD_ATTR maximum
        #  152 LOAD_DEREF s
        #  154 LOAD_ATTR scale
        #  164 BINARY_OP *
        #  168 LOAD_DEREF s
        #  170 LOAD_ATTR offset
        #  180 BINARY_OP +
        #  184 STORE_FAST scaled_max
        #  186 LOAD_GLOBAL asphodel
        #  198 LOAD_ATTR nativelib
        #  208 LOAD_METHOD create_unit_formatter
        #  230 LOAD_DEREF s
        #  232 LOAD_ATTR unit_type
        #  242 LOAD_FAST scaled_min
        #  244 LOAD_FAST scaled_max
        #  246 LOAD_DEREF s
        #  248 LOAD_ATTR scale
        #  258 PRECALL
        #  262 CALL
        #  272 STORE_FAST unit_formatter
        #  274 LOAD_FAST unit_formatter
        #  276 COPY
        #  278 LOAD_ATTR conversion_offset
        #  288 LOAD_DEREF s
        #  290 LOAD_ATTR offset
        #  300 LOAD_FAST unit_formatter
        #  302 LOAD_ATTR conversion_scale
        #  312 BINARY_OP *
        #  316 BINARY_OP +=
        #  320 SWAP
        #  322 STORE_ATTR conversion_offset
        #  332 LOAD_FAST unit_formatter
        #  334 COPY
        #  336 LOAD_ATTR conversion_scale
        #  346 LOAD_DEREF s
        #  348 LOAD_ATTR scale
        #  358 BINARY_OP *=
        #  362 SWAP
        #  364 STORE_ATTR conversion_scale
        #  374 LOAD_FAST unit_formatter
        #  376 LOAD_ATTR conversion_scale
        #  386 LOAD_CONST 0.0
        #  388 COMPARE_OP <
        #  394 POP_JUMP_FORWARD_IF_FALSE to 428
        #  396 LOAD_CONST True
        #  398 STORE_DEREF inverted
        #  400 LOAD_FAST unit_formatter
        #  402 LOAD_ATTR conversion_scale
        #  412 UNARY_NEGATIVE
        #  414 LOAD_FAST unit_formatter
        #  416 STORE_ATTR conversion_scale
        #  426 JUMP_FORWARD to 432
        #  428 LOAD_CONST False
        #  430 STORE_DEREF inverted
        # ... bytecode truncated ...
        pass

    def setup_float(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_value
        #    4 MAKE_CELL inverted
        #    6 MAKE_CELL s
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR float_setting
        #   42 STORE_DEREF s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 LOAD_DEREF s
        #   96 LOAD_ATTR minimum
        #  106 LOAD_DEREF s
        #  108 LOAD_ATTR scale
        #  118 BINARY_OP *
        #  122 LOAD_DEREF s
        #  124 LOAD_ATTR offset
        #  134 BINARY_OP +
        #  138 STORE_FAST scaled_min
        #  140 LOAD_DEREF s
        #  142 LOAD_ATTR maximum
        #  152 LOAD_DEREF s
        #  154 LOAD_ATTR scale
        #  164 BINARY_OP *
        #  168 LOAD_DEREF s
        #  170 LOAD_ATTR offset
        #  180 BINARY_OP +
        #  184 STORE_FAST scaled_max
        #  186 LOAD_GLOBAL asphodel
        #  198 LOAD_ATTR nativelib
        #  208 LOAD_METHOD create_unit_formatter
        #  230 LOAD_DEREF s
        #  232 LOAD_ATTR unit_type
        #  242 LOAD_FAST scaled_min
        #  244 LOAD_FAST scaled_max
        #  246 LOAD_CONST 0
        #  248 PRECALL
        #  252 CALL
        #  262 STORE_FAST unit_formatter
        #  264 LOAD_FAST unit_formatter
        #  266 COPY
        #  268 LOAD_ATTR conversion_offset
        #  278 LOAD_DEREF s
        #  280 LOAD_ATTR offset
        #  290 LOAD_FAST unit_formatter
        #  292 LOAD_ATTR conversion_scale
        #  302 BINARY_OP *
        #  306 BINARY_OP +=
        #  310 SWAP
        #  312 STORE_ATTR conversion_offset
        #  322 LOAD_FAST unit_formatter
        #  324 COPY
        #  326 LOAD_ATTR conversion_scale
        #  336 LOAD_DEREF s
        #  338 LOAD_ATTR scale
        #  348 BINARY_OP *=
        #  352 SWAP
        #  354 STORE_ATTR conversion_scale
        #  364 LOAD_FAST unit_formatter
        #  366 LOAD_ATTR conversion_scale
        #  376 LOAD_CONST 0.0
        #  378 COMPARE_OP <
        #  384 POP_JUMP_FORWARD_IF_FALSE to 418
        #  386 LOAD_CONST True
        #  388 STORE_DEREF inverted
        #  390 LOAD_FAST unit_formatter
        #  392 LOAD_ATTR conversion_scale
        #  402 UNARY_NEGATIVE
        #  404 LOAD_FAST unit_formatter
        #  406 STORE_ATTR conversion_scale
        #  416 JUMP_FORWARD to 422
        #  418 LOAD_CONST False
        #  420 STORE_DEREF inverted
        #  422 LOAD_GLOBAL NULL + UnitFormatterDoubleSpinBox
        # ... bytecode truncated ...
        pass

    def setup_float_array(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL default_str
        #    4 MAKE_CELL len_offset
        #    6 MAKE_CELL offset
        #    8 MAKE_CELL s
        #   10 MAKE_CELL scale
        #   12 RESUME
        #   14 LOAD_DEREF self
        #   16 LOAD_ATTR setting
        #   26 LOAD_ATTR u
        #   36 LOAD_ATTR float_array_setting
        #   46 STORE_DEREF s
        #   48 LOAD_DEREF self
        #   50 LOAD_METHOD create_setting_label
        #   72 PRECALL
        #   76 CALL
        #   86 LOAD_DEREF self
        #   88 STORE_ATTR setting_label
        #   98 LOAD_GLOBAL NULL + QtWidgets
        #  110 LOAD_ATTR QLineEdit
        #  120 LOAD_DEREF self
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_DEREF self
        #  138 STORE_ATTR lineedit
        #  148 LOAD_GLOBAL NULL + QtCore
        #  160 LOAD_ATTR QRegularExpression
        #  170 LOAD_CONST '[1-9, .e\\-]?'
        #  172 PRECALL
        #  176 CALL
        #  186 LOAD_DEREF self
        #  188 STORE_ATTR regexp
        #  198 LOAD_GLOBAL NULL + QtGui
        #  210 LOAD_ATTR QRegularExpressionValidator
        #  220 LOAD_DEREF self
        #  222 LOAD_ATTR regexp
        #  232 PRECALL
        #  236 CALL
        #  246 LOAD_DEREF self
        #  248 STORE_ATTR validator
        #  258 LOAD_DEREF self
        #  260 LOAD_ATTR lineedit
        #  270 LOAD_METHOD setValidator
        #  292 LOAD_DEREF self
        #  294 LOAD_ATTR validator
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 LOAD_DEREF s
        #  322 LOAD_ATTR minimum
        #  332 LOAD_DEREF s
        #  334 LOAD_ATTR scale
        #  344 BINARY_OP *
        #  348 LOAD_DEREF s
        #  350 LOAD_ATTR offset
        #  360 BINARY_OP +
        #  364 STORE_FAST scaled_min
        #  366 LOAD_DEREF s
        #  368 LOAD_ATTR maximum
        #  378 LOAD_DEREF s
        #  380 LOAD_ATTR scale
        #  390 BINARY_OP *
        #  394 LOAD_DEREF s
        #  396 LOAD_ATTR offset
        #  406 BINARY_OP +
        #  410 STORE_FAST scaled_max
        #  412 LOAD_GLOBAL asphodel
        #  424 LOAD_ATTR nativelib
        #  434 LOAD_METHOD create_unit_formatter
        #  456 LOAD_DEREF s
        #  458 LOAD_ATTR unit_type
        #  468 LOAD_FAST scaled_min
        #  470 LOAD_FAST scaled_max
        #  472 LOAD_CONST 0
        #  474 PRECALL
        #  478 CALL
        #  488 STORE_FAST unit_formatter
        #  490 LOAD_FAST unit_formatter
        #  492 LOAD_ATTR conversion_scale
        #  502 LOAD_DEREF s
        # ... bytecode truncated ...
        pass

    def setup_custom_enum(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL byte_offset
        #    4 MAKE_CELL default_index
        #    6 MAKE_CELL option_values
        #    8 RESUME
        #   10 LOAD_DEREF self
        #   12 LOAD_ATTR setting
        #   22 LOAD_ATTR u
        #   32 LOAD_ATTR custom_enum_setting
        #   42 STORE_FAST s
        #   44 LOAD_DEREF self
        #   46 LOAD_METHOD create_setting_label
        #   68 PRECALL
        #   72 CALL
        #   82 LOAD_DEREF self
        #   84 STORE_ATTR setting_label
        #   94 BUILD_LIST
        #   96 STORE_DEREF option_values
        #   98 LOAD_GLOBAL NULL + QtWidgets
        #  110 LOAD_ATTR QComboBox
        #  120 LOAD_DEREF self
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_DEREF self
        #  138 STORE_ATTR combo_box
        #  148 LOAD_GLOBAL NULL + enumerate
        #  160 LOAD_DEREF self
        #  162 LOAD_ATTR custom_enums
        #  172 LOAD_FAST s
        #  174 LOAD_ATTR custom_enum_index
        #  184 BINARY_SUBSCR
        #  194 PRECALL
        #  198 CALL
        #  208 GET_ITER
        #  210 FOR_ITER to 318
        #  212 UNPACK_SEQUENCE
        #  216 STORE_FAST i
        #  218 STORE_FAST name
        #  220 LOAD_DEREF option_values
        #  222 LOAD_METHOD append
        #  244 LOAD_FAST i
        #  246 PRECALL
        #  250 CALL
        #  260 POP_TOP
        #  262 LOAD_DEREF self
        #  264 LOAD_ATTR combo_box
        #  274 LOAD_METHOD insertItem
        #  296 LOAD_FAST i
        #  298 LOAD_FAST name
        #  300 PRECALL
        #  304 CALL
        #  314 POP_TOP
        #  316 JUMP_BACKWARD to 210
        #  318 LOAD_FAST s
        #  320 LOAD_ATTR nvm_word
        #  330 LOAD_CONST 4
        #  332 BINARY_OP *
        #  336 LOAD_FAST s
        #  338 LOAD_ATTR nvm_word_byte
        #  348 BINARY_OP +
        #  352 STORE_DEREF byte_offset
        #  354 LOAD_GLOBAL NULL + struct
        #  366 LOAD_ATTR unpack_from
        #  376 LOAD_CONST '>B'
        #  378 LOAD_DEREF self
        #  380 LOAD_ATTR nvm_bytes
        #  390 LOAD_DEREF byte_offset
        #  392 PRECALL
        #  396 CALL
        #  406 LOAD_CONST 0
        #  408 BINARY_SUBSCR
        #  418 STORE_FAST initial
        #  420 NOP
        #  422 LOAD_DEREF option_values
        #  424 LOAD_METHOD index
        #  446 LOAD_FAST initial
        #  448 PRECALL
        #  452 CALL
        #  462 STORE_FAST initial_index
        #  464 JUMP_FORWARD to 666
        # ... bytecode truncated ...
        pass
