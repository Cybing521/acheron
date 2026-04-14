# Source Generated with Decompyle++
# File: about.pyc (Python 3.11)

import importlib
import logging
import sys
from typing import Optional
from PySide6 import QtWidgets
import asphodel
from .. import build_info
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
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST self
        #   72 LOAD_METHOD setupUi
        #   94 LOAD_FAST self
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL QtWidgets
        #  124 LOAD_ATTR QApplication
        #  134 LOAD_METHOD applicationVersion
        #  156 PRECALL
        #  160 CALL
        #  170 STORE_FAST version
        #  172 LOAD_FAST self
        #  174 LOAD_METHOD tr
        #  196 LOAD_CONST 'Version: {}'
        #  198 PRECALL
        #  202 CALL
        #  212 LOAD_METHOD format
        #  234 LOAD_FAST version
        #  236 PRECALL
        #  240 CALL
        #  250 STORE_FAST label_str
        #  252 LOAD_FAST self
        #  254 LOAD_ATTR version
        #  264 LOAD_METHOD setText
        #  286 LOAD_FAST label_str
        #  288 PRECALL
        #  292 CALL
        #  302 POP_TOP
        #  304 LOAD_GLOBAL NULL + build_info
        #  316 LOAD_ATTR get_build_date
        #  326 PRECALL
        #  330 CALL
        #  340 STORE_FAST build_date
        #  342 LOAD_FAST build_date
        #  344 POP_JUMP_FORWARD_IF_FALSE to 476
        #  346 LOAD_FAST self
        #  348 LOAD_ATTR buildDate
        #  358 LOAD_METHOD setText
        #  380 LOAD_FAST self
        #  382 LOAD_METHOD tr
        #  404 LOAD_CONST 'Build Date: {}'
        #  406 PRECALL
        #  410 CALL
        #  420 LOAD_METHOD format
        #  442 LOAD_FAST build_date
        #  444 PRECALL
        #  448 CALL
        #  458 PRECALL
        #  462 CALL
        #  472 POP_TOP
        #  474 JUMP_FORWARD to 528
        #  476 LOAD_FAST self
        #  478 LOAD_ATTR buildDate
        #  488 LOAD_METHOD setVisible
        #  510 LOAD_CONST False
        #  512 PRECALL
        #  516 CALL
        #  526 POP_TOP
        #  528 LOAD_FAST self
        #  530 LOAD_METHOD update_library_versions
        #  552 PRECALL
        #  556 CALL
        #  566 POP_TOP
        #  568 LOAD_FAST self
        #  570 LOAD_METHOD layout
        #  592 PRECALL
        #  596 CALL
        #  606 LOAD_METHOD setSizeConstraint
        #  628 LOAD_GLOBAL QtWidgets
        # ... bytecode truncated ...
        pass

    def get_version(self, library):
        try:
            lib = importlib.import_module(library)
            return lib.__version__
        except (AttributeError, ImportError):
            return 'ERROR'

    def update_library_versions(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL vers
        #    2 RESUME
        #    4 BUILD_LIST
        #    6 LOAD_CONST ('boto3', 'diskcache', 'hyperborea', 'numpy', 'psutil', 'pymodbus', 'pyqtgraph', 'PySide6', 'requests', 'serial', 'setproctitle')
        #    8 LIST_EXTEND
        #   10 STORE_FAST libraries
        #   12 BUILD_MAP
        #   14 STORE_DEREF vers
        #   16 LOAD_FAST libraries
        #   18 GET_ITER
        #   20 FOR_ITER to 74
        #   22 STORE_FAST lib
        #   24 LOAD_FAST self
        #   26 LOAD_METHOD get_version
        #   48 LOAD_FAST lib
        #   50 PRECALL
        #   54 CALL
        #   64 LOAD_DEREF vers
        #   66 LOAD_FAST lib
        #   68 STORE_SUBSCR
        #   72 JUMP_BACKWARD to 20
        #   74 LOAD_FAST self
        #   76 LOAD_METHOD get_version
        #   98 LOAD_CONST 'asphodel'
        #  100 PRECALL
        #  104 CALL
        #  114 LOAD_DEREF vers
        #  116 LOAD_CONST 'asphodel_py'
        #  118 STORE_SUBSCR
        #  122 LOAD_GLOBAL asphodel
        #  134 LOAD_ATTR build_info
        #  144 LOAD_DEREF vers
        #  146 LOAD_CONST 'asphodel'
        #  148 STORE_SUBSCR
        #  152 LOAD_GLOBAL sys
        #  164 LOAD_ATTR maxsize
        #  174 LOAD_CONST 4294967296
        #  176 COMPARE_OP >
        #  182 STORE_FAST is_64bit
        #  184 LOAD_FAST is_64bit
        #  186 POP_JUMP_FORWARD_IF_FALSE to 192
        #  188 LOAD_CONST '64 bit'
        #  190 JUMP_FORWARD to 194
        #  192 LOAD_CONST '32 bit'
        #  194 STORE_FAST bit_str
        #  196 LOAD_CONST '.'
        #  198 LOAD_METHOD join
        #  220 LOAD_GLOBAL NULL + map
        #  232 LOAD_GLOBAL str
        #  244 LOAD_GLOBAL sys
        #  256 LOAD_ATTR version_info
        #  266 LOAD_CONST None
        #  268 LOAD_CONST 3
        #  270 BUILD_SLICE
        #  272 BINARY_SUBSCR
        #  282 PRECALL
        #  286 CALL
        #  296 PRECALL
        #  300 CALL
        #  310 STORE_FAST python_ver
        #  312 LOAD_CONST '{} ({} {})'
        #  314 LOAD_METHOD format
        #  336 LOAD_FAST python_ver
        #  338 LOAD_GLOBAL sys
        #  350 LOAD_ATTR platform
        #  360 LOAD_FAST bit_str
        #  362 PRECALL
        #  366 CALL
        #  376 STORE_FAST python_str
        #  378 LOAD_FAST python_str
        #  380 LOAD_DEREF vers
        #  382 LOAD_CONST 'python'
        #  384 STORE_SUBSCR
        #  388 LOAD_CONST '\n'
        #  390 LOAD_METHOD join
        #  412 LOAD_CLOSURE vers
        #  414 BUILD_TUPLE
        #  416 LOAD_CONST <code object <genexpr> at 0x105abfe10, file "acheron\gui\about.py", line 66>
        #  418 MAKE_FUNCTION closure
        #  420 LOAD_GLOBAL NULL + sorted
        # ... bytecode truncated ...
        pass
