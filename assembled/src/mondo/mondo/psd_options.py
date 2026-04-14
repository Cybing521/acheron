# Source Generated with Decompyle++
# File: psd_options.pyc (Python 3.11)

import logging
import math
from typing import Literal, Optional, TypedDict
import numpy
from numpy.typing import NDArray
from PySide6 import QtCore, QtWidgets
import scipy.signal.windows as scipy
from .ui.ui_psd_options import Ui_PSDOptionsWidget
logger = logging.getLogger(__name__)
Chunk = tuple[(NDArray[numpy.float64], NDArray[numpy.float64], float, float)]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class PSDOptions(TypedDict):

    Fs: float

    NFFT: int

    noverlap: int

class PSDOptionsWidget(Ui_PSDOptionsWidget, QtWidgets.QWidget):

    def __init__(self, chunks_list, sampling_rate, parent):
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
        #   70 LOAD_FAST chunks_list
        #   72 LOAD_FAST self
        #   74 STORE_ATTR chunks_list
        #   84 LOAD_FAST sampling_rate
        #   86 LOAD_FAST self
        #   88 STORE_ATTR sampling_rate
        #   98 LOAD_FAST self
        #  100 LOAD_METHOD setupUi
        #  122 LOAD_FAST self
        #  124 PRECALL
        #  128 CALL
        #  138 POP_TOP
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD fill_combo_boxes
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_CONST False
        #  182 LOAD_FAST self
        #  184 STORE_ATTR changing_overlap
        #  194 LOAD_FAST self
        #  196 LOAD_ATTR fftPoints
        #  206 LOAD_ATTR currentIndexChanged
        #  216 LOAD_METHOD connect
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR fft_points_changed
        #  250 PRECALL
        #  254 CALL
        #  264 POP_TOP
        #  266 LOAD_FAST self
        #  268 LOAD_ATTR overlapPercent
        #  278 LOAD_ATTR valueChanged
        #  288 LOAD_METHOD connect
        #  310 LOAD_FAST self
        #  312 LOAD_ATTR overlap_percent_changed
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 LOAD_FAST self
        #  340 LOAD_ATTR overlapPoints
        #  350 LOAD_ATTR valueChanged
        #  360 LOAD_METHOD connect
        #  382 LOAD_FAST self
        #  384 LOAD_ATTR overlap_points_changed
        #  394 PRECALL
        #  398 CALL
        #  408 POP_TOP
        #  410 LOAD_FAST self
        #  412 LOAD_METHOD fft_points_changed
        #  434 PRECALL
        #  438 CALL
        #  448 POP_TOP
        #  450 LOAD_FAST self
        #  452 LOAD_ATTR overlapPercent
        #  462 LOAD_METHOD setValue
        #  484 LOAD_CONST 90.0
        #  486 PRECALL
        #  490 CALL
        #  500 POP_TOP
        #  502 LOAD_FAST self
        #  504 LOAD_METHOD layout
        #  526 PRECALL
        #  530 CALL
        #  540 LOAD_METHOD setSizeConstraint
        #  562 LOAD_GLOBAL QtWidgets
        #  574 LOAD_ATTR QLayout
        #  584 LOAD_ATTR SizeConstraint
        #  594 LOAD_ATTR SetFixedSize
        #  604 PRECALL
        #  608 CALL
        # ... bytecode truncated ...
        pass

    def fill_combo_boxes(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL frequency_resolution
        #    2 MAKE_CELL target_resolution
        #    4 RESUME
        #    6 BUILD_LIST
        #    8 STORE_FAST max_lengths
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR chunks_list
        #   22 GET_ITER
        #   24 FOR_ITER to 118
        #   26 STORE_FAST chunks
        #   28 LOAD_FAST max_lengths
        #   30 LOAD_METHOD append
        #   52 LOAD_GLOBAL NULL + max
        #   64 LOAD_CONST <code object <genexpr> at 0x105ab7b30, file "mondo\psd_options.py", line 83>
        #   66 MAKE_FUNCTION
        #   68 LOAD_FAST chunks
        #   70 GET_ITER
        #   72 PRECALL
        #   76 CALL
        #   86 PRECALL
        #   90 CALL
        #  100 PRECALL
        #  104 CALL
        #  114 POP_TOP
        #  116 JUMP_BACKWARD to 24
        #  118 LOAD_GLOBAL NULL + min
        #  130 LOAD_FAST max_lengths
        #  132 PRECALL
        #  136 CALL
        #  146 STORE_FAST max_length
        #  148 LOAD_GLOBAL NULL + math
        #  160 LOAD_ATTR floor
        #  170 LOAD_GLOBAL NULL + math
        #  182 LOAD_ATTR log2
        #  192 LOAD_FAST max_length
        #  194 PRECALL
        #  198 CALL
        #  208 PRECALL
        #  212 CALL
        #  222 STORE_FAST max_pow_2
        #  224 LOAD_GLOBAL NULL + min
        #  236 LOAD_CONST 8
        #  238 LOAD_FAST max_pow_2
        #  240 PRECALL
        #  244 CALL
        #  254 STORE_FAST min_pow_2
        #  256 BUILD_LIST
        #  258 LOAD_FAST self
        #  260 STORE_ATTR fft_points_by_index
        #  270 BUILD_LIST
        #  272 STORE_DEREF frequency_resolution
        #  274 LOAD_GLOBAL NULL + range
        #  286 LOAD_FAST min_pow_2
        #  288 LOAD_FAST max_pow_2
        #  290 LOAD_CONST 1
        #  292 BINARY_OP +
        #  296 PRECALL
        #  300 CALL
        #  310 GET_ITER
        #  312 FOR_ITER to 534
        #  314 STORE_FAST i
        #  316 LOAD_CONST 2
        #  318 LOAD_FAST i
        #  320 BINARY_OP **
        #  324 STORE_FAST points
        #  326 LOAD_CONST '{} (2^{})'
        #  328 LOAD_METHOD format
        #  350 LOAD_FAST points
        #  352 LOAD_FAST i
        #  354 PRECALL
        #  358 CALL
        #  368 STORE_FAST s
        #  370 LOAD_FAST self
        #  372 LOAD_ATTR fft_points_by_index
        #  382 LOAD_METHOD append
        #  404 LOAD_FAST points
        #  406 PRECALL
        #  410 CALL
        #  420 POP_TOP
        #  422 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def update_window_count(self, window_size, overlap_points):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 BUILD_LIST
        #    4 STORE_FAST window_counts
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR chunks_list
        #   18 GET_ITER
        #   20 FOR_ITER to 158
        #   22 STORE_FAST chunks
        #   24 LOAD_CONST 0
        #   26 STORE_FAST window_count
        #   28 LOAD_FAST chunks
        #   30 GET_ITER
        #   32 FOR_ITER to 114
        #   34 STORE_FAST chunk
        #   36 LOAD_GLOBAL NULL + len
        #   48 LOAD_FAST chunk
        #   50 LOAD_CONST 0
        #   52 BINARY_SUBSCR
        #   62 PRECALL
        #   66 CALL
        #   76 STORE_FAST chunk_size
        #   78 LOAD_FAST window_count
        #   80 LOAD_CONST 1
        #   82 LOAD_FAST chunk_size
        #   84 LOAD_FAST window_size
        #   86 BINARY_OP -
        #   90 LOAD_FAST window_size
        #   92 LOAD_FAST overlap_points
        #   94 BINARY_OP -
        #   98 BINARY_OP //
        #  102 BINARY_OP +
        #  106 BINARY_OP +=
        #  110 STORE_FAST window_count
        #  112 JUMP_BACKWARD to 32
        #  114 LOAD_FAST window_counts
        #  116 LOAD_METHOD append
        #  138 LOAD_FAST window_count
        #  140 PRECALL
        #  144 CALL
        #  154 POP_TOP
        #  156 JUMP_BACKWARD to 20
        #  158 LOAD_CONST ', '
        #  160 LOAD_METHOD join
        #  182 LOAD_CONST <code object <genexpr> at 0x105abfc30, file "mondo\psd_options.py", line 130>
        #  184 MAKE_FUNCTION
        #  186 LOAD_FAST window_counts
        #  188 GET_ITER
        #  190 PRECALL
        #  194 CALL
        #  204 PRECALL
        #  208 CALL
        #  218 STORE_FAST s
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR windowCount
        #  232 LOAD_METHOD setText
        #  254 LOAD_FAST s
        #  256 PRECALL
        #  260 CALL
        #  270 POP_TOP
        #  272 LOAD_CONST None
        #  274 RETURN_VALUE
        pass

    def fft_points_changed(self):
        index = self.fftPoints.currentIndex()
        window_size = self.fft_points_by_index[index]
        original_percent = self.overlapPercent.value()
        if self.overlapPoints.value() >= window_size:
            self.overlapPoints.setValue(window_size - 1)
        self.overlapPoints.setMaximum(window_size - 1)
        self.overlapPercent.setMaximum(100 * (window_size - 1) / window_size)
        self.changing_overlap = True
        self.overlapPercent.setValue(original_percent)
        self.changing_overlap = False
        self.overlap_percent_changed()
        window_duration = window_size / self.sampling_rate
        self.duration.setText('{:.3f} s'.format(window_duration))
        frequency_resolution = self.sampling_rate / window_size
        self.resolution.setText('{:.3f} Hz'.format(frequency_resolution))

    def overlap_percent_changed(self):
        if self.changing_overlap:
            return None

        try:
            self.changing_overlap = True
            index = self.fftPoints.currentIndex()
            window_size = self.fft_points_by_index[index]
            percent = self.overlapPercent.value()
            points = math.floor(window_size * percent / 100)
            if points >= window_size:
                points = window_size - 1
            self.overlapPoints.setValue(points)
            self.update_window_count(window_size, points)
            self.changing_overlap = False
            return None
        except:
            self.changing_overlap = False

    def overlap_points_changed(self):
        if self.changing_overlap:
            return None

        try:
            self.changing_overlap = True
            index = self.fftPoints.currentIndex()
            window_size = self.fft_points_by_index[index]
            points = self.overlapPoints.value()
            percent = (points / window_size) * 100
            self.overlapPercent.setValue(percent)
            self.update_window_count(window_size, points)
            self.changing_overlap = False
            return None
        except:
            self.changing_overlap = False

    def hann_window(self, x):
        return scipy.signal.windows.hann(len(x), False) * x

    def hamming_window(self, x):
        return scipy.signal.windows.hamming(len(x), False) * x

    def flattop_window(self, x):
        return scipy.signal.windows.flattop(len(x), False) * x

    def uniform_window(self, x):
        return x

    def get_options(self):
        index = self.fftPoints.currentIndex()
        window_size = self.fft_points_by_index[index]
        index = self.windowFunction.currentIndex()
        window_function = self.window_functions[index][1]
        window = window_function(numpy.ones(window_size, dtype = numpy.double))
        index = self.detrendMethod.currentIndex()
        detrend = self.detrend_options[index][1]
        return {
            'Fs': self.sampling_rate,
            'NFFT': window_size,
            'noverlap': self.overlapPoints.value(),
            'window': window,
            'detrend': detrend }

class PSDOptionsDialog(QtWidgets.QDialog):

    def __init__(self, chunks_list, sampling_rate, parent):
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
        #   54 LOAD_GLOBAL QtCore
        #   66 LOAD_ATTR Qt
        #   76 LOAD_ATTR WindowType
        #   86 LOAD_ATTR MSWindowsFixedSizeDialogHint
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_GLOBAL NULL + QtWidgets
        #  124 LOAD_ATTR QVBoxLayout
        #  134 LOAD_FAST self
        #  136 PRECALL
        #  140 CALL
        #  150 LOAD_FAST self
        #  152 STORE_ATTR verticalLayout
        #  162 LOAD_GLOBAL NULL + PSDOptionsWidget
        #  174 LOAD_FAST chunks_list
        #  176 LOAD_FAST sampling_rate
        #  178 LOAD_FAST self
        #  180 PRECALL
        #  184 CALL
        #  194 LOAD_FAST self
        #  196 STORE_ATTR psd_options
        #  206 LOAD_FAST self
        #  208 LOAD_ATTR verticalLayout
        #  218 LOAD_METHOD addWidget
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR psd_options
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_GLOBAL NULL + QtWidgets
        #  280 LOAD_ATTR QDialogButtonBox
        #  290 LOAD_FAST self
        #  292 PRECALL
        #  296 CALL
        #  306 LOAD_FAST self
        #  308 STORE_ATTR buttonBox
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR buttonBox
        #  330 LOAD_METHOD setOrientation
        #  352 LOAD_GLOBAL QtCore
        #  364 LOAD_ATTR Qt
        #  374 LOAD_ATTR Orientation
        #  384 LOAD_ATTR Horizontal
        #  394 PRECALL
        #  398 CALL
        #  408 POP_TOP
        #  410 LOAD_FAST self
        #  412 LOAD_ATTR buttonBox
        #  422 LOAD_METHOD setStandardButtons
        #  444 LOAD_GLOBAL QtWidgets
        #  456 LOAD_ATTR QDialogButtonBox
        #  466 LOAD_ATTR StandardButton
        #  476 LOAD_ATTR Cancel
        #  486 LOAD_GLOBAL QtWidgets
        #  498 LOAD_ATTR QDialogButtonBox
        #  508 LOAD_ATTR StandardButton
        #  518 LOAD_ATTR Ok
        #  528 BINARY_OP |
        #  532 PRECALL
        #  536 CALL
        #  546 POP_TOP
        #  548 LOAD_FAST self
        #  550 LOAD_ATTR verticalLayout
        #  560 LOAD_METHOD addWidget
        #  582 LOAD_FAST self
        #  584 LOAD_ATTR buttonBox
        #  594 PRECALL
        #  598 CALL
        #  608 POP_TOP
        #  610 LOAD_FAST self
        #  612 LOAD_ATTR buttonBox
        #  622 LOAD_ATTR accepted
        # ... bytecode truncated ...
        pass

    def get_options(self):
        return self.psd_options.get_options()

class MultiplePSDOptionsDialog(QtWidgets.QDialog):

    def __init__(self, sections, parent):
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
        #   54 LOAD_GLOBAL QtCore
        #   66 LOAD_ATTR Qt
        #   76 LOAD_ATTR WindowType
        #   86 LOAD_ATTR WindowTitleHint
        #   96 LOAD_GLOBAL QtCore
        #  108 LOAD_ATTR Qt
        #  118 LOAD_ATTR WindowType
        #  128 LOAD_ATTR WindowSystemMenuHint
        #  138 BINARY_OP |
        #  142 PRECALL
        #  146 CALL
        #  156 POP_TOP
        #  158 BUILD_LIST
        #  160 LOAD_FAST self
        #  162 STORE_ATTR psd_options
        #  172 LOAD_GLOBAL NULL + QtWidgets
        #  184 LOAD_ATTR QVBoxLayout
        #  194 LOAD_FAST self
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_FAST self
        #  212 STORE_ATTR verticalLayout
        #  222 LOAD_GLOBAL NULL + QtWidgets
        #  234 LOAD_ATTR QScrollArea
        #  244 LOAD_FAST self
        #  246 PRECALL
        #  250 CALL
        #  260 LOAD_FAST self
        #  262 STORE_ATTR scrollArea
        #  272 LOAD_FAST self
        #  274 LOAD_ATTR scrollArea
        #  284 LOAD_METHOD setVerticalScrollBarPolicy
        #  306 LOAD_GLOBAL QtCore
        #  318 LOAD_ATTR Qt
        #  328 LOAD_ATTR ScrollBarPolicy
        #  338 LOAD_ATTR ScrollBarAlwaysOff
        #  348 PRECALL
        #  352 CALL
        #  362 POP_TOP
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR scrollArea
        #  376 LOAD_METHOD setHorizontalScrollBarPolicy
        #  398 LOAD_GLOBAL QtCore
        #  410 LOAD_ATTR Qt
        #  420 LOAD_ATTR ScrollBarPolicy
        #  430 LOAD_ATTR ScrollBarAsNeeded
        #  440 PRECALL
        #  444 CALL
        #  454 POP_TOP
        #  456 LOAD_FAST self
        #  458 LOAD_ATTR scrollArea
        #  468 LOAD_METHOD setWidgetResizable
        #  490 LOAD_CONST True
        #  492 PRECALL
        #  496 CALL
        #  506 POP_TOP
        #  508 LOAD_FAST self
        #  510 LOAD_ATTR scrollArea
        #  520 LOAD_METHOD setFrameShape
        #  542 LOAD_GLOBAL QtWidgets
        #  554 LOAD_ATTR QFrame
        #  564 LOAD_ATTR Shape
        #  574 LOAD_ATTR NoFrame
        #  584 PRECALL
        #  588 CALL
        #  598 POP_TOP
        #  600 LOAD_GLOBAL NULL + QtWidgets
        #  612 LOAD_ATTR QWidget
        #  622 PRECALL
        #  626 CALL
        #  636 LOAD_FAST self
        #  638 STORE_ATTR scrollAreaContents
        #  648 LOAD_GLOBAL NULL + QtWidgets
        # ... bytecode truncated ...
        pass

    def get_options(self):
        return self.psd_options()
