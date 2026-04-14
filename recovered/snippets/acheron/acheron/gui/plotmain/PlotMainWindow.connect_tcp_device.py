# Source Generated with Decompyle++
# File: tmpjup5onj5.marshal (Python 3.11)

dialog = TCPConnectDialog(self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    results = None.get_results()
    dialog.deleteLater()
except:
    dialog.deleteLater()

self.dispatcher.create_manual_tcp_proxy(hostname = results['hostname'], port = results['port'], timeout = 1000, serial_number = results['serial_number'], err_cb = self.connect_tcp_device_error)
