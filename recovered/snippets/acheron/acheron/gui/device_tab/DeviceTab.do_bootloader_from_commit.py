# Source Generated with Decompyle++
# File: tmpltyjyfah.marshal (Python 3.11)

(commit, ok) = QtWidgets.QInputDialog.getText(self, self.tr('Firmware Commit'), self.tr('Firmware Commit:'), QtWidgets.QLineEdit.EchoMode.Normal, '')
if not ok:
    return None
commit = None.strip()
self.do_bootloader_web(build_type = None, commit = commit)
