# Source Generated with Decompyle++
# File: tmpq10mre92.marshal (Python 3.11)

import logging
import sys
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from device_process.proxy import DeviceProxyManager
from acheron import force_exit, main_init, __version__
from acheron.logging import setup_logging
from acheron.core.dispatcher import Dispatcher
from acheron.core.preferences import create_empty_settings, Preferences
from acheron.disk.schedule_reader import ScheduleReader
from plotmain import PlotMainWindow
from  import acheron_rc
logger = logging.getLogger(__name__)
MAIN_PROCESS_NAME: str = 'acheron'
DEVICE_PROCESS_NAME = 'acheron-device'
CALC_PROCESS_NAME = 'acheron-calc'

def main():
    main_init(MAIN_PROCESS_NAME)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Acheron')
    app.setOrganizationDomain('suprocktech.com')
    app.setOrganizationName('Suprock Tech')
    QtGui.QIcon.setThemeName('suprock')
    icon = QtGui.QIcon()
    icon_reader = QtGui.QImageReader(':/acheron.ico')
    pixmap = QtGui.QPixmap.fromImage(icon_reader.read())
    icon.addPixmap(pixmap)
    if not icon_reader.jumpToNextImage():
        pass
    
    app.setWindowIcon(icon)
    app.setApplicationVersion(__version__)
    app.setStyleSheet('QMessageBox { messagebox-text-interaction-flags: 5; }')
    setup_logging()
    create_empty_settings()
    logger.info('Acheron started (Version {})'.format(__version__))
    
    try:
        missing_funcs = asphodel.nativelib.missing_funcs
    except AttributeError:
        missing_funcs = []
        message = 'Asphodel python mismatch!'
        logging.warning(message)
        QtWidgets.QMessageBox.warning(None, 'Warning', message)

    if missing_funcs:
        missing_str = ', '.join(sorted(missing_funcs))
        logging.warning('Missing Asphodel functions: {}'.format(missing_str))
        QtWidgets.QMessageBox.warning(None, 'Warning', 'Asphodel library mismatch!')
    proxy_manager = DeviceProxyManager(DEVICE_PROCESS_NAME)
    preferences = Preferences()
    dispatcher = Dispatcher(proxy_manager, preferences, CALC_PROCESS_NAME)
    schedule_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation)
    schedule_reader = ScheduleReader(schedule_path, dispatcher)
    mainwin = PlotMainWindow(dispatcher, preferences, schedule_reader)
    mainwin.show()
    schedule_reader.start()
    app.exec()
    logger.info('Acheron main window closed')
    schedule_reader.stop()
    dispatcher.stop()
    proxy_manager.stop()
    dispatcher.join()
    logger.info('Acheron finished')
    force_exit()

if __name__ == '__main__':
    main()
    return None
