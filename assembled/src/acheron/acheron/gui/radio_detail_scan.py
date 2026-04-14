# Source Generated with Decompyle++
# File: radio_detail_scan.pyc (Python 3.11)

from collections import deque
from dataclasses import dataclass, fields
import datetime
import logging
from typing import Any, cast, Optional
from PySide6 import QtCore, QtGui, QtWidgets
from asphodel.device_info import ActiveScanInfo
from ..core.device_controller import DeviceController
from ..core.preferences import Preferences
from ..core.radio_scan import ActiveScanDatabase, ScanResult
from .ui.ui_detail_scan_dialog import Ui_DetailScanDialog
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

@dataclass
class TableItems:

    serial_number: SortableTableWidgetItem

    scan_strength: SortableTableWidgetItem

    tag1: QtWidgets.QTableWidgetItem

    tag2: QtWidgets.QTableWidgetItem

    board_info: QtWidgets.QTableWidgetItem

    build_info: QtWidgets.QTableWidgetItem

    build_date: QtWidgets.QTableWidgetItem

    bootloader: QtWidgets.QTableWidgetItem

    device_mode: QtWidgets.QTableWidgetItem

    last_seen: SortableTableWidgetItem

@dataclass
class RowInformation:

    table_items: TableItems

    scan: ScanResult

class DetailScanDialog(Ui_DetailScanDialog, QtWidgets.QDialog):

    def __init__(self, active_scan_database, preferences, parent):
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
        #   70 LOAD_FAST active_scan_database
        #   72 LOAD_FAST self
        #   74 STORE_ATTR active_scan_database
        #   84 LOAD_FAST preferences
        #   86 LOAD_FAST self
        #   88 STORE_ATTR preferences
        #   98 BUILD_MAP
        #  100 LOAD_FAST self
        #  102 STORE_ATTR row_info
        #  112 LOAD_GLOBAL NULL + deque
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_FAST self
        #  140 STORE_ATTR scans_to_process
        #  150 LOAD_FAST self
        #  152 LOAD_METHOD setupUi
        #  174 LOAD_FAST self
        #  176 PRECALL
        #  180 CALL
        #  190 POP_TOP
        #  192 LOAD_FAST self
        #  194 LOAD_METHOD extra_ui_setup
        #  216 PRECALL
        #  220 CALL
        #  230 POP_TOP
        #  232 LOAD_FAST self
        #  234 LOAD_METHOD selection_changed
        #  256 PRECALL
        #  260 CALL
        #  270 POP_TOP
        #  272 LOAD_CONST None
        #  274 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        self.bootloader_fg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.black))
        self.bootloader_bg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.yellow))
        self.stale_fg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.black))
        self.stale_bg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.yellow))
        self.old_fg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.black))
        self.old_bg_brush = QtGui.QBrush(QtGui.QColor(QtCore.Qt.GlobalColor.red))
        self.default_font = QtGui.QFont()
        self.bootloader_font = QtGui.QFont()
        self.bootloader_font.setBold(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.clearButton = self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Reset)
        self.clearButton.setText(self.tr('Clear'))
        self.clearButton.clicked.connect(self.clear_button_cb)
        self.active_scan_database.cleared.connect(self.database_cleared)
        self.active_scan_database.active_scan_ready.connect(self.update_active_scan_info)
        self.active_scan_database.remote_connecting.connect(self.update_controller)
        self.backgroundActiveScan.toggled.connect(self.set_background_active_scan)
        self.backgroundActiveScan.setChecked(self.preferences.background_active_scan)
        selection_model = self.tableWidget.selectionModel()
        selection_model.selectionChanged.connect(self.selection_changed)
        self.tableWidget.doubleClicked.connect(self.double_click_cb)
        self.tableWidget.sortByColumn(0, QtCore.Qt.SortOrder.AscendingOrder)
        self.tableWidget.setSortingEnabled(True)
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_rows)
        self.update_timer.start(500)
        self.update_scan_count()

    def set_background_active_scan(self):
        if self.backgroundActiveScan.isChecked():
            self.preferences.background_active_scan = True
            return None
        self.preferences.background_active_scan = None

    def double_click_cb(self):
        self.accept()

    def get_selected_scan(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR tableWidget
        #   14 LOAD_METHOD selectionModel
        #   36 PRECALL
        #   40 CALL
        #   50 LOAD_METHOD selectedRows
        #   72 PRECALL
        #   76 CALL
        #   86 STORE_FAST rows
        #   88 LOAD_FAST rows
        #   90 POP_JUMP_FORWARD_IF_FALSE to 290
        #   92 LOAD_FAST rows
        #   94 LOAD_CONST 0
        #   96 BINARY_SUBSCR
        #  106 LOAD_METHOD row
        #  128 PRECALL
        #  132 CALL
        #  142 STORE_FAST row
        #  144 LOAD_GLOBAL NULL + cast
        #  156 LOAD_GLOBAL SortableTableWidgetItem
        #  168 LOAD_FAST self
        #  170 LOAD_ATTR tableWidget
        #  180 LOAD_METHOD item
        #  202 LOAD_FAST row
        #  204 LOAD_CONST 0
        #  206 PRECALL
        #  210 CALL
        #  220 PRECALL
        #  224 CALL
        #  234 STORE_FAST item
        #  236 LOAD_FAST item
        #  238 LOAD_ATTR sort_value
        #  248 STORE_FAST serial_number
        #  250 LOAD_FAST serial_number
        #  252 POP_JUMP_FORWARD_IF_FALSE to 290
        #  254 LOAD_FAST self
        #  256 LOAD_ATTR row_info
        #  266 LOAD_FAST serial_number
        #  268 BINARY_SUBSCR
        #  278 LOAD_ATTR scan
        #  288 RETURN_VALUE
        #  290 LOAD_CONST None
        #  292 RETURN_VALUE
        pass

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

    def database_cleared(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.row_info.clear()
        self.scans_to_process.clear()
        self.update_scan_count()

    def clear_button_cb(self):
        self.active_scan_database.clear_database()

    def handle_scan(self, scan):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR row_info
        #   14 LOAD_METHOD get
        #   36 LOAD_FAST scan
        #   38 LOAD_ATTR serial_number
        #   48 PRECALL
        #   52 CALL
        #   62 STORE_FAST row_info
        #   64 LOAD_FAST row_info
        #   66 POP_JUMP_FORWARD_IF_TRUE to 558
        #   68 LOAD_FAST self
        #   70 LOAD_METHOD add_row
        #   92 LOAD_FAST scan
        #   94 LOAD_ATTR serial_number
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST table_items
        #  120 LOAD_FAST self
        #  122 LOAD_METHOD update_table_items
        #  144 LOAD_FAST table_items
        #  146 LOAD_FAST scan
        #  148 LOAD_CONST None
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 LOAD_GLOBAL NULL + RowInformation
        #  178 LOAD_FAST table_items
        #  180 LOAD_FAST scan
        #  182 LOAD_CONST None
        #  184 LOAD_CONST None
        #  186 PRECALL
        #  190 CALL
        #  200 STORE_FAST row_info
        #  202 LOAD_FAST row_info
        #  204 LOAD_FAST self
        #  206 LOAD_ATTR row_info
        #  216 LOAD_FAST scan
        #  218 LOAD_ATTR serial_number
        #  228 STORE_SUBSCR
        #  232 LOAD_FAST self
        #  234 LOAD_METHOD update_scan_count
        #  256 PRECALL
        #  260 CALL
        #  270 POP_TOP
        #  272 LOAD_FAST self
        #  274 LOAD_ATTR active_scan_database
        #  284 LOAD_METHOD get_remote_controller
        #  306 LOAD_FAST scan
        #  308 LOAD_ATTR serial_number
        #  318 PRECALL
        #  322 CALL
        #  332 STORE_FAST controller
        #  334 LOAD_FAST controller
        #  336 POP_JUMP_FORWARD_IF_FALSE to 392
        #  338 LOAD_FAST self
        #  340 LOAD_METHOD update_controller
        #  362 LOAD_FAST scan
        #  364 LOAD_ATTR serial_number
        #  374 LOAD_FAST controller
        #  376 PRECALL
        #  380 CALL
        #  390 POP_TOP
        #  392 LOAD_FAST self
        #  394 LOAD_ATTR active_scan_database
        #  404 LOAD_METHOD get_active_scan
        #  426 LOAD_FAST scan
        #  428 LOAD_ATTR serial_number
        #  438 PRECALL
        #  442 CALL
        #  452 STORE_FAST active_scan
        #  454 LOAD_FAST active_scan
        #  456 POP_JUMP_FORWARD_IF_FALSE to 512
        #  458 LOAD_FAST self
        #  460 LOAD_METHOD update_active_scan_info
        #  482 LOAD_FAST scan
        #  484 LOAD_ATTR serial_number
        #  494 LOAD_FAST active_scan
        #  496 PRECALL
        #  500 CALL
        # ... bytecode truncated ...
        pass

    def update_table_items(self, table_items, new_scan, old_scan):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST old_scan
        #    4 POP_JUMP_FORWARD_IF_NONE to 38
        #    6 LOAD_FAST old_scan
        #    8 LOAD_ATTR scan_strength
        #   18 LOAD_FAST new_scan
        #   20 LOAD_ATTR scan_strength
        #   30 COMPARE_OP !=
        #   36 POP_JUMP_FORWARD_IF_FALSE to 180
        #   38 LOAD_FAST new_scan
        #   40 LOAD_ATTR scan_strength
        #   50 POP_JUMP_FORWARD_IF_NONE to 180
        #   52 LOAD_FAST table_items
        #   54 LOAD_ATTR scan_strength
        #   64 STORE_FAST scan_strength
        #   66 LOAD_FAST new_scan
        #   68 LOAD_ATTR scan_strength
        #   78 LOAD_FAST scan_strength
        #   80 STORE_ATTR sort_value
        #   90 LOAD_FAST scan_strength
        #   92 LOAD_METHOD setText
        #  114 LOAD_CONST '{} dBm'
        #  116 LOAD_METHOD format
        #  138 LOAD_FAST new_scan
        #  140 LOAD_ATTR scan_strength
        #  150 PRECALL
        #  154 CALL
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_FAST old_scan
        #  182 POP_JUMP_FORWARD_IF_NONE to 216
        #  184 LOAD_FAST old_scan
        #  186 LOAD_ATTR device_mode
        #  196 LOAD_FAST new_scan
        #  198 LOAD_ATTR device_mode
        #  208 COMPARE_OP !=
        #  214 POP_JUMP_FORWARD_IF_FALSE to 324
        #  216 LOAD_FAST table_items
        #  218 LOAD_ATTR device_mode
        #  228 STORE_FAST device_mode
        #  230 LOAD_FAST device_mode
        #  232 LOAD_METHOD setData
        #  254 LOAD_GLOBAL QtCore
        #  266 LOAD_ATTR Qt
        #  276 LOAD_ATTR ItemDataRole
        #  286 LOAD_ATTR DisplayRole
        #  296 LOAD_FAST new_scan
        #  298 LOAD_ATTR device_mode
        #  308 PRECALL
        #  312 CALL
        #  322 POP_TOP
        #  324 LOAD_FAST old_scan
        #  326 POP_JUMP_FORWARD_IF_NONE to 362
        #  328 LOAD_FAST old_scan
        #  330 LOAD_ATTR bootloader
        #  340 LOAD_FAST new_scan
        #  342 LOAD_ATTR bootloader
        #  352 COMPARE_OP !=
        #  358 EXTENDED_ARG
        #  360 POP_JUMP_FORWARD_IF_FALSE to 1094
        #  362 LOAD_FAST table_items
        #  364 LOAD_ATTR bootloader
        #  374 STORE_FAST bootloader
        #  376 LOAD_FAST new_scan
        #  378 LOAD_ATTR bootloader
        #  388 POP_JUMP_FORWARD_IF_FALSE to 712
        #  390 LOAD_FAST bootloader
        #  392 LOAD_METHOD setData
        #  414 LOAD_GLOBAL QtCore
        #  426 LOAD_ATTR Qt
        #  436 LOAD_ATTR ItemDataRole
        #  446 LOAD_ATTR DisplayRole
        #  456 LOAD_CONST 'Running'
        #  458 PRECALL
        #  462 CALL
        #  472 POP_TOP
        #  474 LOAD_FAST bootloader
        #  476 LOAD_METHOD setFont
        #  498 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def add_row(self, serial_number):
        start_index = self.tableWidget.rowCount()
        self.tableWidget.insertRow(start_index)
        serial_number_item = SortableTableWidgetItem()
        serial_number_item.sort_value = serial_number
        serial_number_item.setData(QtCore.Qt.ItemDataRole.DisplayRole, serial_number)
        self.tableWidget.setItem(start_index, 0, serial_number_item)
        table_items = [
            serial_number_item]

    def update_last_seen(self, row_info, now):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST now
        #    4 POP_JUMP_FORWARD_IF_NOT_NONE to 98
        #    6 LOAD_GLOBAL datetime
        #   18 LOAD_ATTR datetime
        #   28 LOAD_METHOD now
        #   50 LOAD_GLOBAL datetime
        #   62 LOAD_ATTR timezone
        #   72 LOAD_ATTR utc
        #   82 PRECALL
        #   86 CALL
        #   96 STORE_FAST now
        #   98 LOAD_FAST now
        #  100 LOAD_FAST row_info
        #  102 LOAD_ATTR scan
        #  112 LOAD_ATTR last_seen
        #  122 BINARY_OP -
        #  126 STORE_FAST delta
        #  128 LOAD_FAST row_info
        #  130 LOAD_ATTR table_items
        #  140 LOAD_ATTR last_seen
        #  150 STORE_FAST item
        #  152 LOAD_FAST delta
        #  154 LOAD_FAST item
        #  156 STORE_ATTR sort_value
        #  166 LOAD_GLOBAL NULL + int
        #  178 LOAD_FAST delta
        #  180 LOAD_METHOD total_seconds
        #  202 PRECALL
        #  206 CALL
        #  216 PRECALL
        #  220 CALL
        #  230 STORE_FAST seconds
        #  232 LOAD_FAST seconds
        #  234 LOAD_FAST row_info
        #  236 LOAD_ATTR last_seen_seconds
        #  246 COMPARE_OP !=
        #  252 EXTENDED_ARG
        #  254 POP_JUMP_FORWARD_IF_FALSE to 946
        #  256 LOAD_FAST seconds
        #  258 LOAD_FAST row_info
        #  260 STORE_ATTR last_seen_seconds
        #  270 LOAD_FAST seconds
        #  272 LOAD_CONST 1
        #  274 COMPARE_OP ==
        #  280 POP_JUMP_FORWARD_IF_FALSE to 288
        #  282 LOAD_CONST '1 second ago'
        #  284 STORE_FAST text
        #  286 JUMP_FORWARD to 360
        #  288 LOAD_CONST ''
        #  290 LOAD_METHOD join
        #  312 LOAD_GLOBAL NULL + str
        #  324 LOAD_FAST seconds
        #  326 PRECALL
        #  330 CALL
        #  340 LOAD_CONST ' seconds ago'
        #  342 BUILD_TUPLE
        #  344 PRECALL
        #  348 CALL
        #  358 STORE_FAST text
        #  360 LOAD_FAST item
        #  362 LOAD_METHOD setText
        #  384 LOAD_FAST text
        #  386 PRECALL
        #  390 CALL
        #  400 POP_TOP
        #  402 LOAD_FAST seconds
        #  404 LOAD_CONST 10
        #  406 COMPARE_OP <
        #  412 POP_JUMP_FORWARD_IF_FALSE to 718
        #  414 LOAD_FAST row_info
        #  416 LOAD_ATTR scan
        #  426 LOAD_ATTR bootloader
        #  436 POP_JUMP_FORWARD_IF_FALSE to 546
        #  438 LOAD_FAST item
        #  440 LOAD_METHOD setForeground
        #  462 LOAD_FAST self
        #  464 LOAD_ATTR bootloader_fg_brush
        #  474 PRECALL
        #  478 CALL
        # ... bytecode truncated ...
        pass

    def update_rows(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR tableWidget
        #   14 LOAD_METHOD setUpdatesEnabled
        #   36 LOAD_CONST False
        #   38 PRECALL
        #   42 CALL
        #   52 POP_TOP
        #   54 LOAD_FAST self
        #   56 LOAD_ATTR tableWidget
        #   66 LOAD_METHOD horizontalHeader
        #   88 PRECALL
        #   92 CALL
        #  102 STORE_FAST header
        #  104 LOAD_FAST header
        #  106 LOAD_METHOD setSectionResizeMode
        #  128 LOAD_GLOBAL QtWidgets
        #  140 LOAD_ATTR QHeaderView
        #  150 LOAD_ATTR ResizeMode
        #  160 LOAD_ATTR Fixed
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 NOP
        #  188 NOP
        #  190 LOAD_FAST self
        #  192 LOAD_ATTR scans_to_process
        #  202 LOAD_METHOD popleft
        #  224 PRECALL
        #  228 CALL
        #  238 STORE_FAST scan
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR row_info
        #  252 LOAD_METHOD get
        #  274 LOAD_FAST scan
        #  276 LOAD_ATTR serial_number
        #  286 PRECALL
        #  290 CALL
        #  300 STORE_FAST row_info
        #  302 LOAD_FAST row_info
        #  304 POP_JUMP_FORWARD_IF_FALSE to 390
        #  306 LOAD_FAST row_info
        #  308 LOAD_ATTR scan
        #  318 STORE_FAST old_scan
        #  320 LOAD_FAST self
        #  322 LOAD_METHOD update_table_items
        #  344 LOAD_FAST row_info
        #  346 LOAD_ATTR table_items
        #  356 LOAD_FAST scan
        #  358 LOAD_FAST old_scan
        #  360 PRECALL
        #  364 CALL
        #  374 POP_TOP
        #  376 LOAD_FAST scan
        #  378 LOAD_FAST row_info
        #  380 STORE_ATTR scan
        #  390 JUMP_BACKWARD to 190
        #  392 PUSH_EXC_INFO
        #  394 LOAD_GLOBAL IndexError
        #  406 CHECK_EXC_MATCH
        #  408 POP_JUMP_FORWARD_IF_FALSE to 416
        #  410 POP_TOP
        #  412 POP_EXCEPT
        #  414 JUMP_FORWARD to 424
        #  416 RERAISE
        #  418 COPY
        #  420 POP_EXCEPT
        #  422 RERAISE
        #  424 LOAD_GLOBAL datetime
        #  436 LOAD_ATTR datetime
        #  446 LOAD_METHOD now
        #  468 LOAD_GLOBAL datetime
        #  480 LOAD_ATTR timezone
        #  490 LOAD_ATTR utc
        #  500 PRECALL
        #  504 CALL
        #  514 STORE_FAST now
        #  516 LOAD_FAST self
        #  518 LOAD_ATTR row_info
        #  528 LOAD_METHOD values
        # ... bytecode truncated ...
        pass

    def update_active_scan_info(self, remote, active_scan):
        row_info = self.row_info.get(remote)

    def update_controller(self, remote, controller):
        row_info = self.row_info.get(remote)

    def update_scan_count(self):
        self.clearButton.setText('Clear ({})'.format(len(self.row_info)))
