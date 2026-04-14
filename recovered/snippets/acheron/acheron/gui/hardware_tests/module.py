# Source Generated with Decompyle++
# File: tmp0pjryl92.marshal (Python 3.11)

import datetime
import functools
import logging
import os
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel import AsphodelStreamInfo, AsphodelChannelInfo, SupplyInfo
from asphodel.device_info import DeviceInfo
from device_logging import DeviceLoggerAdapter
from core.device_controller import DeviceController
from core.preferences import Preferences
from device_process.hardware_test_funcs import accel_test, bridge_test, supply_test
from device_process.stream_controller import HardwareTestFunction
from ui.ui_hardware_tests import Ui_HardwareTestDialog
logger = logging.getLogger(__name__)
TestInstance = tuple[(HardwareTestFunction, str)]

class HardwareTestDialog(QtWidgets.QDialog, Ui_HardwareTestDialog):
    pass
# WARNING: Decompyle incomplete

