# Source Generated with Decompyle++
# File: tmpeu6_wrbf.marshal (Python 3.11)

dialog = TCPScanDialog(self.dispatcher, self.preferences, initial_devices, self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    devices = None.get_selected_devices()
    dialog.deleteLater()
except:
    dialog.deleteLater()

for device in devices:
    self.dispatcher.create_tcp_proxy_from_device(device)
    return None
