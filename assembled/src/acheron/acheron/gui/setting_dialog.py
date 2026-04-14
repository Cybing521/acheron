# Source Generated with Decompyle++
# File: setting_dialog.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtCore, QtWidgets
from asphodel.device_info import DeviceInfo
from hyperborea.setting_widget import SettingWidget
from .ui.ui_setting_dialog import Ui_SettingDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class SettingDialog(Ui_SettingDialog, QtWidgets.QDialog):

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
        #   72 LOAD_ATTR settings
        #   82 LOAD_FAST self
        #   84 STORE_ATTR settings
        #   94 LOAD_FAST device_info
        #   96 LOAD_ATTR nvm
        #  106 LOAD_FAST self
        #  108 STORE_ATTR nvm_bytes
        #  118 LOAD_FAST device_info
        #  120 LOAD_ATTR custom_enums
        #  130 LOAD_FAST self
        #  132 STORE_ATTR custom_enums
        #  142 LOAD_FAST device_info
        #  144 LOAD_ATTR setting_categories
        #  154 LOAD_FAST self
        #  156 STORE_ATTR setting_categories
        #  166 BUILD_LIST
        #  168 LOAD_FAST self
        #  170 STORE_ATTR setting_widgets
        #  180 LOAD_FAST self
        #  182 LOAD_METHOD setupUi
        #  204 LOAD_FAST self
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_FAST self
        #  224 LOAD_METHOD add_setting_widgets
        #  246 PRECALL
        #  250 CALL
        #  260 POP_TOP
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR buttonBox
        #  274 LOAD_METHOD button
        #  296 LOAD_GLOBAL QtWidgets
        #  308 LOAD_ATTR QDialogButtonBox
        #  318 LOAD_ATTR StandardButton
        #  328 LOAD_ATTR RestoreDefaults
        #  338 PRECALL
        #  342 CALL
        #  352 STORE_FAST b
        #  354 LOAD_FAST b
        #  356 LOAD_ATTR clicked
        #  366 LOAD_METHOD connect
        #  388 LOAD_FAST self
        #  390 LOAD_ATTR restore_defaults
        #  400 PRECALL
        #  404 CALL
        #  414 POP_TOP
        #  416 LOAD_CONST None
        #  418 RETURN_VALUE
        pass

    def add_setting_widgets(self):
        remaining_settings = set(range(len(self.settings)))
        setting_tabs = []

    def get_updated_nvm(self):
        nvm_bytes = bytearray(self.nvm_bytes)
        for widget in self.setting_widgets:
            widget.update_nvm(nvm_bytes)
            return bytes(nvm_bytes)

    def restore_defaults(self):
        for widget in self.setting_widgets:
            widget.restore_defaults()
            return None
