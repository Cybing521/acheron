# Source Generated with Decompyle++
# File: tmprgu8oh2c.marshal (Python 3.11)

import ctypes
import logging.handlers as logging
import multiprocessing
import os
import sys
import time
from PySide6 import QtCore, QtGui, QtWidgets
import mondo
from mondo.export_script import matplotlib_wrapper as matplotlib
from main import MondoMainWindow
from  import mondo_rc
logger = logging.getLogger(__name__)

def main_is_frozen():
    '''Return True if the script is frozen, False otherwise.'''
    return getattr(sys, 'frozen', False)


def setup_logging():
    '''Configure logging for the whole program.'''
    
    def my_excepthook(exctype, value, traceback):
        '''Log the caught exception using the logging module.'''
        exc_info = (exctype, value, traceback)
        logger.error('Uncaught Exception', exc_info = exc_info)

    sys.excepthook = my_excepthook
    logdir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation)
    logfile = os.path.join(logdir, 'main.log')
    os.makedirs(logdir, exist_ok = True)
    file_log_handler = logging.handlers.RotatingFileHandler(logfile, maxBytes = int(5e+07), backupCount = 1, encoding = 'utf-8')
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_formatter.default_time_format = '%Y-%m-%dT%H:%M:%S'
    file_formatter.default_msec_format = '%s,%03dZ'
    file_formatter.converter = time.gmtime
    file_log_handler.setFormatter(file_formatter)
    file_log_handler.setLevel(logging.DEBUG)
    root_logger = logging.getLogger()
    root_logger.addHandler(file_log_handler)
    root_logger.setLevel(logging.DEBUG)
    pyusb_logger = logging.getLogger('usb')
    pyusb_logger.propagate = False
    matplotlib_logger = logging.getLogger('matplotlib')
    matplotlib_logger.setLevel(logging.INFO)


def main():
    '''Run the program.'''
    multiprocessing.freeze_support()
    if main_is_frozen() and sys.platform == 'win32':
        myappid = 'com.sprocktech.mondo.' + mondo.__version__
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    if not sys.stdout or sys.stderr:
        sys.stdout = open(os.devnull)
        sys.stderr = open(os.devnull)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Mondo')
    app.setOrganizationDomain('suprocktech.com')
    app.setOrganizationName('Suprock Tech')
    QtGui.QIcon.setThemeName('suprock')
    icon = QtGui.QIcon()
    icon_reader = QtGui.QImageReader(':/mondo.ico')
    pixmap = QtGui.QPixmap.fromImage(icon_reader.read())
    icon.addPixmap(pixmap)
    if not icon_reader.jumpToNextImage():
        pass
    
    app.setWindowIcon(icon)
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)
    app.setStyleSheet('QMessageBox { messagebox-text-interaction-flags: 5; }')
    app.setApplicationVersion(mondo.__version__)
    setup_logging()
    logger.info('Mondo started (Version {})'.format(mondo.__version__))
    app.setStyleSheet('QMessageBox { messagebox-text-interaction-flags: 5; }')
    matplotlib.rc('font', size = 17)
    mainwin = MondoMainWindow()
    mainwin.show()
    app.exec()
    logger.info('Mondo finished')

if __name__ == '__main__':
    main()
    return None
