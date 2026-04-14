# Source Generated with Decompyle++
# File: tmpaxyywdix.marshal (Python 3.11)

(sn, ok) = QtWidgets.QInputDialog.getInt(self, self.tr('Device Serial'), self.tr('Input device serial number'))
if not ok:
    return None
None.controller.set_remote_target(sn, False)
