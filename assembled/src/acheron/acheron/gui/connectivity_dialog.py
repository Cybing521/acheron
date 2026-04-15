# Source Generated with Decompyle++
# File: connectivity_dialog.pyc (Python 3.11)

import logging
import os
import re
from xml.dom.minidom import getDOMImplementation
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from hyperborea.preferences import read_int_setting
from ..connectivity.modbus import get_numeric_serial
from ..calc_process.types import ChannelInformation
from ..core.preferences import DevicePreferences
from .ui.ui_connectivity_dialog import Ui_ConnectivityDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ConnectivityDialog(Ui_ConnectivityDialog, QtWidgets.QDialog):

    def __init__(self, serial_number, device_info, channel_info, device_prefs, parent):
        super().__init__(parent)
        self.serial_number = serial_number
        self.device_info = device_info
        self.numeric_serial_number = get_numeric_serial(serial_number)
        self.channel_info = channel_info
        self.device_prefs = device_prefs
        self.settings = QtCore.QSettings()
        self.settings.beginGroup(self.serial_number)
        self.setting_names = {}
        self.channel_socket_info = {}
        self.setupUi(self)
        self.add_channel_check_boxes()
        self.read_settings()
        self.accepted.connect(self.write_settings)
        self.modbusDetails.clicked.connect(self.show_modbus_details)

    def add_channel_check_boxes(self):
        total_channels = 0
        row = 5
        for info in sorted(self.channel_info.values(), key = lambda item: item.channel_id):
            for i, subchannel in enumerate(info.subchannel_names):
                setting_name = 'Channel{}_{}_Port'.format(info.channel_id, i)
                checkbox = QtWidgets.QCheckBox(self)
                checkbox.setText(subchannel)
                spinbox = QtWidgets.QSpinBox(self)
                spinbox.setMinimum(1)
                spinbox.setMaximum(65535)
                spinbox.setValue(12345)
                spinbox.setEnabled(False)
                checkbox.toggled.connect(spinbox.setEnabled)
                self.setting_names[setting_name] = (checkbox, spinbox)
                self.channel_socket_info[setting_name] = (info.channel_id, subchannel)
                self.gridLayout.addWidget(checkbox, row, 1, 1, 2)
                self.gridLayout.addWidget(spinbox, row, 3, 1, 1)
                row += 1
                total_channels += 1
        self.modbusChannelCount.setText(str(total_channels))

    def done(self, r):
        if r:
            chosen_ports = set()
            for _setting_name, (checkbox, spinbox) in self.setting_names.items():
                if not checkbox.isChecked():
                    continue
                port = spinbox.value()
                if port in chosen_ports:
                    message = self.tr('Cannot have duplicate ports!')
                    QtWidgets.QMessageBox.warning(self, self.tr('Error'), message)
                    return None
                chosen_ports.add(port)
        super().done(r)
        return None

    def read_settings(self):
        self.modbusCheckBox.setChecked(self.device_prefs.modbus_enable)
        self.modbusOffset.setValue(self.device_prefs.modbus_register_offset)
        for setting_name, (checkbox, spinbox) in self.setting_names.items():
            port = read_int_setting(self.settings, setting_name, 0)
            if not port:
                checkbox.setChecked(False)
                spinbox.setValue(12345)
                continue
            checkbox.setChecked(True)
            spinbox.setValue(port)
        return None

    def write_settings(self):
        self.device_prefs.modbus_enable = self.modbusCheckBox.isChecked()
        self.device_prefs.modbus_register_offset = self.modbusOffset.value()
        for setting_name, (checkbox, spinbox) in self.setting_names.items():
            if checkbox.isChecked():
                port = spinbox.value()
                self.settings.setValue(setting_name, port)
                continue
            self.settings.remove(setting_name)
        return None

    def show_modbus_details(self):
        impl = getDOMImplementation()
        if not impl:
            message = self.tr('Error loading serializer!')
            QtWidgets.QMessageBox.critical(self, self.tr('Error'), message)
            logger.error(message)
            return None

        dt = impl.createDocumentType('html', '-//W3C//DTD XHTML 1.0 Strict//EN', 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd')
        dom = impl.createDocument('http://www.w3.org/1999/xhtml', 'html', dt)
        html = dom.documentElement
        head = dom.createElement('head')
        html.appendChild(head)
        title = dom.createElement('title')
        title_string = f'{self.serial_number} Modbus Details'
        title.appendChild(dom.createTextNode(title_string))
        head.appendChild(title)
        body = dom.createElement('body')
        html.appendChild(body)

        h1 = dom.createElement('h1')
        h1.appendChild(dom.createTextNode(title_string))
        body.appendChild(h1)

        summary = dom.createElement('p')
        summary.appendChild(dom.createTextNode(
            f'Serial: {self.serial_number} | Numeric Serial: {self.numeric_serial_number} | '
            f'Modbus Enabled: {"Yes" if self.modbusCheckBox.isChecked() else "No"} | '
            f'Register Offset: {self.modbusOffset.value()}'
        ))
        body.appendChild(summary)

        channel_list = dom.createElement('ul')
        for setting_name, (checkbox, spinbox) in self.setting_names.items():
            channel_id, subchannel = self.channel_socket_info[setting_name]
            item = dom.createElement('li')
            port_text = str(spinbox.value()) if checkbox.isChecked() else 'disabled'
            item.appendChild(dom.createTextNode(f'Channel {channel_id} / {subchannel}: {port_text}'))
            channel_list.appendChild(item)
        body.appendChild(channel_list)

        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(title_string)
        layout = QtWidgets.QVBoxLayout(dialog)
        browser = QtWidgets.QTextBrowser(dialog)
        browser.setHtml(dom.toxml())
        layout.addWidget(browser)
        button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Close, parent = dialog)
        button_box.rejected.connect(dialog.reject)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)
        dialog.resize(700, 480)
        dialog.exec()
        dialog.deleteLater()
        return None
