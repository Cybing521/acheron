# Source Generated with Decompyle++
# File: psd.pyc (Python 3.11)

import logging
import math
from typing import Literal
from matplotlib.backend_bases import MouseButton
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import numpy
from numpy.typing import NDArray
from PySide6 import QtGui, QtWidgets
from . import util
from .. import export_csv
from .. import export_script
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def get_integrated_power(start_freq, end_freq, freqs, pxx):
    start_index = max(0, numpy.searchsorted(freqs, start_freq, side = 'right').item() - 1)
    end_index = min(len(freqs), numpy.searchsorted(freqs, end_freq, side = 'left').item() + 1)
    dfreq = freqs[1] - freqs[0]
    integrated = numpy.sum(pxx[start_index:end_index]) * dfreq
    return integrated.item()

def add_amplitude_button(fig, ax, data):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL fig
    #    2 MAKE_CELL ax
    #    4 MAKE_CELL data
    #    6 MAKE_CELL rect
    #    8 MAKE_CELL toolbar
    #   10 RESUME
    #   12 LOAD_CONST None
    #   14 STORE_DEREF rect
    #   16 LOAD_DEREF fig
    #   18 LOAD_ATTR canvas
    #   28 LOAD_ATTR toolbar
    #   38 STORE_DEREF toolbar
    #   40 LOAD_GLOBAL QtWidgets
    #   52 LOAD_ATTR QApplication
    #   62 LOAD_METHOD translate
    #   84 LOAD_CONST 'AmplitudeAction'
    #   86 LOAD_CONST 'Amplitude Integration'
    #   88 PRECALL
    #   92 CALL
    #  102 STORE_FAST actionText
    #  104 LOAD_GLOBAL NULL + QtGui
    #  116 LOAD_ATTR QAction
    #  126 LOAD_FAST actionText
    #  128 LOAD_DEREF toolbar
    #  130 PRECALL
    #  134 CALL
    #  144 STORE_FAST action
    #  146 LOAD_FAST action
    #  148 LOAD_METHOD setIcon
    #  170 LOAD_GLOBAL QtGui
    #  182 LOAD_ATTR QIcon
    #  192 LOAD_METHOD fromTheme
    #  214 LOAD_CONST 'measuring_cup'
    #  216 PRECALL
    #  220 CALL
    #  230 PRECALL
    #  234 CALL
    #  244 POP_TOP
    #  246 LOAD_CONST ('return', None)
    #  248 LOAD_CLOSURE ax
    #  250 LOAD_CLOSURE data
    #  252 LOAD_CLOSURE fig
    #  254 LOAD_CLOSURE rect
    #  256 LOAD_CLOSURE toolbar
    #  258 BUILD_TUPLE
    #  260 LOAD_CONST <code object measure_sine_amplitude at 0xaccfd5400, file "mondo\analysis\psd.py", line 72>
    #  262 MAKE_FUNCTION annotations, closure
    #  264 STORE_FAST measure_sine_amplitude
    #  266 LOAD_FAST action
    #  268 LOAD_ATTR triggered
    #  278 LOAD_METHOD connect
    #  300 LOAD_FAST measure_sine_amplitude
    #  302 PRECALL
    #  306 CALL
    #  316 POP_TOP
    #  318 LOAD_DEREF toolbar
    #  320 LOAD_METHOD addAction
    #  342 LOAD_FAST action
    #  344 PRECALL
    #  348 CALL
    #  358 POP_TOP
    #  360 LOAD_CONST None
    #  362 RETURN_VALUE
    pass

def _stride_windows(x, n, noverlap):
    return numpy.lib.stride_tricks.sliding_window_view(x, n, axis = 0)[::n - noverlap].T

def do_psd(sequence, subchannel_index, NFFT, Fs, detrend, window, noverlap):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL numpy
    #   14 LOAD_ATTR fft
    #   24 LOAD_METHOD rfftfreq
    #   46 LOAD_FAST NFFT
    #   48 LOAD_CONST 1
    #   50 LOAD_FAST Fs
    #   52 BINARY_OP /
    #   56 PRECALL
    #   60 CALL
    #   70 STORE_FAST freqs
    #   72 LOAD_CONST 0
    #   74 STORE_FAST windows
    #   76 LOAD_GLOBAL NULL + numpy
    #   88 LOAD_ATTR zeros
    #   98 LOAD_FAST freqs
    #  100 LOAD_ATTR shape
    #  110 PRECALL
    #  114 CALL
    #  124 STORE_FAST sums
    #  126 LOAD_FAST sequence
    #  128 GET_ITER
    #  130 EXTENDED_ARG
    #  132 FOR_ITER to 714
    #  134 UNPACK_SEQUENCE
    #  138 STORE_FAST _time
    #  140 STORE_FAST data
    #  142 STORE_FAST _start
    #  144 STORE_FAST _end
    #  146 LOAD_GLOBAL NULL + numpy
    #  158 LOAD_ATTR asarray
    #  168 LOAD_FAST data
    #  170 LOAD_CONST None
    #  172 LOAD_CONST None
    #  174 BUILD_SLICE
    #  176 LOAD_FAST subchannel_index
    #  178 BUILD_TUPLE
    #  180 BINARY_SUBSCR
    #  190 PRECALL
    #  194 CALL
    #  204 STORE_FAST x
    #  206 LOAD_GLOBAL NULL + len
    #  218 LOAD_FAST x
    #  220 PRECALL
    #  224 CALL
    #  234 LOAD_FAST NFFT
    #  236 COMPARE_OP <
    #  242 POP_JUMP_FORWARD_IF_FALSE to 246
    #  244 JUMP_BACKWARD to 130
    #  246 LOAD_GLOBAL NULL + _stride_windows
    #  258 LOAD_FAST x
    #  260 LOAD_FAST NFFT
    #  262 LOAD_FAST noverlap
    #  264 PRECALL
    #  268 CALL
    #  278 STORE_FAST result
    #  280 LOAD_GLOBAL NULL + mlab
    #  292 LOAD_ATTR detrend
    #  302 LOAD_FAST result
    #  304 LOAD_FAST detrend
    #  306 LOAD_CONST 0
    #  308 KW_NAMES
    #  310 PRECALL
    #  314 CALL
    #  324 STORE_FAST result
    #  326 LOAD_GLOBAL NULL + numpy
    #  338 LOAD_ATTR asarray
    #  348 LOAD_FAST result
    #  350 PRECALL
    #  354 CALL
    #  364 LOAD_FAST window
    #  366 LOAD_METHOD reshape
    #  388 LOAD_CONST (-1, 1)
    #  390 PRECALL
    #  394 CALL
    #  404 BINARY_OP *
    #  408 STORE_FAST result
    #  410 LOAD_GLOBAL numpy
    #  422 LOAD_ATTR fft
    #  432 LOAD_METHOD rfft
    # ... bytecode truncated ...
    pass

def psd_analysis(parent):
    ret = util.load_batch(parent)

def single_channel_psd_analysis(parent):
    channel_index = None
    subchannel_index = None
    sampling_rate = None
    sequences = []
    units = []
    names = []
    files = set()
    ret = util.load_batch(parent)

def single_slice_psd_analysis(parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL batch_info
    #    2 RESUME
    #    4 LOAD_GLOBAL NULL + util
    #   16 LOAD_ATTR load_batch
    #   26 LOAD_FAST parent
    #   28 PRECALL
    #   32 CALL
    #   42 STORE_FAST ret
    #   44 LOAD_FAST ret
    #   46 POP_JUMP_FORWARD_IF_NOT_NONE to 52
    #   48 LOAD_CONST None
    #   50 RETURN_VALUE
    #   52 LOAD_FAST ret
    #   54 UNPACK_SEQUENCE
    #   58 STORE_FAST file_infos
    #   60 STORE_FAST header
    #   62 LOAD_GLOBAL NULL + util
    #   74 LOAD_ATTR choose_subchannels
    #   84 LOAD_FAST header
    #   86 LOAD_FAST parent
    #   88 PRECALL
    #   92 CALL
    #  102 STORE_FAST subchannels_list
    #  104 LOAD_FAST subchannels_list
    #  106 POP_JUMP_FORWARD_IF_TRUE to 112
    #  108 LOAD_CONST None
    #  110 RETURN_VALUE
    #  112 LOAD_CONST <code object <setcomp> at 0x105af98b0, file "mondo\analysis\psd.py", line 427>
    #  114 MAKE_FUNCTION
    #  116 LOAD_FAST subchannels_list
    #  118 GET_ITER
    #  120 PRECALL
    #  124 CALL
    #  134 STORE_FAST channel_indexes
    #  136 LOAD_GLOBAL NULL + util
    #  148 LOAD_ATTR decode_batch
    #  158 LOAD_FAST file_infos
    #  160 LOAD_FAST header
    #  162 LOAD_FAST channel_indexes
    #  164 LOAD_FAST parent
    #  166 PRECALL
    #  170 CALL
    #  180 STORE_DEREF batch_info
    #  182 LOAD_DEREF batch_info
    #  184 POP_JUMP_FORWARD_IF_NOT_NONE to 190
    #  186 LOAD_CONST None
    #  188 RETURN_VALUE
    #  190 LOAD_GLOBAL NULL + util
    #  202 LOAD_ATTR get_datetime_subset
    #  212 LOAD_DEREF batch_info
    #  214 LOAD_FAST parent
    #  216 PRECALL
    #  220 CALL
    #  230 STORE_DEREF batch_info
    #  232 LOAD_DEREF batch_info
    #  234 POP_JUMP_FORWARD_IF_NOT_NONE to 240
    #  236 LOAD_CONST None
    #  238 RETURN_VALUE
    #  240 LOAD_GLOBAL NULL + util
    #  252 LOAD_ATTR warn_about_lost_packets
    #  262 LOAD_DEREF batch_info
    #  264 LOAD_FAST parent
    #  266 PRECALL
    #  270 CALL
    #  280 STORE_FAST ret_lost_packets
    #  282 LOAD_FAST ret_lost_packets
    #  284 POP_JUMP_FORWARD_IF_TRUE to 290
    #  286 LOAD_CONST None
    #  288 RETURN_VALUE
    #  290 LOAD_GLOBAL NULL + util
    #  302 LOAD_ATTR sequence_data
    #  312 LOAD_DEREF batch_info
    #  314 LOAD_FAST parent
    #  316 LOAD_CONST True
    #  318 LOAD_CONST True
    #  320 KW_NAMES
    #  322 PRECALL
    #  326 CALL
    #  336 UNPACK_SEQUENCE
    #  340 STORE_FAST sequence_info
    # ... bytecode truncated ...
    pass

def overlaid_psd_analysis(parent):
    sequences = []
    names = []
    sampling_rates = []
    ret = util.load_batch(parent = parent)
