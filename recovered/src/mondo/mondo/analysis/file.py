# Source Generated with Decompyle++
# File: file.pyc (Python 3.11)

import datetime
import json
import logging
import lzma
import os
import struct
from typing import Iterable, Optional
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as matplotlib
import numpy
from PySide6 import QtCore, QtWidgets
from asphodel.device_info import DeviceInfo
from hyperborea.device_info_dialog import DeviceInfoDialog
from  import util
from setting_viewer import SettingViewerDialog
logger = logging.getLogger(__name__)

def get_save_file(default_name = None, parent = None):
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


def file_information(parent = None):
    ret = util.load_single_file(parent)
# WARNING: Decompyle incomplete


def view_settings(parent = None):
    ret = util.load_single_file(parent)
# WARNING: Decompyle incomplete


def raw_export(parent = None):
    filename = util.get_packdata_file(parent)
# WARNING: Decompyle incomplete


def split_file(parent = None):
    sequences = []
    unit_types = []
    unit_names = []
    ret = util.load_single_file(parent)
# WARNING: Decompyle incomplete

