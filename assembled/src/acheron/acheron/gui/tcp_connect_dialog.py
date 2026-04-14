# Source Generated with Decompyle++
# File: tcp_connect_dialog.pyc (Python 3.11)

import logging
from typing import Any, Optional
from PySide6 import QtCore, QtWidgets
from .ui.ui_tcp_connect_dialog import Ui_TCPConnectDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class TCPConnectDialog(Ui_TCPConnectDialog, QtWidgets.QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.settings = QtCore.QSettings()
        self.setupUi(self)
        self.extra_ui_setup()

    def extra_ui_setup(self):
        hostname = self.settings.value('connectHostname')
        if hostname and isinstance(hostname, str):
            self.hostname.setText(hostname.strip())
        port = self.settings.value('connectPort')
        if port is not None:
            try:
                self.port.setValue(int(port))
            except (TypeError, ValueError):
                logger.warning('Invalid saved TCP port: %r', port)
        serial = self.settings.value('connectSerial')
        if serial and isinstance(serial, str):
            self.serial.setText(serial.strip())
        self.hostname.textChanged.connect(self.values_updated)
        self.port.valueChanged.connect(self.values_updated)
        self.serial.textChanged.connect(self.values_updated)
        self.values_updated()

    def is_valid(self):
        if not self.hostname.text().strip():
            return False
        return True

    def done(self, r):
        if r and not self.is_valid():
            return None
        self.settings.setValue('connectHostname', self.hostname.text().strip())
        self.settings.setValue('connectPort', self.port.value())
        self.settings.setValue('connectSerial', self.serial.text().strip())
        super().done(r)
        return None

    def values_updated(self):
        ok_button = self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        ok_button.setEnabled(self.is_valid())
        return None

    def get_results(self):
        results = {
            'hostname': self.hostname.text().strip(),
            'port': self.port.value() }
        sn = self.serial.text().strip()
        if len(sn) != 0:
            results['serial_number'] = sn
        else:
            results['serial_number'] = None
        return results
