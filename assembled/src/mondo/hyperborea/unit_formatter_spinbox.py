# Source Generated with Decompyle++
# File: unit_formatter_spinbox.pyc (Python 3.11)

import math
from typing import Optional
from PySide6 import QtGui, QtWidgets
import asphodel

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class UnitFormatterSpinBox(QtWidgets.QSpinBox):

    def __init__(self, parent):
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
        #   70 LOAD_GLOBAL asphodel
        #   82 LOAD_ATTR nativelib
        #   92 LOAD_METHOD create_custom_unit_formatter
        #  114 LOAD_CONST 1.0
        #  116 LOAD_CONST 0.0
        #  118 LOAD_CONST 0.0
        #  120 LOAD_CONST ''
        #  122 LOAD_CONST ''
        #  124 LOAD_CONST ''
        #  126 PRECALL
        #  130 CALL
        #  140 LOAD_FAST self
        #  142 STORE_ATTR unit_formatter
        #  152 LOAD_GLOBAL NULL + QtGui
        #  164 LOAD_ATTR QDoubleValidator
        #  174 LOAD_FAST self
        #  176 PRECALL
        #  180 CALL
        #  190 LOAD_FAST self
        #  192 STORE_ATTR validator
        #  202 LOAD_FAST self
        #  204 LOAD_METHOD set_unit_formatter
        #  226 LOAD_CONST None
        #  228 PRECALL
        #  232 CALL
        #  242 POP_TOP
        #  244 LOAD_CONST None
        #  246 RETURN_VALUE
        pass

    def set_unit_formatter(self, unit_formatter):
        value = self.value()
        minimum = self.minimum()
        maximum = self.maximum()
        scaled_value = value * self.unit_formatter.conversion_scale + self.unit_formatter.conversion_offset

    def setMinimum(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST value
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR unit_formatter
        #   18 LOAD_ATTR conversion_scale
        #   28 BINARY_OP *
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR unit_formatter
        #   44 LOAD_ATTR conversion_offset
        #   54 BINARY_OP +
        #   58 STORE_FAST scaled_value
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR validator
        #   72 LOAD_METHOD setBottom
        #   94 LOAD_FAST scaled_value
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL NULL + super
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_METHOD setMinimum
        #  160 LOAD_FAST value
        #  162 PRECALL
        #  166 CALL
        #  176 RETURN_VALUE
        pass

    def setMaximum(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST value
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR unit_formatter
        #   18 LOAD_ATTR conversion_scale
        #   28 BINARY_OP *
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR unit_formatter
        #   44 LOAD_ATTR conversion_offset
        #   54 BINARY_OP +
        #   58 STORE_FAST scaled_value
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR validator
        #   72 LOAD_METHOD setTop
        #   94 LOAD_FAST scaled_value
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL NULL + super
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_METHOD setMaximum
        #  160 LOAD_FAST value
        #  162 PRECALL
        #  166 CALL
        #  176 RETURN_VALUE
        pass

    def textFromValue(self, value):
        scaled_value = value * self.unit_formatter.conversion_scale + self.unit_formatter.conversion_offset
        return self.unit_formatter.format_bare(scaled_value)

    def valueFromText(self, text):
        if self.suffix():
            s = text.rsplit(self.suffix(), 1)[0]
        else:
            s = text
        scaled_value = float(s)
        value = (scaled_value - self.unit_formatter.conversion_offset) / self.unit_formatter.conversion_scale
        return round(value)

    def validate(self, input_text, pos):
        if self.suffix():
            remove_suffix = input_text.endswith(self.suffix())
            if remove_suffix:
                s = input_text.rsplit(self.suffix(), 1)[0]
            else:
                s = input_text
        else:
            remove_suffix = False
            s = input_text
        ret = self.validator.validate(s, pos)
        if remove_suffix:
            return (ret[0], ret[1] + self.suffix(), ret[2])

class UnitFormatterDoubleSpinBox(QtWidgets.QDoubleSpinBox):

    def __init__(self, parent):
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
        #   70 LOAD_GLOBAL asphodel
        #   82 LOAD_ATTR nativelib
        #   92 LOAD_METHOD create_custom_unit_formatter
        #  114 LOAD_CONST 1.0
        #  116 LOAD_CONST 0.0
        #  118 LOAD_CONST 0.0
        #  120 LOAD_CONST ''
        #  122 LOAD_CONST ''
        #  124 LOAD_CONST ''
        #  126 PRECALL
        #  130 CALL
        #  140 LOAD_FAST self
        #  142 STORE_ATTR unit_formatter
        #  152 LOAD_GLOBAL NULL + QtGui
        #  164 LOAD_ATTR QDoubleValidator
        #  174 LOAD_FAST self
        #  176 PRECALL
        #  180 CALL
        #  190 LOAD_FAST self
        #  192 STORE_ATTR validator
        #  202 LOAD_FAST self
        #  204 LOAD_METHOD setDecimals
        #  226 LOAD_CONST 1000
        #  228 PRECALL
        #  232 CALL
        #  242 POP_TOP
        #  244 LOAD_FAST self
        #  246 LOAD_METHOD set_unit_formatter
        #  268 LOAD_CONST None
        #  270 PRECALL
        #  274 CALL
        #  284 POP_TOP
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        pass

    def set_unit_formatter(self, unit_formatter):
        value = self.value()
        minimum = self.minimum()
        maximum = self.maximum()
        scaled_value = value * self.unit_formatter.conversion_scale + self.unit_formatter.conversion_offset

    def setMinimum(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST value
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR unit_formatter
        #   18 LOAD_ATTR conversion_scale
        #   28 BINARY_OP *
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR unit_formatter
        #   44 LOAD_ATTR conversion_offset
        #   54 BINARY_OP +
        #   58 STORE_FAST scaled_value
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR validator
        #   72 LOAD_METHOD setBottom
        #   94 LOAD_FAST scaled_value
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL NULL + super
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_METHOD setMinimum
        #  160 LOAD_FAST value
        #  162 PRECALL
        #  166 CALL
        #  176 RETURN_VALUE
        pass

    def setMaximum(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST value
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR unit_formatter
        #   18 LOAD_ATTR conversion_scale
        #   28 BINARY_OP *
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR unit_formatter
        #   44 LOAD_ATTR conversion_offset
        #   54 BINARY_OP +
        #   58 STORE_FAST scaled_value
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR validator
        #   72 LOAD_METHOD setTop
        #   94 LOAD_FAST scaled_value
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL NULL + super
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_METHOD setMaximum
        #  160 LOAD_FAST value
        #  162 PRECALL
        #  166 CALL
        #  176 RETURN_VALUE
        pass

    def textFromValue(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR unit_formatter
        #   14 POP_JUMP_FORWARD_IF_FALSE to 124
        #   16 LOAD_FAST value
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR unit_formatter
        #   30 LOAD_ATTR conversion_scale
        #   40 BINARY_OP *
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR unit_formatter
        #   56 LOAD_ATTR conversion_offset
        #   66 BINARY_OP +
        #   70 STORE_FAST scaled_value
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR unit_formatter
        #   84 LOAD_METHOD format_bare
        #  106 LOAD_FAST scaled_value
        #  108 PRECALL
        #  112 CALL
        #  122 RETURN_VALUE
        #  124 LOAD_GLOBAL NULL + str
        #  136 LOAD_FAST value
        #  138 PRECALL
        #  142 CALL
        #  152 RETURN_VALUE
        pass

    def valueFromText(self, text):
        if self.suffix():
            s = text.rsplit(self.suffix(), 1)[0]
        else:
            s = text
        scaled_value = float(s)
        value = (scaled_value - self.unit_formatter.conversion_offset) / self.unit_formatter.conversion_scale
        return value

    def validate(self, input_text, pos):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD suffix
        #   26 PRECALL
        #   30 CALL
        #   40 POP_JUMP_FORWARD_IF_FALSE to 224
        #   42 LOAD_FAST input_text
        #   44 LOAD_METHOD endswith
        #   66 LOAD_FAST self
        #   68 LOAD_METHOD suffix
        #   90 PRECALL
        #   94 CALL
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST remove_suffix
        #  120 LOAD_FAST remove_suffix
        #  122 POP_JUMP_FORWARD_IF_FALSE to 218
        #  124 LOAD_FAST input_text
        #  126 LOAD_METHOD rsplit
        #  148 LOAD_FAST self
        #  150 LOAD_METHOD suffix
        #  172 PRECALL
        #  176 CALL
        #  186 LOAD_CONST 1
        #  188 PRECALL
        #  192 CALL
        #  202 LOAD_CONST 0
        #  204 BINARY_SUBSCR
        #  214 STORE_FAST s
        #  216 JUMP_FORWARD to 232
        #  218 LOAD_FAST input_text
        #  220 STORE_FAST s
        #  222 JUMP_FORWARD to 232
        #  224 LOAD_CONST False
        #  226 STORE_FAST remove_suffix
        #  228 LOAD_FAST input_text
        #  230 STORE_FAST s
        #  232 LOAD_GLOBAL NULL + math
        #  244 LOAD_ATTR isinf
        #  254 LOAD_FAST self
        #  256 LOAD_ATTR validator
        #  266 LOAD_METHOD bottom
        #  288 PRECALL
        #  292 CALL
        #  302 PRECALL
        #  306 CALL
        #  316 POP_JUMP_FORWARD_IF_FALSE to 472
        #  318 LOAD_FAST s
        #  320 LOAD_CONST '-inf'
        #  322 COMPARE_OP ==
        #  328 POP_JUMP_FORWARD_IF_FALSE to 380
        #  330 LOAD_GLOBAL QtGui
        #  342 LOAD_ATTR QValidator
        #  352 LOAD_ATTR State
        #  362 LOAD_ATTR Acceptable
        #  372 LOAD_FAST input_text
        #  374 LOAD_FAST pos
        #  376 BUILD_TUPLE
        #  378 RETURN_VALUE
        #  380 LOAD_CONST '-inf'
        #  382 LOAD_METHOD startswith
        #  404 LOAD_FAST s
        #  406 PRECALL
        #  410 CALL
        #  420 POP_JUMP_FORWARD_IF_FALSE to 472
        #  422 LOAD_GLOBAL QtGui
        #  434 LOAD_ATTR QValidator
        #  444 LOAD_ATTR State
        #  454 LOAD_ATTR Intermediate
        #  464 LOAD_FAST input_text
        #  466 LOAD_FAST pos
        #  468 BUILD_TUPLE
        #  470 RETURN_VALUE
        #  472 LOAD_GLOBAL NULL + math
        #  484 LOAD_ATTR isinf
        #  494 LOAD_FAST self
        #  496 LOAD_ATTR validator
        #  506 LOAD_METHOD top
        #  528 PRECALL
        #  532 CALL
        # ... bytecode truncated ...
        pass
