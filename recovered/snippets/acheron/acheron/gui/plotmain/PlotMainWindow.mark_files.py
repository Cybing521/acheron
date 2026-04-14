# Source Generated with Decompyle++
# File: tmpg1t8j9iy.marshal (Python 3.11)

file_filter = self.tr('Data Files (*.apd)')
val = QtWidgets.QFileDialog.getOpenFileNames(self, self.tr('Select Files'), self.preferences.base_dir, file_filter)
files = val[0]
self.dispatcher.mark_for_upload(files)
