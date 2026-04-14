# Source Generated with Decompyle++
# File: tmpd0m8ajvt.marshal (Python 3.11)

logdir = os.path.abspath(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation))
logfile = os.path.join(logdir, 'main.log')
if sys.platform == 'win32':
    subprocess.Popen([
        'explorer',
        '/select,',
        logfile])
    return None
if None.platform == 'darwin':
    args = [
        'osascript',
        '-e',
        'tell application "Finder"',
        '-e',
        'activate',
        '-e',
        f'''select POSIX file "{logfile}"''',
        '-e',
        'end tell']
    subprocess.Popen(args)
    return None
url = None.QUrl.fromLocalFile(logdir)
QtGui.QDesktopServices.openUrl(url)
