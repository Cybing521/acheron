# Source Generated with Decompyle++
# File: tmpj_e00vac.marshal (Python 3.11)

import logging
import os
import re
from xml.dom.minidom import getDOMImplementation
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from hyperborea.preferences import read_int_setting
from connectivity.modbus import get_numeric_serial
from calc_process.types import ChannelInformation
from core.preferences import DevicePreferences
from ui.ui_connectivity_dialog import Ui_ConnectivityDialog
logger = logging.getLogger(__name__)

class ConnectivityDialog(QtWidgets.QDialog, Ui_ConnectivityDialog):
    pass
# WARNING: Decompyle incomplete

