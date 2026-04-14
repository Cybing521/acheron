# Source Generated with Decompyle++
# File: psd_options.pyc (Python 3.11)

import logging
import math
from typing import Literal, Optional, TypedDict
import numpy
from numpy.typing import NDArray
from PySide6 import QtCore, QtWidgets
import scipy.signal.windows as scipy
from ui.ui_psd_options import Ui_PSDOptionsWidget
logger = logging.getLogger(__name__)
Chunk = tuple[(NDArray[numpy.float64], NDArray[numpy.float64], float, float)]

class PSDOptions(TypedDict):
    detrend: Literal[('mean', 'linear', 'none')] = 'PSDOptions'


class PSDOptionsWidget(QtWidgets.QWidget, Ui_PSDOptionsWidget):
    pass
# WARNING: Decompyle incomplete


class PSDOptionsDialog(QtWidgets.QDialog):
    pass
# WARNING: Decompyle incomplete


class MultiplePSDOptionsDialog(QtWidgets.QDialog):
    pass
# WARNING: Decompyle incomplete

