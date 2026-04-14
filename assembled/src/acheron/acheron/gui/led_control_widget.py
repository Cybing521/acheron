# Source Generated with Decompyle++
# File: led_control_widget.pyc (Python 3.11)

import logging
from typing import Callable, Optional
from PySide6 import QtCore, QtWidgets
from ..core.update_func_limiter import UpdateFuncLimiter
from .ui.ui_led_control_widget import Ui_LEDControlWidget
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class LEDControlWidget(Ui_LEDControlWidget, QtWidgets.QWidget):

    def __init__(self, set_led, initial_value, parent):
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
        #   70 LOAD_CONST False
        #   72 LOAD_FAST self
        #   74 STORE_ATTR setting_value
        #   84 LOAD_GLOBAL NULL + UpdateFuncLimiter
        #   96 LOAD_FAST set_led
        #   98 LOAD_CONST 100
        #  100 LOAD_FAST self
        #  102 PRECALL
        #  106 CALL
        #  116 LOAD_FAST self
        #  118 STORE_ATTR updater
        #  128 LOAD_FAST self
        #  130 LOAD_METHOD setupUi
        #  152 LOAD_FAST self
        #  154 PRECALL
        #  158 CALL
        #  168 POP_TOP
        #  170 LOAD_FAST self
        #  172 LOAD_METHOD setup_callbacks
        #  194 PRECALL
        #  198 CALL
        #  208 POP_TOP
        #  210 LOAD_FAST self
        #  212 LOAD_METHOD set_value
        #  234 LOAD_FAST initial_value
        #  236 PRECALL
        #  240 CALL
        #  250 POP_TOP
        #  252 LOAD_CONST None
        #  254 RETURN_VALUE
        pass

    def setup_callbacks(self):
        self.slider.valueChanged.connect(self.value_changed)

    def set_value(self, value):
        self.setting_value = True
        self.slider.setValue(value)
        self.setting_value = False

    def value_changed(self):
        if not self.setting_value:
            value = self.slider.value()
            self.updater.update(value)
            return None
