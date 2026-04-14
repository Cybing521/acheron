# Source Generated with Decompyle++
# File: plotmain.pyc (Python 3.11)

import bisect
import datetime
import logging
import math
import os
import subprocess
import sys
import tempfile
from typing import Any, BinaryIO, Optional, Union
import urllib.parse as urllib
import diskcache
from PySide6 import QtCore, QtGui, QtSvgWidgets, QtWidgets
import asphodel
from hyperborea.dark_mode import set_style
import hyperborea.download as hyperborea
from .. import build_info
from ..core.dispatcher import Dispatcher
from ..core.device_controller import DeviceController
from ..core.preferences import Preferences
from ..connectivity.s3upload import S3UploadManager
from .about import AboutDialog
from .device_tab import DeviceTab
from .tcp_connect_dialog import TCPConnectDialog
from .download_firmware_dialog import DownloadFirmwareDialog
from .preferences_dialog import PreferencesDialog
from .tcp_scan_dialog import TCPScanDialog
from .ui.ui_plotmain import Ui_PlotMainWindow
logger = logging.getLogger(__name__)

try:
    from ..disk.schedule_reader import ScheduleReader
except Exception:
    ScheduleReader = Any

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class PaddedItemDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, padding, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = padding

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setWidth(size.width() + self.padding)
        return size

    def paint(self, painter, option, index):
        option.rect.setWidth(option.rect.width() - self.padding)
        super().paint(painter, option, index)

class PlotMainWindow(Ui_PlotMainWindow, QtWidgets.QMainWindow):

    def __init__(self, dispatcher, preferences, schedule_reader, parent = None):
        super().__init__(parent)
        self.dispatcher = dispatcher
        self.preferences = preferences
        self.settings = QtCore.QSettings()
        self.schedule_reader = schedule_reader
        self.firmware_cache = diskcache.Cache(self.preferences.firmware_dir, size_limit = 100000000.0)
        set_style(QtWidgets.QApplication.instance(), self.preferences.dark_mode)
        self.tab_widgets = []
        self.tab_tree_items = {}
        self.shown_tab = None
        self.setupUi(self)
        self.extra_ui_setup()
        self.setup_logo()
        self.setup_callbacks()
        self.setup_update_actions()
        self.collapsed = self.preferences.collapsed
        self.connecting_icon = QtGui.QIcon.fromTheme('nav_refresh_red')
        self.connected_icon = QtGui.QIcon.fromTheme('nav_plain_blue')
        if sys.platform == 'darwin':
            self.menubar.setNativeMenuBar(False)
        geometry = self.settings.value('Geometry', b'')
        self.restoreGeometry(geometry)

    def setup_logo(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_DEREF self
        #    6 LOAD_ATTR stackedWidget
        #   16 LOAD_METHOD setCurrentIndex
        #   38 LOAD_CONST 1
        #   40 PRECALL
        #   44 CALL
        #   54 POP_TOP
        #   56 LOAD_GLOBAL NULL + QtSvgWidgets
        #   68 LOAD_ATTR QSvgWidget
        #   78 LOAD_CONST ':/logo.svg'
        #   80 PRECALL
        #   84 CALL
        #   94 LOAD_DEREF self
        #   96 STORE_ATTR logo
        #  106 LOAD_GLOBAL NULL + QtWidgets
        #  118 LOAD_ATTR QSizePolicy
        #  128 LOAD_GLOBAL QtWidgets
        #  140 LOAD_ATTR QSizePolicy
        #  150 LOAD_ATTR Policy
        #  160 LOAD_ATTR Ignored
        #  170 LOAD_GLOBAL QtWidgets
        #  182 LOAD_ATTR QSizePolicy
        #  192 LOAD_ATTR Policy
        #  202 LOAD_ATTR Ignored
        #  212 PRECALL
        #  216 CALL
        #  226 STORE_FAST size_policy
        #  228 LOAD_DEREF self
        #  230 LOAD_ATTR logo
        #  240 LOAD_METHOD setSizePolicy
        #  262 LOAD_FAST size_policy
        #  264 PRECALL
        #  268 CALL
        #  278 POP_TOP
        #  280 LOAD_CONST 'event'
        #  282 LOAD_GLOBAL QtGui
        #  294 LOAD_ATTR QResizeEvent
        #  304 LOAD_CONST 'return'
        #  306 LOAD_CONST None
        #  308 BUILD_TUPLE
        #  310 LOAD_CLOSURE self
        #  312 BUILD_TUPLE
        #  314 LOAD_CONST <code object resizeEvent at 0xacd215c00, file "acheron\gui\plotmain.py", line 107>
        #  316 MAKE_FUNCTION annotations, closure
        #  318 STORE_FAST resizeEvent
        #  320 LOAD_FAST resizeEvent
        #  322 LOAD_DEREF self
        #  324 LOAD_ATTR logo
        #  334 STORE_ATTR resizeEvent
        #  344 LOAD_DEREF self
        #  346 LOAD_ATTR logoLayout
        #  356 LOAD_METHOD addWidget
        #  378 LOAD_DEREF self
        #  380 LOAD_ATTR logo
        #  390 PRECALL
        #  394 CALL
        #  404 POP_TOP
        #  406 LOAD_GLOBAL NULL + QtWidgets
        #  418 LOAD_ATTR QGraphicsOpacityEffect
        #  428 LOAD_DEREF self
        #  430 LOAD_ATTR logo
        #  440 PRECALL
        #  444 CALL
        #  454 LOAD_DEREF self
        #  456 STORE_ATTR opacity_effect
        #  466 LOAD_DEREF self
        #  468 LOAD_ATTR opacity_effect
        #  478 LOAD_METHOD setOpacity
        #  500 LOAD_CONST 0.0
        #  502 PRECALL
        #  506 CALL
        #  516 POP_TOP
        #  518 LOAD_DEREF self
        #  520 LOAD_ATTR logo
        #  530 LOAD_METHOD setGraphicsEffect
        #  552 LOAD_DEREF self
        #  554 LOAD_ATTR opacity_effect
        #  564 PRECALL
        # ... bytecode truncated ...
        pass

    def extra_ui_setup(self):
        app_name = QtWidgets.QApplication.applicationName()
        version = QtWidgets.QApplication.applicationVersion()
        is_frozen = getattr(sys, 'frozen', False)
        if is_frozen:
            title = self.tr('{} ({})').format(app_name, version)
        else:
            title = self.tr('{} (dev)').format(app_name)
        self.setWindowTitle(title)
        self.warningLabel.setVisible(False)

    def setup_callbacks(self):
        self.dispatcher.controller_created.connect(self.controller_created)
        self.dispatcher.controller_stopped.connect(self.remove_controller)
        self.dispatcher.initial_devices_connected.connect(self.initial_devices_connected_cb)
        self.actionEnableRFPower.triggered.connect(self.dispatcher.enable_all_rf_power)
        self.actionDisableRFPower.triggered.connect(self.dispatcher.disable_all_rf_power)
        self.dispatcher.rf_power_changed.connect(self.rf_power_changed_cb)
        self.dispatcher.upload_manager_changed.connect(self.upload_manager_changed_cb)
        self.dispatcher.active_triggers_changed.connect(self.active_triggers_changed)
        self.actionRescanUSB.triggered.connect(self.dispatcher.rescan_usb)
        self.actionFindTCPDevices.triggered.connect(self.find_tcp_devices)
        self.actionConnectTCPDevice.triggered.connect(self.connect_tcp_device)
        self.actionDisableStreaming.triggered.connect(self.set_disable_streaming)
        self.actionDisableArchiving.triggered.connect(self.set_disable_archiving)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionChannelTable.triggered.connect(self.show_channel_table)
        self.actionPreferences.triggered.connect(self.show_preferences)
        self.actionReloadSchedule.triggered.connect(self.reload_schedule_cb)
        self.actionClosableTabs.triggered.connect(self.closable_tabs_cb)
        self.actionShowLogs.triggered.connect(self.show_log_dir)
        self.actionShowConfig.triggered.connect(self.show_config_dir)
        config = self.preferences.settings.fileName()
        if not os.path.exists(config):
            self.actionShowConfig.setVisible(False)
        self.clock_timer = QtCore.QTimer(self)
        self.clock_timer.timeout.connect(self.update_datetime_label)
        self.clock_timer.start(1000)
        self.upload_timeout_timer = QtCore.QTimer(self)
        self.upload_timeout_timer.setSingleShot(True)
        self.upload_timeout_timer.timeout.connect(self.upload_timeout_cb)
        self.tabWidget.tabCloseRequested.connect(self.tab_close_requested)
        self.tabWidget.currentChanged.connect(self.current_tab_changed_cb)
        self.treeWidget.itemDoubleClicked.connect(self.tree_item_double_clicked)
        self.actionDownloadFirmware.triggered.connect(self.download_firmware)
        self.firmware_finder = hyperborea.download.FirmwareFinder(logger)
        self.firmware_finder.completed.connect(self.firmware_finder_completed)
        self.firmware_finder.error.connect(self.firmware_finder_error)
        self.firmware_downloader = hyperborea.download.Downloader(logger)
        self.firmware_downloader.update.connect(self.update_progress_cb)
        self.firmware_downloader.completed.connect(self.firmware_download_completed)
        self.firmware_downloader.error.connect(self.firmware_download_error)
        self.actionUpdateLatestStable.triggered.connect(self.update_latest_stable)
        self.actionUpdateCurrentBranch.triggered.connect(self.update_current_branch)
        self.actionUpdateSpecificBranch.triggered.connect(self.update_specific_branch)
        self.actionUpdateSpecificCommit.triggered.connect(self.update_specific_commit)
        self.software_finder = hyperborea.download.SoftwareFinder(logger)
        self.software_finder.completed.connect(self.update_finder_completed)
        self.software_finder.error.connect(self.update_finder_error)
        self.ref_finder = hyperborea.download.RefFinder(logger)
        self.ref_finder.completed.connect(self.ref_finder_completed)
        self.ref_finder.error.connect(self.ref_finder_error)
        self.software_downloader = hyperborea.download.Downloader(logger)
        self.software_downloader.update.connect(self.update_progress_cb)
        self.software_downloader.completed.connect(self.software_download_completed)
        self.software_downloader.error.connect(self.software_download_error)
        self.actionMarkDirectory.triggered.connect(self.mark_directory)
        self.actionMarkFiles.triggered.connect(self.mark_files)
        self.next_tab_shortcut = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+PgDown'), self)
        self.next_tab_shortcut.activated.connect(self.next_tab)
        self.prev_tab_shortcut = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+PgUp'), self)
        self.prev_tab_shortcut.activated.connect(self.prev_tab)
        self.schedule_reader.error.connect(self.schedule_error_cb)
        self.schedule_reader.warning.connect(self.schedule_warning_cb)

    def setup_update_actions(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + build_info
        #   14 LOAD_ATTR get_branch_name
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST branch_name
        #   40 LOAD_FAST branch_name
        #   42 POP_JUMP_FORWARD_IF_TRUE to 398
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR menuCheckForUpdates
        #   56 LOAD_METHOD setEnabled
        #   78 LOAD_CONST False
        #   80 PRECALL
        #   84 CALL
        #   94 POP_TOP
        #   96 LOAD_FAST self
        #   98 LOAD_ATTR menuCheckForUpdates
        #  108 LOAD_METHOD setTitle
        #  130 LOAD_FAST self
        #  132 LOAD_METHOD tr
        #  154 LOAD_CONST 'Not Updatable'
        #  156 PRECALL
        #  160 CALL
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR actionUpdateLatestStable
        #  198 LOAD_METHOD setEnabled
        #  220 LOAD_CONST False
        #  222 PRECALL
        #  226 CALL
        #  236 POP_TOP
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR actionUpdateCurrentBranch
        #  250 LOAD_METHOD setEnabled
        #  272 LOAD_CONST False
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 LOAD_FAST self
        #  292 LOAD_ATTR actionUpdateSpecificBranch
        #  302 LOAD_METHOD setEnabled
        #  324 LOAD_CONST False
        #  326 PRECALL
        #  330 CALL
        #  340 POP_TOP
        #  342 LOAD_FAST self
        #  344 LOAD_ATTR actionUpdateSpecificCommit
        #  354 LOAD_METHOD setEnabled
        #  376 LOAD_CONST False
        #  378 PRECALL
        #  382 CALL
        #  392 POP_TOP
        #  394 LOAD_CONST None
        #  396 RETURN_VALUE
        #  398 LOAD_FAST branch_name
        #  400 LOAD_CONST 'master'
        #  402 COMPARE_OP ==
        #  408 POP_JUMP_FORWARD_IF_FALSE to 518
        #  410 LOAD_FAST self
        #  412 LOAD_ATTR actionUpdateCurrentBranch
        #  422 LOAD_METHOD setEnabled
        #  444 LOAD_CONST False
        #  446 PRECALL
        #  450 CALL
        #  460 POP_TOP
        #  462 LOAD_FAST self
        #  464 LOAD_ATTR actionUpdateCurrentBranch
        #  474 LOAD_METHOD setVisible
        #  496 LOAD_CONST False
        #  498 PRECALL
        #  502 CALL
        #  512 POP_TOP
        #  514 LOAD_CONST None
        #  516 RETURN_VALUE
        #  518 LOAD_FAST self
        #  520 LOAD_METHOD tr
        #  542 LOAD_CONST 'Latest {}'
        #  544 PRECALL
        # ... bytecode truncated ...
        pass

    def find_update(self, branch, commit, fallback_branch):
        build_key = build_info.get_build_key()
        if not build_key:
            return None
        self.update_fallback_branch = None
        self.update_progress.setMinimum(0)
        self.update_progress.setMaximum(0)
        self.update_progress.setValue(0)
        self.update_progress.setLabelText(self.tr('Checking for update...'))
        self.update_progress.forceShow()
        self.software_finder.find_software('acheron', build_key, branch, commit)

    def update_finder_error(self, error_str):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR update_fallback_branch
        #   14 POP_JUMP_FORWARD_IF_FALSE to 74
        #   16 LOAD_FAST self
        #   18 LOAD_METHOD find_update
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR update_fallback_branch
        #   52 KW_NAMES
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_CONST None
        #   72 RETURN_VALUE
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR update_progress
        #   86 LOAD_METHOD reset
        #  108 PRECALL
        #  112 CALL
        #  122 POP_TOP
        #  124 LOAD_GLOBAL QtWidgets
        #  136 LOAD_ATTR QMessageBox
        #  146 LOAD_METHOD critical
        #  168 LOAD_FAST self
        #  170 LOAD_FAST self
        #  172 LOAD_METHOD tr
        #  194 LOAD_CONST 'Error'
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_FAST error_str
        #  212 PRECALL
        #  216 CALL
        #  226 POP_TOP
        #  228 LOAD_CONST None
        #  230 RETURN_VALUE
        pass

    def update_finder_completed(self, params):
        self.update_progress.reset()
        (url, commit, ready) = params

    def update_progress_cb(self, written_bytes, total_length):
        if total_length != 0:
            self.update_progress.setMinimum(0)
            self.update_progress.setMaximum(total_length)
            self.update_progress.setValue(written_bytes)
            return None

    def software_download_error(self, file, error_str):
        self.update_progress.reset()
        file.close()
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)
        os.unlink(file.filename)

    def software_download_completed(self, _url, file):
        self.update_progress.reset()
        file.close()
        self.dispatcher.stop()
        subprocess.Popen([
            file.filename,
            '/silent',
            '/DeleteInstaller=Yes',
            '/SP-',
            '/SUPPRESSMSGBOXES',
            '/NORESTART',
            '/NOCANCEL'])
        self.close()

    def update_latest_stable(self):
        self.find_update(branch = 'master')

    def update_current_branch(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + build_info
        #   14 LOAD_ATTR get_branch_name
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST branch_name
        #   40 LOAD_FAST branch_name
        #   42 POP_JUMP_FORWARD_IF_TRUE to 48
        #   44 LOAD_CONST None
        #   46 RETURN_VALUE
        #   48 LOAD_FAST branch_name
        #   50 LOAD_CONST ('master', 'develop')
        #   52 CONTAINS_OP
        #   54 POP_JUMP_FORWARD_IF_FALSE to 62
        #   56 LOAD_CONST None
        #   58 STORE_FAST fallback
        #   60 JUMP_FORWARD to 66
        #   62 LOAD_CONST 'develop'
        #   64 STORE_FAST fallback
        #   66 LOAD_FAST self
        #   68 LOAD_METHOD find_update
        #   90 LOAD_FAST branch_name
        #   92 LOAD_FAST fallback
        #   94 KW_NAMES
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_CONST None
        #  114 RETURN_VALUE
        pass

    def update_specific_branch(self):
        self.update_progress.setMinimum(0)
        self.update_progress.setMaximum(0)
        self.update_progress.setValue(0)
        self.update_progress.setLabelText(self.tr('Collecting branches...'))
        self.update_progress.forceShow()
        self.ref_finder.get_software_refs('acheron')

    def ref_finder_error(self):
        self.ref_finder_completed([])

    def ref_finder_completed(self, refs):
        self.update_progress.reset()
        default_branch = build_info.get_branch_name()

    def update_specific_commit(self):
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
        #   72 LOAD_CONST 'Commit'
        #   74 PRECALL
        #   78 CALL
        #   88 LOAD_FAST self
        #   90 LOAD_METHOD tr
        #  112 LOAD_CONST 'Commit:'
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
        #  244 LOAD_METHOD find_update
        #  266 LOAD_FAST commit
        #  268 KW_NAMES
        #  270 PRECALL
        #  274 CALL
        #  284 POP_TOP
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        pass

    def download_firmware(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + DownloadFirmwareDialog
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
        #  134 LOAD_METHOD get_results
        #  156 PRECALL
        #  160 CALL
        #  170 STORE_FAST results
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
        #  264 PUSH_NULL
        #  266 LOAD_FAST self
        #  268 LOAD_ATTR firmware_finder
        #  278 LOAD_ATTR find_firmware
        #  288 LOAD_CONST ()
        #  290 LOAD_CONST 'build_type'
        #  292 LOAD_CONST None
        #  294 BUILD_MAP
        #  296 LOAD_FAST results
        #  298 DICT_MERGE
        #  300 CALL_FUNCTION_EX
        #  302 POP_TOP
        #  304 LOAD_CONST None
        #  306 RETURN_VALUE
        pass

    def firmware_finder_error(self, error_str):
        self.update_progress.reset()
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)

    def get_firmware_save_file(self, default_name):
        directory = self.settings.value('fileSaveDirectory')
        if directory:
            if isinstance(directory, str):
                if not os.path.isdir(directory):
                    directory = ''
                else:
                    directory = ''
            else:
                directory = ''
        file_and_dir = os.path.join(directory, default_name)
        caption = self.tr('Save Firmware File')
        file_filter = self.tr('Firmware Files (*.firmware);;All Files (*.*)')
        val = QtWidgets.QFileDialog.getSaveFileName(self, caption, file_and_dir, file_filter)
        output_path = val[0]
        if output_path:
            output_dir = os.path.dirname(output_path)
            self.settings.setValue('fileSaveDirectory', output_dir)
            return output_path

    def firmware_finder_completed(self, build_urls):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR update_progress
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
        #  452 LOAD_GLOBAL urllib
        #  464 LOAD_ATTR parse
        #  474 LOAD_METHOD urlparse
        # ... bytecode truncated ...
        pass

    def firmware_download_error(self, file, error_str):
        self.update_progress.reset()
        file.close()
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)
        os.unlink(file.filename)

    def firmware_download_completed(self, url, file):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR update_progress
        #   14 LOAD_METHOD reset
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 NOP
        #   54 LOAD_FAST file
        #   56 LOAD_METHOD seek
        #   78 LOAD_CONST 0
        #   80 PRECALL
        #   84 CALL
        #   94 POP_TOP
        #   96 LOAD_FAST file
        #   98 LOAD_METHOD read
        #  120 PRECALL
        #  124 CALL
        #  134 STORE_FAST firmware_bytes
        #  136 JUMP_FORWARD to 174
        #  138 PUSH_EXC_INFO
        #  140 LOAD_GLOBAL Exception
        #  152 CHECK_EXC_MATCH
        #  154 POP_JUMP_FORWARD_IF_FALSE to 166
        #  156 POP_TOP
        #  158 LOAD_CONST None
        #  160 STORE_FAST firmware_bytes
        #  162 POP_EXCEPT
        #  164 JUMP_FORWARD to 174
        #  166 RERAISE
        #  168 COPY
        #  170 POP_EXCEPT
        #  172 RERAISE
        #  174 LOAD_FAST file
        #  176 LOAD_METHOD close
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 JUMP_FORWARD to 266
        #  216 PUSH_EXC_INFO
        #  218 LOAD_FAST file
        #  220 LOAD_METHOD close
        #  242 PRECALL
        #  246 CALL
        #  256 POP_TOP
        #  258 RERAISE
        #  260 COPY
        #  262 POP_EXCEPT
        #  264 RERAISE
        #  266 LOAD_FAST firmware_bytes
        #  268 POP_JUMP_FORWARD_IF_FALSE to 324
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR firmware_cache
        #  282 LOAD_METHOD set
        #  304 LOAD_FAST url
        #  306 LOAD_FAST firmware_bytes
        #  308 PRECALL
        #  312 CALL
        #  322 POP_TOP
        #  324 LOAD_GLOBAL QtWidgets
        #  336 LOAD_ATTR QMessageBox
        #  346 LOAD_METHOD information
        #  368 LOAD_FAST self
        #  370 LOAD_FAST self
        #  372 LOAD_METHOD tr
        #  394 LOAD_CONST 'Finished'
        #  396 PRECALL
        #  400 CALL
        #  410 LOAD_FAST self
        #  412 LOAD_METHOD tr
        #  434 LOAD_CONST 'Finished download'
        #  436 PRECALL
        #  440 CALL
        #  450 PRECALL
        #  454 CALL
        #  464 POP_TOP
        #  466 LOAD_CONST None
        #  468 RETURN_VALUE
        pass

    def closeEvent(self, event):
        geometry = self.saveGeometry()
        self.settings.setValue('Geometry', geometry)
        QtWidgets.QWidget.closeEvent(self, event)

    def controller_created(self, controller):
        parent_tree_item = None
        parent_controller = controller.parent_controller

    def get_tab_widget(self, controller):
        for tab_widget in self.tab_widgets:
            if tab_widget.controller == controller:
                
                return None, tab_widget
            return None

    def remove_controller(self, controller):
        tab_widget = self.get_tab_widget(controller)
        if not tab_widget:
            return None

        try:
            if self.shown_tab == tab_widget:
                self.shown_tab = None
            index = self.tab_widgets.index(tab_widget)
            self.tab_widgets.pop(index)
            self.tabWidget.removeTab(index + 1)
        except ValueError:
            pass

        tab_widget.deleteLater()
        if len(self.tab_widgets) == 0:
            self.stackedWidget.setCurrentIndex(1)
            self.logo_animation.start()
        tree_item = self.tab_tree_items.pop(tab_widget, None)

    def update_device_name(self, widget, name):
        try:
            index = self.tab_widgets.index(widget)
            self.tabWidget.setTabText(index + 1, name)
            return None
        except ValueError:
            return None

    def set_tab_connected(self, widget):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR tab_widgets
        #   16 LOAD_METHOD index
        #   38 LOAD_FAST widget
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST index
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR tabWidget
        #   68 LOAD_METHOD setTabIcon
        #   90 LOAD_FAST index
        #   92 LOAD_CONST 1
        #   94 BINARY_OP +
        #   98 LOAD_FAST self
        #  100 LOAD_ATTR connected_icon
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR tab_tree_items
        #  138 LOAD_METHOD get
        #  160 LOAD_FAST widget
        #  162 LOAD_CONST None
        #  164 PRECALL
        #  168 CALL
        #  178 STORE_FAST tree_item
        #  180 LOAD_FAST tree_item
        #  182 POP_JUMP_FORWARD_IF_NONE to 238
        #  184 LOAD_FAST tree_item
        #  186 LOAD_METHOD setIcon
        #  208 LOAD_CONST 0
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR connected_icon
        #  222 PRECALL
        #  226 CALL
        #  236 POP_TOP
        #  238 LOAD_FAST widget
        #  240 LOAD_ATTR controller
        #  250 LOAD_ATTR parent_controller
        #  260 STORE_FAST parent_controller
        #  262 LOAD_FAST parent_controller
        #  264 POP_JUMP_FORWARD_IF_NONE to 360
        #  266 LOAD_FAST self
        #  268 LOAD_METHOD get_tab_widget
        #  290 LOAD_FAST parent_controller
        #  292 PRECALL
        #  296 CALL
        #  306 STORE_FAST parent_widget
        #  308 LOAD_FAST parent_widget
        #  310 POP_JUMP_FORWARD_IF_NONE to 364
        #  312 LOAD_FAST self
        #  314 LOAD_METHOD show_tab
        #  336 LOAD_FAST widget
        #  338 LOAD_FAST parent_widget
        #  340 PRECALL
        #  344 CALL
        #  354 POP_TOP
        #  356 LOAD_CONST None
        #  358 RETURN_VALUE
        #  360 LOAD_CONST None
        #  362 RETURN_VALUE
        #  364 LOAD_CONST None
        #  366 RETURN_VALUE
        #  368 PUSH_EXC_INFO
        #  370 LOAD_GLOBAL ValueError
        #  382 CHECK_EXC_MATCH
        #  384 POP_JUMP_FORWARD_IF_FALSE to 394
        #  386 POP_TOP
        #  388 POP_EXCEPT
        #  390 LOAD_CONST None
        #  392 RETURN_VALUE
        #  394 RERAISE
        #  396 COPY
        #  398 POP_EXCEPT
        #  400 RERAISE
        pass

    def set_tab_disconnected(self, widget):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR tab_widgets
        #   16 LOAD_METHOD index
        #   38 LOAD_FAST widget
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST index
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR tabWidget
        #   68 LOAD_METHOD setTabIcon
        #   90 LOAD_FAST index
        #   92 LOAD_CONST 1
        #   94 BINARY_OP +
        #   98 LOAD_FAST self
        #  100 LOAD_ATTR connecting_icon
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR tab_tree_items
        #  138 LOAD_METHOD get
        #  160 LOAD_FAST widget
        #  162 LOAD_CONST None
        #  164 PRECALL
        #  168 CALL
        #  178 STORE_FAST tree_item
        #  180 LOAD_FAST tree_item
        #  182 POP_JUMP_FORWARD_IF_NONE to 242
        #  184 LOAD_FAST tree_item
        #  186 LOAD_METHOD setIcon
        #  208 LOAD_CONST 0
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR connecting_icon
        #  222 PRECALL
        #  226 CALL
        #  236 POP_TOP
        #  238 LOAD_CONST None
        #  240 RETURN_VALUE
        #  242 LOAD_CONST None
        #  244 RETURN_VALUE
        #  246 PUSH_EXC_INFO
        #  248 LOAD_GLOBAL ValueError
        #  260 CHECK_EXC_MATCH
        #  262 POP_JUMP_FORWARD_IF_FALSE to 272
        #  264 POP_TOP
        #  266 POP_EXCEPT
        #  268 LOAD_CONST None
        #  270 RETURN_VALUE
        #  272 RERAISE
        #  274 COPY
        #  276 POP_EXCEPT
        #  278 RERAISE
        pass

    def show_tab(self, widget, src):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST src
        #    4 POP_JUMP_FORWARD_IF_FALSE to 68
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR tabWidget
        #   18 LOAD_METHOD currentWidget
        #   40 PRECALL
        #   44 CALL
        #   54 LOAD_FAST src
        #   56 COMPARE_OP !=
        #   62 POP_JUMP_FORWARD_IF_FALSE to 68
        #   64 LOAD_CONST None
        #   66 RETURN_VALUE
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR tabWidget
        #   80 LOAD_METHOD setCurrentWidget
        #  102 LOAD_FAST widget
        #  104 PRECALL
        #  108 CALL
        #  118 POP_TOP
        #  120 LOAD_CONST None
        #  122 RETURN_VALUE
        pass

    def show_about(self):
        dialog = AboutDialog(self)

        try:
            dialog.exec()
            dialog.deleteLater()
            return None
        except:
            dialog.deleteLater()

    def get_html_dir(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + getattr
        #   14 LOAD_GLOBAL sys
        #   26 LOAD_CONST 'frozen'
        #   28 LOAD_CONST False
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST is_frozen
        #   46 LOAD_FAST is_frozen
        #   48 POP_JUMP_FORWARD_IF_FALSE to 192
        #   50 LOAD_GLOBAL os
        #   62 LOAD_ATTR path
        #   72 LOAD_METHOD join
        #   94 LOAD_GLOBAL os
        #  106 LOAD_ATTR path
        #  116 LOAD_METHOD dirname
        #  138 LOAD_GLOBAL sys
        #  150 LOAD_ATTR executable
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_CONST 'html'
        #  176 PRECALL
        #  180 CALL
        #  190 RETURN_VALUE
        #  192 LOAD_GLOBAL os
        #  204 LOAD_ATTR path
        #  214 LOAD_METHOD join
        #  236 LOAD_GLOBAL os
        #  248 LOAD_ATTR path
        #  258 LOAD_METHOD dirname
        #  280 LOAD_GLOBAL __file__
        #  292 PRECALL
        #  296 CALL
        #  306 LOAD_CONST 'html'
        #  308 PRECALL
        #  312 CALL
        #  322 RETURN_VALUE
        pass

    def show_channel_table(self):
        filename = os.path.join(self.get_html_dir(), 'asphodel_channels.html')
        url = QtCore.QUrl.fromLocalFile(filename)
        QtGui.QDesktopServices.openUrl(url)

    def show_file_on_disk(self, file):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL os
        #   14 LOAD_ATTR path
        #   24 LOAD_METHOD abspath
        #   46 LOAD_FAST file
        #   48 PRECALL
        #   52 CALL
        #   62 STORE_FAST file
        #   64 LOAD_GLOBAL sys
        #   76 LOAD_ATTR platform
        #   86 LOAD_CONST 'win32'
        #   88 COMPARE_OP ==
        #   94 POP_JUMP_FORWARD_IF_FALSE to 146
        #   96 LOAD_GLOBAL NULL + subprocess
        #  108 LOAD_ATTR Popen
        #  118 LOAD_CONST 'explorer'
        #  120 LOAD_CONST '/select,'
        #  122 LOAD_FAST file
        #  124 BUILD_LIST
        #  126 PRECALL
        #  130 CALL
        #  140 POP_TOP
        #  142 LOAD_CONST None
        #  144 RETURN_VALUE
        #  146 LOAD_GLOBAL sys
        #  158 LOAD_ATTR platform
        #  168 LOAD_CONST 'darwin'
        #  170 COMPARE_OP ==
        #  176 POP_JUMP_FORWARD_IF_FALSE to 252
        #  178 LOAD_CONST 'osascript'
        #  180 LOAD_CONST '-e'
        #  182 LOAD_CONST 'tell application "Finder"'
        #  184 LOAD_CONST '-e'
        #  186 LOAD_CONST 'activate'
        #  188 LOAD_CONST '-e'
        #  190 LOAD_CONST 'select POSIX file "'
        #  192 LOAD_FAST file
        #  194 FORMAT_VALUE
        #  196 LOAD_CONST '"'
        #  198 BUILD_STRING
        #  200 LOAD_CONST '-e'
        #  202 LOAD_CONST 'end tell'
        #  204 BUILD_LIST
        #  206 STORE_FAST args
        #  208 LOAD_GLOBAL NULL + subprocess
        #  220 LOAD_ATTR Popen
        #  230 LOAD_FAST args
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_CONST None
        #  250 RETURN_VALUE
        #  252 LOAD_GLOBAL QtCore
        #  264 LOAD_ATTR QUrl
        #  274 LOAD_METHOD fromLocalFile
        #  296 LOAD_GLOBAL os
        #  308 LOAD_ATTR path
        #  318 LOAD_METHOD dirname
        #  340 LOAD_FAST file
        #  342 PRECALL
        #  346 CALL
        #  356 PRECALL
        #  360 CALL
        #  370 STORE_FAST url
        #  372 LOAD_GLOBAL QtGui
        #  384 LOAD_ATTR QDesktopServices
        #  394 LOAD_METHOD openUrl
        #  416 LOAD_FAST url
        #  418 PRECALL
        #  422 CALL
        #  432 POP_TOP
        #  434 LOAD_CONST None
        #  436 RETURN_VALUE
        pass

    def show_log_dir(self):
        logdir = os.path.abspath(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation))
        logfile = os.path.join(logdir, 'main.log')
        self.show_file_on_disk(logfile)

    def show_config_dir(self):
        config = self.preferences.settings.fileName()
        if os.path.exists(config):
            self.show_file_on_disk(config)
            return None

    def set_disable_streaming(self):
        disable_streaming = self.actionDisableStreaming.isChecked()
        self.dispatcher.set_disable_streaming(disable_streaming)

    def set_disable_archiving(self):
        disable_archiving = self.actionDisableArchiving.isChecked()
        self.warningLabel.setVisible(disable_archiving)
        self.dispatcher.set_disable_archiving(disable_archiving)

    def show_preferences(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + PreferencesDialog
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR preferences
        #   26 LOAD_FAST self
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST dialog
        #   44 NOP
        #   46 LOAD_FAST dialog
        #   48 LOAD_METHOD exec
        #   70 PRECALL
        #   74 CALL
        #   84 POP_JUMP_FORWARD_IF_FALSE to 196
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR dispatcher
        #   98 LOAD_METHOD update_preferences
        #  120 PRECALL
        #  124 CALL
        #  134 POP_TOP
        #  136 LOAD_FAST self
        #  138 LOAD_ATTR tab_widgets
        #  148 GET_ITER
        #  150 FOR_ITER to 196
        #  152 STORE_FAST device_tab
        #  154 LOAD_FAST device_tab
        #  156 LOAD_METHOD update_preferences
        #  178 PRECALL
        #  182 CALL
        #  192 POP_TOP
        #  194 JUMP_BACKWARD to 150
        #  196 LOAD_FAST dialog
        #  198 LOAD_METHOD deleteLater
        #  220 PRECALL
        #  224 CALL
        #  234 POP_TOP
        #  236 LOAD_CONST None
        #  238 RETURN_VALUE
        #  240 PUSH_EXC_INFO
        #  242 LOAD_FAST dialog
        #  244 LOAD_METHOD deleteLater
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 RERAISE
        #  284 COPY
        #  286 POP_EXCEPT
        #  288 RERAISE
        pass

    def update_datetime_label(self):
        dt = datetime.datetime.now(tz = datetime.timezone.utc)
        s = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.datetimeLabel.setText(s)

    def rate_status_cb(self, uploading, rate):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST uploading
        #    4 POP_JUMP_FORWARD_IF_FALSE to 106
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR uploadRateLabel
        #   18 LOAD_METHOD setText
        #   40 LOAD_CONST '{:.1f} KB/s'
        #   42 LOAD_METHOD format
        #   64 LOAD_FAST rate
        #   66 LOAD_CONST 1000
        #   68 BINARY_OP /
        #   72 PRECALL
        #   76 CALL
        #   86 PRECALL
        #   90 CALL
        #  100 POP_TOP
        #  102 LOAD_CONST None
        #  104 RETURN_VALUE
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR uploadRateLabel
        #  118 LOAD_METHOD setText
        #  140 LOAD_CONST '0.0 KB/s'
        #  142 PRECALL
        #  146 CALL
        #  156 POP_TOP
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR upload_timeout_timer
        #  170 LOAD_METHOD start
        #  192 LOAD_CONST 1000
        #  194 PRECALL
        #  198 CALL
        #  208 POP_TOP
        #  210 LOAD_CONST None
        #  212 RETURN_VALUE
        pass

    def upload_status_cb(self, filename, sent_bytes, total_bytes):
        self.uploadNameLabel.setText(filename)
        self.uploadProgress.setVisible(True)
        self.uploadProgress.setRange(0, total_bytes)
        self.uploadProgress.setValue(sent_bytes)
        self.upload_timeout_timer.stop()

    def upload_timeout_cb(self):
        self.uploadProgress.setVisible(False)
        self.uploadNameLabel.setText('Waiting for file to upload')

    def upload_manager_error(self):
        self.uploadNameLabel.setText('Error')
        msg = 'Error connecting. Check upload configuration.'
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), self.tr(msg))

    def closable_tabs_cb(self):
        new_value = self.actionClosableTabs.isChecked()
        self.tabWidget.setTabsClosable(new_value)
        self.preferences.closeable_tabs = new_value
        if new_value:
            tab_bar = self.tabWidget.tabBar()
            tab_bar.setTabButton(0, QtWidgets.QTabBar.ButtonPosition.LeftSide, None)
            tab_bar.setTabButton(0, QtWidgets.QTabBar.ButtonPosition.RightSide, None)
            return None

    def tab_close_requested(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST index
        #    4 LOAD_CONST 0
        #    6 COMPARE_OP <=
        #   12 POP_JUMP_FORWARD_IF_FALSE to 18
        #   14 LOAD_CONST None
        #   16 RETURN_VALUE
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR tab_widgets
        #   30 LOAD_FAST index
        #   32 LOAD_CONST 1
        #   34 BINARY_OP -
        #   38 BINARY_SUBSCR
        #   48 STORE_FAST widget
        #   50 LOAD_FAST widget
        #   52 LOAD_METHOD close_controller
        #   74 PRECALL
        #   78 CALL
        #   88 POP_TOP
        #   90 LOAD_CONST None
        #   92 RETURN_VALUE
        pass

    def tree_item_double_clicked(self, item, col):
        tab_widget = item.data(0, QtCore.Qt.ItemDataRole.UserRole)

    def mark_directory(self):
        output_dir = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr('Select Directory'), self.preferences.base_dir)
        if not output_dir:
            return None
        collected_files = None
        for root, _dirs, files in os.walk(output_dir):
            for name in files:
                if name.endswith('.apd'):
                    apd_filename = os.path.join(root, name)
                    collected_files.append(apd_filename)
                self.dispatcher.mark_for_upload(collected_files)
                return None

    def mark_files(self):
        file_filter = self.tr('Data Files (*.apd)')
        val = QtWidgets.QFileDialog.getOpenFileNames(self, self.tr('Select Files'), self.preferences.base_dir, file_filter)
        files = val[0]
        self.dispatcher.mark_for_upload(files)

    def next_tab(self):
        new_index = self.tabWidget.currentIndex() + 1
        if new_index >= self.tabWidget.count():
            new_index = 1
        self.tabWidget.setCurrentIndex(new_index)

    def prev_tab(self):
        new_index = self.tabWidget.currentIndex() - 1
        if new_index < 1:
            new_index = self.tabWidget.count() - 1
        self.tabWidget.setCurrentIndex(new_index)

    def collapsed_set(self, collapsed):
        self.collapsed = collapsed
        self.preferences.collapsed = collapsed
        for tab_widget in self.tab_widgets:
            tab_widget.set_collapsed(collapsed)
            return None

    def current_tab_changed_cb(self, index):
        if index == -1 or index == 0:
            new_tab = None
        else:
            new_tab = self.tab_widgets[index - 1]
        if self.shown_tab == new_tab:
            return None

    def rf_power_changed_cb(self, enabled, total):
        disabled = max(0, total - enabled)
        enable_text = self.tr('Enable RF Power ({})').format(disabled)
        self.actionEnableRFPower.setText(enable_text)
        self.actionEnableRFPower.setEnabled(disabled > 0)
        disable_text = self.tr('Disable RF Power ({})').format(enabled)
        self.actionDisableRFPower.setText(disable_text)
        self.actionDisableRFPower.setEnabled(enabled > 0)

    def find_tcp_devices(self, *, initial_devices):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + TCPScanDialog
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR dispatcher
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR preferences
        #   38 LOAD_FAST initial_devices
        #   40 LOAD_FAST self
        #   42 PRECALL
        #   46 CALL
        #   56 STORE_FAST dialog
        #   58 NOP
        #   60 LOAD_FAST dialog
        #   62 LOAD_METHOD exec
        #   84 PRECALL
        #   88 CALL
        #   98 STORE_FAST ret
        #  100 LOAD_FAST ret
        #  102 LOAD_CONST 0
        #  104 COMPARE_OP ==
        #  110 POP_JUMP_FORWARD_IF_FALSE to 158
        #  112 NOP
        #  114 LOAD_FAST dialog
        #  116 LOAD_METHOD deleteLater
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        #  158 LOAD_FAST dialog
        #  160 LOAD_METHOD get_selected_devices
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST devices
        #  198 LOAD_FAST dialog
        #  200 LOAD_METHOD deleteLater
        #  222 PRECALL
        #  226 CALL
        #  236 POP_TOP
        #  238 JUMP_FORWARD to 290
        #  240 PUSH_EXC_INFO
        #  242 LOAD_FAST dialog
        #  244 LOAD_METHOD deleteLater
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 RERAISE
        #  284 COPY
        #  286 POP_EXCEPT
        #  288 RERAISE
        #  290 LOAD_FAST devices
        #  292 GET_ITER
        #  294 FOR_ITER to 352
        #  296 STORE_FAST device
        #  298 LOAD_FAST self
        #  300 LOAD_ATTR dispatcher
        #  310 LOAD_METHOD create_tcp_proxy_from_device
        #  332 LOAD_FAST device
        #  334 PRECALL
        #  338 CALL
        #  348 POP_TOP
        #  350 JUMP_BACKWARD to 294
        #  352 LOAD_CONST None
        #  354 RETURN_VALUE
        pass

    def connect_tcp_device_error(self):
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), self.tr('Could not connect to device!'))

    def connect_tcp_device(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + TCPConnectDialog
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
        #  134 LOAD_METHOD get_results
        #  156 PRECALL
        #  160 CALL
        #  170 STORE_FAST results
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
        #  264 LOAD_FAST self
        #  266 LOAD_ATTR dispatcher
        #  276 LOAD_METHOD create_manual_tcp_proxy
        #  298 LOAD_FAST results
        #  300 LOAD_CONST 'hostname'
        #  302 BINARY_SUBSCR
        #  312 LOAD_FAST results
        #  314 LOAD_CONST 'port'
        #  316 BINARY_SUBSCR
        #  326 LOAD_CONST 1000
        #  328 LOAD_FAST results
        #  330 LOAD_CONST 'serial_number'
        #  332 BINARY_SUBSCR
        #  342 LOAD_FAST self
        #  344 LOAD_ATTR connect_tcp_device_error
        #  354 KW_NAMES
        #  356 PRECALL
        #  360 CALL
        #  370 POP_TOP
        #  372 LOAD_CONST None
        #  374 RETURN_VALUE
        pass

    def initial_devices_connected_cb(self, tcp_scanned, tcp_devices):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR tab_widgets
        #   14 POP_JUMP_FORWARD_IF_FALSE to 84
        #   16 LOAD_FAST self
        #   18 LOAD_METHOD show_tab
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR tab_widgets
        #   52 LOAD_CONST 0
        #   54 BINARY_SUBSCR
        #   64 PRECALL
        #   68 CALL
        #   78 POP_TOP
        #   80 LOAD_CONST None
        #   82 RETURN_VALUE
        #   84 LOAD_FAST tcp_scanned
        #   86 POP_JUMP_FORWARD_IF_TRUE to 126
        #   88 LOAD_GLOBAL NULL + asphodel
        #  100 LOAD_ATTR find_tcp_devices
        #  110 PRECALL
        #  114 CALL
        #  124 STORE_FAST tcp_devices
        #  126 LOAD_FAST tcp_devices
        #  128 POP_JUMP_FORWARD_IF_FALSE to 178
        #  130 LOAD_FAST self
        #  132 LOAD_METHOD find_tcp_devices
        #  154 LOAD_FAST tcp_devices
        #  156 KW_NAMES
        #  158 PRECALL
        #  162 CALL
        #  172 POP_TOP
        #  174 LOAD_CONST None
        #  176 RETURN_VALUE
        #  178 LOAD_CONST None
        #  180 RETURN_VALUE
        pass

    def upload_manager_changed_cb(self, upload_manager):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST upload_manager
        #    4 POP_JUMP_FORWARD_IF_FALSE to 456
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR uploadRateLabel
        #   18 LOAD_METHOD setVisible
        #   40 LOAD_CONST True
        #   42 PRECALL
        #   46 CALL
        #   56 POP_TOP
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR uploadProgress
        #   70 LOAD_METHOD setVisible
        #   92 LOAD_CONST False
        #   94 PRECALL
        #   98 CALL
        #  108 POP_TOP
        #  110 LOAD_FAST self
        #  112 LOAD_ATTR uploadNameLabel
        #  122 LOAD_METHOD setVisible
        #  144 LOAD_CONST True
        #  146 PRECALL
        #  150 CALL
        #  160 POP_TOP
        #  162 LOAD_FAST self
        #  164 LOAD_ATTR uploadRateLabel
        #  174 LOAD_METHOD setText
        #  196 LOAD_CONST '0.0 kB/s'
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR uploadNameLabel
        #  226 LOAD_METHOD setText
        #  248 LOAD_CONST 'Waiting for file to upload'
        #  250 PRECALL
        #  254 CALL
        #  264 POP_TOP
        #  266 LOAD_FAST upload_manager
        #  268 LOAD_ATTR rate_status
        #  278 LOAD_METHOD connect
        #  300 LOAD_FAST self
        #  302 LOAD_ATTR rate_status_cb
        #  312 PRECALL
        #  316 CALL
        #  326 POP_TOP
        #  328 LOAD_FAST upload_manager
        #  330 LOAD_ATTR upload_status
        #  340 LOAD_METHOD connect
        #  362 LOAD_FAST self
        #  364 LOAD_ATTR upload_status_cb
        #  374 PRECALL
        #  378 CALL
        #  388 POP_TOP
        #  390 LOAD_FAST upload_manager
        #  392 LOAD_ATTR error
        #  402 LOAD_METHOD connect
        #  424 LOAD_FAST self
        #  426 LOAD_ATTR upload_manager_error
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_CONST None
        #  454 RETURN_VALUE
        #  456 LOAD_FAST self
        #  458 LOAD_ATTR uploadRateLabel
        #  468 LOAD_METHOD setVisible
        #  490 LOAD_CONST False
        #  492 PRECALL
        #  496 CALL
        #  506 POP_TOP
        #  508 LOAD_FAST self
        #  510 LOAD_ATTR uploadProgress
        #  520 LOAD_METHOD setVisible
        #  542 LOAD_CONST False
        #  544 PRECALL
        #  548 CALL
        #  558 POP_TOP
        #  560 LOAD_FAST self
        #  562 LOAD_ATTR uploadNameLabel
        # ... bytecode truncated ...
        pass

    def schedule_error_cb(self, error):
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), error)

    def schedule_warning_cb(self, warning):
        QtWidgets.QMessageBox.warning(self, self.tr('Warning'), warning)

    def reload_schedule_cb(self):
        self.schedule_reader.reload()

    def active_triggers_changed(self, active_triggers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST active_triggers
        #    4 POP_JUMP_FORWARD_IF_FALSE to 286
        #    6 LOAD_FAST self
        #    8 LOAD_METHOD tr
        #   30 LOAD_CONST 'Active triggers: {}'
        #   32 PRECALL
        #   36 CALL
        #   46 STORE_FAST active_trigger_str
        #   48 LOAD_FAST active_trigger_str
        #   50 LOAD_METHOD format
        #   72 LOAD_CONST ', '
        #   74 LOAD_METHOD join
        #   96 LOAD_GLOBAL NULL + sorted
        #  108 LOAD_FAST active_triggers
        #  110 LOAD_GLOBAL str
        #  122 LOAD_ATTR casefold
        #  132 KW_NAMES
        #  134 PRECALL
        #  138 CALL
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 STORE_FAST s
        #  178 LOAD_FAST self
        #  180 LOAD_ATTR activeTriggerLabel
        #  190 LOAD_METHOD setText
        #  212 LOAD_FAST s
        #  214 PRECALL
        #  218 CALL
        #  228 POP_TOP
        #  230 LOAD_FAST self
        #  232 LOAD_ATTR activeTriggerLabel
        #  242 LOAD_METHOD setVisible
        #  264 LOAD_CONST True
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_CONST None
        #  284 RETURN_VALUE
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR activeTriggerLabel
        #  298 LOAD_METHOD setVisible
        #  320 LOAD_CONST False
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 LOAD_CONST None
        #  340 RETURN_VALUE
        pass
