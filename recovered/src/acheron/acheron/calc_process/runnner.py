# Source Generated with Decompyle++
# File: runnner.pyc (Python 3.11)

import logging
from logging.handlers import QueueListener
import multiprocessing
from multiprocessing.connection import Connection
import threading
from typing import Any, Optional
from PySide6 import QtCore
from hyperborea.namedprocess import NamedProcess
from device_logging import DeviceLoggerAdapter, RemoteToLocalLogHandler
from remote import run_calc_runner
from types import CalcControl, CalcData, CalcSettings, Trigger
logger = logging.getLogger(__name__)

class CalcProcess(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

