# Source Generated with Decompyle++
# File: tmphju9f6vk.marshal (Python 3.11)

settings = QtCore.QSettings()
directory = settings.value('fileSaveDirectory')
if directory and isinstance(directory, str):
    if not os.path.isdir(directory):
        directory = None
    else:
        directory = None
if not directory:
    directory = ''
file_and_dir = os.path.join(directory, default_name)
caption = 'Save File'
file_filter = 'Python Script (*.py);;All Files (*.*)'
val = QtWidgets.QFileDialog.getSaveFileName(parent, caption, file_and_dir, file_filter)
output_path = val[0]
if output_path:
    output_dir = os.path.dirname(output_path)
    settings.setValue('fileSaveDirectory', output_dir)
    return output_path
