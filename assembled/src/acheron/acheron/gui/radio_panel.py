# Source Generated with Decompyle++
# File: radio_panel.pyc (Python 3.11)

from __future__ import annotations
import bisect
from collections import deque
import datetime
import logging
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
from ..device_logging import DeviceLoggerAdapter
from ..core.device_controller import DeviceController, DeviceControllerState
from ..core.preferences import Preferences
from ..core.radio_scan import ActiveScanDatabase, ScanResult
from .radio_detail_scan import DetailScanDialog
from .ui.ui_radio_panel import Ui_RadioPanel
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RadioPanel(Ui_RadioPanel, QtWidgets.QGroupBox):

    show_remote_clicked = QtCore.Signal()

    def __init__(self, controller, active_scan_database, preferences, parent):
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
        #   84 LOAD_FAST active_scan_database
        #   86 LOAD_FAST self
        #   88 STORE_ATTR active_scan_database
        #   98 LOAD_FAST preferences
        #  100 LOAD_FAST self
        #  102 STORE_ATTR preferences
        #  112 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #  124 LOAD_GLOBAL logger
        #  136 LOAD_FAST controller
        #  138 LOAD_ATTR serial_number
        #  148 PRECALL
        #  152 CALL
        #  162 LOAD_FAST self
        #  164 STORE_ATTR logger
        #  174 BUILD_LIST
        #  176 LOAD_FAST self
        #  178 STORE_ATTR scan_serials
        #  188 BUILD_MAP
        #  190 LOAD_FAST self
        #  192 STORE_ATTR scans
        #  202 LOAD_GLOBAL NULL + deque
        #  214 PRECALL
        #  218 CALL
        #  228 LOAD_FAST self
        #  230 STORE_ATTR device_list_additions
        #  240 LOAD_FAST self
        #  242 LOAD_METHOD setupUi
        #  264 LOAD_FAST self
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_FAST self
        #  284 LOAD_METHOD extra_ui_setup
        #  306 PRECALL
        #  310 CALL
        #  320 POP_TOP
        #  322 LOAD_FAST self
        #  324 LOAD_METHOD setup_callbacks
        #  346 PRECALL
        #  350 CALL
        #  360 POP_TOP
        #  362 LOAD_CONST None
        #  364 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        self.detail_scan_dialog = DetailScanDialog(self.active_scan_database, self.preferences, self)
        self.menu = QtWidgets.QMenu(self)
        self.menu.addAction(self.actionConnectNoStreaming)
        self.menu.addSeparator()
        self.menu.addAction(self.actionConnectSpecificBootloader)
        self.menu.addAction(self.actionConnectSpecificSerial)
        self.advancedMenuButton.setMenu(self.menu)
        self.deviceList.addAction(self.actionClear)
        self.actionClear.setIcon(QtGui.QIcon.fromTheme('delete'))
        self.clearButton.setDefaultAction(self.actionClear)

    def setup_callbacks(self):
        self.detailScanButton.clicked.connect(self.detail_scan)
        self.connectButton.clicked.connect(self.connect_button_cb)
        self.disconnectButton.clicked.connect(self.disconnect_button_cb)
        self.goToRemoteButton.clicked.connect(self.show_remote_clicked)
        self.deviceList.currentRowChanged.connect(self.current_row_changed_cb)
        self.deviceList.itemDoubleClicked.connect(self.item_double_clicked_cb)
        self.actionConnectNoStreaming.triggered.connect(self.connect_no_streaming_cb)
        self.actionConnectSpecificBootloader.triggered.connect(self.connect_specific_bootloader_cb)
        self.actionConnectSpecificSerial.triggered.connect(self.connect_specific_serial_cb)
        self.actionClear.triggered.connect(self.clear_list)
        self.update_device_list_timer = QtCore.QTimer(self)
        self.update_device_list_timer.timeout.connect(self.update_device_list)
        self.update_device_list_timer.start(250)
        self.controller.scan_data.connect(self.scan_data_cb)
        self.controller.remote_target_changed.connect(self.remote_target_changed_cb)
        self.controller.scan_first_pass.connect(self.scan_first_pass_cb)
        self.controller.state_changed_signal.connect(self.controller_state_changed_cb)
        self.controller.remote_connected.connect(self.remote_connected_cb)
        self.controller.remote_target_connected.connect(self.remote_target_connected_cb)

    def add_ctrl_var_widget(self, widget):
        self.ctrlVarLayout.addWidget(widget)

    def clear_ctrl_var_widgets(self):
        item = self.ctrlVarLayout.takeAt(0)
        if not item:
            return None

    def connect_button_cb(self):
        scan = self.get_selected_scan()
        if scan:
            self.controller.set_remote_target(scan.serial_number, scan.bootloader)
            return None

    def connect_no_streaming_cb(self):
        scan = self.get_selected_scan()
        if scan:
            self.controller.set_remote_target(scan.serial_number, scan.bootloader, streaming = False)
            return None

    def connect_specific_bootloader_cb(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL QtWidgets
        #   14 LOAD_ATTR QInputDialog
        #   24 LOAD_METHOD getInt
        #   46 LOAD_FAST self
        #   48 LOAD_FAST self
        #   50 LOAD_METHOD tr
        #   72 LOAD_CONST 'Bootloader Serial'
        #   74 PRECALL
        #   78 CALL
        #   88 LOAD_FAST self
        #   90 LOAD_METHOD tr
        #  112 LOAD_CONST 'Input bootloader serial number'
        #  114 PRECALL
        #  118 CALL
        #  128 PRECALL
        #  132 CALL
        #  142 UNPACK_SEQUENCE
        #  146 STORE_FAST sn
        #  148 STORE_FAST ok
        #  150 LOAD_FAST ok
        #  152 POP_JUMP_FORWARD_IF_TRUE to 158
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR controller
        #  170 LOAD_METHOD set_remote_target
        #  192 LOAD_FAST sn
        #  194 LOAD_CONST True
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 LOAD_CONST None
        #  214 RETURN_VALUE
        pass

    def connect_specific_serial_cb(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL QtWidgets
        #   14 LOAD_ATTR QInputDialog
        #   24 LOAD_METHOD getInt
        #   46 LOAD_FAST self
        #   48 LOAD_FAST self
        #   50 LOAD_METHOD tr
        #   72 LOAD_CONST 'Device Serial'
        #   74 PRECALL
        #   78 CALL
        #   88 LOAD_FAST self
        #   90 LOAD_METHOD tr
        #  112 LOAD_CONST 'Input device serial number'
        #  114 PRECALL
        #  118 CALL
        #  128 PRECALL
        #  132 CALL
        #  142 UNPACK_SEQUENCE
        #  146 STORE_FAST sn
        #  148 STORE_FAST ok
        #  150 LOAD_FAST ok
        #  152 POP_JUMP_FORWARD_IF_TRUE to 158
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR controller
        #  170 LOAD_METHOD set_remote_target
        #  192 LOAD_FAST sn
        #  194 LOAD_CONST False
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 LOAD_CONST None
        #  214 RETURN_VALUE
        pass

    def disconnect_button_cb(self):
        self.controller.clear_remote_target()

    def remote_target_changed_cb(self, serial_number, bootloader, streaming):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST serial_number
        #    4 EXTENDED_ARG
        #    6 POP_JUMP_FORWARD_IF_NOT_NONE to 562
        #    8 LOAD_FAST self
        #   10 LOAD_ATTR actionConnectNoStreaming
        #   20 LOAD_METHOD setEnabled
        #   42 LOAD_CONST True
        #   44 PRECALL
        #   48 CALL
        #   58 POP_TOP
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR actionConnectSpecificBootloader
        #   72 LOAD_METHOD setEnabled
        #   94 LOAD_CONST True
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR actionConnectSpecificSerial
        #  124 LOAD_METHOD setEnabled
        #  146 LOAD_CONST True
        #  148 PRECALL
        #  152 CALL
        #  162 POP_TOP
        #  164 LOAD_FAST self
        #  166 LOAD_ATTR detailScanButton
        #  176 LOAD_METHOD setEnabled
        #  198 LOAD_CONST True
        #  200 PRECALL
        #  204 CALL
        #  214 POP_TOP
        #  216 LOAD_FAST self
        #  218 LOAD_ATTR deviceList
        #  228 LOAD_METHOD setEnabled
        #  250 LOAD_CONST True
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_FAST self
        #  270 LOAD_ATTR clearButton
        #  280 LOAD_METHOD setEnabled
        #  302 LOAD_CONST True
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 LOAD_FAST self
        #  322 LOAD_ATTR disconnectButton
        #  332 LOAD_METHOD setEnabled
        #  354 LOAD_CONST False
        #  356 PRECALL
        #  360 CALL
        #  370 POP_TOP
        #  372 LOAD_FAST self
        #  374 LOAD_ATTR connectButton
        #  384 LOAD_METHOD setText
        #  406 LOAD_FAST self
        #  408 LOAD_METHOD tr
        #  430 LOAD_CONST 'Connect'
        #  432 PRECALL
        #  436 CALL
        #  446 PRECALL
        #  450 CALL
        #  460 POP_TOP
        #  462 LOAD_FAST self
        #  464 LOAD_METHOD get_selected_scan
        #  486 PRECALL
        #  490 CALL
        #  500 LOAD_CONST None
        #  502 IS_OP
        #  504 STORE_FAST selected
        #  506 LOAD_FAST self
        #  508 LOAD_ATTR connectButton
        #  518 LOAD_METHOD setEnabled
        #  540 LOAD_FAST selected
        #  542 PRECALL
        #  546 CALL
        #  556 POP_TOP
        #  558 LOAD_CONST None
        #  560 RETURN_VALUE
        # ... bytecode truncated ...
        pass

    def remote_target_connected_cb(self, connected):
        if connected:
            self.actionConnectNoStreaming.setEnabled(False)
            self.actionConnectSpecificBootloader.setEnabled(False)
            self.actionConnectSpecificSerial.setEnabled(False)
            self.detailScanButton.setEnabled(False)
            self.deviceList.setEnabled(False)
            self.clearButton.setEnabled(False)
            self.disconnectButton.setEnabled(True)
            self.connectButton.setText(self.tr('Connected'))
            self.connectButton.setEnabled(False)
            return None

    def remote_connected_cb(self, connected):
        self.goToRemoteButton.setEnabled(connected)

    def scan_first_pass_cb(self):
        self.update_device_list()

    def controller_state_changed_cb(self, state, _message):
        if state == DeviceControllerState.STREAMING_STARTING:
            self.clear_list()
            return None

    def detail_scan(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR active_scan_database
        #   14 LOAD_METHOD detail_scan_opened
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 NOP
        #   54 LOAD_FAST self
        #   56 LOAD_ATTR detail_scan_dialog
        #   66 LOAD_METHOD exec
        #   88 PRECALL
        #   92 CALL
        #  102 STORE_FAST ret
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR active_scan_database
        #  116 LOAD_METHOD detail_scan_closed
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 JUMP_FORWARD to 216
        #  156 PUSH_EXC_INFO
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR active_scan_database
        #  170 LOAD_METHOD detail_scan_closed
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 RERAISE
        #  210 COPY
        #  212 POP_EXCEPT
        #  214 RERAISE
        #  216 LOAD_FAST ret
        #  218 LOAD_CONST 0
        #  220 COMPARE_OP ==
        #  226 POP_JUMP_FORWARD_IF_FALSE to 232
        #  228 LOAD_CONST None
        #  230 RETURN_VALUE
        #  232 LOAD_FAST self
        #  234 LOAD_ATTR detail_scan_dialog
        #  244 LOAD_METHOD get_selected_scan
        #  266 PRECALL
        #  270 CALL
        #  280 STORE_FAST scan
        #  282 LOAD_FAST scan
        #  284 POP_JUMP_FORWARD_IF_FALSE to 364
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR controller
        #  298 LOAD_METHOD set_remote_target
        #  320 LOAD_FAST scan
        #  322 LOAD_ATTR serial_number
        #  332 LOAD_FAST scan
        #  334 LOAD_ATTR bootloader
        #  344 PRECALL
        #  348 CALL
        #  358 POP_TOP
        #  360 LOAD_CONST None
        #  362 RETURN_VALUE
        #  364 LOAD_CONST None
        #  366 RETURN_VALUE
        pass

    def current_row_changed_cb(self, row):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST row
        #    4 LOAD_CONST -1
        #    6 COMPARE_OP ==
        #   12 POP_JUMP_FORWARD_IF_FALSE to 70
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR connectButton
        #   26 LOAD_METHOD setEnabled
        #   48 LOAD_CONST False
        #   50 PRECALL
        #   54 CALL
        #   64 POP_TOP
        #   66 LOAD_CONST None
        #   68 RETURN_VALUE
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR connectButton
        #   82 LOAD_METHOD setEnabled
        #  104 LOAD_CONST True
        #  106 PRECALL
        #  110 CALL
        #  120 POP_TOP
        #  122 LOAD_CONST None
        #  124 RETURN_VALUE
        pass

    def item_double_clicked_cb(self, item):
        self.handle_device_list_additions()
        row = self.deviceList.row(item)
        if row != -1:
            serial_number = self.scan_serials[row]
            scan = self.scans.get(serial_number)
            if scan:
                self.controller.set_remote_target(scan.serial_number, scan.bootloader)
                return None
            return None

    def get_selected_scan(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD handle_device_list_additions
        #   26 PRECALL
        #   30 CALL
        #   40 POP_TOP
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR deviceList
        #   54 LOAD_METHOD currentRow
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST row
        #   92 LOAD_FAST row
        #   94 LOAD_CONST -1
        #   96 COMPARE_OP ==
        #  102 POP_JUMP_FORWARD_IF_FALSE to 108
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        #  108 LOAD_FAST self
        #  110 LOAD_ATTR scan_serials
        #  120 LOAD_FAST row
        #  122 BINARY_SUBSCR
        #  132 STORE_FAST serial_number
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR scans
        #  146 LOAD_METHOD get
        #  168 LOAD_FAST serial_number
        #  170 PRECALL
        #  174 CALL
        #  184 RETURN_VALUE
        pass

    def scan_data_cb(self, _controller, scans):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST scans
        #    4 GET_ITER
        #    6 FOR_ITER to 94
        #    8 STORE_FAST scan
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR detail_scan_dialog
        #   22 LOAD_METHOD handle_scan
        #   44 LOAD_FAST scan
        #   46 PRECALL
        #   50 CALL
        #   60 POP_TOP
        #   62 LOAD_FAST scan
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR scans
        #   76 LOAD_FAST scan
        #   78 LOAD_ATTR serial_number
        #   88 STORE_SUBSCR
        #   92 JUMP_BACKWARD to 6
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR controller
        #  106 LOAD_ATTR remote_target_serial
        #  116 POP_JUMP_FORWARD_IF_NOT_NONE to 542
        #  118 LOAD_CONST False
        #  120 STORE_FAST changed_scan_count
        #  122 LOAD_FAST scans
        #  124 GET_ITER
        #  126 FOR_ITER to 494
        #  128 STORE_FAST scan
        #  130 LOAD_GLOBAL NULL + bisect
        #  142 LOAD_ATTR bisect_left
        #  152 LOAD_FAST self
        #  154 LOAD_ATTR scan_serials
        #  164 LOAD_FAST scan
        #  166 LOAD_ATTR serial_number
        #  176 PRECALL
        #  180 CALL
        #  190 STORE_FAST index
        #  192 LOAD_FAST index
        #  194 LOAD_GLOBAL NULL + len
        #  206 LOAD_FAST self
        #  208 LOAD_ATTR scan_serials
        #  218 PRECALL
        #  222 CALL
        #  232 COMPARE_OP !=
        #  238 POP_JUMP_FORWARD_IF_FALSE to 286
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR scan_serials
        #  252 LOAD_FAST index
        #  254 BINARY_SUBSCR
        #  264 LOAD_FAST scan
        #  266 LOAD_ATTR serial_number
        #  276 COMPARE_OP ==
        #  282 POP_JUMP_FORWARD_IF_FALSE to 286
        #  284 JUMP_BACKWARD to 126
        #  286 LOAD_GLOBAL NULL + QtWidgets
        #  298 LOAD_ATTR QListWidgetItem
        #  308 PRECALL
        #  312 CALL
        #  322 STORE_FAST list_item
        #  324 LOAD_FAST self
        #  326 LOAD_METHOD update_list_item
        #  348 LOAD_FAST list_item
        #  350 LOAD_FAST scan
        #  352 PRECALL
        #  356 CALL
        #  366 POP_TOP
        #  368 LOAD_FAST self
        #  370 LOAD_ATTR scan_serials
        #  380 LOAD_METHOD insert
        #  402 LOAD_FAST index
        #  404 LOAD_FAST scan
        #  406 LOAD_ATTR serial_number
        #  416 PRECALL
        #  420 CALL
        #  430 POP_TOP
        #  432 LOAD_FAST self
        #  434 LOAD_ATTR device_list_additions
        #  444 LOAD_METHOD append
        #  466 LOAD_FAST index
        # ... bytecode truncated ...
        pass

    def _get_scan_strength_bars(scan_strength):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST scan_strength
        #    4 LOAD_CONST -30
        #    6 COMPARE_OP >=
        #   12 POP_JUMP_FORWARD_IF_FALSE to 18
        #   14 LOAD_CONST '▁\u200a▂\u200a▃\u200a▅\u200a▇'
        #   16 RETURN_VALUE
        #   18 LOAD_FAST scan_strength
        #   20 LOAD_CONST -40
        #   22 COMPARE_OP >=
        #   28 POP_JUMP_FORWARD_IF_FALSE to 34
        #   30 LOAD_CONST '▁\u200a▂\u200a▃\u200a▅\u200a▁'
        #   32 RETURN_VALUE
        #   34 LOAD_FAST scan_strength
        #   36 LOAD_CONST -50
        #   38 COMPARE_OP >=
        #   44 POP_JUMP_FORWARD_IF_FALSE to 50
        #   46 LOAD_CONST '▁\u200a▂\u200a▃\u200a▁\u200a▁'
        #   48 RETURN_VALUE
        #   50 LOAD_FAST scan_strength
        #   52 LOAD_CONST -60
        #   54 COMPARE_OP >=
        #   60 POP_JUMP_FORWARD_IF_FALSE to 66
        #   62 LOAD_CONST '▁\u200a▂\u200a▃\u200a▁\u200a▁'
        #   64 RETURN_VALUE
        #   66 LOAD_CONST '▁\u200a▁\u200a▁\u200a▁\u200a▁'
        #   68 RETURN_VALUE
        pass

    def update_list_item(self, list_item, scan):
        text_elements = []
        active_scan = self.active_scan_database.get_active_scan(scan.serial_number)
        if scan.serial_number != 0xFFFFFFFF:
            text_elements.append(str(scan.serial_number))
        else:
            text_elements.append('Any')
        if scan.serial_number == self.controller.default_remote_target:
            text_elements.append('<Auto>')

    def _get_placeholder_scan(self, serial_number, bootloader):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR scans
        #   14 LOAD_METHOD get
        #   36 LOAD_FAST serial_number
        #   38 PRECALL
        #   42 CALL
        #   52 STORE_FAST scan
        #   54 LOAD_FAST scan
        #   56 POP_JUMP_FORWARD_IF_FALSE to 62
        #   58 LOAD_FAST scan
        #   60 RETURN_VALUE
        #   62 LOAD_GLOBAL datetime
        #   74 LOAD_ATTR datetime
        #   84 LOAD_METHOD now
        #  106 LOAD_GLOBAL datetime
        #  118 LOAD_ATTR timezone
        #  128 LOAD_ATTR utc
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST now
        #  154 LOAD_GLOBAL NULL + ScanResult
        #  166 LOAD_FAST serial_number
        #  168 LOAD_FAST now
        #  170 LOAD_FAST bootloader
        #  172 LOAD_CONST 0
        #  174 LOAD_CONST 0
        #  176 LOAD_CONST None
        #  178 LOAD_CONST None
        #  180 KW_NAMES
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST scan
        #  198 LOAD_FAST scan
        #  200 LOAD_FAST self
        #  202 LOAD_ATTR scans
        #  212 LOAD_FAST serial_number
        #  214 STORE_SUBSCR
        #  218 LOAD_FAST scan
        #  220 RETURN_VALUE
        pass

    def prune_list(self, connected_serial, connected_bootloader):
        self.deviceList.clear()
        self.scan_serials.clear()
        self.device_list_additions.clear()
        restore_scans = { }
        if connected_serial:
            scan = self._get_placeholder_scan(connected_serial, connected_bootloader)
            scan.scan_strength = None
            restore_scans[connected_serial] = scan
        if self.controller.default_remote_target and self.controller.default_remote_target != connected_serial:
            scan = self._get_placeholder_scan(self.controller.default_remote_target, False)
            scan.scan_strength = None
            scan.bootloader = False
            restore_scans[self.controller.default_remote_target] = scan
        for i, serial_number in enumerate(sorted(restore_scans.keys())):
            scan = restore_scans[serial_number]
            list_item = QtWidgets.QListWidgetItem()
            self.update_list_item(list_item, scan)
            self.scan_serials.append(scan.serial_number)
            self.deviceList.insertItem(i, list_item)
            if serial_number == connected_serial:
                self.deviceList.setCurrentRow(i)
            self.update_scan_count()
            return None

    def clear_list(self):
        self.prune_list(None, False)

    def update_scan_count(self):
        text = 'Clear ({})'.format(len(self.scan_serials))
        self.clearButton.setText(text)
        self.clearButton.setToolTip(text)

    def handle_device_list_additions(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST False
        #    4 STORE_FAST updated
        #    6 NOP
        #    8 NOP
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR device_list_additions
        #   22 LOAD_METHOD popleft
        #   44 PRECALL
        #   48 CALL
        #   58 UNPACK_SEQUENCE
        #   62 STORE_FAST index
        #   64 STORE_FAST list_item
        #   66 LOAD_FAST updated
        #   68 POP_JUMP_FORWARD_IF_TRUE to 126
        #   70 LOAD_CONST True
        #   72 STORE_FAST updated
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR deviceList
        #   86 LOAD_METHOD setUpdatesEnabled
        #  108 LOAD_CONST False
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR deviceList
        #  138 LOAD_METHOD insertItem
        #  160 LOAD_FAST index
        #  162 LOAD_FAST list_item
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 JUMP_BACKWARD to 10
        #  182 PUSH_EXC_INFO
        #  184 LOAD_GLOBAL IndexError
        #  196 CHECK_EXC_MATCH
        #  198 POP_JUMP_FORWARD_IF_FALSE to 206
        #  200 POP_TOP
        #  202 POP_EXCEPT
        #  204 JUMP_FORWARD to 214
        #  206 RERAISE
        #  208 COPY
        #  210 POP_EXCEPT
        #  212 RERAISE
        #  214 LOAD_FAST updated
        #  216 POP_JUMP_FORWARD_IF_FALSE to 274
        #  218 LOAD_FAST self
        #  220 LOAD_ATTR deviceList
        #  230 LOAD_METHOD setUpdatesEnabled
        #  252 LOAD_CONST True
        #  254 PRECALL
        #  258 CALL
        #  268 POP_TOP
        #  270 LOAD_CONST None
        #  272 RETURN_VALUE
        #  274 LOAD_CONST None
        #  276 RETURN_VALUE
        pass

    def update_device_list(self):
        self.handle_device_list_additions()
