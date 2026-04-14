# Source Generated with Decompyle++
# File: unit_selection_dialog.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtCore, QtWidgets
import asphodel
from . import unit_preferences
from .ui.ui_unit_selection_dialog import Ui_UnitSelectionDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class UnitSelectionDialog(Ui_UnitSelectionDialog, QtWidgets.QDialog):

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
        #   70 BUILD_MAP
        #   72 LOAD_FAST self
        #   74 STORE_ATTR unit_info
        #   84 LOAD_FAST self
        #   86 LOAD_METHOD setupUi
        #  108 LOAD_FAST self
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_METHOD add_radio_buttons
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 LOAD_FAST self
        #  168 LOAD_METHOD values_updated
        #  190 PRECALL
        #  194 CALL
        #  204 POP_TOP
        #  206 LOAD_CONST None
        #  208 RETURN_VALUE
        pass

    def add_radio_buttons(self):
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.buttonClicked.connect(self.values_updated)

    def is_valid(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR button_group
        #   14 LOAD_METHOD checkedButton
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_NOT_NONE to 56
        #   52 LOAD_CONST False
        #   54 RETURN_VALUE
        #   56 LOAD_CONST True
        #   58 RETURN_VALUE
        pass

    def done(self, r):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST r
        #    6 POP_JUMP_FORWARD_IF_FALSE to 52
        #    8 LOAD_FAST self
        #   10 LOAD_METHOD is_valid
        #   32 PRECALL
        #   36 CALL
        #   46 POP_JUMP_FORWARD_IF_TRUE to 52
        #   48 LOAD_CONST None
        #   50 RETURN_VALUE
        #   52 LOAD_GLOBAL NULL + super
        #   64 PRECALL
        #   68 CALL
        #   78 LOAD_METHOD done
        #  100 LOAD_FAST r
        #  102 PRECALL
        #  106 CALL
        #  116 POP_TOP
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass

    def values_updated(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR buttonBox
        #   14 LOAD_METHOD button
        #   36 LOAD_GLOBAL QtWidgets
        #   48 LOAD_ATTR QDialogButtonBox
        #   58 LOAD_ATTR StandardButton
        #   68 LOAD_ATTR Ok
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST ok_button
        #   94 LOAD_FAST self
        #   96 LOAD_METHOD is_valid
        #  118 PRECALL
        #  122 CALL
        #  132 POP_JUMP_FORWARD_IF_FALSE to 180
        #  134 LOAD_FAST ok_button
        #  136 LOAD_METHOD setEnabled
        #  158 LOAD_CONST True
        #  160 PRECALL
        #  164 CALL
        #  174 POP_TOP
        #  176 LOAD_CONST None
        #  178 RETURN_VALUE
        #  180 LOAD_FAST ok_button
        #  182 LOAD_METHOD setEnabled
        #  204 LOAD_CONST False
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        pass

    def get_unit_info(self):
        button = self.button_group.checkedButton()
        if button in self.unit_info:
            return self.unit_info[button]
