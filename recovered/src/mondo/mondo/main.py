# Source Generated with Decompyle++
# File: main.pyc (Python 3.11)

import importlib
import logging
import os
import subprocess
import sys
import tempfile
import threading
from typing import Callable, Concatenate, Optional, ParamSpec
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from hyperborea.dark_mode import set_style
import hyperborea.download as hyperborea
from hyperborea.preferences import read_bool_setting
from ui.ui_main import Ui_MondoMainWindow
from about import AboutDialog
from analysis import csv, file, psd, spectrogram, time
from preferences import PreferencesDialog
logger = logging.getLogger(__name__)
P = ParamSpec('P')

class MondoMainWindow(QtWidgets.QMainWindow, Ui_MondoMainWindow):
    pass
# WARNING: Decompyle incomplete

