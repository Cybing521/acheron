# Source Generated with Decompyle++
# File: time.pyc (Python 3.11)

import logging
from matplotlib.backend_bases import MouseButton
from matplotlib.figure import Figure
import numpy
from numpy.typing import NDArray
from PySide6 import QtGui, QtWidgets
from . import util
from .. import export_script
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def get_mean_std_dev_in_range(start_time, end_time, x, y):
    start_index = max(0, numpy.searchsorted(x, start_time, side = 'right').item() - 1)
    end_index = min(len(x), numpy.searchsorted(x, end_time, side = 'left').item() + 1)
    data = y[start_index:end_index]
    mean = numpy.mean(data, axis = 0).item()
    std_dev = numpy.std(data, axis = 0).item()
    return (mean, std_dev)

def display_mean_and_std_dev(start_time, end_time, data, title, parent):
    value_strings = []
    for x, y, name, unit in data:
        (mean, std_dev) = get_mean_std_dev_in_range(start_time, end_time, x, y)
        base_str = f'''mean={mean} {unit.utf8}, std dev={std_dev} {unit.utf8}'''
        if name:
            value_strings.append(f'''{name}: {base_str}''')
            continue
        value_strings.append(base_str)
        text = '\n'.join(value_strings)
        QtWidgets.QMessageBox.information(parent, title, text)
        return None

def add_mean_std_dev_summary_buttons(fig, axes, data):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL fig
    #    2 MAKE_CELL axes
    #    4 MAKE_CELL data
    #    6 MAKE_CELL range_action_text
    #    8 MAKE_CELL rects
    #   10 MAKE_CELL toolbar
    #   12 MAKE_CELL total_action_text
    #   14 RESUME
    #   16 LOAD_CONST <code object <dictcomp> at 0x105b62320, file "mondo\analysis\time.py", line 86>
    #   18 MAKE_FUNCTION
    #   20 LOAD_DEREF axes
    #   22 GET_ITER
    #   24 PRECALL
    #   28 CALL
    #   38 STORE_DEREF rects
    #   40 LOAD_DEREF fig
    #   42 LOAD_ATTR canvas
    #   52 LOAD_ATTR toolbar
    #   62 STORE_DEREF toolbar
    #   64 LOAD_GLOBAL QtWidgets
    #   76 LOAD_ATTR QApplication
    #   86 LOAD_METHOD translate
    #  108 LOAD_CONST 'RMSTotalAction'
    #  110 LOAD_CONST 'Mean and Std Dev (All)'
    #  112 PRECALL
    #  116 CALL
    #  126 STORE_DEREF total_action_text
    #  128 LOAD_GLOBAL NULL + QtGui
    #  140 LOAD_ATTR QAction
    #  150 LOAD_DEREF total_action_text
    #  152 LOAD_DEREF toolbar
    #  154 PRECALL
    #  158 CALL
    #  168 STORE_FAST total_action
    #  170 LOAD_FAST total_action
    #  172 LOAD_METHOD setIcon
    #  194 LOAD_GLOBAL QtGui
    #  206 LOAD_ATTR QIcon
    #  216 LOAD_METHOD fromTheme
    #  238 LOAD_CONST 'multimeter_analog'
    #  240 PRECALL
    #  244 CALL
    #  254 PRECALL
    #  258 CALL
    #  268 POP_TOP
    #  270 LOAD_GLOBAL QtWidgets
    #  282 LOAD_ATTR QApplication
    #  292 LOAD_METHOD translate
    #  314 LOAD_CONST 'RMSRangeAction'
    #  316 LOAD_CONST 'Mean and Std Dev (Range)'
    #  318 PRECALL
    #  322 CALL
    #  332 STORE_DEREF range_action_text
    #  334 LOAD_GLOBAL NULL + QtGui
    #  346 LOAD_ATTR QAction
    #  356 LOAD_DEREF range_action_text
    #  358 LOAD_DEREF toolbar
    #  360 PRECALL
    #  364 CALL
    #  374 STORE_FAST range_action
    #  376 LOAD_FAST range_action
    #  378 LOAD_METHOD setIcon
    #  400 LOAD_GLOBAL QtGui
    #  412 LOAD_ATTR QIcon
    #  422 LOAD_METHOD fromTheme
    #  444 LOAD_CONST 'measuring_cup'
    #  446 PRECALL
    #  450 CALL
    #  460 PRECALL
    #  464 CALL
    #  474 POP_TOP
    #  476 LOAD_CONST ('return', None)
    #  478 LOAD_CLOSURE data
    #  480 LOAD_CLOSURE toolbar
    #  482 LOAD_CLOSURE total_action_text
    #  484 BUILD_TUPLE
    #  486 LOAD_CONST <code object measure_total at 0x100acf9f0, file "mondo\analysis\time.py", line 99>
    #  488 MAKE_FUNCTION annotations, closure
    #  490 STORE_FAST measure_total
    #  492 LOAD_CONST ('return', None)
    # ... bytecode truncated ...
    pass

def time_analysis(parent):
    ret = util.load_batch(parent)

def synchronous_time_analysis(parent):
    ret = util.load_batch(parent)

def overlaid_time_analysis(parent):
    sequences = []
    subchannel_indexes = []
    unit_types = []
    unit_names = []
    unit_infos = []
    names = []
    ret = util.load_batch(parent)
