# Source Generated with Decompyle++
# File: setting_viewer.pyc (Python 3.11)

from typing import Optional
from PySide6 import QtWidgets
from asphodel.device_info import DeviceInfo
from hyperborea.setting_widget import SettingWidget
from .ui.ui_setting_viewer import Ui_SettingViewerDialog

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class SettingViewerDialog(Ui_SettingViewerDialog, QtWidgets.QDialog):

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
        #  262 LOAD_CONST None
        #  264 RETURN_VALUE
        pass

    def add_setting_widgets(self):
        remaining_settings = set(range(len(self.settings)))
        setting_tabs = []
