# Source Generated with Decompyle++
# File: tmphvk6thhp.marshal (Python 3.11)

app_name = QtWidgets.QApplication.applicationName()
version = QtWidgets.QApplication.applicationVersion()
is_frozen = getattr(sys, 'frozen', False)
if is_frozen:
    title = self.tr('{} ({})').format(app_name, version)
else:
    title = self.tr('{} (dev)').format(app_name)
self.setWindowTitle(title)
self.warningLabel.setVisible(False)
# WARNING: Decompyle incomplete
