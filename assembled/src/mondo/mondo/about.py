# Source Generated with Decompyle++
# File: about.pyc (Python 3.11)

import logging
import os
import sys
from typing import Optional
from PySide6 import QtCore, QtWidgets
from . import __version__ as version
from .ui.ui_about import Ui_AboutDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class AboutDialog(Ui_AboutDialog, QtWidgets.QDialog):

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
        #   54 LOAD_GLOBAL QtCore
        #   66 LOAD_ATTR Qt
        #   76 LOAD_ATTR WindowType
        #   86 LOAD_ATTR MSWindowsFixedSizeDialogHint
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_FAST self
        #  114 LOAD_METHOD setupUi
        #  136 LOAD_FAST self
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_GLOBAL NULL + getattr
        #  166 LOAD_GLOBAL sys
        #  178 LOAD_CONST 'frozen'
        #  180 LOAD_CONST False
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST is_frozen
        #  198 LOAD_FAST is_frozen
        #  200 POP_JUMP_FORWARD_IF_FALSE to 616
        #  202 LOAD_GLOBAL os
        #  214 LOAD_ATTR path
        #  224 LOAD_METHOD dirname
        #  246 LOAD_GLOBAL sys
        #  258 LOAD_ATTR executable
        #  268 PRECALL
        #  272 CALL
        #  282 STORE_FAST main_dir
        #  284 LOAD_GLOBAL os
        #  296 LOAD_ATTR path
        #  306 LOAD_METHOD join
        #  328 LOAD_FAST main_dir
        #  330 LOAD_CONST 'build_info.txt'
        #  332 PRECALL
        #  336 CALL
        #  346 STORE_FAST build_info_filename
        #  348 NOP
        #  350 LOAD_GLOBAL NULL + open
        #  362 LOAD_FAST build_info_filename
        #  364 LOAD_CONST 'r'
        #  366 LOAD_CONST 'utf-8'
        #  368 KW_NAMES
        #  370 PRECALL
        #  374 CALL
        #  384 BEFORE_WITH
        #  386 STORE_FAST f
        #  388 LOAD_FAST f
        #  390 LOAD_METHOD readlines
        #  412 PRECALL
        #  416 CALL
        #  426 STORE_FAST lines
        #  428 LOAD_FAST lines
        #  430 LOAD_CONST 3
        #  432 BINARY_SUBSCR
        #  442 LOAD_METHOD strip
        #  464 PRECALL
        #  468 CALL
        #  478 STORE_FAST build_date
        #  480 LOAD_CONST None
        #  482 LOAD_CONST None
        #  484 LOAD_CONST None
        #  486 PRECALL
        #  490 CALL
        #  500 POP_TOP
        #  502 JUMP_FORWARD to 526
        #  504 PUSH_EXC_INFO
        #  506 WITH_EXCEPT_START
        #  508 POP_JUMP_FORWARD_IF_TRUE to 518
        #  510 RERAISE
        #  512 COPY
        #  514 POP_EXCEPT
        # ... bytecode truncated ...
        pass
