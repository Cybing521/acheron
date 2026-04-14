# Source Generated with Decompyle++
# File: calibration.pyc (Python 3.11)

from dataclasses import dataclass
import functools
import logging
import math
import platform
from typing import Any, Callable, cast, Optional, TYPE_CHECKING
import weakref
from weakref import ReferenceType
import numpy
from numpy.typing import NDArray
import pyqtgraph
from PySide6 import QtCore, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from hyperborea.unit_formatter_spinbox import UnitFormatterDoubleSpinBox
from hyperborea.unit_selection_dialog import UnitSelectionDialog
from ..device_logging import DeviceLoggerAdapter
from ..core.calibration import get_channel_setting_values, update_nvm
from ..connectivity.event_upload import EventUploader
from .ui.ui_calibration_panel import Ui_CalibrationPanel
from .ui.ui_calibration_channel import Ui_CalibrationChannel
if TYPE_CHECKING:
    from .device_tab import DeviceTab
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: CalibrationConnection = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class CalibrationConnection:

    name: str

    calibration_info: asphodel.ChannelCalibration

    channel_id: int

    device_tab: 'ReferenceType[DeviceTab]'

    unit_formatter: asphodel.AsphodelNativeUnitFormatter

class CalibrationChannel(Ui_CalibrationChannel, QtWidgets.QWidget):

    value_changed = QtCore.Signal()

    def __init__(self, cal, unit_selection_dialog, cal_panel):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST cal_panel
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST cal
        #   72 LOAD_FAST self
        #   74 STORE_ATTR cal
        #   84 LOAD_FAST unit_selection_dialog
        #   86 LOAD_FAST self
        #   88 STORE_ATTR unit_selection_dialog
        #   98 LOAD_FAST cal
        #  100 LOAD_ATTR unit_formatter
        #  110 STORE_FAST unit_formatter
        #  112 LOAD_GLOBAL asphodel
        #  124 LOAD_ATTR nativelib
        #  134 LOAD_METHOD create_custom_unit_formatter
        #  156 LOAD_FAST unit_formatter
        #  158 LOAD_ATTR conversion_scale
        #  168 LOAD_CONST 0.0
        #  170 LOAD_CONST 0.0
        #  172 LOAD_FAST unit_formatter
        #  174 LOAD_ATTR unit_ascii
        #  184 LOAD_FAST unit_formatter
        #  186 LOAD_ATTR unit_utf8
        #  196 LOAD_FAST unit_formatter
        #  198 LOAD_ATTR unit_html
        #  208 PRECALL
        #  212 CALL
        #  222 LOAD_FAST self
        #  224 STORE_ATTR rms_formatter
        #  234 LOAD_GLOBAL asphodel
        #  246 LOAD_ATTR nativelib
        #  256 LOAD_METHOD create_custom_unit_formatter
        #  278 LOAD_FAST unit_formatter
        #  280 LOAD_ATTR conversion_scale
        #  290 LOAD_FAST unit_formatter
        #  292 LOAD_ATTR conversion_offset
        #  302 LOAD_CONST 0.0
        #  304 LOAD_FAST unit_formatter
        #  306 LOAD_ATTR unit_ascii
        #  316 LOAD_FAST unit_formatter
        #  318 LOAD_ATTR unit_utf8
        #  328 LOAD_FAST unit_formatter
        #  330 LOAD_ATTR unit_html
        #  340 PRECALL
        #  344 CALL
        #  354 LOAD_FAST self
        #  356 STORE_ATTR dc_formatter
        #  366 LOAD_CONST None
        #  368 LOAD_FAST self
        #  370 STORE_ATTR unit_info
        #  380 LOAD_CONST None
        #  382 LOAD_FAST self
        #  384 STORE_ATTR scale_offset
        #  394 LOAD_GLOBAL NULL + numpy
        #  406 LOAD_ATTR zeros
        #  416 LOAD_CONST 0
        #  418 PRECALL
        #  422 CALL
        #  432 LOAD_FAST self
        #  434 STORE_ATTR linear_x
        #  444 LOAD_GLOBAL NULL + numpy
        #  456 LOAD_ATTR zeros
        #  466 LOAD_CONST 0
        #  468 PRECALL
        #  472 CALL
        #  482 LOAD_FAST self
        #  484 STORE_ATTR linear_y
        #  494 LOAD_FAST self
        #  496 LOAD_METHOD setupUi
        #  518 LOAD_FAST self
        #  520 PRECALL
        #  524 CALL
        #  534 POP_TOP
        # ... bytecode truncated ...
        pass

    def extra_ui_setup(self):
        self.calibrationEnabled.toggled.connect(self.update_all)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.update_all)
        self.selectUnit.clicked.connect(self.select_unit)
        self.unit.setText('')
        self.acCapture.clicked.connect(self.ac_capture)
        self.linearCapture.clicked.connect(self.linear_capture)
        self.plotButton.clicked.connect(self.plot_linear)
        self.capturedMagnitude.set_unit_formatter(self.rms_formatter)
        self.capturedOffset.set_unit_formatter(self.dc_formatter)
        self.capturedMagnitude.setMinimum(-(math.inf))
        self.capturedMagnitude.setMaximum(math.inf)
        self.capturedOffset.setMinimum(-(math.inf))
        self.capturedOffset.setMaximum(math.inf)
        self.actualMagnitude.setMinimum(-(math.inf))
        self.actualMagnitude.setMaximum(math.inf)
        self.actualOffset.setMinimum(-(math.inf))
        self.actualOffset.setMaximum(math.inf)
        self.capturedMagnitude.valueChanged.connect(self.update_scale_offset)
        self.capturedOffset.valueChanged.connect(self.update_scale_offset)
        self.actualMagnitude.valueChanged.connect(self.update_scale_offset)
        self.actualOffset.valueChanged.connect(self.update_scale_offset)
        header = self.linearTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def setup_plot(self):
        self.plot = cast(pyqtgraph.PlotItem, self.graphicsView.getPlotItem())
        self.plot.showGrid(x = True, y = True)
        self.plot.setLabel('bottom', 'Time (s)')
        self.plot.setTitle('Linear Fit')
        self.plot.setLabel('bottom', self.dc_formatter.unit_html)
        self.points_curve = self.plot.plot(pen = None, symbol = 'o', symbolBrush = (255, 0, 0), symbolPen = 'w', name = 'Data')
        self.regression_curve = self.plot.plot(pen = (0, 0, 255), name = 'Fit')
        self.text_items = []

    def select_unit(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR unit_selection_dialog
        #   14 STORE_FAST dialog
        #   16 LOAD_FAST dialog
        #   18 LOAD_METHOD exec
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST ret
        #   56 LOAD_FAST ret
        #   58 LOAD_CONST 0
        #   60 COMPARE_OP ==
        #   66 POP_JUMP_FORWARD_IF_FALSE to 72
        #   68 LOAD_CONST None
        #   70 RETURN_VALUE
        #   72 LOAD_FAST dialog
        #   74 LOAD_METHOD get_unit_info
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST unit_info
        #  112 LOAD_FAST unit_info
        #  114 POP_JUMP_FORWARD_IF_TRUE to 120
        #  116 LOAD_CONST None
        #  118 RETURN_VALUE
        #  120 LOAD_FAST unit_info
        #  122 LOAD_FAST self
        #  124 STORE_ATTR unit_info
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR unit_info
        #  146 LOAD_CONST 1
        #  148 BINARY_SUBSCR
        #  158 STORE_FAST unit_formatter
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR unit
        #  172 LOAD_METHOD setText
        #  194 LOAD_FAST unit_formatter
        #  196 LOAD_ATTR unit_utf8
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_GLOBAL asphodel
        #  234 LOAD_ATTR nativelib
        #  244 LOAD_METHOD create_custom_unit_formatter
        #  266 LOAD_FAST unit_formatter
        #  268 LOAD_ATTR conversion_scale
        #  278 LOAD_CONST 0.0
        #  280 LOAD_CONST 0.0
        #  282 LOAD_FAST unit_formatter
        #  284 LOAD_ATTR unit_ascii
        #  294 LOAD_FAST unit_formatter
        #  296 LOAD_ATTR unit_utf8
        #  306 LOAD_FAST unit_formatter
        #  308 LOAD_ATTR unit_html
        #  318 PRECALL
        #  322 CALL
        #  332 STORE_FAST rms_formatter
        #  334 LOAD_FAST self
        #  336 LOAD_ATTR actualMagnitude
        #  346 LOAD_METHOD set_unit_formatter
        #  368 LOAD_FAST rms_formatter
        #  370 PRECALL
        #  374 CALL
        #  384 POP_TOP
        #  386 LOAD_FAST self
        #  388 LOAD_ATTR actualOffset
        #  398 LOAD_METHOD set_unit_formatter
        #  420 LOAD_FAST unit_formatter
        #  422 PRECALL
        #  426 CALL
        #  436 POP_TOP
        #  438 LOAD_FAST self
        #  440 LOAD_ATTR linearTable
        #  450 LOAD_METHOD rowCount
        #  472 PRECALL
        #  476 CALL
        #  486 STORE_FAST row_count
        #  488 LOAD_GLOBAL NULL + range
        #  500 LOAD_FAST row_count
        #  502 PRECALL
        #  506 CALL
        # ... bytecode truncated ...
        pass

    def update_enabled(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calibrationEnabled
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST enabled
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR unitLabel
        #   64 LOAD_METHOD setEnabled
        #   86 LOAD_FAST enabled
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR unit
        #  116 LOAD_METHOD setEnabled
        #  138 LOAD_FAST enabled
        #  140 PRECALL
        #  144 CALL
        #  154 POP_TOP
        #  156 LOAD_FAST self
        #  158 LOAD_ATTR selectUnit
        #  168 LOAD_METHOD setEnabled
        #  190 LOAD_FAST enabled
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 LOAD_FAST enabled
        #  210 POP_JUMP_FORWARD_IF_FALSE to 232
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR unit_info
        #  224 LOAD_CONST None
        #  226 IS_OP
        #  228 STORE_FAST unit_ready
        #  230 JUMP_FORWARD to 236
        #  232 LOAD_CONST False
        #  234 STORE_FAST unit_ready
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR linearPage
        #  248 LOAD_METHOD setEnabled
        #  270 LOAD_FAST unit_ready
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_FAST self
        #  290 LOAD_ATTR acPage
        #  300 LOAD_METHOD setEnabled
        #  322 LOAD_FAST unit_ready
        #  324 PRECALL
        #  328 CALL
        #  338 POP_TOP
        #  340 LOAD_FAST self
        #  342 LOAD_ATTR scaleLabel
        #  352 LOAD_METHOD setEnabled
        #  374 LOAD_FAST unit_ready
        #  376 PRECALL
        #  380 CALL
        #  390 POP_TOP
        #  392 LOAD_FAST self
        #  394 LOAD_ATTR scale
        #  404 LOAD_METHOD setEnabled
        #  426 LOAD_FAST unit_ready
        #  428 PRECALL
        #  432 CALL
        #  442 POP_TOP
        #  444 LOAD_FAST self
        #  446 LOAD_ATTR offsetLabel
        #  456 LOAD_METHOD setEnabled
        #  478 LOAD_FAST unit_ready
        #  480 PRECALL
        #  484 CALL
        #  494 POP_TOP
        #  496 LOAD_FAST self
        #  498 LOAD_ATTR offset
        #  508 LOAD_METHOD setEnabled
        #  530 LOAD_FAST unit_ready
        #  532 PRECALL
        #  536 CALL
        #  546 POP_TOP
        # ... bytecode truncated ...
        pass

    def update_all(self):
        self.update_enabled()
        self.update_scale_offset()

    def get_ac_scale_offset(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR capturedMagnitude
        #   16 LOAD_METHOD value
        #   38 PRECALL
        #   42 CALL
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR cal
        #   64 LOAD_ATTR calibration_info
        #   74 LOAD_ATTR scale
        #   84 BINARY_OP /
        #   88 STORE_FAST unscaled_captured_mag
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR capturedOffset
        #  102 LOAD_METHOD value
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR cal
        #  150 LOAD_ATTR calibration_info
        #  160 LOAD_ATTR offset
        #  170 BINARY_OP -
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR cal
        #  186 LOAD_ATTR calibration_info
        #  196 LOAD_ATTR scale
        #  206 BINARY_OP /
        #  210 STORE_FAST unscaled_captured_offset
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR actualMagnitude
        #  224 LOAD_METHOD value
        #  246 PRECALL
        #  250 CALL
        #  260 LOAD_FAST unscaled_captured_mag
        #  262 BINARY_OP /
        #  266 STORE_FAST scale
        #  268 LOAD_FAST scale
        #  270 LOAD_CONST 0
        #  272 COMPARE_OP ==
        #  278 POP_JUMP_FORWARD_IF_FALSE to 284
        #  280 LOAD_CONST None
        #  282 RETURN_VALUE
        #  284 LOAD_FAST self
        #  286 LOAD_ATTR actualOffset
        #  296 LOAD_METHOD value
        #  318 PRECALL
        #  322 CALL
        #  332 LOAD_FAST unscaled_captured_offset
        #  334 LOAD_FAST scale
        #  336 BINARY_OP *
        #  340 BINARY_OP -
        #  344 STORE_FAST offset
        #  346 LOAD_FAST scale
        #  348 LOAD_FAST offset
        #  350 BUILD_TUPLE
        #  352 RETURN_VALUE
        #  354 PUSH_EXC_INFO
        #  356 LOAD_GLOBAL ZeroDivisionError
        #  368 CHECK_EXC_MATCH
        #  370 POP_JUMP_FORWARD_IF_FALSE to 380
        #  372 POP_TOP
        #  374 POP_EXCEPT
        #  376 LOAD_CONST None
        #  378 RETURN_VALUE
        #  380 RERAISE
        #  382 COPY
        #  384 POP_EXCEPT
        #  386 RERAISE
        pass

    def get_linear_scale_offset(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR linearTable
        #   16 LOAD_METHOD rowCount
        #   38 PRECALL
        #   42 CALL
        #   52 STORE_FAST row_count
        #   54 LOAD_FAST row_count
        #   56 LOAD_CONST 2
        #   58 COMPARE_OP <
        #   64 POP_JUMP_FORWARD_IF_FALSE to 70
        #   66 LOAD_CONST None
        #   68 RETURN_VALUE
        #   70 LOAD_GLOBAL NULL + numpy
        #   82 LOAD_ATTR zeros
        #   92 LOAD_FAST row_count
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST x
        #  110 LOAD_GLOBAL NULL + numpy
        #  122 LOAD_ATTR zeros
        #  132 LOAD_FAST row_count
        #  134 PRECALL
        #  138 CALL
        #  148 STORE_FAST y
        #  150 LOAD_GLOBAL NULL + range
        #  162 LOAD_FAST row_count
        #  164 PRECALL
        #  168 CALL
        #  178 GET_ITER
        #  180 FOR_ITER to 538
        #  182 STORE_FAST row
        #  184 LOAD_GLOBAL NULL + cast
        #  196 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  208 LOAD_FAST self
        #  210 LOAD_ATTR linearTable
        #  220 LOAD_METHOD cellWidget
        #  242 LOAD_FAST row
        #  244 LOAD_CONST 0
        #  246 PRECALL
        #  250 CALL
        #  260 PRECALL
        #  264 CALL
        #  274 STORE_FAST captured
        #  276 LOAD_GLOBAL NULL + cast
        #  288 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  300 LOAD_FAST self
        #  302 LOAD_ATTR linearTable
        #  312 LOAD_METHOD cellWidget
        #  334 LOAD_FAST row
        #  336 LOAD_CONST 1
        #  338 PRECALL
        #  342 CALL
        #  352 PRECALL
        #  356 CALL
        #  366 STORE_FAST actual
        #  368 LOAD_FAST captured
        #  370 LOAD_METHOD value
        #  392 PRECALL
        #  396 CALL
        #  406 LOAD_FAST self
        #  408 LOAD_ATTR cal
        #  418 LOAD_ATTR calibration_info
        #  428 LOAD_ATTR offset
        #  438 BINARY_OP -
        #  442 LOAD_FAST self
        #  444 LOAD_ATTR cal
        #  454 LOAD_ATTR calibration_info
        #  464 LOAD_ATTR scale
        #  474 BINARY_OP /
        #  478 STORE_FAST unscaled
        #  480 LOAD_FAST unscaled
        #  482 LOAD_FAST x
        #  484 LOAD_FAST row
        #  486 STORE_SUBSCR
        #  490 LOAD_FAST actual
        #  492 LOAD_METHOD value
        #  514 PRECALL
        #  518 CALL
        # ... bytecode truncated ...
        pass

    def update_linear_plot(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR linearTable
        #   14 LOAD_METHOD rowCount
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST row_count
        #   52 LOAD_GLOBAL NULL + numpy
        #   64 LOAD_ATTR zeros
        #   74 LOAD_FAST row_count
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST x
        #   92 LOAD_GLOBAL NULL + numpy
        #  104 LOAD_ATTR zeros
        #  114 LOAD_FAST row_count
        #  116 PRECALL
        #  120 CALL
        #  130 STORE_FAST y
        #  132 LOAD_GLOBAL NULL + range
        #  144 LOAD_FAST row_count
        #  146 PRECALL
        #  150 CALL
        #  160 GET_ITER
        #  162 FOR_ITER to 444
        #  164 STORE_FAST row
        #  166 LOAD_GLOBAL NULL + cast
        #  178 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  190 LOAD_FAST self
        #  192 LOAD_ATTR linearTable
        #  202 LOAD_METHOD cellWidget
        #  224 LOAD_FAST row
        #  226 LOAD_CONST 0
        #  228 PRECALL
        #  232 CALL
        #  242 PRECALL
        #  246 CALL
        #  256 STORE_FAST captured
        #  258 LOAD_GLOBAL NULL + cast
        #  270 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  282 LOAD_FAST self
        #  284 LOAD_ATTR linearTable
        #  294 LOAD_METHOD cellWidget
        #  316 LOAD_FAST row
        #  318 LOAD_CONST 1
        #  320 PRECALL
        #  324 CALL
        #  334 PRECALL
        #  338 CALL
        #  348 STORE_FAST actual
        #  350 LOAD_FAST captured
        #  352 LOAD_METHOD value
        #  374 PRECALL
        #  378 CALL
        #  388 LOAD_FAST x
        #  390 LOAD_FAST row
        #  392 STORE_SUBSCR
        #  396 LOAD_FAST actual
        #  398 LOAD_METHOD value
        #  420 PRECALL
        #  424 CALL
        #  434 LOAD_FAST y
        #  436 LOAD_FAST row
        #  438 STORE_SUBSCR
        #  442 JUMP_BACKWARD to 162
        #  444 LOAD_FAST x
        #  446 LOAD_FAST self
        #  448 LOAD_ATTR dc_formatter
        #  458 LOAD_ATTR conversion_scale
        #  468 BINARY_OP *
        #  472 LOAD_FAST self
        #  474 LOAD_ATTR dc_formatter
        #  484 LOAD_ATTR conversion_offset
        #  494 BINARY_OP +
        #  498 STORE_FAST x
        #  500 LOAD_FAST self
        #  502 LOAD_ATTR unit_info
        #  512 POP_JUMP_FORWARD_IF_FALSE to 576
        #  514 LOAD_FAST self
        #  516 LOAD_ATTR unit_info
        # ... bytecode truncated ...
        pass

    def update_scale_offset(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR unit_info
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 32
        #   16 LOAD_CONST None
        #   18 LOAD_FAST self
        #   20 STORE_ATTR scale_offset
        #   30 JUMP_FORWARD to 232
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR tabWidget
        #   44 LOAD_METHOD currentIndex
        #   66 PRECALL
        #   70 CALL
        #   80 LOAD_CONST 0
        #   82 COMPARE_OP ==
        #   88 POP_JUMP_FORWARD_IF_FALSE to 182
        #   90 LOAD_FAST self
        #   92 LOAD_METHOD get_linear_scale_offset
        #  114 PRECALL
        #  118 CALL
        #  128 LOAD_FAST self
        #  130 STORE_ATTR scale_offset
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD update_linear_plot
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 JUMP_FORWARD to 232
        #  182 LOAD_FAST self
        #  184 LOAD_METHOD get_ac_scale_offset
        #  206 PRECALL
        #  210 CALL
        #  220 LOAD_FAST self
        #  222 STORE_ATTR scale_offset
        #  232 LOAD_FAST self
        #  234 LOAD_ATTR scale_offset
        #  244 POP_JUMP_FORWARD_IF_NOT_NONE to 404
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR scale
        #  258 LOAD_METHOD setText
        #  280 LOAD_CONST ''
        #  282 PRECALL
        #  286 CALL
        #  296 POP_TOP
        #  298 LOAD_FAST self
        #  300 LOAD_ATTR offset
        #  310 LOAD_METHOD setText
        #  332 LOAD_CONST ''
        #  334 PRECALL
        #  338 CALL
        #  348 POP_TOP
        #  350 LOAD_FAST self
        #  352 LOAD_ATTR plotButton
        #  362 LOAD_METHOD setEnabled
        #  384 LOAD_CONST False
        #  386 PRECALL
        #  390 CALL
        #  400 POP_TOP
        #  402 JUMP_FORWARD to 632
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR scale_offset
        #  416 UNPACK_SEQUENCE
        #  420 STORE_FAST scale
        #  422 STORE_FAST offset
        #  424 LOAD_FAST self
        #  426 LOAD_ATTR scale
        #  436 LOAD_METHOD setText
        #  458 LOAD_GLOBAL NULL + str
        #  470 LOAD_FAST scale
        #  472 PRECALL
        #  476 CALL
        #  486 PRECALL
        #  490 CALL
        #  500 POP_TOP
        #  502 LOAD_FAST self
        #  504 LOAD_ATTR offset
        #  514 LOAD_METHOD setText
        #  536 LOAD_GLOBAL NULL + str
        #  548 LOAD_FAST offset
        #  550 PRECALL
        # ... bytecode truncated ...
        pass

    def get_results(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL channel_suffix
        #    2 RESUME
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR unit_info
        #   16 POP_JUMP_FORWARD_IF_NOT_NONE to 22
        #   18 LOAD_CONST None
        #   20 RETURN_VALUE
        #   22 LOAD_FAST self
        #   24 LOAD_ATTR unit_info
        #   34 UNPACK_SEQUENCE
        #   38 STORE_FAST unit_type
        #   40 STORE_FAST unit_formatter
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR scale_offset
        #   54 POP_JUMP_FORWARD_IF_NOT_NONE to 60
        #   56 LOAD_CONST None
        #   58 RETURN_VALUE
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR scale_offset
        #   72 UNPACK_SEQUENCE
        #   76 STORE_FAST scale
        #   78 STORE_FAST offset
        #   80 NOP
        #   82 LOAD_GLOBAL asphodel
        #   94 LOAD_ATTR unit_type_names
        #  104 LOAD_FAST unit_type
        #  106 BINARY_SUBSCR
        #  116 STORE_FAST unit_type_str
        #  118 JUMP_FORWARD to 182
        #  120 PUSH_EXC_INFO
        #  122 LOAD_GLOBAL IndexError
        #  134 CHECK_EXC_MATCH
        #  136 POP_JUMP_FORWARD_IF_FALSE to 174
        #  138 POP_TOP
        #  140 LOAD_GLOBAL NULL + str
        #  152 LOAD_FAST unit_type
        #  154 PRECALL
        #  158 CALL
        #  168 STORE_FAST unit_type_str
        #  170 POP_EXCEPT
        #  172 JUMP_FORWARD to 182
        #  174 RERAISE
        #  176 COPY
        #  178 POP_EXCEPT
        #  180 RERAISE
        #  182 LOAD_FAST unit_formatter
        #  184 LOAD_ATTR unit_utf8
        #  194 LOAD_FAST unit_type_str
        #  196 LOAD_FAST scale
        #  198 LOAD_FAST offset
        #  200 LOAD_CONST ('calibration_unit', 'output_unit', 'scale', 'offset')
        #  202 BUILD_CONST_KEY_MAP
        #  204 STORE_FAST base_event_data
        #  206 LOAD_FAST self
        #  208 LOAD_ATTR tabWidget
        #  218 LOAD_METHOD currentIndex
        #  240 PRECALL
        #  244 CALL
        #  254 LOAD_CONST 0
        #  256 COMPARE_OP ==
        #  262 POP_JUMP_FORWARD_IF_FALSE to 368
        #  264 LOAD_CONST 'Linear'
        #  266 LOAD_FAST base_event_data
        #  268 LOAD_CONST 'calibration_type'
        #  270 STORE_SUBSCR
        #  274 LOAD_GLOBAL NULL + list
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR linear_x
        #  298 PRECALL
        #  302 CALL
        #  312 LOAD_FAST base_event_data
        #  314 LOAD_CONST 'x'
        #  316 STORE_SUBSCR
        #  320 LOAD_GLOBAL NULL + list
        #  332 LOAD_FAST self
        #  334 LOAD_ATTR linear_y
        #  344 PRECALL
        #  348 CALL
        #  358 LOAD_FAST base_event_data
        #  360 LOAD_CONST 'y'
        # ... bytecode truncated ...
        pass

    def ac_capture(self):
        device_tab = self.cal.device_tab()

    def linear_capture(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR unit_info
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR cal
        #   32 LOAD_METHOD device_tab
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST device_tab
        #   70 LOAD_FAST device_tab
        #   72 POP_JUMP_FORWARD_IF_NOT_NONE to 78
        #   74 LOAD_CONST None
        #   76 RETURN_VALUE
        #   78 LOAD_FAST device_tab
        #   80 LOAD_METHOD capture_func
        #  102 LOAD_FAST self
        #  104 LOAD_ATTR cal
        #  114 LOAD_ATTR channel_id
        #  124 PRECALL
        #  128 CALL
        #  138 UNPACK_SEQUENCE
        #  142 STORE_FAST mean
        #  144 STORE_FAST std_dev
        #  146 LOAD_FAST mean
        #  148 LOAD_METHOD item
        #  170 PRECALL
        #  174 CALL
        #  184 STORE_FAST mean_value
        #  186 LOAD_FAST std_dev
        #  188 LOAD_METHOD item
        #  210 PRECALL
        #  214 CALL
        #  224 STORE_FAST std_dev_value
        #  226 LOAD_GLOBAL NULL + math
        #  238 LOAD_ATTR isfinite
        #  248 LOAD_FAST mean_value
        #  250 PRECALL
        #  254 CALL
        #  264 EXTENDED_ARG
        #  266 POP_JUMP_FORWARD_IF_FALSE to 1554
        #  268 LOAD_GLOBAL NULL + math
        #  280 LOAD_ATTR isfinite
        #  290 LOAD_FAST std_dev_value
        #  292 PRECALL
        #  296 CALL
        #  306 EXTENDED_ARG
        #  308 POP_JUMP_FORWARD_IF_FALSE to 1558
        #  310 LOAD_GLOBAL NULL + UnitFormatterDoubleSpinBox
        #  322 LOAD_FAST self
        #  324 PRECALL
        #  328 CALL
        #  338 STORE_FAST captured
        #  340 LOAD_FAST captured
        #  342 LOAD_METHOD set_unit_formatter
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR dc_formatter
        #  376 PRECALL
        #  380 CALL
        #  390 POP_TOP
        #  392 LOAD_FAST captured
        #  394 LOAD_METHOD setMinimum
        #  416 LOAD_GLOBAL math
        #  428 LOAD_ATTR inf
        #  438 UNARY_NEGATIVE
        #  440 PRECALL
        #  444 CALL
        #  454 POP_TOP
        #  456 LOAD_FAST captured
        #  458 LOAD_METHOD setMaximum
        #  480 LOAD_GLOBAL math
        #  492 LOAD_ATTR inf
        #  502 PRECALL
        #  506 CALL
        #  516 POP_TOP
        #  518 LOAD_FAST captured
        #  520 LOAD_METHOD setValue
        #  542 LOAD_FAST mean_value
        # ... bytecode truncated ...
        pass

    def plot_linear(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR scale_offset
        #   14 POP_JUMP_FORWARD_IF_NONE to 30
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR unit_info
        #   28 POP_JUMP_FORWARD_IF_NOT_NONE to 34
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR linearTable
        #   46 LOAD_METHOD rowCount
        #   68 PRECALL
        #   72 CALL
        #   82 STORE_FAST row_count
        #   84 LOAD_FAST row_count
        #   86 LOAD_CONST 2
        #   88 COMPARE_OP <
        #   94 POP_JUMP_FORWARD_IF_FALSE to 100
        #   96 LOAD_CONST None
        #   98 RETURN_VALUE
        #  100 LOAD_GLOBAL NULL + numpy
        #  112 LOAD_ATTR zeros
        #  122 LOAD_FAST row_count
        #  124 PRECALL
        #  128 CALL
        #  138 STORE_FAST y
        #  140 LOAD_GLOBAL NULL + numpy
        #  152 LOAD_ATTR zeros
        #  162 LOAD_FAST row_count
        #  164 PRECALL
        #  168 CALL
        #  178 STORE_FAST x
        #  180 LOAD_GLOBAL NULL + range
        #  192 LOAD_FAST row_count
        #  194 PRECALL
        #  198 CALL
        #  208 GET_ITER
        #  210 FOR_ITER to 492
        #  212 STORE_FAST row
        #  214 LOAD_GLOBAL NULL + cast
        #  226 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR linearTable
        #  250 LOAD_METHOD cellWidget
        #  272 LOAD_FAST row
        #  274 LOAD_CONST 0
        #  276 PRECALL
        #  280 CALL
        #  290 PRECALL
        #  294 CALL
        #  304 STORE_FAST captured
        #  306 LOAD_GLOBAL NULL + cast
        #  318 LOAD_GLOBAL UnitFormatterDoubleSpinBox
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR linearTable
        #  342 LOAD_METHOD cellWidget
        #  364 LOAD_FAST row
        #  366 LOAD_CONST 1
        #  368 PRECALL
        #  372 CALL
        #  382 PRECALL
        #  386 CALL
        #  396 STORE_FAST actual
        #  398 LOAD_FAST actual
        #  400 LOAD_METHOD value
        #  422 PRECALL
        #  426 CALL
        #  436 LOAD_FAST y
        #  438 LOAD_FAST row
        #  440 STORE_SUBSCR
        #  444 LOAD_FAST captured
        #  446 LOAD_METHOD value
        #  468 PRECALL
        #  472 CALL
        #  482 LOAD_FAST x
        #  484 LOAD_FAST row
        #  486 STORE_SUBSCR
        #  490 JUMP_BACKWARD to 210
        #  492 LOAD_FAST x
        # ... bytecode truncated ...
        pass

    def delete_cb(self, ref):
        button = ref()

class CalibrationPanel(Ui_CalibrationPanel, QtWidgets.QGroupBox):

    def __init__(self, device_info, cals, logger, write_nvm, event_uploader, parent):
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
        #   70 LOAD_FAST device_info
        #   72 LOAD_FAST self
        #   74 STORE_ATTR device_info
        #   84 LOAD_FAST cals
        #   86 LOAD_FAST self
        #   88 STORE_ATTR cals
        #   98 LOAD_FAST logger
        #  100 LOAD_FAST self
        #  102 STORE_ATTR logger
        #  112 LOAD_FAST write_nvm
        #  114 LOAD_FAST self
        #  116 STORE_ATTR write_nvm
        #  126 LOAD_FAST event_uploader
        #  128 LOAD_FAST self
        #  130 STORE_ATTR event_uploader
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD setupUi
        #  164 LOAD_FAST self
        #  166 PRECALL
        #  170 CALL
        #  180 POP_TOP
        #  182 LOAD_FAST self
        #  184 LOAD_METHOD extra_ui_setup
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + UnitSelectionDialog
        #   14 LOAD_FAST self
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_FAST self
        #   32 STORE_ATTR unit_selection_dialog
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR buttonBox
        #   54 LOAD_METHOD button
        #   76 LOAD_GLOBAL QtWidgets
        #   88 LOAD_ATTR QDialogButtonBox
        #   98 LOAD_ATTR StandardButton
        #  108 LOAD_ATTR Save
        #  118 PRECALL
        #  122 CALL
        #  132 LOAD_FAST self
        #  134 STORE_ATTR saveButton
        #  144 LOAD_FAST self
        #  146 LOAD_ATTR saveButton
        #  156 LOAD_METHOD setText
        #  178 LOAD_FAST self
        #  180 LOAD_METHOD tr
        #  202 LOAD_CONST 'Write NVM'
        #  204 PRECALL
        #  208 CALL
        #  218 PRECALL
        #  222 CALL
        #  232 POP_TOP
        #  234 LOAD_FAST self
        #  236 LOAD_ATTR saveButton
        #  246 LOAD_ATTR clicked
        #  256 LOAD_METHOD connect
        #  278 LOAD_FAST self
        #  280 LOAD_ATTR save
        #  290 PRECALL
        #  294 CALL
        #  304 POP_TOP
        #  306 BUILD_LIST
        #  308 LOAD_FAST self
        #  310 STORE_ATTR channel_widgets
        #  320 LOAD_FAST self
        #  322 LOAD_ATTR cals
        #  332 GET_ITER
        #  334 FOR_ITER to 492
        #  336 STORE_FAST cal
        #  338 LOAD_GLOBAL NULL + CalibrationChannel
        #  350 LOAD_FAST cal
        #  352 LOAD_FAST self
        #  354 LOAD_ATTR unit_selection_dialog
        #  364 LOAD_FAST self
        #  366 PRECALL
        #  370 CALL
        #  380 STORE_FAST channel_widget
        #  382 LOAD_FAST self
        #  384 LOAD_ATTR channel_widgets
        #  394 LOAD_METHOD append
        #  416 LOAD_FAST cal
        #  418 LOAD_ATTR name
        #  428 LOAD_FAST channel_widget
        #  430 BUILD_TUPLE
        #  432 PRECALL
        #  436 CALL
        #  446 POP_TOP
        #  448 LOAD_FAST self
        #  450 LOAD_METHOD setup_channel_signals
        #  472 LOAD_FAST channel_widget
        #  474 PRECALL
        #  478 CALL
        #  488 POP_TOP
        #  490 JUMP_BACKWARD to 334
        #  492 LOAD_GLOBAL NULL + len
        #  504 LOAD_FAST self
        #  506 LOAD_ATTR channel_widgets
        #  516 PRECALL
        #  520 CALL
        #  530 LOAD_CONST 1
        #  532 COMPARE_OP ==
        #  538 POP_JUMP_FORWARD_IF_FALSE to 740
        #  540 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def setup_channel_signals(self, channel_widget):
        channel_widget.value_changed.connect(self.values_updated)

    def is_valid(self):
        all_valid = False

    def values_updated(self):
        valid = self.is_valid()
        self.saveButton.setEnabled(valid)

    def save(self):
        settings = self.device_info.settings
        unit_settings = { }
        float_settings = { }
        event_data = {
            'board_type': self.device_info.board_info[0],
            'board_rev': self.device_info.board_info[1],
            'computer': platform.node() }
        for _name, channel_widget in self.channel_widgets:
            if channel_widget.calibrationEnabled.isChecked():
                results = channel_widget.get_results()
                if results:
                    (unit_type, scale, offset, channel_event_data) = results
                    (u, f) = get_channel_setting_values(len(settings), channel_widget.cal.calibration_info, unit_type, scale, offset)
                    unit_settings.update(u)
                    float_settings.update(f)
                    event_data.update(channel_event_data)
            new_nvm = update_nvm(self.device_info.nvm, settings, unit_settings, float_settings, self.logger)
            self.event_uploader.calibration_finished(self.device_info.serial_number, event_data)
            self.write_nvm(new_nvm)
            return None
