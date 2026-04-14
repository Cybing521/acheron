# Source Generated with Decompyle++
# File: rf_power_panel.pyc (Python 3.11)

import logging
from PySide6 import QtCore, QtWidgets
from ..core.device_controller import DeviceController, RFPowerStatus
from .ui.ui_rf_power_panel import Ui_RFPowerPanel
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RFPowerPanel(Ui_RFPowerPanel, QtWidgets.QGroupBox):

    def __init__(self, controller, parent):
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
        #   70 LOAD_FAST controller
        #   72 LOAD_FAST self
        #   74 STORE_ATTR controller
        #   84 LOAD_FAST self
        #   86 LOAD_METHOD setupUi
        #  108 LOAD_FAST self
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR controller
        #  138 LOAD_ATTR rf_power_changed
        #  148 LOAD_METHOD connect
        #  170 LOAD_FAST self
        #  172 LOAD_ATTR rf_power_changed_cb
        #  182 PRECALL
        #  186 CALL
        #  196 POP_TOP
        #  198 LOAD_FAST self
        #  200 LOAD_METHOD rf_power_changed_cb
        #  222 LOAD_FAST controller
        #  224 LOAD_FAST self
        #  226 LOAD_ATTR controller
        #  236 LOAD_METHOD get_rf_power_status
        #  258 PRECALL
        #  262 CALL
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_FAST self
        #  290 LOAD_ATTR enableButton
        #  300 LOAD_ATTR clicked
        #  310 LOAD_METHOD connect
        #  332 LOAD_FAST self
        #  334 LOAD_ATTR controller
        #  344 LOAD_ATTR enable_rf_power
        #  354 PRECALL
        #  358 CALL
        #  368 POP_TOP
        #  370 LOAD_FAST self
        #  372 LOAD_ATTR disableButton
        #  382 LOAD_ATTR clicked
        #  392 LOAD_METHOD connect
        #  414 LOAD_FAST self
        #  416 LOAD_ATTR controller
        #  426 LOAD_ATTR disable_rf_power
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_CONST None
        #  454 RETURN_VALUE
        pass

    def add_ctrl_var_widget(self, widget):
        self.ctrlVarLayout.addWidget(widget)

    def clear_ctrl_var_widgets(self):
        item = self.ctrlVarLayout.takeAt(0)
        if not item:
            return None

    def rf_power_changed_cb(self, _controller, status):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST status
        #    4 LOAD_GLOBAL RFPowerStatus
        #   16 LOAD_ATTR NOT_SUPPORTED
        #   26 COMPARE_OP ==
        #   32 POP_JUMP_FORWARD_IF_FALSE to 142
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR enableButton
        #   46 LOAD_METHOD setEnabled
        #   68 LOAD_CONST False
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR disableButton
        #   98 LOAD_METHOD setEnabled
        #  120 LOAD_CONST False
        #  122 PRECALL
        #  126 CALL
        #  136 POP_TOP
        #  138 LOAD_CONST None
        #  140 RETURN_VALUE
        #  142 LOAD_FAST status
        #  144 LOAD_GLOBAL RFPowerStatus
        #  156 LOAD_ATTR ENABLED
        #  166 COMPARE_OP ==
        #  172 POP_JUMP_FORWARD_IF_FALSE to 282
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR enableButton
        #  186 LOAD_METHOD setEnabled
        #  208 LOAD_CONST False
        #  210 PRECALL
        #  214 CALL
        #  224 POP_TOP
        #  226 LOAD_FAST self
        #  228 LOAD_ATTR disableButton
        #  238 LOAD_METHOD setEnabled
        #  260 LOAD_CONST True
        #  262 PRECALL
        #  266 CALL
        #  276 POP_TOP
        #  278 LOAD_CONST None
        #  280 RETURN_VALUE
        #  282 LOAD_FAST self
        #  284 LOAD_ATTR enableButton
        #  294 LOAD_METHOD setEnabled
        #  316 LOAD_CONST True
        #  318 PRECALL
        #  322 CALL
        #  332 POP_TOP
        #  334 LOAD_FAST self
        #  336 LOAD_ATTR disableButton
        #  346 LOAD_METHOD setEnabled
        #  368 LOAD_CONST False
        #  370 PRECALL
        #  374 CALL
        #  384 POP_TOP
        #  386 LOAD_CONST None
        #  388 RETURN_VALUE
        pass
