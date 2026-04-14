# Source Generated with Decompyle++
# File: tmph8tp9nu3.marshal (Python 3.11)

serial_number = self.device_info.serial_number
default_name = f'''{serial_number}.txt'''
settings = QtCore.QSettings()
directory = settings.value('infoSaveDirectory')
if not directory or isinstance(directory, str):
    directory = None
elif not os.path.isdir(directory):
    directory = None
if not directory:
    directory = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
file_and_dir = os.path.join(directory, default_name)
caption = self.tr('Save Device Information')
file_filter = self.tr('Text Files (*.txt);;All Files (*.*)')
val = QtWidgets.QFileDialog.getSaveFileName(self, caption, file_and_dir, file_filter)
output_path = val[0]
if output_path:
    output_dir = os.path.dirname(output_path)
    settings.setValue('infoSaveDirectory', output_dir)
    return os.path.abspath(output_path)
