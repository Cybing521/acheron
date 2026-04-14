# Source Generated with Decompyle++
# File: tmpsge1w5dw.marshal (Python 3.11)

import logging
import os
import struct
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from ui.ui_device_info_dialog import Ui_DeviceInfoDialog
logger = logging.getLogger(__name__)

def format_bitrate(bitrate = None):
    scales = [
        (1, 'bit/s'),
        (1000, 'kbit/s'),
        (1e+06, 'Mbit/s'),
        (1e+09, 'Gbit/s')]
    for factor, suffix in scales:
        if bitrate < factor * 1000:
            
            return None, f'''{bitrate / factor:.1f} {suffix}'''
        return f'''{bitrate / 1e+09:.3f} Gbit/s'''


class DeviceInfoDialog(QtWidgets.QDialog, Ui_DeviceInfoDialog):
    pass
# WARNING: Decompyle incomplete

