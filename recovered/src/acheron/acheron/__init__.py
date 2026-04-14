# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import setproctitle
import ctypes
import logging
import multiprocessing
import os
import signal
import sys
from typing import Any
logger = logging.getLogger(__name__)

try:
    from version import version as __version__
except ImportError:
    __version__ = 'UNKNOWN'


def main_is_frozen():
    '''Return True if the script is frozen, False otherwise.'''
    return getattr(sys, 'frozen', False)


def force_exit():
    import atexit
    atexit._run_exitfuncs()
    if sys.platform == 'darwin':
        os.closerange(3, 7)
        os.closerange(8, 4096)
    else:
        os.closerange(3, 4096)
    os._exit(0)


def shutdown_signal(*args):
    QtCore = QtCore
    import PySide6
    QtCore.QCoreApplication.quit()


def main_init(main_process_title = None):
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    setproctitle.setproctitle(main_process_title)
    if main_is_frozen():
        cacert = os.path.join(os.path.dirname(sys.executable), 'botodata', 'cacert.pem')
        os.environ['AWS_CA_BUNDLE'] = cacert
        botodata = os.path.join(os.path.dirname(sys.executable), 'botodata')
        os.environ['AWS_DATA_PATH'] = botodata
    elif sys.platform == 'win32':
        myappid = 'com.sprocktech.' + main_process_title + '.' + __version__
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    if not sys.stdout or sys.stderr:
        sys.stdout = open(os.devnull)
        sys.stderr = open(os.devnull)
    QtCore = QtCore
    import PySide6
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)
    signal.signal(signal.SIGINT, shutdown_signal)
    signal.signal(signal.SIGTERM, shutdown_signal)

if __name__ == '__main__':
    from gui import __main__
    __main__.main()
    return None
