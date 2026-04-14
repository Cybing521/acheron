# Source Generated with Decompyle++
# File: tmpupetxguk.marshal (Python 3.11)

settings = QtCore.QSettings()
directory = settings.value('fileOpenDirectory')
if directory and isinstance(directory, str):
    if not os.path.isdir(directory):
        directory = None
    else:
        directory = None
if not directory:
    directory = ''
caption = 'Open Files'
file_filter = 'Packed Data Files (*.apd);;All Files (*.*)'
val = QtWidgets.QFileDialog.getOpenFileNames(parent, caption, directory, file_filter)
files = val[0]
if files:
    output_dir = os.path.dirname(files[0])
    settings.setValue('fileOpenDirectory', output_dir)
    return sorted(files)
