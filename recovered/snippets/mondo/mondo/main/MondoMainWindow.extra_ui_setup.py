# Source Generated with Decompyle++
# File: tmpvwlmo7gv.marshal (Python 3.11)

app_name = QtWidgets.QApplication.applicationName()
is_frozen = getattr(sys, 'frozen', False)
if is_frozen:
    version = QtWidgets.QApplication.applicationVersion()
    title = self.tr('{} ({})').format(app_name, version)
else:
    title = self.tr('{} (dev)').format(app_name)
self.setWindowTitle(title)
self.update_progress = QtWidgets.QProgressDialog('', '', 0, 100)
self.update_progress.setLabelText(self.tr(''))
self.update_progress.setWindowTitle(self.tr('Check for Update'))
self.update_progress.setCancelButton(None)
self.update_progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
self.update_progress.setMinimumDuration(0)
self.update_progress.setAutoReset(False)
self.update_progress.reset()
