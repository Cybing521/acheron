# Source Generated with Decompyle++
# File: device_tab.pyc (Python 3.11)

from __future__ import annotations
import datetime
import functools
import io
import json
import logging
import lzma
import math
import multiprocessing.connection as multiprocessing
import os
import pathlib
import platform
import struct
from typing import Any, cast, Optional, TYPE_CHECKING, Union
import weakref
import diskcache
import numpy
from numpy.typing import NDArray
from PySide6 import QtCore, QtGui, QtWidgets
import pyqtgraph
import asphodel
from asphodel import ChannelCalibration
from asphodel.device_info import DeviceInfo
import hyperborea.download as hyperborea
from hyperborea.unit_preferences import get_default_option, get_unit_options, UnitOption
from hyperborea.device_info_dialog import DeviceInfoDialog
from ..calc_process.types import ChannelInformation, LimitType
from ..core.calibration import get_channel_setting_values, update_nvm
from ..core.device_controller import DeviceController, DeviceControllerState
from ..core.preferences import Preferences
from ..device_logging import DeviceLoggerAdapter
from ..device_process import bootloader
from ..device_process.stream_controller import RFTestParams
from .calibration import CalibrationConnection, CalibrationPanel
from .change_stream_dialog import ChangeStreamDialog
from .connectivity_dialog import ConnectivityDialog
from .ctrl_var_panel import CtrlVarPanel
from .ctrl_var_widget import CtrlVarWidget
from .edit_alert_dialog import EditAlertDialog
from .gui_log import get_log_list_model
from .hardware_tests import HardwareTestDialog
from .led_control_widget import LEDControlWidget
from .radio_panel import RadioPanel
from .remote_panel import RemotePanel
from .rf_power_panel import RFPowerPanel
from .rf_test_dialog import RFTestDialog
from .rgb_control_widget import RGBControlWidget
from .setting_dialog import SettingDialog
from .ui.ui_device_tab import Ui_DeviceTab
if TYPE_CHECKING:
    from .plotmain import PlotMainWindow
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class MeasurementLineEdit(QtWidgets.QLineEdit):

    def __init__(self, unit_actions, parent):
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
        #   70 LOAD_FAST unit_actions
        #   72 LOAD_FAST self
        #   74 STORE_ATTR unit_actions
        #   84 LOAD_CONST False
        #   86 LOAD_FAST self
        #   88 STORE_ATTR alert
        #   98 LOAD_FAST self
        #  100 LOAD_METHOD setReadOnly
        #  122 LOAD_CONST True
        #  124 PRECALL
        #  128 CALL
        #  138 POP_TOP
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD setAlignment
        #  164 LOAD_GLOBAL QtCore
        #  176 LOAD_ATTR Qt
        #  186 LOAD_ATTR AlignmentFlag
        #  196 LOAD_ATTR AlignRight
        #  206 LOAD_GLOBAL QtCore
        #  218 LOAD_ATTR Qt
        #  228 LOAD_ATTR AlignmentFlag
        #  238 LOAD_ATTR AlignVCenter
        #  248 BINARY_OP |
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_FAST self
        #  270 LOAD_METHOD setSizePolicy
        #  292 LOAD_GLOBAL NULL + QtWidgets
        #  304 LOAD_ATTR QSizePolicy
        #  314 LOAD_GLOBAL QtWidgets
        #  326 LOAD_ATTR QSizePolicy
        #  336 LOAD_ATTR Policy
        #  346 LOAD_ATTR Minimum
        #  356 LOAD_GLOBAL QtWidgets
        #  368 LOAD_ATTR QSizePolicy
        #  378 LOAD_ATTR Policy
        #  388 LOAD_ATTR Minimum
        #  398 PRECALL
        #  402 CALL
        #  412 PRECALL
        #  416 CALL
        #  426 POP_TOP
        #  428 LOAD_FAST self
        #  430 LOAD_METHOD setFixedWidth
        #  452 LOAD_CONST 100
        #  454 PRECALL
        #  458 CALL
        #  468 POP_TOP
        #  470 LOAD_GLOBAL NULL + QtGui
        #  482 LOAD_ATTR QAction
        #  492 LOAD_FAST self
        #  494 PRECALL
        #  498 CALL
        #  508 LOAD_FAST self
        #  510 STORE_ATTR copy_action
        #  520 LOAD_FAST self
        #  522 LOAD_ATTR copy_action
        #  532 LOAD_METHOD setText
        #  554 LOAD_FAST self
        #  556 LOAD_METHOD tr
        #  578 LOAD_CONST 'Copy Text'
        #  580 PRECALL
        #  584 CALL
        #  594 PRECALL
        #  598 CALL
        #  608 POP_TOP
        #  610 LOAD_FAST self
        #  612 LOAD_ATTR copy_action
        #  622 LOAD_METHOD setShortcut
        # ... bytecode truncated ...
        pass

    def _copy_cb(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.text())

    def set_alert(self, new_alert):
        if not new_alert and self.alert:
            self.alert = True
            self.setStyleSheet('* { color: black; background-color: red; }')
        if not self.alert or new_alert:
            self.alert = False
            self.setStyleSheet('')
            return None
        return None

class EditAlertAction(QtGui.QAction):

    def __init__(self, channel_id, subchannel_index, subchannel_name, device_tab, parent):
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
        #   70 LOAD_GLOBAL NULL + weakref
        #   82 LOAD_ATTR ref
        #   92 LOAD_FAST device_tab
        #   94 PRECALL
        #   98 CALL
        #  108 LOAD_FAST self
        #  110 STORE_ATTR device_tab
        #  120 LOAD_FAST channel_id
        #  122 LOAD_FAST self
        #  124 STORE_ATTR channel_id
        #  134 LOAD_FAST subchannel_index
        #  136 LOAD_FAST self
        #  138 STORE_ATTR subchannel_index
        #  148 LOAD_FAST self
        #  150 LOAD_METHOD setText
        #  172 LOAD_FAST self
        #  174 LOAD_METHOD tr
        #  196 LOAD_CONST 'Edit Alert for {}'
        #  198 PRECALL
        #  202 CALL
        #  212 LOAD_METHOD format
        #  234 LOAD_FAST subchannel_name
        #  236 PRECALL
        #  240 CALL
        #  250 PRECALL
        #  254 CALL
        #  264 POP_TOP
        #  266 LOAD_FAST self
        #  268 LOAD_ATTR triggered
        #  278 LOAD_METHOD connect
        #  300 LOAD_FAST self
        #  302 LOAD_ATTR handle_edit
        #  312 PRECALL
        #  316 CALL
        #  326 POP_TOP
        #  328 LOAD_CONST None
        #  330 RETURN_VALUE
        pass

    def handle_edit(self):
        device_tab = self.device_tab()

class DeviceTab(Ui_DeviceTab, QtWidgets.QWidget):

    collapsed_set = QtCore.Signal(bool)

    def __init__(self, controller, plotmain, preferences, collapsed, firmware_cache, tree_item):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_CONST None
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST controller
        #   72 LOAD_FAST self
        #   74 STORE_ATTR controller
        #   84 LOAD_FAST plotmain
        #   86 LOAD_FAST self
        #   88 STORE_ATTR plotmain
        #   98 LOAD_FAST preferences
        #  100 LOAD_FAST self
        #  102 STORE_ATTR preferences
        #  112 LOAD_FAST collapsed
        #  114 LOAD_FAST self
        #  116 STORE_ATTR collapsed
        #  126 LOAD_FAST firmware_cache
        #  128 LOAD_FAST self
        #  130 STORE_ATTR firmware_cache
        #  140 LOAD_FAST tree_item
        #  142 LOAD_FAST self
        #  144 STORE_ATTR tree_item
        #  154 LOAD_GLOBAL NULL + QtCore
        #  166 LOAD_ATTR QSettings
        #  176 PRECALL
        #  180 CALL
        #  190 LOAD_FAST self
        #  192 STORE_ATTR settings
        #  202 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #  214 LOAD_GLOBAL logger
        #  226 LOAD_FAST self
        #  228 LOAD_ATTR controller
        #  238 LOAD_ATTR serial_number
        #  248 PRECALL
        #  252 CALL
        #  262 LOAD_FAST self
        #  264 STORE_ATTR logger
        #  274 BUILD_MAP
        #  276 LOAD_FAST self
        #  278 STORE_ATTR subchannel_fields
        #  288 BUILD_MAP
        #  290 LOAD_FAST self
        #  292 STORE_ATTR channel_unit_options
        #  302 BUILD_MAP
        #  304 LOAD_FAST self
        #  306 STORE_ATTR channel_unit_actions
        #  316 BUILD_MAP
        #  318 LOAD_FAST self
        #  320 STORE_ATTR channel_unit_action_group
        #  330 BUILD_MAP
        #  332 LOAD_FAST self
        #  334 STORE_ATTR channel_unit_type
        #  344 BUILD_MAP
        #  346 LOAD_FAST self
        #  348 STORE_ATTR channel_unit_default
        #  358 BUILD_MAP
        #  360 LOAD_FAST self
        #  362 STORE_ATTR channel_unit
        #  372 BUILD_MAP
        #  374 LOAD_FAST self
        #  376 STORE_ATTR channel_alert_actions
        #  386 BUILD_LIST
        #  388 LOAD_FAST self
        #  390 STORE_ATTR rgb_widgets
        #  400 BUILD_LIST
        #  402 LOAD_FAST self
        #  404 STORE_ATTR led_widgets
        #  414 BUILD_LIST
        #  416 LOAD_FAST self
        #  418 STORE_ATTR ctrl_var_widgets
        #  428 LOAD_CONST None
        #  430 LOAD_FAST self
        #  432 STORE_ATTR calibration_panel
        #  442 BUILD_LIST
        # ... bytecode truncated ...
        pass

    def extra_ui_setup(self):
        self.stackedWidget.setCurrentIndex(0)
        self.statusProgressBar.setVisible(False)
        self.serialNumber.setText(self.controller.serial_number)
        self.userTag1.setText('')
        self.userTag2.setText('')
        self.boardInfo.setText('')
        self.buildInfo.setText('')
        self.buildDate.setText('')
        self.branch.setText('')
        self.bootloaderIndicator.setVisible(False)
        self.nvmModifiedIndicator.setVisible(False)
        self.schedule_or_trigger_count_updated()
        self.menu = QtWidgets.QMenu()
        self.firmware_menu = self.menu.addMenu(self.tr('Update Firmware'))
        self.firmware_menu.setEnabled(False)
        self.firmware_menu.addAction(self.actionFirmwareLatestStable)
        self.firmware_menu.addAction(self.actionFirmwareFromBranch)
        self.firmware_menu.addAction(self.actionFirmwareFromCommit)
        self.firmware_menu.addAction(self.actionFirmwareFromFile)
        self.advanced_menu = self.menu.addMenu(self.tr('Advanced Actions'))
        self.advanced_menu.addAction(self.actionForceRunBootloader)
        self.advanced_menu.addAction(self.actionForceRunApplication)
        self.advanced_menu.addAction(self.actionForceReset)
        self.advanced_menu.addAction(self.actionRaiseException)
        self.advanced_menu.addAction(self.actionRecoverNVM)
        self.menu.addSeparator()
        self.menu.addAction(self.actionCalibrate)
        self.menu.addAction(self.actionShakerCalibrate)
        self.menu.addSeparator()
        self.menu.addAction(self.actionConnectivity)
        self.actionRFTestSeparator = self.menu.addSeparator()
        self.menu.addAction(self.actionRFTest)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSetDeviceMode)
        self.menu.addAction(self.actionChangeActiveStreams)
        self.menu.addAction(self.actionRunTests)
        self.menuButton.setMenu(self.menu)
        self.actionCalibrate.setIcon(QtGui.QIcon.fromTheme('caliper'))
        self.actionChangeActiveStreams.setIcon(QtGui.QIcon.fromTheme('preferences_edit'))
        self.actionConnectivity.setIcon(QtGui.QIcon.fromTheme('client_network'))
        self.actionEditDeviceSettings.setIcon(QtGui.QIcon.fromTheme('gear'))
        self.actionFirmwareFromBranch.setIcon(QtGui.QIcon.fromTheme('branch_view'))
        self.actionFirmwareFromCommit.setIcon(QtGui.QIcon.fromTheme('symbol_hash'))
        self.actionFirmwareFromFile.setIcon(QtGui.QIcon.fromTheme('document_plain'))
        self.actionFirmwareLatestStable.setIcon(QtGui.QIcon.fromTheme('branch'))
        self.actionForceReset.setIcon(QtGui.QIcon.fromTheme('redo'))
        self.actionForceRunApplication.setIcon(QtGui.QIcon.fromTheme('application'))
        self.actionForceRunBootloader.setIcon(QtGui.QIcon.fromTheme('flash_yellow'))
        self.actionRaiseException.setIcon(QtGui.QIcon.fromTheme('bomb'))
        self.actionRecoverNVM.setIcon(QtGui.QIcon.fromTheme('document_gear'))
        self.actionRFTest.setIcon(QtGui.QIcon.fromTheme('rf_test'))
        self.actionRunTests.setIcon(QtGui.QIcon.fromTheme('stethoscope'))
        self.actionSetDeviceMode.setIcon(QtGui.QIcon.fromTheme('text_list_numbers'))
        self.actionCopySerialNumber.setIcon(QtGui.QIcon.fromTheme('copy'))
        self.actionSetUserTag1.setIcon(QtGui.QIcon.fromTheme('tag'))
        self.actionSetUserTag2.setIcon(QtGui.QIcon.fromTheme('tag'))
        self.actionShakerCalibrate.setIcon(QtGui.QIcon.fromTheme('shaker'))
        self.actionShowDeviceInfo.setIcon(QtGui.QIcon.fromTheme('information'))
        self.actionFlushLostPackets.setIcon(QtGui.QIcon.fromTheme('replace2'))
        self.actionShowPacketStats.setIcon(QtGui.QIcon.fromTheme('chart_column'))
        self.firmware_menu.setIcon(QtGui.QIcon.fromTheme('cpu_flash'))
        self.advanced_menu.setIcon(QtGui.QIcon.fromTheme('wrench'))
        self.firmware_progress = QtWidgets.QProgressDialog('', '', 0, 100)
        self.firmware_progress.setLabelText(self.tr(''))
        self.firmware_progress.setWindowTitle(self.tr('Firmware Update'))
        self.firmware_progress.setCancelButton(None)
        self.firmware_progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        self.firmware_progress.setMinimumDuration(0)
        self.firmware_progress.setAutoReset(False)
        self.firmware_progress.reset()
        self.set_collapsed(self.collapsed)
        self.deviceInfo.setDefaultAction(self.actionShowDeviceInfo)
        self.copySerialNumber.setDefaultAction(self.actionCopySerialNumber)
        self.setUserTag1.setDefaultAction(self.actionSetUserTag1)
        self.setUserTag2.setDefaultAction(self.actionSetUserTag2)
        self.flushLostPackets.setDefaultAction(self.actionFlushLostPackets)
        self.lostPacketDetails.setDefaultAction(self.actionShowPacketStats)
        self.editDeviceSettings.setDefaultAction(self.actionEditDeviceSettings)
        self.ctrl_var_panel = CtrlVarPanel(self)
        self.panelLayout.addWidget(self.ctrl_var_panel)
        self.rf_power_panel = RFPowerPanel(self.controller, self)
        self.panelLayout.addWidget(self.rf_power_panel)
        self.radio_panel = RadioPanel(self.controller, self.plotmain.dispatcher.active_scan_database, self.preferences, self)
        self.radio_panel.show_remote_clicked.connect(self.show_remote_tab)
        self.panelLayout.addWidget(self.radio_panel)
        self.remote_panel = RemotePanel(self)
        self.remote_panel.show_radio_clicked.connect(self.show_radio_tab)
        self.panelLayout.addWidget(self.remote_panel)
        inactive_triggers = self.controller.trigger_names.difference(self.controller.last_emitted_active_triggers)
        self.active_triggers_changed_cb(self.controller, self.controller.last_emitted_active_triggers, inactive_triggers)

    def setup_callbacks(self):
        self.closeButton.clicked.connect(self.close_controller)
        self.graphChannelComboBox.currentIndexChanged.connect(self.graph_channel_changed)
        self.fftSubchannelComboBox.currentIndexChanged.connect(self.fft_subchannel_changed)
        self.actionCopySerialNumber.triggered.connect(self.copy_serial_number)
        self.actionSetUserTag1.triggered.connect(self.set_user_tag_1)
        self.actionSetUserTag2.triggered.connect(self.set_user_tag_2)
        self.actionFirmwareLatestStable.triggered.connect(self.do_bootloader_latest_stable)
        self.actionFirmwareFromBranch.triggered.connect(self.do_bootloader_from_branch)
        self.actionFirmwareFromCommit.triggered.connect(self.do_bootloader_from_commit)
        self.actionFirmwareFromFile.triggered.connect(self.do_bootloader_from_file)
        self.actionForceRunBootloader.triggered.connect(self.controller.force_run_bootloader)
        self.actionForceRunApplication.triggered.connect(self.controller.force_run_application)
        self.actionForceReset.triggered.connect(self.controller.force_reset)
        self.actionRaiseException.triggered.connect(self.controller.do_explode)
        self.actionRecoverNVM.triggered.connect(self.recover_nvm)
        self.actionFlushLostPackets.triggered.connect(self.flush_lost_packets)
        self.actionShowPacketStats.triggered.connect(self.show_packet_stats)
        self.actionChangeActiveStreams.triggered.connect(self.change_active_streams)
        self.actionShowDeviceInfo.triggered.connect(self.show_device_info)
        self.actionCalibrate.triggered.connect(self.calibrate)
        self.actionShakerCalibrate.triggered.connect(self.shaker_calibrate)
        self.actionConnectivity.triggered.connect(self.show_connectivity_dialog)
        self.actionRFTest.triggered.connect(self.rf_test)
        self.actionEditDeviceSettings.triggered.connect(self.edit_settings)
        self.actionRunTests.triggered.connect(self.run_tests)
        self.actionSetDeviceMode.triggered.connect(self.set_device_mode)
        self.collapseButton.clicked.connect(self.toggle_collapsed)
        self.controller.state_changed_signal.connect(self.controller_state_changed)
        self.controller.progress_signal.connect(self.progress_update)
        self.controller.channel_update.connect(self.channel_update_cb)
        self.controller.plot_update.connect(self.plot_update_cb)
        self.controller.fft_update.connect(self.fft_update_cb)
        self.controller.lost_packet_update.connect(self.lost_packet_update)
        self.controller.rgb_updated.connect(self.rgb_updated_cb)
        self.controller.led_updated.connect(self.led_updated_cb)
        self.controller.ctrl_var_updated.connect(self.ctrl_var_updated_cb)
        self.controller.alerts_changed.connect(self.alerts_changed_cb)
        self.controller.manual_control_changed.connect(self._manual_control_changed_cb)
        self.controller.trigger_count_changed.connect(self.schedule_or_trigger_count_updated)
        self.controller.schedule_count_changed.connect(self.schedule_or_trigger_count_updated)
        self.controller.active_triggers_changed.connect(self.active_triggers_changed_cb)
        self.firmware_finder = hyperborea.download.FirmwareFinder(self.logger)
        self.firmware_finder.completed.connect(self.firmware_finder_completed)
        self.firmware_finder.error.connect(self.firmware_finder_error)
        self.ref_finder = hyperborea.download.RefFinder(self.logger)
        self.ref_finder.completed.connect(self.ref_finder_completed)
        self.ref_finder.error.connect(self.ref_finder_error)
        self.downloader = hyperborea.download.Downloader(self.logger)
        self.downloader.completed.connect(self.download_completed)
        self.downloader.error.connect(self.download_error)
        self.downloader.update.connect(self.download_update_progress)

    def update_preferences(self):
        show_rf_test = self.preferences.show_rf_test
        self.actionRFTestSeparator.setVisible(show_rf_test)
        self.actionRFTest.setVisible(show_rf_test)
        device_info = self.controller.device_info
        if device_info:
            self.update_supply_display(device_info)
        for channel_id, unit_options in self.channel_unit_options.items():
            unit_type = self.channel_unit_type[channel_id]
            new_default = get_default_option(self.settings, unit_type, unit_options)
            old_default = self.channel_unit_default[channel_id]
            if new_default != old_default:
                if old_default == self.channel_unit[channel_id]:
                    self.channel_unit[channel_id] = new_default
                    index = unit_options.index(new_default)
                    action = self.channel_unit_actions[channel_id][index]
                    action.setChecked(True)
                self.channel_unit_default[channel_id] = new_default
            self.update_alert_action_icons()
            self.graph_channel_changed()
            return None

    def setup_logging(self):
        self.log_list_model = get_log_list_model(self.controller.serial_number)
        self.log_list_model.dataChanged.connect(self.log_list_updated)
        self.logList.setModel(self.log_list_model)
        self.logListDisconnected.setModel(self.log_list_model)
        self.log_selection_model = QtCore.QItemSelectionModel(self.log_list_model)
        self.logList.setSelectionModel(self.log_selection_model)
        self.logListDisconnected.setSelectionModel(self.log_selection_model)
        self.logListDisconnected.setVisible(False)
        self.logList.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.logListDisconnected.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.copy_log_action = QtGui.QAction()
        self.copy_log_action.setText(self.tr('Copy'))
        self.copy_log_action.setShortcut(QtGui.QKeySequence.StandardKey.Copy)
        self.copy_log_action.setShortcutContext(QtCore.Qt.ShortcutContext.WidgetShortcut)
        self.copy_log_action.triggered.connect(self._copy_log_cb)
        self.logList.addAction(self.copy_log_action)
        self.logListDisconnected.addAction(self.copy_log_action)
        sb1 = self.logList.verticalScrollBar()
        sb2 = self.logListDisconnected.verticalScrollBar()
        sb1.valueChanged.connect(sb2.setValue)
        sb2.valueChanged.connect(sb1.setValue)

    def log_list_updated(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR logList
        #   14 LOAD_METHOD verticalScrollBar
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST sb1
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR logListDisconnected
        #   64 LOAD_METHOD verticalScrollBar
        #   86 PRECALL
        #   90 CALL
        #  100 STORE_FAST sb2
        #  102 LOAD_FAST sb1
        #  104 LOAD_METHOD value
        #  126 PRECALL
        #  130 CALL
        #  140 LOAD_FAST sb1
        #  142 LOAD_METHOD maximum
        #  164 PRECALL
        #  168 CALL
        #  178 COMPARE_OP ==
        #  184 JUMP_IF_TRUE_OR_POP to 268
        #  186 LOAD_FAST sb2
        #  188 LOAD_METHOD value
        #  210 PRECALL
        #  214 CALL
        #  224 LOAD_FAST sb2
        #  226 LOAD_METHOD maximum
        #  248 PRECALL
        #  252 CALL
        #  262 COMPARE_OP ==
        #  268 STORE_FAST at_bottom
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR logListDisconnected
        #  282 LOAD_METHOD setVisible
        #  304 LOAD_CONST True
        #  306 PRECALL
        #  310 CALL
        #  320 POP_TOP
        #  322 LOAD_FAST at_bottom
        #  324 POP_JUMP_FORWARD_IF_FALSE to 430
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR logListDisconnected
        #  338 LOAD_METHOD scrollToBottom
        #  360 PRECALL
        #  364 CALL
        #  374 POP_TOP
        #  376 LOAD_FAST self
        #  378 LOAD_ATTR logList
        #  388 LOAD_METHOD scrollToBottom
        #  410 PRECALL
        #  414 CALL
        #  424 POP_TOP
        #  426 LOAD_CONST None
        #  428 RETURN_VALUE
        #  430 LOAD_CONST None
        #  432 RETURN_VALUE
        pass

    def _copy_log_cb(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL QtWidgets
        #   14 LOAD_ATTR QApplication
        #   24 LOAD_METHOD clipboard
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST clipboard
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR logList
        #   74 LOAD_METHOD selectedIndexes
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST indexes
        #  112 LOAD_CONST '\n'
        #  114 LOAD_METHOD join
        #  136 LOAD_CONST <code object <listcomp> at 0x105abfa50, file "acheron\gui\device_tab.py", line 515>
        #  138 MAKE_FUNCTION
        #  140 LOAD_FAST indexes
        #  142 GET_ITER
        #  144 PRECALL
        #  148 CALL
        #  158 PRECALL
        #  162 CALL
        #  172 STORE_FAST text
        #  174 LOAD_FAST text
        #  176 POP_JUMP_FORWARD_IF_FALSE to 224
        #  178 LOAD_FAST clipboard
        #  180 LOAD_METHOD setText
        #  202 LOAD_FAST text
        #  204 PRECALL
        #  208 CALL
        #  218 POP_TOP
        #  220 LOAD_CONST None
        #  222 RETURN_VALUE
        #  224 LOAD_CONST None
        #  226 RETURN_VALUE
        pass

    def setup_graphics(self):
        fft_pen = 'c'
        self.timePlot = self.timePlotWidget.getPlotItem()
        self.fftPlot = self.fftPlotWidget.getPlotItem()

    def update_supply_display(self, device_info):
        supply_strings = []
        battery_strings = []
        supplies = device_info.supplies

    def toggle_collapsed(self):
        new_collapsed = not (self.collapsed)
        self.collapsed_set.emit(new_collapsed)

    def set_collapsed(self, collapsed):
        self.collapsed = collapsed
        if collapsed:
            self.collapseButton.setText(self.tr('▲ Expand ▲'))
        else:
            self.collapseButton.setText(self.tr('▼ Collapse ▼'))
        self.bottomGroup.setVisible(not collapsed)

    def copy_serial_number(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.controller.serial_number)

    def set_user_tag_1(self):
        self.set_user_tag(0)

    def set_user_tag_2(self):
        self.set_user_tag(1)

    def set_user_tag(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_TRUE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_CONST 'user_tag_'
        #   32 LOAD_GLOBAL NULL + str
        #   44 LOAD_FAST index
        #   46 LOAD_CONST 1
        #   48 BINARY_OP +
        #   52 PRECALL
        #   56 CALL
        #   66 BINARY_OP +
        #   70 STORE_FAST tag_key
        #   72 LOAD_GLOBAL NULL + getattr
        #   84 LOAD_FAST self
        #   86 LOAD_ATTR controller
        #   96 LOAD_ATTR device_info
        #  106 LOAD_FAST tag_key
        #  108 PRECALL
        #  112 CALL
        #  122 STORE_FAST old_str
        #  124 LOAD_GLOBAL QtWidgets
        #  136 LOAD_ATTR QInputDialog
        #  146 LOAD_METHOD getText
        #  168 LOAD_FAST self
        #  170 LOAD_FAST self
        #  172 LOAD_METHOD tr
        #  194 LOAD_CONST 'New Tag'
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_FAST self
        #  212 LOAD_METHOD tr
        #  234 LOAD_CONST 'New Tag:'
        #  236 PRECALL
        #  240 CALL
        #  250 LOAD_GLOBAL QtWidgets
        #  262 LOAD_ATTR QLineEdit
        #  272 LOAD_ATTR EchoMode
        #  282 LOAD_ATTR Normal
        #  292 LOAD_FAST old_str
        #  294 PRECALL
        #  298 CALL
        #  308 UNPACK_SEQUENCE
        #  312 STORE_FAST new_str
        #  314 STORE_FAST ok
        #  316 LOAD_FAST ok
        #  318 POP_JUMP_FORWARD_IF_TRUE to 324
        #  320 LOAD_CONST None
        #  322 RETURN_VALUE
        #  324 LOAD_FAST new_str
        #  326 LOAD_METHOD strip
        #  348 PRECALL
        #  352 CALL
        #  362 STORE_FAST new_str
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR controller
        #  376 LOAD_METHOD set_user_tag
        #  398 LOAD_FAST index
        #  400 LOAD_FAST new_str
        #  402 PRECALL
        #  406 CALL
        #  416 POP_TOP
        #  418 LOAD_CONST None
        #  420 RETURN_VALUE
        pass

    def recover_nvm(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_TRUE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_GLOBAL NULL + len
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR controller
        #   54 LOAD_ATTR device_info
        #   64 LOAD_ATTR nvm
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST current_length
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR preferences
        #  102 LOAD_ATTR base_dir
        #  112 STORE_FAST apd_dir
        #  114 LOAD_FAST self
        #  116 LOAD_METHOD tr
        #  138 LOAD_CONST 'Open Data File'
        #  140 PRECALL
        #  144 CALL
        #  154 STORE_FAST caption
        #  156 LOAD_FAST self
        #  158 LOAD_METHOD tr
        #  180 LOAD_CONST 'Data Files (*.apd);;All Files (*.*)'
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST file_filter
        #  198 LOAD_GLOBAL QtWidgets
        #  210 LOAD_ATTR QFileDialog
        #  220 LOAD_METHOD getOpenFileName
        #  242 LOAD_FAST self
        #  244 LOAD_FAST caption
        #  246 LOAD_FAST apd_dir
        #  248 LOAD_FAST file_filter
        #  250 PRECALL
        #  254 CALL
        #  264 STORE_FAST val
        #  266 LOAD_FAST val
        #  268 LOAD_CONST 0
        #  270 BINARY_SUBSCR
        #  280 STORE_FAST filename
        #  282 LOAD_FAST filename
        #  284 LOAD_CONST ''
        #  286 COMPARE_OP ==
        #  292 POP_JUMP_FORWARD_IF_FALSE to 298
        #  294 LOAD_CONST None
        #  296 RETURN_VALUE
        #  298 LOAD_GLOBAL NULL + lzma
        #  310 LOAD_ATTR open
        #  320 LOAD_FAST filename
        #  322 LOAD_CONST 'rb'
        #  324 PRECALL
        #  328 CALL
        #  338 STORE_FAST fp
        #  340 LOAD_FAST fp
        #  342 LOAD_METHOD read
        #  364 LOAD_CONST 12
        #  366 PRECALL
        #  370 CALL
        #  380 STORE_FAST leader_bytes
        #  382 LOAD_GLOBAL NULL + struct
        #  394 LOAD_ATTR unpack
        #  404 LOAD_CONST '>dI'
        #  406 LOAD_FAST leader_bytes
        #  408 PRECALL
        #  412 CALL
        #  422 STORE_FAST header_leader
        #  424 LOAD_FAST fp
        #  426 LOAD_METHOD read
        #  448 LOAD_FAST header_leader
        #  450 LOAD_CONST 1
        #  452 BINARY_SUBSCR
        #  462 PRECALL
        #  466 CALL
        #  476 STORE_FAST header_bytes
        #  478 LOAD_FAST header_bytes
        # ... bytecode truncated ...
        pass

    def flush_lost_packets(self):
        self.controller.reset_lost_packets()
        self.recentLostPackets.setText(str(0))
        if self.recent_lost_packet_highlight:
            self.recent_lost_packet_highlight = False
            self.recentLostPackets.setStyleSheet('')
            return None

    def show_packet_stats(self):
        count_since_last = self.lost_packet_count - self.last_displayed_packet_count
        self.last_displayed_packet_count = self.lost_packet_count
        now = datetime.datetime.now(tz = datetime.timezone.utc)

    def lost_packet_update(self, total, last_datetime, recent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST total
        #    4 LOAD_FAST self
        #    6 STORE_ATTR lost_packet_count
        #   16 LOAD_FAST last_datetime
        #   18 LOAD_FAST self
        #   20 STORE_ATTR lost_packet_last_time
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR recentLostPackets
        #   42 LOAD_METHOD setText
        #   64 LOAD_GLOBAL NULL + str
        #   76 LOAD_FAST recent
        #   78 PRECALL
        #   82 CALL
        #   92 PRECALL
        #   96 CALL
        #  106 POP_TOP
        #  108 LOAD_FAST recent
        #  110 LOAD_CONST 0
        #  112 COMPARE_OP >
        #  118 POP_JUMP_FORWARD_IF_FALSE to 208
        #  120 LOAD_FAST self
        #  122 LOAD_ATTR recent_lost_packet_highlight
        #  132 POP_JUMP_FORWARD_IF_TRUE to 204
        #  134 LOAD_CONST True
        #  136 LOAD_FAST self
        #  138 STORE_ATTR recent_lost_packet_highlight
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR recentLostPackets
        #  160 LOAD_METHOD setStyleSheet
        #  182 LOAD_CONST '* { color: black; background-color: red }'
        #  184 PRECALL
        #  188 CALL
        #  198 POP_TOP
        #  200 LOAD_CONST None
        #  202 RETURN_VALUE
        #  204 LOAD_CONST None
        #  206 RETURN_VALUE
        #  208 LOAD_FAST self
        #  210 LOAD_ATTR recent_lost_packet_highlight
        #  220 POP_JUMP_FORWARD_IF_FALSE to 292
        #  222 LOAD_CONST False
        #  224 LOAD_FAST self
        #  226 STORE_ATTR recent_lost_packet_highlight
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR recentLostPackets
        #  248 LOAD_METHOD setStyleSheet
        #  270 LOAD_CONST ''
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_CONST None
        #  290 RETURN_VALUE
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        pass

    def change_active_streams(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_TRUE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_GLOBAL NULL + ChangeStreamDialog
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR controller
        #   54 LOAD_ATTR device_info
        #   64 LOAD_ATTR streams
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR controller
        #   86 LOAD_ATTR device_info
        #   96 LOAD_ATTR channels
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR controller
        #  118 LOAD_ATTR active_streams
        #  128 LOAD_FAST self
        #  130 PRECALL
        #  134 CALL
        #  144 STORE_FAST dialog
        #  146 NOP
        #  148 LOAD_FAST dialog
        #  150 LOAD_METHOD exec
        #  172 PRECALL
        #  176 CALL
        #  186 STORE_FAST ret
        #  188 LOAD_FAST ret
        #  190 LOAD_CONST 0
        #  192 COMPARE_OP ==
        #  198 POP_JUMP_FORWARD_IF_FALSE to 246
        #  200 NOP
        #  202 LOAD_FAST dialog
        #  204 LOAD_METHOD deleteLater
        #  226 PRECALL
        #  230 CALL
        #  240 POP_TOP
        #  242 LOAD_CONST None
        #  244 RETURN_VALUE
        #  246 LOAD_FAST dialog
        #  248 LOAD_METHOD get_new_stream_list
        #  270 PRECALL
        #  274 CALL
        #  284 STORE_FAST stream_list
        #  286 LOAD_FAST dialog
        #  288 LOAD_METHOD deleteLater
        #  310 PRECALL
        #  314 CALL
        #  324 POP_TOP
        #  326 JUMP_FORWARD to 378
        #  328 PUSH_EXC_INFO
        #  330 LOAD_FAST dialog
        #  332 LOAD_METHOD deleteLater
        #  354 PRECALL
        #  358 CALL
        #  368 POP_TOP
        #  370 RERAISE
        #  372 COPY
        #  374 POP_EXCEPT
        #  376 RERAISE
        #  378 LOAD_FAST self
        #  380 LOAD_ATTR controller
        #  390 LOAD_METHOD set_active_streams
        #  412 LOAD_FAST stream_list
        #  414 PRECALL
        #  418 CALL
        #  428 POP_TOP
        #  430 LOAD_CONST None
        #  432 RETURN_VALUE
        pass

    def show_connectivity_dialog(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_TRUE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_GLOBAL NULL + ConnectivityDialog
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR controller
        #   54 LOAD_ATTR serial_number
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR controller
        #   76 LOAD_ATTR device_info
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR controller
        #   98 LOAD_ATTR channel_info
        #  108 LOAD_FAST self
        #  110 LOAD_ATTR controller
        #  120 LOAD_ATTR device_prefs
        #  130 LOAD_FAST self
        #  132 PRECALL
        #  136 CALL
        #  146 STORE_FAST dialog
        #  148 NOP
        #  150 LOAD_FAST dialog
        #  152 LOAD_METHOD exec
        #  174 PRECALL
        #  178 CALL
        #  188 STORE_FAST ret
        #  190 LOAD_FAST ret
        #  192 LOAD_CONST 0
        #  194 COMPARE_OP ==
        #  200 POP_JUMP_FORWARD_IF_FALSE to 248
        #  202 NOP
        #  204 LOAD_FAST dialog
        #  206 LOAD_METHOD deleteLater
        #  228 PRECALL
        #  232 CALL
        #  242 POP_TOP
        #  244 LOAD_CONST None
        #  246 RETURN_VALUE
        #  248 NOP
        #  250 LOAD_FAST dialog
        #  252 LOAD_METHOD deleteLater
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 JUMP_FORWARD to 342
        #  292 PUSH_EXC_INFO
        #  294 LOAD_FAST dialog
        #  296 LOAD_METHOD deleteLater
        #  318 PRECALL
        #  322 CALL
        #  332 POP_TOP
        #  334 RERAISE
        #  336 COPY
        #  338 POP_EXCEPT
        #  340 RERAISE
        #  342 LOAD_FAST self
        #  344 LOAD_METHOD update_preferences
        #  366 PRECALL
        #  370 CALL
        #  380 POP_TOP
        #  382 LOAD_FAST self
        #  384 LOAD_ATTR controller
        #  394 LOAD_METHOD update_preferences
        #  416 PRECALL
        #  420 CALL
        #  430 POP_TOP
        #  432 LOAD_FAST self
        #  434 LOAD_ATTR controller
        #  444 LOAD_METHOD start_connectivity
        #  466 PRECALL
        #  470 CALL
        #  480 POP_TOP
        #  482 LOAD_CONST None
        #  484 RETURN_VALUE
        pass

    def show_device_info(self):
        if self.controller.device_info:
            dialog = DeviceInfoDialog(self.controller.device_info, self)
            
            try:
                dialog.exec()
                dialog.deleteLater()
                return None
            except:
                dialog.deleteLater()
                return None

    def run_tests(self):
        if self.controller.device_info:
            dialog = HardwareTestDialog(self.controller.device_info, self.controller, self.preferences, self.logger, self)
            
            try:
                dialog.start_tests()
                dialog.exec()
                dialog.deleteLater()
                return None
            except:
                dialog.deleteLater()
                return None

    def set_device_mode(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_FALSE to 70
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR controller
        #   38 LOAD_ATTR device_info
        #   48 LOAD_ATTR device_mode
        #   58 STORE_FAST old_mode
        #   60 LOAD_FAST old_mode
        #   62 POP_JUMP_FORWARD_IF_NOT_NONE to 68
        #   64 LOAD_CONST 0
        #   66 STORE_FAST old_mode
        #   68 JUMP_FORWARD to 74
        #   70 LOAD_CONST 0
        #   72 STORE_FAST old_mode
        #   74 LOAD_GLOBAL QtWidgets
        #   86 LOAD_ATTR QInputDialog
        #   96 LOAD_METHOD getInt
        #  118 LOAD_FAST self
        #  120 LOAD_FAST self
        #  122 LOAD_METHOD tr
        #  144 LOAD_CONST 'Device Mode'
        #  146 PRECALL
        #  150 CALL
        #  160 LOAD_FAST self
        #  162 LOAD_METHOD tr
        #  184 LOAD_CONST 'Input new device mode'
        #  186 PRECALL
        #  190 CALL
        #  200 LOAD_FAST old_mode
        #  202 LOAD_CONST 0
        #  204 LOAD_CONST 255
        #  206 PRECALL
        #  210 CALL
        #  220 UNPACK_SEQUENCE
        #  224 STORE_FAST new_mode
        #  226 STORE_FAST ok
        #  228 LOAD_FAST ok
        #  230 POP_JUMP_FORWARD_IF_TRUE to 236
        #  232 LOAD_CONST None
        #  234 RETURN_VALUE
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR controller
        #  248 LOAD_METHOD set_device_mode
        #  270 LOAD_FAST new_mode
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_CONST None
        #  290 RETURN_VALUE
        pass

    def calibrate(self):
        if not self.controller.device_info:
            return None

    def rf_test(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + RFTestDialog
        #   14 LOAD_FAST self
        #   16 PRECALL
        #   20 CALL
        #   30 STORE_FAST dialog
        #   32 NOP
        #   34 LOAD_FAST dialog
        #   36 LOAD_METHOD exec
        #   58 PRECALL
        #   62 CALL
        #   72 STORE_FAST ret
        #   74 LOAD_FAST ret
        #   76 LOAD_CONST 0
        #   78 COMPARE_OP ==
        #   84 POP_JUMP_FORWARD_IF_FALSE to 132
        #   86 NOP
        #   88 LOAD_FAST dialog
        #   90 LOAD_METHOD deleteLater
        #  112 PRECALL
        #  116 CALL
        #  126 POP_TOP
        #  128 LOAD_CONST None
        #  130 RETURN_VALUE
        #  132 LOAD_FAST dialog
        #  134 LOAD_METHOD get_test_params
        #  156 PRECALL
        #  160 CALL
        #  170 STORE_FAST test_params
        #  172 LOAD_FAST dialog
        #  174 LOAD_METHOD deleteLater
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 JUMP_FORWARD to 264
        #  214 PUSH_EXC_INFO
        #  216 LOAD_FAST dialog
        #  218 LOAD_METHOD deleteLater
        #  240 PRECALL
        #  244 CALL
        #  254 POP_TOP
        #  256 RERAISE
        #  258 COPY
        #  260 POP_EXCEPT
        #  262 RERAISE
        #  264 LOAD_GLOBAL NULL + multiprocessing
        #  276 LOAD_ATTR Pipe
        #  286 LOAD_CONST False
        #  288 PRECALL
        #  292 CALL
        #  302 UNPACK_SEQUENCE
        #  306 STORE_FAST finished_rx_pipe
        #  308 STORE_FAST finished_tx_pipe
        #  310 LOAD_GLOBAL NULL + RFTestParams
        #  322 LOAD_FAST test_params
        #  324 LOAD_GLOBAL NULL + cast
        #  336 LOAD_GLOBAL multiprocessing
        #  348 LOAD_ATTR connection
        #  358 LOAD_ATTR Connection
        #  368 LOAD_FAST finished_rx_pipe
        #  370 PRECALL
        #  374 CALL
        #  384 PRECALL
        #  388 CALL
        #  398 STORE_FAST params
        #  400 LOAD_FAST self
        #  402 LOAD_ATTR controller
        #  412 LOAD_METHOD start_rf_test
        #  434 LOAD_FAST params
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_GLOBAL NULL + QtWidgets
        #  464 LOAD_ATTR QMessageBox
        #  474 LOAD_FAST self
        #  476 PRECALL
        #  480 CALL
        #  490 STORE_FAST msg_box
        #  492 LOAD_FAST msg_box
        #  494 LOAD_METHOD setWindowTitle
        # ... bytecode truncated ...
        pass

    def edit_settings(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_TRUE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_GLOBAL NULL + SettingDialog
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR controller
        #   54 LOAD_ATTR device_info
        #   64 LOAD_FAST self
        #   66 PRECALL
        #   70 CALL
        #   80 STORE_FAST dialog
        #   82 NOP
        #   84 LOAD_FAST dialog
        #   86 LOAD_METHOD exec
        #  108 PRECALL
        #  112 CALL
        #  122 STORE_FAST ret
        #  124 LOAD_FAST ret
        #  126 LOAD_CONST 0
        #  128 COMPARE_OP ==
        #  134 POP_JUMP_FORWARD_IF_FALSE to 182
        #  136 NOP
        #  138 LOAD_FAST dialog
        #  140 LOAD_METHOD deleteLater
        #  162 PRECALL
        #  166 CALL
        #  176 POP_TOP
        #  178 LOAD_CONST None
        #  180 RETURN_VALUE
        #  182 NOP
        #  184 LOAD_FAST dialog
        #  186 LOAD_METHOD get_updated_nvm
        #  208 PRECALL
        #  212 CALL
        #  222 STORE_FAST new_nvm
        #  224 JUMP_FORWARD to 494
        #  226 PUSH_EXC_INFO
        #  228 LOAD_GLOBAL Exception
        #  240 CHECK_EXC_MATCH
        #  242 POP_JUMP_FORWARD_IF_FALSE to 486
        #  244 POP_TOP
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR logger
        #  258 LOAD_METHOD exception
        #  280 LOAD_CONST 'Unhandled Exception in edit_settings'
        #  282 PRECALL
        #  286 CALL
        #  296 POP_TOP
        #  298 LOAD_GLOBAL QtWidgets
        #  310 LOAD_ATTR QMessageBox
        #  320 LOAD_METHOD critical
        #  342 LOAD_FAST self
        #  344 LOAD_FAST self
        #  346 LOAD_METHOD tr
        #  368 LOAD_CONST 'Error'
        #  370 PRECALL
        #  374 CALL
        #  384 LOAD_FAST self
        #  386 LOAD_METHOD tr
        #  408 LOAD_CONST 'Error parsing settings!'
        #  410 PRECALL
        #  414 CALL
        #  424 PRECALL
        #  428 CALL
        #  438 POP_TOP
        #  440 POP_EXCEPT
        #  442 LOAD_FAST dialog
        #  444 LOAD_METHOD deleteLater
        #  466 PRECALL
        #  470 CALL
        #  480 POP_TOP
        #  482 LOAD_CONST None
        #  484 RETURN_VALUE
        #  486 RERAISE
        #  488 COPY
        #  490 POP_EXCEPT
        # ... bytecode truncated ...
        pass

    def capture_func(self, channel_id):
        try:
            (mean, std_dev) = self.channel_data[channel_id]
            return (mean, std_dev)
        except KeyError:
            nanarray = numpy.array([
                [
                    numpy.nan]])
            return 

    def shaker_calibrate(self):
        device_info = self.controller.device_info
        if not device_info:
            self.logger.error('No device information for shaker calibration')
            return None

    def create_calibration_info(self, device_info, manual_control):
        if self.calibration_panel:
            self.panelLayout.removeWidget(self.calibration_panel)
            self.calibration_panel.deleteLater()
            self.calibration_panel = None
        self.calibration_cals.clear()
        channel_calibration = device_info.channel_calibration

    def channel_update_cb(self, channel_id, mean, std_dev):
        self.channel_data[channel_id] = (mean, std_dev)
        unit_formatter = self.channel_unit[channel_id].unit_formatter
        mean_scaled = mean * unit_formatter.conversion_scale + unit_formatter.conversion_offset
        std_dev_scaled = std_dev * unit_formatter.conversion_scale
        for i, fields in enumerate(self.subchannel_fields[channel_id]):
            (mean_field, std_dev_field) = fields
            mean_string = unit_formatter.format_utf8(mean_scaled[i])
            mean_field.setText(mean_string)
            std_dev_string = unit_formatter.format_utf8(std_dev_scaled[i])
            std_dev_field.setText(std_dev_string)
            return None

    def plot_update_cb(self, channel_id, time, data):
        selected_channel_id = self.get_current_channel_id()
        if channel_id != selected_channel_id:
            return None

        try:
            channel_info = self.controller.channel_info[channel_id]
        except KeyError:
            return None

        if self.last_channel_id != channel_id:
            self.last_channel_id = channel_id
            if channel_info.downsample_factor == 1:
                self.timePlot.setTitle('Time Domain')
            else:
                s = 'Time Domain (Downsampled {}x)'.format(channel_info.downsample_factor)
                self.timePlot.setTitle(s)
        unit_formatter = self.channel_unit[channel_id].unit_formatter
        data = data * unit_formatter.conversion_scale + unit_formatter.conversion_offset
        for array, curve in zip(data.transpose(), self.time_curves):
            curve.setData(time, array.flatten())
            return None

    def fft_update_cb(self, channel_id, subchannel_id, fft_freqs, fft_data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD get_current_channel_id
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST selected_channel_id
        #   42 LOAD_FAST channel_id
        #   44 LOAD_FAST selected_channel_id
        #   46 COMPARE_OP !=
        #   52 POP_JUMP_FORWARD_IF_FALSE to 58
        #   54 LOAD_CONST None
        #   56 RETURN_VALUE
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR fftSubchannelComboBox
        #   70 LOAD_METHOD currentIndex
        #   92 PRECALL
        #   96 CALL
        #  106 STORE_FAST selected_subchannel_index
        #  108 LOAD_FAST subchannel_id
        #  110 LOAD_FAST selected_subchannel_index
        #  112 COMPARE_OP !=
        #  118 POP_JUMP_FORWARD_IF_FALSE to 124
        #  120 LOAD_CONST None
        #  122 RETURN_VALUE
        #  124 NOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR channel_unit
        #  138 LOAD_FAST channel_id
        #  140 BINARY_SUBSCR
        #  150 LOAD_ATTR unit_formatter
        #  160 STORE_FAST unit_formatter
        #  162 JUMP_FORWARD to 198
        #  164 PUSH_EXC_INFO
        #  166 LOAD_GLOBAL KeyError
        #  178 CHECK_EXC_MATCH
        #  180 POP_JUMP_FORWARD_IF_FALSE to 190
        #  182 POP_TOP
        #  184 POP_EXCEPT
        #  186 LOAD_CONST None
        #  188 RETURN_VALUE
        #  190 RERAISE
        #  192 COPY
        #  194 POP_EXCEPT
        #  196 RERAISE
        #  198 LOAD_GLOBAL NULL + numpy
        #  210 LOAD_ATTR ndim
        #  220 LOAD_FAST fft_data
        #  222 PRECALL
        #  226 CALL
        #  236 LOAD_CONST 0
        #  238 COMPARE_OP ==
        #  244 POP_JUMP_FORWARD_IF_FALSE to 470
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR buffering
        #  258 POP_JUMP_FORWARD_IF_TRUE to 326
        #  260 LOAD_FAST self
        #  262 LOAD_ATTR bufferingLabel
        #  272 LOAD_METHOD setVisible
        #  294 LOAD_CONST True
        #  296 PRECALL
        #  300 CALL
        #  310 POP_TOP
        #  312 LOAD_CONST True
        #  314 LOAD_FAST self
        #  316 STORE_ATTR buffering
        #  326 NOP
        #  328 LOAD_GLOBAL NULL + int
        #  340 LOAD_CONST 100
        #  342 LOAD_FAST fft_data
        #  344 BINARY_OP *
        #  348 PRECALL
        #  352 CALL
        #  362 STORE_FAST percent
        #  364 LOAD_CONST 'Buffering '
        #  366 LOAD_FAST percent
        #  368 FORMAT_VALUE
        #  370 LOAD_CONST '%'
        #  372 BUILD_STRING
        #  374 STORE_FAST text
        #  376 JUMP_FORWARD to 414
        # ... bytecode truncated ...
        pass

    def get_plot_pens(self, subchannel_count):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST subchannel_count
        #    4 LOAD_CONST 1
        #    6 COMPARE_OP ==
        #   12 POP_JUMP_FORWARD_IF_FALSE to 20
        #   14 LOAD_CONST 'c'
        #   16 BUILD_LIST
        #   18 RETURN_VALUE
        #   20 BUILD_LIST
        #   22 LOAD_CONST ('b', 'g', 'r')
        #   24 LIST_EXTEND
        #   26 STORE_FAST pens
        #   28 LOAD_FAST subchannel_count
        #   30 LOAD_CONST 3
        #   32 COMPARE_OP <=
        #   38 POP_JUMP_FORWARD_IF_FALSE to 60
        #   40 LOAD_FAST pens
        #   42 LOAD_CONST None
        #   44 LOAD_FAST subchannel_count
        #   46 BUILD_SLICE
        #   48 BINARY_SUBSCR
        #   58 RETURN_VALUE
        #   60 LOAD_FAST pens
        #   62 LOAD_CONST 'c'
        #   64 BUILD_LIST
        #   66 LOAD_FAST subchannel_count
        #   68 LOAD_GLOBAL NULL + len
        #   80 LOAD_FAST pens
        #   82 PRECALL
        #   86 CALL
        #   96 BINARY_OP -
        #  100 BINARY_OP *
        #  104 BINARY_OP +
        #  108 RETURN_VALUE
        pass

    def save_plot_range(self, channel_id):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR saved_plot_ranges
        #   14 LOAD_METHOD setdefault
        #   36 LOAD_FAST channel_id
        #   38 BUILD_MAP
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST save_dict
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR timePlot
        #   68 LOAD_METHOD getViewBox
        #   90 PRECALL
        #   94 CALL
        #  104 STORE_FAST time_vb
        #  106 LOAD_GLOBAL NULL + isinstance
        #  118 LOAD_FAST time_vb
        #  120 LOAD_GLOBAL pyqtgraph
        #  132 LOAD_ATTR ViewBox
        #  142 PRECALL
        #  146 CALL
        #  156 POP_JUMP_FORWARD_IF_TRUE to 162
        #  158 LOAD_CONST None
        #  160 RETURN_VALUE
        #  162 LOAD_FAST time_vb
        #  164 LOAD_METHOD autoRangeEnabled
        #  186 PRECALL
        #  190 CALL
        #  200 STORE_FAST time_autorange
        #  202 LOAD_FAST time_vb
        #  204 LOAD_METHOD targetRange
        #  226 PRECALL
        #  230 CALL
        #  240 STORE_FAST time_range
        #  242 LOAD_FAST time_autorange
        #  244 LOAD_FAST time_range
        #  246 BUILD_TUPLE
        #  248 LOAD_FAST save_dict
        #  250 LOAD_CONST 'time'
        #  252 STORE_SUBSCR
        #  256 LOAD_FAST self
        #  258 LOAD_ATTR fft_curve
        #  268 LOAD_METHOD getData
        #  290 PRECALL
        #  294 CALL
        #  304 LOAD_CONST 0
        #  306 BINARY_SUBSCR
        #  316 POP_JUMP_FORWARD_IF_NONE to 522
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR fftPlot
        #  330 LOAD_METHOD getViewBox
        #  352 PRECALL
        #  356 CALL
        #  366 STORE_FAST fft_vb
        #  368 LOAD_GLOBAL NULL + isinstance
        #  380 LOAD_FAST fft_vb
        #  382 LOAD_GLOBAL pyqtgraph
        #  394 LOAD_ATTR ViewBox
        #  404 PRECALL
        #  408 CALL
        #  418 POP_JUMP_FORWARD_IF_TRUE to 424
        #  420 LOAD_CONST None
        #  422 RETURN_VALUE
        #  424 LOAD_FAST fft_vb
        #  426 LOAD_METHOD autoRangeEnabled
        #  448 PRECALL
        #  452 CALL
        #  462 STORE_FAST fft_autorange
        #  464 LOAD_FAST fft_vb
        #  466 LOAD_METHOD targetRange
        #  488 PRECALL
        #  492 CALL
        #  502 STORE_FAST fft_range
        #  504 LOAD_FAST fft_autorange
        #  506 LOAD_FAST fft_range
        #  508 BUILD_TUPLE
        #  510 LOAD_FAST save_dict
        #  512 LOAD_CONST 'fft'
        #  514 STORE_SUBSCR
        #  518 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def restore_plot_range(self, channel_id):
        save_dict = self.saved_plot_ranges.get(channel_id, { })

        def restore(vb = None, autorange = None, targetrange = None):
            (x_autorange, y_autorange) = autorange
            vb.enableAutoRange(x = x_autorange, y = y_autorange)

    def graph_channel_changed(self):
        self.fftSubchannelComboBox.clear()
        self.timePlot.clear()
        self.time_curves.clear()
        self.fft_curve.clear()
        channel_id = self.get_current_channel_id()

    def _unit_selected(self, channel_id, unit_option):
        self.channel_unit[channel_id] = unit_option
        self.graph_channel_changed()

    def fft_subchannel_changed(self):
        self.fft_curve.clear()
        channel_id = self.get_current_channel_id()
        subchannel_index = self.fftSubchannelComboBox.currentIndex()
        self.controller.plot_change(channel_id, subchannel_index)

    def set_is_shown(self, is_shown):
        self.controller.set_is_shown(is_shown)

    def create_rgb_widget(self, index, initial_values, manual_control):
        set_values = functools.partial(self.controller.set_rgb, index)
        widget = RGBControlWidget(set_values, initial_values)
        widget.setEnabled(manual_control)
        self.LEDLayout.addWidget(widget)
        self.rgb_widgets.append(widget)

    def create_led_widget(self, index, initial_value, manual_control):
        set_value = functools.partial(self.controller.set_led, index)
        widget = LEDControlWidget(set_value, initial_value)
        widget.setEnabled(manual_control)
        self.LEDLayout.addWidget(widget)
        self.led_widgets.append(widget)

    def setup_rgb_and_led_widgets(self, device_info, manual_control):
        item = self.LEDLayout.takeAt(0)
        if not item:
            pass

        for rgb_widget in self.rgb_widgets:
            rgb_widget.deleteLater()
            self.rgb_widgets.clear()
            for led_widget in self.led_widgets:
                led_widget.deleteLater()
                self.led_widgets.clear()
                for i, values in enumerate(device_info.rgb_settings):
                    self.create_rgb_widget(i, values, manual_control)
                    for i, value in enumerate(device_info.led_settings):
                        self.create_led_widget(i, value, manual_control)
                        return None

    def setup_ctrl_vars(self, device_info, manual_control):
        self.rf_power_panel.clear_ctrl_var_widgets()
        self.radio_panel.clear_ctrl_var_widgets()
        self.ctrl_var_panel.clear_ctrl_var_widgets()

    def setup_channel(self, channel_id, channel_info):
        channel = channel_info.channel
        unit_options = get_unit_options(channel.unit_type, channel.minimum, channel.maximum, channel.resolution)
        default = get_default_option(self.settings, channel.unit_type, unit_options)
        action_group = QtGui.QActionGroup(self)
        unit_actions = []
        for unit_option in unit_options:
            action = QtGui.QAction(action_group)
            if unit_option.metric_relation:
                action.setText('{} ({})'.format(unit_option.base_str, unit_option.metric_relation))
            else:
                action.setText(unit_option.base_str)
            action.setCheckable(True)
            if unit_option == default:
                action.setChecked(True)
            action_cb = functools.partial(self._unit_selected, channel_id, unit_option)
            action.triggered.connect(action_cb)
            unit_actions.append(action)
            self.channel_unit_options[channel_id] = unit_options
            self.channel_unit_actions[channel_id] = unit_actions
            self.channel_unit_action_group[channel_id] = action_group
            self.channel_unit_type[channel_id] = channel.unit_type
            self.channel_unit_default[channel_id] = default
            self.channel_unit[channel_id] = default
            field_list = []
            alert_actions = []
            for i, subchannel_name in enumerate(channel_info.subchannel_names):
                label = QtWidgets.QLabel(subchannel_name)
                mean_field = MeasurementLineEdit(unit_actions)
                std_dev_field = MeasurementLineEdit(unit_actions)
                sampling_rate_field = MeasurementLineEdit(None)
                sampling_rate = '{:g} sps'.format(channel_info.rate)
                sampling_rate_field.setText(sampling_rate)
                edit_alert_button = QtWidgets.QToolButton()
                edit_alert_action = EditAlertAction(channel_id, i, subchannel_name, self, edit_alert_button)
                edit_alert_button.setDefaultAction(edit_alert_action)
                alert_actions.append(edit_alert_action)
                row = self.channelLayout.rowCount()
                self.channelLayout.addWidget(label, row, 0)
                self.channelLayout.addWidget(mean_field, row, 1)
                self.channelLayout.addWidget(std_dev_field, row, 2)
                self.channelLayout.addWidget(sampling_rate_field, row, 3)
                self.channelLayout.addWidget(edit_alert_button, row, 4)
                field_list.append((mean_field, std_dev_field))
                self.subchannel_fields[channel_id] = field_list
                self.channel_alert_actions[channel_id] = alert_actions
                return None

    def disable_interaction(self):
        self.actionCalibrate.setEnabled(False)
        self.actionChangeActiveStreams.setEnabled(False)
        self.actionEditDeviceSettings.setEnabled(False)
        self.actionFirmwareFromBranch.setEnabled(False)
        self.actionFirmwareFromCommit.setEnabled(False)
        self.actionFirmwareFromFile.setEnabled(False)
        self.actionFirmwareLatestStable.setEnabled(False)
        self.actionForceReset.setEnabled(False)
        self.actionForceRunApplication.setEnabled(False)
        self.actionForceRunBootloader.setEnabled(False)
        self.actionRaiseException.setEnabled(False)
        self.actionRecoverNVM.setEnabled(False)
        self.actionRFTest.setEnabled(False)
        self.actionRunTests.setEnabled(False)
        self.actionSetDeviceMode.setEnabled(False)
        self.actionSetUserTag1.setEnabled(False)
        self.actionSetUserTag2.setEnabled(False)
        self.actionShakerCalibrate.setEnabled(False)
        if self.calibration_panel:
            self.calibration_panel.setEnabled(False)
        self.firmware_menu.setEnabled(False)
        self.menuButton.setEnabled(False)
        self.radio_panel.setEnabled(False)

    def device_info_updated(self, device_info, manual_control):
        old_channel_id = self.get_current_channel_id()
        new_index = None
        self.last_channel_id = None
        self.combo_box_channel_ids.clear()
        self.graphChannelComboBox.clear()
        self.subchannel_fields.clear()
        self.channel_unit_options.clear()
        self.channel_unit_actions.clear()

    def get_current_channel_id(self):
        index = self.graphChannelComboBox.currentIndex()
        if index == -1:
            return None

        try:
            return self.combo_box_channel_ids[index]
        except IndexError:
            return None

    def close_controller(self):
        self.logger.debug('Close button pressed')
        self.controller.clear_manual_control()
        self.plotmain.dispatcher.mark_manually_disconnected(self.controller)

    def controller_state_changed(self, state, message):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR statusLabel
        #   14 LOAD_METHOD setText
        #   36 LOAD_FAST message
        #   38 PRECALL
        #   42 CALL
        #   52 POP_TOP
        #   54 LOAD_FAST state
        #   56 LOAD_GLOBAL DeviceControllerState
        #   68 LOAD_ATTR DISCONNECTED
        #   78 COMPARE_OP ==
        #   84 POP_JUMP_FORWARD_IF_FALSE to 286
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR statusProgressBar
        #   98 LOAD_METHOD setVisible
        #  120 LOAD_CONST False
        #  122 PRECALL
        #  126 CALL
        #  136 POP_TOP
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR stackedWidget
        #  150 LOAD_METHOD setCurrentIndex
        #  172 LOAD_CONST 0
        #  174 PRECALL
        #  178 CALL
        #  188 POP_TOP
        #  190 LOAD_FAST self
        #  192 LOAD_ATTR plotmain
        #  202 LOAD_METHOD set_tab_disconnected
        #  224 LOAD_FAST self
        #  226 PRECALL
        #  230 CALL
        #  240 POP_TOP
        #  242 LOAD_FAST self
        #  244 LOAD_METHOD disable_interaction
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_CONST None
        #  284 RETURN_VALUE
        #  286 LOAD_FAST state
        #  288 LOAD_GLOBAL DeviceControllerState
        #  300 LOAD_ATTR CONNECTING
        #  310 COMPARE_OP ==
        #  316 POP_JUMP_FORWARD_IF_FALSE to 674
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR stackedWidget
        #  330 LOAD_METHOD setCurrentIndex
        #  352 LOAD_CONST 0
        #  354 PRECALL
        #  358 CALL
        #  368 POP_TOP
        #  370 LOAD_FAST self
        #  372 LOAD_ATTR plotmain
        #  382 LOAD_METHOD set_tab_disconnected
        #  404 LOAD_FAST self
        #  406 PRECALL
        #  410 CALL
        #  420 POP_TOP
        #  422 LOAD_FAST self
        #  424 LOAD_METHOD disable_interaction
        #  446 PRECALL
        #  450 CALL
        #  460 POP_TOP
        #  462 LOAD_FAST self
        #  464 LOAD_ATTR statusProgressBar
        #  474 LOAD_METHOD setMinimum
        #  496 LOAD_CONST 0
        #  498 PRECALL
        #  502 CALL
        #  512 POP_TOP
        #  514 LOAD_FAST self
        #  516 LOAD_ATTR statusProgressBar
        #  526 LOAD_METHOD setMaximum
        #  548 LOAD_CONST 0
        #  550 PRECALL
        #  554 CALL
        #  564 POP_TOP
        #  566 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def progress_update(self, finished, total, message):
        self.statusProgressBar.setMaximum(total)
        self.statusProgressBar.setValue(finished)
        self.statusProgressBar.setVisible(True)
        self.statusLabel.setText(message)

    def rgb_updated_cb(self, index, values):
        try:
            widget = self.rgb_widgets[index]
        except IndexError:
            return None

        widget.set_values(values)

    def led_updated_cb(self, index, value):
        try:
            widget = self.led_widgets[index]
        except IndexError:
            return None

        widget.set_value(value)

    def ctrl_var_updated_cb(self, index, value):
        try:
            widget = self.ctrl_var_widgets[index]
        except IndexError:
            return None

        widget.set_value(value)

    def download_update_progress(self, read_bytes, total_length):
        self.firmware_progress.setMaximum(total_length)
        self.firmware_progress.setMinimum(read_bytes)

    def download_error(self, file, error_str):
        self.firmware_progress.reset()
        file.close()
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)

    def download_completed(self, url, file):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR firmware_progress
        #   14 LOAD_METHOD reset
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 LOAD_FAST file
        #   54 LOAD_METHOD getvalue
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST firmware_bytes
        #   92 NOP
        #   94 LOAD_GLOBAL NULL + bootloader
        #  106 LOAD_ATTR decode_firm_bytes
        #  116 LOAD_FAST firmware_bytes
        #  118 PRECALL
        #  122 CALL
        #  132 STORE_FAST firm_data
        #  134 JUMP_FORWARD to 408
        #  136 PUSH_EXC_INFO
        #  138 LOAD_GLOBAL Exception
        #  150 CHECK_EXC_MATCH
        #  152 POP_JUMP_FORWARD_IF_FALSE to 400
        #  154 POP_TOP
        #  156 LOAD_FAST self
        #  158 LOAD_ATTR logger
        #  168 LOAD_METHOD exception
        #  190 LOAD_CONST 'Error decoding downloaded firmware'
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 LOAD_FAST self
        #  210 LOAD_METHOD tr
        #  232 LOAD_CONST 'Error decoding downloaded firmware!'
        #  234 PRECALL
        #  238 CALL
        #  248 STORE_FAST m
        #  250 LOAD_GLOBAL QtWidgets
        #  262 LOAD_ATTR QMessageBox
        #  272 LOAD_METHOD critical
        #  294 LOAD_FAST self
        #  296 LOAD_FAST self
        #  298 LOAD_METHOD tr
        #  320 LOAD_CONST 'Error'
        #  322 PRECALL
        #  326 CALL
        #  336 LOAD_FAST m
        #  338 PRECALL
        #  342 CALL
        #  352 POP_TOP
        #  354 POP_EXCEPT
        #  356 LOAD_FAST file
        #  358 LOAD_METHOD close
        #  380 PRECALL
        #  384 CALL
        #  394 POP_TOP
        #  396 LOAD_CONST None
        #  398 RETURN_VALUE
        #  400 RERAISE
        #  402 COPY
        #  404 POP_EXCEPT
        #  406 RERAISE
        #  408 NOP
        #  410 LOAD_FAST file
        #  412 LOAD_METHOD close
        #  434 PRECALL
        #  438 CALL
        #  448 POP_TOP
        #  450 JUMP_FORWARD to 502
        #  452 PUSH_EXC_INFO
        #  454 LOAD_FAST file
        #  456 LOAD_METHOD close
        #  478 PRECALL
        #  482 CALL
        #  492 POP_TOP
        #  494 RERAISE
        #  496 COPY
        #  498 POP_EXCEPT
        #  500 RERAISE
        # ... bytecode truncated ...
        pass

    def firmware_finder_error(self, error_str):
        self.firmware_progress.reset()
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)

    def firmware_finder_completed(self, build_urls):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR firmware_progress
        #   14 LOAD_METHOD reset
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 LOAD_GLOBAL NULL + sorted
        #   64 LOAD_FAST build_urls
        #   66 LOAD_METHOD keys
        #   88 PRECALL
        #   92 CALL
        #  102 PRECALL
        #  106 CALL
        #  116 STORE_FAST build_types
        #  118 LOAD_CONST 'firmware'
        #  120 LOAD_FAST build_types
        #  122 CONTAINS_OP
        #  124 POP_JUMP_FORWARD_IF_FALSE to 212
        #  126 LOAD_FAST build_types
        #  128 LOAD_METHOD remove
        #  150 LOAD_CONST 'firmware'
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_FAST build_types
        #  170 LOAD_METHOD insert
        #  192 LOAD_CONST 0
        #  194 LOAD_CONST 'firmware'
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + len
        #  224 LOAD_FAST build_types
        #  226 PRECALL
        #  230 CALL
        #  240 LOAD_CONST 1
        #  242 COMPARE_OP ==
        #  248 POP_JUMP_FORWARD_IF_FALSE to 268
        #  250 LOAD_FAST build_types
        #  252 LOAD_CONST 0
        #  254 BINARY_SUBSCR
        #  264 STORE_FAST build_type
        #  266 JUMP_FORWARD to 436
        #  268 LOAD_GLOBAL QtWidgets
        #  280 LOAD_ATTR QInputDialog
        #  290 LOAD_METHOD getItem
        #  312 LOAD_FAST self
        #  314 LOAD_FAST self
        #  316 LOAD_METHOD tr
        #  338 LOAD_CONST 'Select Build Type'
        #  340 PRECALL
        #  344 CALL
        #  354 LOAD_FAST self
        #  356 LOAD_METHOD tr
        #  378 LOAD_CONST 'Select Build Type'
        #  380 PRECALL
        #  384 CALL
        #  394 LOAD_FAST build_types
        #  396 LOAD_CONST 0
        #  398 LOAD_CONST False
        #  400 KW_NAMES
        #  402 PRECALL
        #  406 CALL
        #  416 UNPACK_SEQUENCE
        #  420 STORE_FAST value
        #  422 STORE_FAST ok
        #  424 LOAD_FAST ok
        #  426 POP_JUMP_FORWARD_IF_TRUE to 432
        #  428 LOAD_CONST None
        #  430 RETURN_VALUE
        #  432 LOAD_FAST value
        #  434 STORE_FAST build_type
        #  436 LOAD_FAST build_urls
        #  438 LOAD_FAST build_type
        #  440 BINARY_SUBSCR
        #  450 STORE_FAST url
        #  452 LOAD_GLOBAL NULL + cast
        #  464 LOAD_GLOBAL Optional
        #  476 LOAD_GLOBAL bytes
        # ... bytecode truncated ...
        pass

    def do_bootloader_web(self, build_type, branch, commit):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_NOT_NONE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR firmware_progress
        #   42 LOAD_METHOD setMinimum
        #   64 LOAD_CONST 0
        #   66 PRECALL
        #   70 CALL
        #   80 POP_TOP
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR firmware_progress
        #   94 LOAD_METHOD setMaximum
        #  116 LOAD_CONST 0
        #  118 PRECALL
        #  122 CALL
        #  132 POP_TOP
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR firmware_progress
        #  146 LOAD_METHOD setValue
        #  168 LOAD_CONST 0
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR firmware_progress
        #  198 LOAD_METHOD setLabelText
        #  220 LOAD_FAST self
        #  222 LOAD_METHOD tr
        #  244 LOAD_CONST 'Searching for firmware...'
        #  246 PRECALL
        #  250 CALL
        #  260 PRECALL
        #  264 CALL
        #  274 POP_TOP
        #  276 LOAD_FAST self
        #  278 LOAD_ATTR firmware_progress
        #  288 LOAD_METHOD forceShow
        #  310 PRECALL
        #  314 CALL
        #  324 POP_TOP
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR controller
        #  338 LOAD_ATTR device_info
        #  348 LOAD_ATTR repo_name
        #  358 STORE_FAST repo
        #  360 LOAD_FAST repo
        #  362 POP_JUMP_FORWARD_IF_TRUE to 400
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR controller
        #  376 LOAD_ATTR device_info
        #  386 LOAD_ATTR board_info
        #  396 STORE_FAST board_info
        #  398 JUMP_FORWARD to 404
        #  400 LOAD_CONST None
        #  402 STORE_FAST board_info
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR firmware_finder
        #  416 LOAD_METHOD find_firmware
        #  438 LOAD_FAST build_type
        #  440 LOAD_FAST board_info
        #  442 LOAD_FAST repo
        #  444 LOAD_FAST branch
        #  446 LOAD_FAST commit
        #  448 KW_NAMES
        #  450 PRECALL
        #  454 CALL
        #  464 POP_TOP
        #  466 LOAD_CONST None
        #  468 RETURN_VALUE
        pass

    def do_bootloader_latest_stable(self):
        self.do_bootloader_web(build_type = 'firmware', branch = 'master')

    def ref_finder_completed(self, refs):
        self.firmware_progress.reset()

    def ref_finder_error(self):
        self.ref_finder_completed([])

    def do_bootloader_from_branch(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_NOT_NONE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR firmware_progress
        #   42 LOAD_METHOD setMinimum
        #   64 LOAD_CONST 0
        #   66 PRECALL
        #   70 CALL
        #   80 POP_TOP
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR firmware_progress
        #   94 LOAD_METHOD setMaximum
        #  116 LOAD_CONST 0
        #  118 PRECALL
        #  122 CALL
        #  132 POP_TOP
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR firmware_progress
        #  146 LOAD_METHOD setValue
        #  168 LOAD_CONST 0
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR firmware_progress
        #  198 LOAD_METHOD setLabelText
        #  220 LOAD_FAST self
        #  222 LOAD_METHOD tr
        #  244 LOAD_CONST 'Collecting branches...'
        #  246 PRECALL
        #  250 CALL
        #  260 PRECALL
        #  264 CALL
        #  274 POP_TOP
        #  276 LOAD_FAST self
        #  278 LOAD_ATTR firmware_progress
        #  288 LOAD_METHOD forceShow
        #  310 PRECALL
        #  314 CALL
        #  324 POP_TOP
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR controller
        #  338 LOAD_ATTR device_info
        #  348 LOAD_ATTR repo_name
        #  358 STORE_FAST repo
        #  360 LOAD_FAST repo
        #  362 POP_JUMP_FORWARD_IF_TRUE to 400
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR controller
        #  376 LOAD_ATTR device_info
        #  386 LOAD_ATTR board_info
        #  396 STORE_FAST board_info
        #  398 JUMP_FORWARD to 404
        #  400 LOAD_CONST None
        #  402 STORE_FAST board_info
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR ref_finder
        #  416 LOAD_METHOD get_firmware_refs
        #  438 LOAD_FAST board_info
        #  440 LOAD_FAST repo
        #  442 KW_NAMES
        #  444 PRECALL
        #  448 CALL
        #  458 POP_TOP
        #  460 LOAD_CONST None
        #  462 RETURN_VALUE
        pass

    def do_bootloader_from_commit(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL QtWidgets
        #   14 LOAD_ATTR QInputDialog
        #   24 LOAD_METHOD getText
        #   46 LOAD_FAST self
        #   48 LOAD_FAST self
        #   50 LOAD_METHOD tr
        #   72 LOAD_CONST 'Firmware Commit'
        #   74 PRECALL
        #   78 CALL
        #   88 LOAD_FAST self
        #   90 LOAD_METHOD tr
        #  112 LOAD_CONST 'Firmware Commit:'
        #  114 PRECALL
        #  118 CALL
        #  128 LOAD_GLOBAL QtWidgets
        #  140 LOAD_ATTR QLineEdit
        #  150 LOAD_ATTR EchoMode
        #  160 LOAD_ATTR Normal
        #  170 LOAD_CONST ''
        #  172 PRECALL
        #  176 CALL
        #  186 UNPACK_SEQUENCE
        #  190 STORE_FAST commit
        #  192 STORE_FAST ok
        #  194 LOAD_FAST ok
        #  196 POP_JUMP_FORWARD_IF_TRUE to 202
        #  198 LOAD_CONST None
        #  200 RETURN_VALUE
        #  202 LOAD_FAST commit
        #  204 LOAD_METHOD strip
        #  226 PRECALL
        #  230 CALL
        #  240 STORE_FAST commit
        #  242 LOAD_FAST self
        #  244 LOAD_METHOD do_bootloader_web
        #  266 LOAD_CONST None
        #  268 LOAD_FAST commit
        #  270 KW_NAMES
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_CONST None
        #  290 RETURN_VALUE
        pass

    def get_firmware_file(self, device_info):
        settings = QtCore.QSettings()
        (board_name, board_rev) = device_info.board_info
        short_board_name = board_name.replace(' ', '')
        keys = [
            f'''firmDirectory/{short_board_name}/Rev{board_rev}''',
            f'''firmDirectory/{short_board_name}/last''',
            'firmDirectory/last']
        firm_dir = None
        for key in keys:
            test_dir = settings.value(key)
            if test_dir and isinstance(test_dir, str) and os.path.isdir(test_dir):
                firm_dir = test_dir
            
            if not firm_dir:
                firm_dir = ''
        caption = self.tr('Open Firmware File')
        file_filter = self.tr('Firmware Files (*.firmware);;All Files (*.*)')
        val = QtWidgets.QFileDialog.getOpenFileName(self, caption, firm_dir, file_filter)
        output_path = val[0]
        if output_path:
            output_dir = os.path.dirname(output_path)
            for key in keys:
                settings.setValue(key, output_dir)
                return output_path
                return None

    def do_bootloader_from_file(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR device_info
        #   24 POP_JUMP_FORWARD_IF_NOT_NONE to 30
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR preferences
        #   42 LOAD_ATTR firmware_root_dir
        #   52 STORE_FAST base_dir
        #   54 LOAD_FAST base_dir
        #   56 POP_JUMP_FORWARD_IF_FALSE to 88
        #   58 LOAD_GLOBAL NULL + str
        #   70 LOAD_FAST base_dir
        #   72 PRECALL
        #   76 CALL
        #   86 STORE_FAST base_dir
        #   88 LOAD_GLOBAL NULL + bootloader
        #  100 LOAD_ATTR get_default_file
        #  110 LOAD_FAST self
        #  112 LOAD_ATTR controller
        #  122 LOAD_ATTR device_info
        #  132 LOAD_FAST base_dir
        #  134 PRECALL
        #  138 CALL
        #  148 UNPACK_SEQUENCE
        #  152 STORE_FAST firm_dir
        #  154 STORE_FAST firm_name
        #  156 LOAD_FAST firm_dir
        #  158 POP_JUMP_FORWARD_IF_TRUE to 226
        #  160 LOAD_FAST self
        #  162 LOAD_METHOD get_firmware_file
        #  184 LOAD_FAST self
        #  186 LOAD_ATTR controller
        #  196 LOAD_ATTR device_info
        #  206 PRECALL
        #  210 CALL
        #  220 STORE_FAST firm_file
        #  222 EXTENDED_ARG
        #  224 JUMP_FORWARD to 820
        #  226 LOAD_GLOBAL os
        #  238 LOAD_ATTR path
        #  248 LOAD_METHOD join
        #  270 LOAD_FAST firm_dir
        #  272 LOAD_FAST firm_name
        #  274 PRECALL
        #  278 CALL
        #  288 STORE_FAST firm_file
        #  290 LOAD_FAST self
        #  292 LOAD_METHOD tr
        #  314 LOAD_CONST 'Use {}?'
        #  316 PRECALL
        #  320 CALL
        #  330 LOAD_METHOD format
        #  352 LOAD_FAST firm_file
        #  354 PRECALL
        #  358 CALL
        #  368 STORE_FAST message
        #  370 LOAD_GLOBAL QtWidgets
        #  382 LOAD_ATTR QMessageBox
        #  392 LOAD_METHOD question
        #  414 LOAD_FAST self
        #  416 LOAD_FAST self
        #  418 LOAD_METHOD tr
        #  440 LOAD_CONST 'Update Firmware'
        #  442 PRECALL
        #  446 CALL
        #  456 LOAD_FAST message
        #  458 LOAD_GLOBAL QtWidgets
        #  470 LOAD_ATTR QMessageBox
        #  480 LOAD_ATTR StandardButton
        #  490 LOAD_ATTR Yes
        #  500 LOAD_GLOBAL QtWidgets
        #  512 LOAD_ATTR QMessageBox
        #  522 LOAD_ATTR StandardButton
        #  532 LOAD_ATTR No
        #  542 BINARY_OP |
        #  546 LOAD_GLOBAL QtWidgets
        #  558 LOAD_ATTR QMessageBox
        # ... bytecode truncated ...
        pass

    def alerts_changed_cb(self, alerts):
        for channel_id, fields in self.subchannel_fields.items():
            for mean_field, std_dev_field in enumerate(fields):
                for limit_type in (LimitType.MEAN_HIGH_LIMIT, LimitType.MEAN_LOW_LIMIT):
                    id = f'''_alert_{channel_id}_{i}_{limit_type}'''
                    if id in alerts:
                        mean_field.set_alert(True)
                    
                    mean_field.set_alert(False)
                    for limit_type in (LimitType.STD_HIGH_LIMIT, LimitType.STD_LOW_LIMIT):
                        id = f'''_alert_{channel_id}_{i}_{limit_type}'''
                        if id in alerts:
                            std_dev_field.set_alert(True)
                        
                        std_dev_field.set_alert(False)
                        return None

    def update_alert_action_icons(self):
        for channel_id, alert_actions in self.channel_alert_actions.items():
            for i, alert_action in enumerate(alert_actions):
                alert_limits = self.controller.device_prefs.get_alert_limits(channel_id, i)
                if alert_limits:
                    alert_action.setIcon(QtGui.QIcon.fromTheme('signal_flag_red'))
                    continue
                alert_action.setIcon(QtGui.QIcon.fromTheme('signal_flag_white'))
                return None

    def _manual_control_changed_cb(self, manual_control):
        if self.controller.device_info:
            self.device_info_updated(self.controller.device_info, manual_control)
        self.closeButton.setEnabled(manual_control)

    def schedule_or_trigger_count_updated(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR controller
        #   14 LOAD_ATTR trigger_count
        #   24 STORE_FAST trigger_count
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR controller
        #   38 LOAD_ATTR schedule_count
        #   48 STORE_FAST schedule_count
        #   50 LOAD_FAST trigger_count
        #   52 LOAD_CONST 1
        #   54 COMPARE_OP ==
        #   60 POP_JUMP_FORWARD_IF_FALSE to 106
        #   62 LOAD_FAST self
        #   64 LOAD_METHOD tr
        #   86 LOAD_CONST '1 trigger'
        #   88 PRECALL
        #   92 CALL
        #  102 STORE_FAST trigger_str
        #  104 JUMP_FORWARD to 204
        #  106 LOAD_FAST trigger_count
        #  108 LOAD_CONST 1
        #  110 COMPARE_OP >
        #  116 POP_JUMP_FORWARD_IF_FALSE to 200
        #  118 LOAD_FAST self
        #  120 LOAD_METHOD tr
        #  142 LOAD_CONST '{} triggers'
        #  144 PRECALL
        #  148 CALL
        #  158 LOAD_METHOD format
        #  180 LOAD_FAST trigger_count
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST trigger_str
        #  198 JUMP_FORWARD to 204
        #  200 LOAD_CONST ''
        #  202 STORE_FAST trigger_str
        #  204 LOAD_FAST schedule_count
        #  206 LOAD_CONST 1
        #  208 COMPARE_OP ==
        #  214 POP_JUMP_FORWARD_IF_FALSE to 260
        #  216 LOAD_FAST self
        #  218 LOAD_METHOD tr
        #  240 LOAD_CONST '1 schedule item'
        #  242 PRECALL
        #  246 CALL
        #  256 STORE_FAST schedule_str
        #  258 JUMP_FORWARD to 358
        #  260 LOAD_FAST schedule_count
        #  262 LOAD_CONST 1
        #  264 COMPARE_OP >
        #  270 POP_JUMP_FORWARD_IF_FALSE to 354
        #  272 LOAD_FAST self
        #  274 LOAD_METHOD tr
        #  296 LOAD_CONST '{} schedule items'
        #  298 PRECALL
        #  302 CALL
        #  312 LOAD_METHOD format
        #  334 LOAD_FAST schedule_count
        #  336 PRECALL
        #  340 CALL
        #  350 STORE_FAST schedule_str
        #  352 JUMP_FORWARD to 358
        #  354 LOAD_CONST ''
        #  356 STORE_FAST schedule_str
        #  358 LOAD_FAST self
        #  360 LOAD_ATTR tree_item
        #  370 LOAD_METHOD setText
        #  392 LOAD_CONST 6
        #  394 LOAD_GLOBAL NULL + str
        #  406 LOAD_FAST schedule_count
        #  408 PRECALL
        #  412 CALL
        #  422 PRECALL
        #  426 CALL
        #  436 POP_TOP
        #  438 LOAD_FAST trigger_str
        #  440 POP_JUMP_FORWARD_IF_FALSE to 566
        #  442 LOAD_FAST schedule_str
        #  444 POP_JUMP_FORWARD_IF_FALSE to 566
        # ... bytecode truncated ...
        pass

    def active_triggers_changed_cb(self, controller, active_triggers, inactive_triggers):
        active_str = ', '.join(sorted(active_triggers, key = str.casefold))
        self.tree_item.setText(7, active_str)
        inactive_str = ', '.join(sorted(inactive_triggers, key = str.casefold))
        self.tree_item.setText(8, inactive_str)

    def show_remote_tab(self):
        remote_controller = self.controller.remote_controller
        if remote_controller:
            remote_tab = self.plotmain.get_tab_widget(remote_controller)
            if remote_tab:
                self.plotmain.show_tab(remote_tab, self)
                return None
            return None

    def show_radio_tab(self):
        radio_controller = self.controller.parent_controller
        if radio_controller:
            radio_tab = self.plotmain.get_tab_widget(radio_controller)
            if radio_tab:
                self.plotmain.show_tab(radio_tab, self)
                return None
            return None
