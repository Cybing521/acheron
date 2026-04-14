# Source Generated with Decompyle++
# File: tmp6ipsouih.marshal (Python 3.11)

import datetime
import functools
import logging
import math
import os.path as os
from typing import Optional
import numpy
from PySide6 import QtCore, QtWidgets
from  import util
logger = logging.getLogger(__name__)

def get_csv_file(default_name = None, parent = None):
    settings = QtCore.QSettings()
    directory = settings.value('fileSaveDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
        else:
            directory = None
    if not directory:
        directory = ''
    file_and_dir = os.path.join(directory, default_name)
    caption = 'Save File'
    file_filter = 'Comma Seperated Value Files (*.csv);;All Files (*.*)'
    val = QtWidgets.QFileDialog.getSaveFileName(parent, caption, file_and_dir, file_filter)
    output_path = val[0]
    if output_path:
        output_dir = os.path.dirname(output_path)
        settings.setValue('fileSaveDirectory', output_dir)
        return output_path


def do_downsample(array, downsample_factor):
    pad_size = downsample_factor - array.size % downsample_factor
    if pad_size == downsample_factor:
        pad_size = 0
    padded_array = numpy.append(array, numpy.zeros(pad_size) * numpy.nan)
    reshaped = padded_array.reshape((-1, downsample_factor))
    result = numpy.nanmean(reshaped, axis = 1)
    return result


def csv_export(parent = None, downsample = None):
    pass
# WARNING: Decompyle incomplete

