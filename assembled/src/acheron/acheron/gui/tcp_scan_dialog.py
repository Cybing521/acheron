# Source Generated with Decompyle++
# File: tcp_scan_dialog.pyc (Python 3.11)

import collections
import logging
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from ..core.dispatcher import Dispatcher
from ..core.preferences import Preferences
from .ui.ui_tcp_scan_dialog import Ui_TCPScanDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class SortableTableWidgetItem(QtWidgets.QTableWidgetItem):

    def __init__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_CONST None
        #   70 LOAD_FAST self
        #   72 STORE_ATTR sort_value
        #   82 LOAD_CONST None
        #   84 RETURN_VALUE
        pass

    def __lt__(self, other):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST other
        #    6 LOAD_ATTR sort_value
        #   16 STORE_FAST other_sort_value
        #   18 LOAD_FAST other_sort_value
        #   20 POP_JUMP_FORWARD_IF_NONE to 58
        #   22 LOAD_FAST self
        #   24 LOAD_ATTR sort_value
        #   34 POP_JUMP_FORWARD_IF_NONE to 58
        #   36 LOAD_FAST self
        #   38 LOAD_ATTR sort_value
        #   48 LOAD_FAST other_sort_value
        #   50 COMPARE_OP <
        #   56 RETURN_VALUE
        #   58 JUMP_FORWARD to 92
        #   60 PUSH_EXC_INFO
        #   62 LOAD_GLOBAL AttributeError
        #   74 CHECK_EXC_MATCH
        #   76 POP_JUMP_FORWARD_IF_FALSE to 84
        #   78 POP_TOP
        #   80 POP_EXCEPT
        #   82 JUMP_FORWARD to 92
        #   84 RERAISE
        #   86 COPY
        #   88 POP_EXCEPT
        #   90 RERAISE
        #   92 LOAD_FAST self
        #   94 LOAD_METHOD text
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_FAST other
        #  132 LOAD_METHOD text
        #  154 PRECALL
        #  158 CALL
        #  168 COMPARE_OP <
        #  174 RETURN_VALUE
        pass

class RowInformation:

    def __init__(self, table_items):
        self.table_items = table_items
        self.device = None
        self.connected = False

class TCPScanDialog(Ui_TCPScanDialog, QtWidgets.QDialog):

    def __init__(self, dispatcher, preferences, initial_devices, parent):
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
        #   70 LOAD_FAST dispatcher
        #   72 LOAD_FAST self
        #   74 STORE_ATTR dispatcher
        #   84 LOAD_FAST preferences
        #   86 LOAD_FAST self
        #   88 STORE_ATTR preferences
        #   98 BUILD_MAP
        #  100 LOAD_FAST self
        #  102 STORE_ATTR row_info
        #  112 LOAD_FAST self
        #  114 LOAD_METHOD setupUi
        #  136 LOAD_FAST self
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_FAST self
        #  156 LOAD_METHOD extra_ui_setup
        #  178 PRECALL
        #  182 CALL
        #  192 POP_TOP
        #  194 LOAD_FAST initial_devices
        #  196 POP_JUMP_FORWARD_IF_NONE to 244
        #  198 LOAD_FAST self
        #  200 LOAD_METHOD update_devices
        #  222 LOAD_FAST initial_devices
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 LOAD_CONST None
        #  242 RETURN_VALUE
        #  244 LOAD_FAST self
        #  246 LOAD_METHOD rescan
        #  268 PRECALL
        #  272 CALL
        #  282 POP_TOP
        #  284 LOAD_CONST None
        #  286 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        self.bootloader_fg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.black))
        self.bootloader_bg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.yellow))
        self.default_font = QtGui.QFont()
        self.bootloader_font = QtGui.QFont()
        self.bootloader_font.setBold(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.rescanButton = self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Reset)
        self.rescanButton.setText(self.tr('Rescan'))
        self.rescanButton.clicked.connect(self.rescan)
        selection_model = self.tableWidget.selectionModel()
        selection_model.selectionChanged.connect(self.selection_changed)
        self.tableWidget.doubleClicked.connect(self.double_click_cb)
        self.tableWidget.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder)
        self.tableWidget.setSortingEnabled(True)
        self.rescan_timer = QtCore.QTimer(self)
        self.rescan_timer.timeout.connect(self.rescan)
        self.automaticRescan.toggled.connect(self.set_automatic_rescan)
        self.automaticRescan.setChecked(self.preferences.automatic_rescan)
        self.finished.connect(self.rescan_timer.stop)

    def set_automatic_rescan(self):
        if self.automaticRescan.isChecked():
            self.preferences.automatic_rescan = True
            self.rescan_timer.start(1000)
            return None
        self.preferences.automatic_rescan = None
        self.rescan_timer.stop()

    def double_click_cb(self):
        self.accept()

    def get_selected_devices(self):
        selected_devices = []

    def selection_changed(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR buttonBox
        #   14 LOAD_METHOD button
        #   36 LOAD_GLOBAL QtWidgets
        #   48 LOAD_ATTR QDialogButtonBox
        #   58 LOAD_ATTR StandardButton
        #   68 LOAD_ATTR Ok
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST ok_button
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR tableWidget
        #  106 LOAD_METHOD selectionModel
        #  128 PRECALL
        #  132 CALL
        #  142 LOAD_METHOD hasSelection
        #  164 PRECALL
        #  168 CALL
        #  178 POP_JUMP_FORWARD_IF_FALSE to 226
        #  180 LOAD_FAST ok_button
        #  182 LOAD_METHOD setEnabled
        #  204 LOAD_CONST True
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        #  226 LOAD_FAST ok_button
        #  228 LOAD_METHOD setEnabled
        #  250 LOAD_CONST False
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_CONST None
        #  270 RETURN_VALUE
        pass

    def update_row_with_device(self, row_info, device, connected):
        old_device = row_info.device
        row_info.device = device
        old_connected = row_info.connected
        row_info.connected = connected
        adv = device.tcp_get_advertisement()

    def add_row(self, serial_number):
        start_index = self.tableWidget.rowCount()
        self.tableWidget.insertRow(start_index)
        serial_number_item = SortableTableWidgetItem()
        serial_number_item.sort_value = serial_number
        serial_number_item.setData(QtCore.Qt.ItemDataRole.DisplayRole, serial_number)
        self.tableWidget.setItem(start_index, 0, serial_number_item)
        table_items = [
            serial_number_item]

    def remove_row(self, serial_number):
        row_info = self.row_info.pop(serial_number)
        serial_number_item = row_info.table_items.serial_number
        self.tableWidget.removeRow(serial_number_item.row())

    def update_devices(self, devices):
        connected_location_strs = self.dispatcher.get_proxy_locations()
        existing_serials = set()
        for device in devices:
            adv = device.tcp_get_advertisement()
            serial_number = adv.serial_number
            existing_serials.add(serial_number)
            location_str = device.get_location_string()
            connected = location_str in connected_location_strs
            row_info = self.row_info.get(serial_number)
            if not row_info:
                table_items = self.add_row(serial_number)
                row_info = RowInformation(table_items)
                self.row_info[serial_number] = row_info
            self.update_row_with_device(row_info, device, connected)
            old_serials = set(self.row_info.keys())
            old_serials.difference_update(existing_serials)
            for serial_number in old_serials:
                self.remove_row(serial_number)
                self.selection_changed()
                return None

    def rescan(self):
        try:
            new_devices = asphodel.find_tcp_devices()
        except Exception:
            return None

        self.update_devices(new_devices)
