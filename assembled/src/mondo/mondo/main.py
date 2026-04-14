# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

import importlib
import logging
import os
import subprocess
import sys
import tempfile
import threading
from typing import Callable, Concatenate, Optional, ParamSpec
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from hyperborea.dark_mode import set_style
import hyperborea.download as hyperborea
from hyperborea.preferences import read_bool_setting
from .ui.ui_main import Ui_MondoMainWindow
from .about import AboutDialog
from .analysis import csv, file, psd, spectrogram, time
from .preferences import PreferencesDialog
logger = logging.getLogger(__name__)
P = ParamSpec('P')

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class MondoMainWindow(Ui_MondoMainWindow, QtWidgets.QMainWindow):

    find_update_finished = QtCore.Signal(object)

    update_download_finished = QtCore.Signal(object)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.update_progress_lock = threading.Lock()
        self.settings = QtCore.QSettings()
        self.update_style()
        self.setupUi(self)
        self.extra_ui_setup()
        self.setup_callbacks()
        self.setup_update_actions()

    def extra_ui_setup(self):
        app_name = QtWidgets.QApplication.applicationName()
        is_frozen = getattr(sys, 'frozen', False)
        if is_frozen:
            version = QtWidgets.QApplication.applicationVersion()
            title = self.tr('{} ({})').format(app_name, version)
        else:
            title = self.tr('{} (dev)').format(app_name)
        self.setWindowTitle(title)
        self.update_progress = QtWidgets.QProgressDialog('', '', 0, 100)
        self.update_progress.setLabelText(self.tr(''))
        self.update_progress.setWindowTitle(self.tr('Check for Update'))
        self.update_progress.setCancelButton(None)
        self.update_progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        self.update_progress.setMinimumDuration(0)
        self.update_progress.setAutoReset(False)
        self.update_progress.reset()

    def setup_callbacks(self):
        self.timeButton.clicked.connect(self.time_analysis)
        self.synchronousTimeButton.clicked.connect(self.synchronous_time_analysis)
        self.overlaidTimeButton.clicked.connect(self.overlaid_time_analysis)
        self.spectrogramButton.clicked.connect(self.spectrogram_analysis)
        self.psdButton.clicked.connect(self.psd_analysis)
        self.singleChannelPsdButton.clicked.connect(self.single_channel_psd_analysis)
        self.singleSlicePsdButton.clicked.connect(self.single_slice_psd_analysis)
        self.overlaidPsdButton.clicked.connect(self.overlaid_psd_analysis)
        self.csvButton.clicked.connect(self.csv_export)
        self.csvDownsampledButton.clicked.connect(self.csv_downsampled_export)
        self.fileInformationButton.clicked.connect(self.file_information)
        self.viewSettingsButton.clicked.connect(self.view_settings)
        self.rawExportButton.clicked.connect(self.raw_export)
        self.splitFileButton.clicked.connect(self.split_file)
        self.actionPreferences.triggered.connect(self.show_preferences)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAboutLibraries.triggered.connect(self.show_about_libraries)
        self.actionShowLogs.triggered.connect(self.show_log_dir)
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

    def setup_update_actions(self):
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
        #   46 LOAD_CONST False
        #   48 STORE_FAST valid_info
        #   50 LOAD_FAST is_frozen
        #   52 EXTENDED_ARG
        #   54 POP_JUMP_FORWARD_IF_FALSE to 604
        #   56 LOAD_GLOBAL os
        #   68 LOAD_ATTR path
        #   78 LOAD_METHOD dirname
        #  100 LOAD_GLOBAL sys
        #  112 LOAD_ATTR executable
        #  122 PRECALL
        #  126 CALL
        #  136 STORE_FAST main_dir
        #  138 LOAD_GLOBAL os
        #  150 LOAD_ATTR path
        #  160 LOAD_METHOD join
        #  182 LOAD_FAST main_dir
        #  184 LOAD_CONST 'build_info.txt'
        #  186 PRECALL
        #  190 CALL
        #  200 STORE_FAST build_info_filename
        #  202 NOP
        #  204 LOAD_GLOBAL NULL + open
        #  216 LOAD_FAST build_info_filename
        #  218 LOAD_CONST 'r'
        #  220 LOAD_CONST 'utf-8'
        #  222 KW_NAMES
        #  224 PRECALL
        #  228 CALL
        #  238 BEFORE_WITH
        #  240 STORE_FAST f
        #  242 LOAD_FAST f
        #  244 LOAD_METHOD readlines
        #  266 PRECALL
        #  270 CALL
        #  280 STORE_FAST lines
        #  282 LOAD_FAST lines
        #  284 LOAD_CONST 0
        #  286 BINARY_SUBSCR
        #  296 LOAD_METHOD strip
        #  318 PRECALL
        #  322 CALL
        #  332 LOAD_FAST self
        #  334 STORE_ATTR branch_name
        #  344 LOAD_FAST lines
        #  346 LOAD_CONST 1
        #  348 BINARY_SUBSCR
        #  358 LOAD_METHOD strip
        #  380 PRECALL
        #  384 CALL
        #  394 LOAD_FAST self
        #  396 STORE_ATTR commit_hash
        #  406 LOAD_FAST lines
        #  408 LOAD_CONST 2
        #  410 BINARY_SUBSCR
        #  420 LOAD_METHOD strip
        #  442 PRECALL
        #  446 CALL
        #  456 LOAD_FAST self
        #  458 STORE_ATTR build_key
        #  468 LOAD_CONST True
        #  470 STORE_FAST valid_info
        #  472 LOAD_CONST None
        #  474 LOAD_CONST None
        #  476 LOAD_CONST None
        #  478 PRECALL
        #  482 CALL
        #  492 POP_TOP
        #  494 JUMP_FORWARD to 518
        #  496 PUSH_EXC_INFO
        #  498 WITH_EXCEPT_START
        #  500 POP_JUMP_FORWARD_IF_TRUE to 510
        # ... bytecode truncated ...
        pass

    def find_update(self, branch, commit, fallback_branch):
        self.update_fallback_branch = fallback_branch
        self.update_progress.setMinimum(0)
        self.update_progress.setMaximum(0)
        self.update_progress.setValue(0)
        self.update_progress.setLabelText(self.tr('Checking for update...'))
        self.update_progress.forceShow()
        self.software_finder.find_software('mondo', self.build_key, branch, commit)

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
        if self.branch_name in ('master', 'develop'):
            fallback = None
        else:
            fallback = 'develop'
        self.find_update(branch = self.branch_name, fallback_branch = fallback)

    def update_specific_branch(self):
        self.update_progress.setMinimum(0)
        self.update_progress.setMaximum(0)
        self.update_progress.setValue(0)
        self.update_progress.setLabelText(self.tr('Collecting branches...'))
        self.update_progress.forceShow()
        self.ref_finder.get_software_refs('mondo')

    def ref_finder_error(self):
        self.ref_finder_completed([])

    def ref_finder_completed(self, refs):
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
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR branch_name
        #   64 STORE_FAST default_branch
        #   66 LOAD_FAST default_branch
        #   68 BUILD_LIST
        #   70 STORE_FAST branch_choices
        #   72 LOAD_FAST default_branch
        #   74 LOAD_CONST 'master'
        #   76 COMPARE_OP !=
        #   82 POP_JUMP_FORWARD_IF_FALSE to 126
        #   84 LOAD_FAST branch_choices
        #   86 LOAD_METHOD append
        #  108 LOAD_CONST 'master'
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST default_branch
        #  128 LOAD_CONST 'develop'
        #  130 COMPARE_OP !=
        #  136 POP_JUMP_FORWARD_IF_FALSE to 180
        #  138 LOAD_FAST branch_choices
        #  140 LOAD_METHOD append
        #  162 LOAD_CONST 'develop'
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 BUILD_LIST
        #  182 STORE_FAST ref_names
        #  184 LOAD_FAST refs
        #  186 GET_ITER
        #  188 FOR_ITER to 292
        #  190 STORE_FAST ref
        #  192 LOAD_FAST ref
        #  194 LOAD_METHOD get
        #  216 LOAD_CONST 'name'
        #  218 LOAD_CONST None
        #  220 PRECALL
        #  224 CALL
        #  234 STORE_FAST ref_name
        #  236 LOAD_FAST ref_name
        #  238 POP_JUMP_FORWARD_IF_FALSE to 290
        #  240 LOAD_FAST ref_name
        #  242 LOAD_FAST branch_choices
        #  244 CONTAINS_OP
        #  246 POP_JUMP_FORWARD_IF_FALSE to 290
        #  248 LOAD_FAST ref_names
        #  250 LOAD_METHOD append
        #  272 LOAD_FAST ref_name
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 JUMP_BACKWARD to 188
        #  292 LOAD_FAST ref_names
        #  294 POP_JUMP_FORWARD_IF_FALSE to 340
        #  296 LOAD_FAST self
        #  298 LOAD_METHOD tr
        #  320 LOAD_CONST 'Branch:'
        #  322 PRECALL
        #  326 CALL
        #  336 STORE_FAST label
        #  338 JUMP_FORWARD to 382
        #  340 LOAD_FAST self
        #  342 LOAD_METHOD tr
        #  364 LOAD_CONST 'No list of branches!\nBranch:'
        #  366 PRECALL
        #  370 CALL
        #  380 STORE_FAST label
        #  382 LOAD_FAST branch_choices
        #  384 LOAD_METHOD extend
        #  406 LOAD_GLOBAL NULL + sorted
        #  418 LOAD_FAST ref_names
        #  420 LOAD_GLOBAL hyperborea
        #  432 LOAD_ATTR download
        # ... bytecode truncated ...
        pass

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

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec()

    def _get_version(self, library):
        try:
            lib = importlib.import_module(library)
            return lib.__version__
        except (AttributeError, ImportError):
            return 'ERROR'

    def show_about_libraries(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL vers
        #    2 RESUME
        #    4 BUILD_LIST
        #    6 LOAD_CONST ('hyperborea', 'matplotlib', 'numpy', 'PySide6', 'requests', 'scipy')
        #    8 LIST_EXTEND
        #   10 STORE_FAST libraries
        #   12 BUILD_MAP
        #   14 STORE_DEREF vers
        #   16 LOAD_FAST libraries
        #   18 GET_ITER
        #   20 FOR_ITER to 74
        #   22 STORE_FAST lib
        #   24 LOAD_FAST self
        #   26 LOAD_METHOD _get_version
        #   48 LOAD_FAST lib
        #   50 PRECALL
        #   54 CALL
        #   64 LOAD_DEREF vers
        #   66 LOAD_FAST lib
        #   68 STORE_SUBSCR
        #   72 JUMP_BACKWARD to 20
        #   74 LOAD_FAST self
        #   76 LOAD_METHOD _get_version
        #   98 LOAD_CONST 'asphodel'
        #  100 PRECALL
        #  104 CALL
        #  114 LOAD_DEREF vers
        #  116 LOAD_CONST 'asphodel_py'
        #  118 STORE_SUBSCR
        #  122 LOAD_GLOBAL asphodel
        #  134 LOAD_ATTR build_info
        #  144 LOAD_DEREF vers
        #  146 LOAD_CONST 'asphodel'
        #  148 STORE_SUBSCR
        #  152 LOAD_GLOBAL sys
        #  164 LOAD_ATTR maxsize
        #  174 LOAD_CONST 4294967296
        #  176 COMPARE_OP >
        #  182 STORE_FAST is_64bit
        #  184 LOAD_FAST is_64bit
        #  186 POP_JUMP_FORWARD_IF_FALSE to 192
        #  188 LOAD_CONST '64 bit'
        #  190 JUMP_FORWARD to 194
        #  192 LOAD_CONST '32 bit'
        #  194 STORE_FAST bit_str
        #  196 LOAD_CONST '.'
        #  198 LOAD_METHOD join
        #  220 LOAD_GLOBAL NULL + map
        #  232 LOAD_GLOBAL str
        #  244 LOAD_GLOBAL sys
        #  256 LOAD_ATTR version_info
        #  266 LOAD_CONST None
        #  268 LOAD_CONST 3
        #  270 BUILD_SLICE
        #  272 BINARY_SUBSCR
        #  282 PRECALL
        #  286 CALL
        #  296 PRECALL
        #  300 CALL
        #  310 STORE_FAST python_ver
        #  312 LOAD_CONST '{} ({} {})'
        #  314 LOAD_METHOD format
        #  336 LOAD_FAST python_ver
        #  338 LOAD_GLOBAL sys
        #  350 LOAD_ATTR platform
        #  360 LOAD_FAST bit_str
        #  362 PRECALL
        #  366 CALL
        #  376 STORE_FAST python_str
        #  378 LOAD_FAST python_str
        #  380 LOAD_DEREF vers
        #  382 LOAD_CONST 'python'
        #  384 STORE_SUBSCR
        #  388 LOAD_CONST '\n'
        #  390 LOAD_METHOD join
        #  412 LOAD_CLOSURE vers
        #  414 BUILD_TUPLE
        #  416 LOAD_CONST <code object <genexpr> at 0x105abfa50, file "mondo\main.py", line 374>
        #  418 MAKE_FUNCTION closure
        #  420 LOAD_GLOBAL NULL + sorted
        # ... bytecode truncated ...
        pass

    def show_log_dir(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL os
        #   14 LOAD_ATTR path
        #   24 LOAD_METHOD abspath
        #   46 LOAD_GLOBAL QtCore
        #   58 LOAD_ATTR QStandardPaths
        #   68 LOAD_METHOD writableLocation
        #   90 LOAD_GLOBAL QtCore
        #  102 LOAD_ATTR QStandardPaths
        #  112 LOAD_ATTR StandardLocation
        #  122 LOAD_ATTR AppLocalDataLocation
        #  132 PRECALL
        #  136 CALL
        #  146 PRECALL
        #  150 CALL
        #  160 STORE_FAST logdir
        #  162 LOAD_GLOBAL os
        #  174 LOAD_ATTR path
        #  184 LOAD_METHOD join
        #  206 LOAD_FAST logdir
        #  208 LOAD_CONST 'main.log'
        #  210 PRECALL
        #  214 CALL
        #  224 STORE_FAST logfile
        #  226 LOAD_GLOBAL sys
        #  238 LOAD_ATTR platform
        #  248 LOAD_CONST 'win32'
        #  250 COMPARE_OP ==
        #  256 POP_JUMP_FORWARD_IF_FALSE to 308
        #  258 LOAD_GLOBAL NULL + subprocess
        #  270 LOAD_ATTR Popen
        #  280 LOAD_CONST 'explorer'
        #  282 LOAD_CONST '/select,'
        #  284 LOAD_FAST logfile
        #  286 BUILD_LIST
        #  288 PRECALL
        #  292 CALL
        #  302 POP_TOP
        #  304 LOAD_CONST None
        #  306 RETURN_VALUE
        #  308 LOAD_GLOBAL sys
        #  320 LOAD_ATTR platform
        #  330 LOAD_CONST 'darwin'
        #  332 COMPARE_OP ==
        #  338 POP_JUMP_FORWARD_IF_FALSE to 414
        #  340 LOAD_CONST 'osascript'
        #  342 LOAD_CONST '-e'
        #  344 LOAD_CONST 'tell application "Finder"'
        #  346 LOAD_CONST '-e'
        #  348 LOAD_CONST 'activate'
        #  350 LOAD_CONST '-e'
        #  352 LOAD_CONST 'select POSIX file "'
        #  354 LOAD_FAST logfile
        #  356 FORMAT_VALUE
        #  358 LOAD_CONST '"'
        #  360 BUILD_STRING
        #  362 LOAD_CONST '-e'
        #  364 LOAD_CONST 'end tell'
        #  366 BUILD_LIST
        #  368 STORE_FAST args
        #  370 LOAD_GLOBAL NULL + subprocess
        #  382 LOAD_ATTR Popen
        #  392 LOAD_FAST args
        #  394 PRECALL
        #  398 CALL
        #  408 POP_TOP
        #  410 LOAD_CONST None
        #  412 RETURN_VALUE
        #  414 LOAD_GLOBAL QtCore
        #  426 LOAD_ATTR QUrl
        #  436 LOAD_METHOD fromLocalFile
        #  458 LOAD_FAST logdir
        #  460 PRECALL
        #  464 CALL
        #  474 STORE_FAST url
        #  476 LOAD_GLOBAL QtGui
        #  488 LOAD_ATTR QDesktopServices
        #  498 LOAD_METHOD openUrl
        #  520 LOAD_FAST url
        #  522 PRECALL
        # ... bytecode truncated ...
        pass

    def do_analysis(self, analysis, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 PUSH_NULL
        #    6 LOAD_FAST analysis
        #    8 LOAD_FAST self
        #   10 BUILD_LIST
        #   12 LOAD_FAST args
        #   14 LIST_EXTEND
        #   16 LIST_TO_TUPLE
        #   18 BUILD_MAP
        #   20 LOAD_FAST kwargs
        #   22 DICT_MERGE
        #   24 CALL_FUNCTION_EX
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        #   32 PUSH_EXC_INFO
        #   34 LOAD_GLOBAL Exception
        #   46 CHECK_EXC_MATCH
        #   48 POP_JUMP_FORWARD_IF_FALSE to 176
        #   50 POP_TOP
        #   52 LOAD_GLOBAL logger
        #   64 LOAD_METHOD exception
        #   86 LOAD_CONST 'Uncaught exception'
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_GLOBAL QtWidgets
        #  116 LOAD_ATTR QMessageBox
        #  126 LOAD_METHOD critical
        #  148 LOAD_FAST self
        #  150 LOAD_CONST 'Error'
        #  152 LOAD_CONST 'Uncaught exception. See log for details.'
        #  154 PRECALL
        #  158 CALL
        #  168 POP_TOP
        #  170 POP_EXCEPT
        #  172 LOAD_CONST None
        #  174 RETURN_VALUE
        #  176 RERAISE
        #  178 COPY
        #  180 POP_EXCEPT
        #  182 RERAISE
        pass

    def time_analysis(self):
        self.do_analysis(time.time_analysis)

    def synchronous_time_analysis(self):
        self.do_analysis(time.synchronous_time_analysis)

    def overlaid_time_analysis(self):
        self.do_analysis(time.overlaid_time_analysis)

    def spectrogram_analysis(self):
        self.do_analysis(spectrogram.spectrogram_analysis)

    def psd_analysis(self):
        self.do_analysis(psd.psd_analysis)

    def single_channel_psd_analysis(self):
        self.do_analysis(psd.single_channel_psd_analysis)

    def single_slice_psd_analysis(self):
        self.do_analysis(psd.single_slice_psd_analysis)

    def overlaid_psd_analysis(self):
        self.do_analysis(psd.overlaid_psd_analysis)

    def csv_export(self):
        self.do_analysis(csv.csv_export)

    def csv_downsampled_export(self):
        self.do_analysis(csv.csv_export, downsample = True)

    def file_information(self):
        self.do_analysis(file.file_information)

    def view_settings(self):
        self.do_analysis(file.view_settings)

    def raw_export(self):
        self.do_analysis(file.raw_export)

    def split_file(self):
        self.do_analysis(file.split_file)

    def show_preferences(self):
        dialog = PreferencesDialog(self)
        dialog.exec()
        self.update_style()

    def update_style(self):
        dark_mode = read_bool_setting(self.settings, 'DarkMode', True)
        set_style(QtWidgets.QApplication.instance(), dark_mode)
