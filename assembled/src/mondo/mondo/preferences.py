# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtCore, QtWidgets
from hyperborea.dark_mode import set_style
from hyperborea.preferences import read_bool_setting, write_bool_setting
from .ui.ui_preferences import Ui_PreferencesDialog
logger = logging.getLogger(__name__)
original_palette = None

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class PreferencesDialog(Ui_PreferencesDialog, QtWidgets.QDialog):

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
        #   70 LOAD_GLOBAL NULL + QtCore
        #   82 LOAD_ATTR QSettings
        #   92 PRECALL
        #   96 CALL
        #  106 LOAD_FAST self
        #  108 STORE_ATTR settings
        #  118 LOAD_FAST self
        #  120 LOAD_METHOD setupUi
        #  142 LOAD_FAST self
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR tabWidget
        #  172 LOAD_METHOD setCurrentIndex
        #  194 LOAD_CONST 0
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR accepted
        #  224 LOAD_METHOD connect
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR write_settings
        #  258 PRECALL
        #  262 CALL
        #  272 POP_TOP
        #  274 LOAD_FAST self
        #  276 LOAD_ATTR darkMode
        #  286 LOAD_ATTR toggled
        #  296 LOAD_METHOD connect
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR dark_mode_updated
        #  330 PRECALL
        #  334 CALL
        #  344 POP_TOP
        #  346 LOAD_FAST self
        #  348 LOAD_ATTR lightMode
        #  358 LOAD_ATTR toggled
        #  368 LOAD_METHOD connect
        #  390 LOAD_FAST self
        #  392 LOAD_ATTR dark_mode_updated
        #  402 PRECALL
        #  406 CALL
        #  416 POP_TOP
        #  418 LOAD_FAST self
        #  420 LOAD_METHOD read_settings
        #  442 PRECALL
        #  446 CALL
        #  456 POP_TOP
        #  458 LOAD_CONST None
        #  460 RETURN_VALUE
        pass

    def dark_mode_updated(self):
        dark_mode = self.darkMode.isChecked()
        set_style(QtWidgets.QApplication.instance(), dark_mode)

    def read_settings(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR unitPreferences
        #   14 LOAD_METHOD read_settings
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 LOAD_GLOBAL NULL + read_bool_setting
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR settings
        #   76 LOAD_CONST 'DarkMode'
        #   78 LOAD_CONST True
        #   80 PRECALL
        #   84 CALL
        #   94 STORE_FAST dark_mode
        #   96 LOAD_FAST dark_mode
        #   98 POP_JUMP_FORWARD_IF_FALSE to 156
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR darkMode
        #  112 LOAD_METHOD setChecked
        #  134 LOAD_CONST True
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 LOAD_CONST None
        #  154 RETURN_VALUE
        #  156 LOAD_FAST self
        #  158 LOAD_ATTR lightMode
        #  168 LOAD_METHOD setChecked
        #  190 LOAD_CONST True
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 LOAD_CONST None
        #  210 RETURN_VALUE
        pass

    def write_settings(self):
        self.unitPreferences.write_settings()
        dark_mode = self.darkMode.isChecked()
        write_bool_setting(self.settings, 'DarkMode', dark_mode)
