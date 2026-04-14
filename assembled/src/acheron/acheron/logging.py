# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

import datetime
import faulthandler
import logging
import logging
import logging.handlers
import os
import sys
import time
from types import TracebackType
from typing import Optional
from PySide6 import QtCore
from .device_logging import OptionalDeviceStringFilter
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class GUILogFormatter(logging.Formatter):

    __doc__ = '\n    a logging.Formatter to only show basic exception info (e.g. no stack) and\n    show "ERROR - " or "WARNING - " at the beginning of the message as relevant\n    '

    def __init__(self):
        super().__init__(
            '[%(asctime)s] %(optdevice)s%(optlevel)s%(message)s',
            '%Y-%m-%dT%H:%M:%SZ',
            defaults={'optlevel': ''},
        )
        return None

    def format(self, record):
        if record.levelno >= logging.WARNING:
            record.optlevel = record.levelname + ' - '
        s = super().format(record)
        lines = s.split('\n')
        if len(lines) <= 1:
            return s
        return lines[0] + ' | ' + lines[-1]

def _clean_fault_dir(fault_dir):
    with os.scandir(fault_dir) as it:
        for entry in it:
            if not entry.name.endswith('.log') or not entry.is_file():
                continue
            try:
                if entry.stat().st_size == 0:
                    os.unlink(os.path.join(fault_dir, entry.name))
            except OSError:
                continue
    return None

def setup_logging(console):
    def my_excepthook(exctype=None, value=None, traceback=None):
        exc_info = (exctype, value, traceback)
        logger.error('Uncaught Exception', exc_info=exc_info)

    sys.excepthook = my_excepthook
    logdir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation)
    logfile = os.path.join(logdir, 'main.log')
    os.makedirs(logdir, exist_ok=True)
    optdevice_filter = OptionalDeviceStringFilter('[%s] ', '')
    file_log_handler = logging.handlers.RotatingFileHandler(
        logfile,
        maxBytes=int(1e+07),
        backupCount=9,
        encoding='utf-8',
    )
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(optdevice)s%(message)s')
    file_formatter.default_time_format = '%Y-%m-%dT%H:%M:%S'
    file_formatter.default_msec_format = '%s,%03dZ'
    file_formatter.converter = time.gmtime
    file_log_handler.addFilter(optdevice_filter)
    file_log_handler.setFormatter(file_formatter)
    file_log_handler.setLevel(logging.DEBUG)
    root_logger = logging.getLogger()
    root_logger.addHandler(file_log_handler)
    root_logger.setLevel(logging.DEBUG)
    if console:
        console_formatter = logging.Formatter('[%(asctime)s] %(optdevice)s%(message)s')
        console_formatter.default_time_format = '%Y-%m-%dT%H:%M:%S'
        console_formatter.default_msec_format = '%s,%03dZ'
        console_formatter.converter = time.gmtime
        console_handler = logging.StreamHandler()
        console_handler.addFilter(optdevice_filter)
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)
    else:
        from acheron.gui.gui_log import GUILogHandler

        nodevice_filter = OptionalDeviceStringFilter('%.0s', '[*] ')
        gui_formatter = GUILogFormatter()
        gui_formatter.converter = time.gmtime
        gui_handler = GUILogHandler()
        gui_handler.addFilter(nodevice_filter)
        gui_handler.setFormatter(gui_formatter)
        gui_handler.setLevel(logging.INFO)
        root_logger.addHandler(gui_handler)
    pyusb_logger = logging.getLogger('usb')
    pyusb_logger.propagate = False
    logging.getLogger('boto3').setLevel(logging.INFO)
    logging.getLogger('botocore').setLevel(logging.INFO)
    logging.getLogger('s3transfer').setLevel(logging.INFO)
    logging.getLogger('urllib3').setLevel(logging.INFO)
    logging.getLogger('pymodbus').setLevel(logging.INFO)
    fault_dir = os.path.join(logdir, 'fault')
    os.makedirs(fault_dir, exist_ok=True)
    dt = datetime.datetime.now(tz=datetime.timezone.utc)
    dt_str = dt.strftime('fault_%Y%m%dT%H%M%SZ.log')
    fault_filename = os.path.join(fault_dir, dt_str)
    _clean_fault_dir(fault_dir)
    fault_file = open(fault_filename, 'wt')
    faulthandler.enable(fault_file)
    return None
