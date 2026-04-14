# Source Generated with Decompyle++
# File: tmpfzgmsldr.marshal (Python 3.11)

import logging
from matplotlib.backend_bases import MouseButton
from matplotlib.figure import Figure
import numpy
from numpy.typing import NDArray
from PySide6 import QtGui, QtWidgets
from  import util
from  import export_script
logger = logging.getLogger(__name__)

def get_mean_std_dev_in_range(start_time = None, end_time = None, x = None, y = ('start_time', float, 'end_time', float, 'x', NDArray[numpy.float64], 'y', NDArray[numpy.float64], 'return', tuple[(float, float)])):
    start_index = max(0, numpy.searchsorted(x, start_time, side = 'right').item() - 1)
    end_index = min(len(x), numpy.searchsorted(x, end_time, side = 'left').item() + 1)
    data = y[start_index:end_index]
    mean = numpy.mean(data, axis = 0).item()
    std_dev = numpy.std(data, axis = 0).item()
    return (mean, std_dev)


def display_mean_and_std_dev(start_time, end_time = None, data = None, title = None, parent = ('start_time', float, 'end_time', float, 'data', list[tuple[(NDArray[numpy.float64], NDArray[numpy.float64], str, util.UnitInfo)]], 'title', str, 'parent', QtWidgets.QWidget, 'return', None)):
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


def add_mean_std_dev_summary_buttons(fig = None, axes = None, data = None):
    pass
# WARNING: Decompyle incomplete


def time_analysis(parent = None):
    ret = util.load_batch(parent)
# WARNING: Decompyle incomplete


def synchronous_time_analysis(parent = None):
    ret = util.load_batch(parent)
# WARNING: Decompyle incomplete


def overlaid_time_analysis(parent = None):
    sequences = []
    subchannel_indexes = []
    unit_types = []
    unit_names = []
    unit_infos = []
    names = []
    ret = util.load_batch(parent)
# WARNING: Decompyle incomplete

