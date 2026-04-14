# Source Generated with Decompyle++
# File: tmpwaydxv8n.marshal (Python 3.11)

(commit, ok) = QtWidgets.QInputDialog.getText(self, self.tr('Commit'), self.tr('Commit:'), QtWidgets.QLineEdit.EchoMode.Normal, '')
if not ok:
    return None
commit = None.strip()
self.find_update(commit = commit)
