# Source Generated with Decompyle++
# File: ctrl_var_panel.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtWidgets
from .ui.ui_ctrl_var_panel import Ui_CtrlVarPanel
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class CtrlVarPanel(Ui_CtrlVarPanel, QtWidgets.QGroupBox):

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
        #   70 LOAD_FAST self
        #   72 LOAD_METHOD setupUi
        #   94 LOAD_FAST self
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_CONST None
        #  114 RETURN_VALUE
        pass

    def add_ctrl_var_widget(self, widget):
        self.ctrlVarLayout.addWidget(widget)

    def clear_ctrl_var_widgets(self):
        item = self.ctrlVarLayout.takeAt(0)
        if not item:
            return None
