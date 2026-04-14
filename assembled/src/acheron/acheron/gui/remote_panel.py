# Source Generated with Decompyle++
# File: remote_panel.pyc (Python 3.11)

from __future__ import annotations
import logging
from PySide6 import QtCore, QtWidgets
from .ui.ui_remote_panel import Ui_RemotePanel
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RemotePanel(Ui_RemotePanel, QtWidgets.QGroupBox):

    show_radio_clicked = QtCore.Signal()

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
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR goToParentButton
        #  124 LOAD_ATTR clicked
        #  134 LOAD_METHOD connect
        #  156 LOAD_FAST self
        #  158 LOAD_ATTR show_radio_clicked
        #  168 PRECALL
        #  172 CALL
        #  182 POP_TOP
        #  184 LOAD_CONST None
        #  186 RETURN_VALUE
        pass
