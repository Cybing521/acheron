# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

import datetime
import faulthandler
import logging
import logging.handlers as logging
import os
import sys
import time
from types import TracebackType
from typing import Optional
from PySide6 import QtCore
from device_logging import OptionalDeviceStringFilter
logger = logging.getLogger(__name__)

class GUILogFormatter(logging.Formatter):
    pass
# WARNING: Decompyle incomplete


def _clean_fault_dir(fault_dir = None):
    it = os.scandir(fault_dir)
    for entry in it:
        if entry.name.endswith('.log') and entry.is_file():
            stat = entry.stat()
            if stat.st_size == 0:
                filename = os.path.join(fault_dir, entry.name)
                os.unlink(filename)
                continue
                except OSError:
                    continue
        None(None, None)
        return None
        with None:
            if not None:
                pass


def setup_logging(console = None):
    '''Configure logging for the whole program.'''
    
    def my_excepthook(exctype = None, value = None, traceback = None):
        '''Log the caught exception using the logging module.'''
        exc_info = (exctype, value, traceback)
        logger.error('Uncaught Exception', exc_info = exc_info)

    sys.excepthook = my_excepthook
    logdir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation)
    logfile = os.path.join(logdir, 'main.log')
    os.makedirs(logdir, exist_ok = True)
    optdevice_filter = OptionalDeviceStringFilter('[%s] ', '')
    file_log_handler = logging.handlers.RotatingFileHandler(logfile, maxBytes = int(1e+07), backupCount = 9, encoding = 'utf-8')
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
        nodevice_filter = OptionalDeviceStringFilter('%.0s', '[*] ')
        gui_formatter = GUILogFormatter()
        gui_formatter.converter = time.gmtime
        GUILogHandler = GUILogHandler
        import gui.gui_log
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
    os.makedirs(fault_dir, exist_ok = True)
    dt = datetime.datetime.now(tz = datetime.timezone.utc)
    dt_str = dt.strftime('fault_%Y%m%dT%H%M%SZ.log')
    fault_filename = os.path.join(fault_dir, dt_str)
    _clean_fault_dir(fault_dir)
    fault_file = open(fault_filename, 'wt')
    faulthandler.enable(fault_file)

