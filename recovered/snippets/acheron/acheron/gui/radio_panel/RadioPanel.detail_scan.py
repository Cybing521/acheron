# Source Generated with Decompyle++
# File: tmp7g2z8fx7.marshal (Python 3.11)

self.active_scan_database.detail_scan_opened()

try:
    ret = self.detail_scan_dialog.exec()
    self.active_scan_database.detail_scan_closed()
except:
    self.active_scan_database.detail_scan_closed()

if ret == 0:
    return None
scan = None.detail_scan_dialog.get_selected_scan()
if scan:
    self.controller.set_remote_target(scan.serial_number, scan.bootloader)
    return None
