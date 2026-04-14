# Source Generated with Decompyle++
# File: tmppcd__u_0.marshal (Python 3.11)

dialog = DownloadFirmwareDialog(self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    results = None.get_results()
    dialog.deleteLater()
except:
    dialog.deleteLater()

# WARNING: Decompyle incomplete
