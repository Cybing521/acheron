# Source Generated with Decompyle++
# File: tmp2ivcy1uf.marshal (Python 3.11)

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
from device_logging import DeviceLoggerAdapter
from core.calibration import get_channel_setting_values, update_nvm
from connectivity.event_upload import EventUploader
from ui.ui_calibration_panel import Ui_CalibrationPanel
from ui.ui_calibration_channel import Ui_CalibrationChannel
if TYPE_CHECKING:
    from device_tab import DeviceTab
logger = logging.getLogger(__name__)
CalibrationConnection = <NODE:12>()

class CalibrationChannel(QtWidgets.QWidget, Ui_CalibrationChannel):
    pass
# WARNING: Decompyle incomplete


class CalibrationPanel(QtWidgets.QGroupBox, Ui_CalibrationPanel):
    pass
# WARNING: Decompyle incomplete

