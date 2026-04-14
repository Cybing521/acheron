# Source Generated with Decompyle++
# File: tmpwq5wjugn.marshal (Python 3.11)

file = os.path.abspath(file)
if sys.platform == 'win32':
    subprocess.Popen([
        'explorer',
        '/select,',
        file])
    return None
if None.platform == 'darwin':
    args = [
        'osascript',
        '-e',
        'tell application "Finder"',
        '-e',
        'activate',
        '-e',
        f'''select POSIX file "{file}"''',
        '-e',
        'end tell']
    subprocess.Popen(args)
    return None
url = None.QUrl.fromLocalFile(os.path.dirname(file))
QtGui.QDesktopServices.openUrl(url)
