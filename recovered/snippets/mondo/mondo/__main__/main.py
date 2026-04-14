# Source Generated with Decompyle++
# File: tmp6h59yvi7.marshal (Python 3.11)

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
