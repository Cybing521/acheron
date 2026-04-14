# Source Generated with Decompyle++
# File: tmpbxothkh3.marshal (Python 3.11)


try:
    remote = self.controller_remotes.pop(controller)
    self.remote_connecting.emit(remote, None)
except KeyError:
    pass

if controller in self.active_scan_ongoing:
    return None
ongoing_scan_serials = None(self.active_scan_ongoing.values())
for scan in scans:
    if scan.serial_number in self.active_scans:
        continue
    if scan.serial_number in ongoing_scan_serials:
        continue
    if scan.bootloader:
        continue
    if not scan.board_info and self.active_scan_desired:
        continue
    self.active_scan_ongoing[controller] = scan.serial_number
    controller.start_active_scan(scan.serial_number, scan.bootloader)
    return None
    return None
