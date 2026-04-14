# Source Generated with Decompyle++
# File: tmpkfqylemi.marshal (Python 3.11)

settings = QtCore.QSettings()
directory = settings.value('fileOpenDirectory')
if directory and isinstance(directory, str):
    if not os.path.isdir(directory):
        directory = None
    else:
        directory = None
if not directory:
    directory = ''
caption = 'Open File'
file_filter = 'Packed Data Files (*.apd);;All Files (*.*)'
val = QtWidgets.QFileDialog.getOpenFileName(parent, caption, directory, file_filter)
output_path = val[0]
if output_path:
    output_dir = os.path.dirname(output_path)
    settings.setValue('fileOpenDirectory', output_dir)
    return output_path
