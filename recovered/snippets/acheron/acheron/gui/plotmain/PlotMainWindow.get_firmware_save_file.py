# Source Generated with Decompyle++
# File: tmped3_bd3l.marshal (Python 3.11)

directory = self.settings.value('fileSaveDirectory')
if directory:
    if isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = ''
        else:
            directory = ''
    else:
        directory = ''
file_and_dir = os.path.join(directory, default_name)
caption = self.tr('Save Firmware File')
file_filter = self.tr('Firmware Files (*.firmware);;All Files (*.*)')
val = QtWidgets.QFileDialog.getSaveFileName(self, caption, file_and_dir, file_filter)
output_path = val[0]
if output_path:
    output_dir = os.path.dirname(output_path)
    self.settings.setValue('fileSaveDirectory', output_dir)
    return output_path
