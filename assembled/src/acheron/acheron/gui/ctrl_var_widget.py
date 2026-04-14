# Source Generated with Decompyle++
# File: ctrl_var_widget.pyc (Python 3.11)

import logging
from typing import Callable, Optional
from PySide6 import QtCore, QtWidgets
import asphodel
from hyperborea.unit_formatter_spinbox import UnitFormatterSpinBox
from ..core.update_func_limiter import UpdateFuncLimiter
from .ui.ui_ctrl_var_widget import Ui_CtrlVarWidget
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class CtrlVarWidget(Ui_CtrlVarWidget, QtWidgets.QWidget):

    def __init__(self, set_setting, name, ctrl_var_info, initial_value, parent):
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
        #   70 LOAD_FAST ctrl_var_info
        #   72 LOAD_FAST self
        #   74 STORE_ATTR ctrl_var_info
        #   84 LOAD_CONST False
        #   86 LOAD_FAST self
        #   88 STORE_ATTR setting_value
        #   98 LOAD_GLOBAL NULL + UpdateFuncLimiter
        #  110 LOAD_FAST set_setting
        #  112 LOAD_CONST 100
        #  114 LOAD_FAST self
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_FAST self
        #  132 STORE_ATTR updater
        #  142 LOAD_FAST self
        #  144 LOAD_METHOD setupUi
        #  166 LOAD_FAST self
        #  168 PRECALL
        #  172 CALL
        #  182 POP_TOP
        #  184 LOAD_FAST self
        #  186 LOAD_ATTR nameLabel
        #  196 LOAD_METHOD setText
        #  218 LOAD_FAST name
        #  220 PRECALL
        #  224 CALL
        #  234 POP_TOP
        #  236 LOAD_FAST self
        #  238 LOAD_METHOD setup_spinbox
        #  260 LOAD_FAST initial_value
        #  262 PRECALL
        #  266 CALL
        #  276 POP_TOP
        #  278 LOAD_FAST self
        #  280 LOAD_METHOD setup_callbacks
        #  302 PRECALL
        #  306 CALL
        #  316 POP_TOP
        #  318 LOAD_FAST self
        #  320 LOAD_METHOD set_value
        #  342 LOAD_FAST initial_value
        #  344 PRECALL
        #  348 CALL
        #  358 POP_TOP
        #  360 LOAD_CONST None
        #  362 RETURN_VALUE
        pass

    def setup_spinbox(self, initial_value):
        scaled_min = self.ctrl_var_info.minimum * self.ctrl_var_info.scale + self.ctrl_var_info.offset
        scaled_max = self.ctrl_var_info.maximum * self.ctrl_var_info.scale + self.ctrl_var_info.offset
        unit_formatter = asphodel.nativelib.create_unit_formatter(self.ctrl_var_info.unit_type, scaled_min, scaled_max, self.ctrl_var_info.scale)
        self.spinBox = UnitFormatterSpinBox(self)
        self.spinBox.set_unit_formatter(unit_formatter)
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox.setMinimum(minimum)
        self.spinBox.setMaximum(maximum)
        self.spinBox.setValue(value)
        self.slider.setMinimum(minimum)
        self.slider.setMaximum(maximum)
        self.slider.setValue(value)
        self.spinBox.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.spinBox.setValue)

    def setup_callbacks(self):
        self.slider.valueChanged.connect(self.value_changed)

    def set_value(self, value):
        self.setting_value = True
        if not self.inverted:
            self.slider.setValue(value)
        else:
            self.slider.setValue(-value)
        self.setting_value = False

    def value_changed(self):
        if not self.setting_value:
            value = self.slider.value()
            if self.inverted:
                value = -value
            self.updater.update(value)
            return None
