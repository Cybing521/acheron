# Source Generated with Decompyle++
# File: tmp97n0e8xo.marshal (Python 3.11)

(sn, ok) = QtWidgets.QInputDialog.getInt(self, self.tr('Bootloader Serial'), self.tr('Input bootloader serial number'))
if not ok:
    return None
None.controller.set_remote_target(sn, True)
