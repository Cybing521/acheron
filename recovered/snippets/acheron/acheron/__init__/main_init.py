# Source Generated with Decompyle++
# File: tmp0yq0u3nt.marshal (Python 3.11)

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
