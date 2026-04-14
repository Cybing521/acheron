# Source Generated with Decompyle++
# File: tmp7dm06gpk.marshal (Python 3.11)


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
