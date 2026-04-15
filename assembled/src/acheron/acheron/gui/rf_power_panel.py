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
        super().__init__(parent)
        self.controller = controller
        self.setupUi(self)
        self.controller.rf_power_changed.connect(self.rf_power_changed_cb)
        self.rf_power_changed_cb(controller, self.controller.get_rf_power_status())
        self.enableButton.clicked.connect(self.controller.enable_rf_power)
        self.disableButton.clicked.connect(self.controller.disable_rf_power)

    def add_ctrl_var_widget(self, widget):
        self.ctrlVarLayout.addWidget(widget)

    def clear_ctrl_var_widgets(self):
        while True:
            item = self.ctrlVarLayout.takeAt(0)
            if not item:
                return None
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def rf_power_changed_cb(self, _controller, status):
        if status == RFPowerStatus.NOT_SUPPORTED:
            self.enableButton.setEnabled(False)
            self.disableButton.setEnabled(False)
            return None
        if status == RFPowerStatus.ENABLED:
            self.enableButton.setEnabled(False)
            self.disableButton.setEnabled(True)
            return None
        self.enableButton.setEnabled(True)
        self.disableButton.setEnabled(False)
        return None
