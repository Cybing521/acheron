# Source Generated with Decompyle++
# File: tmpf3e0hdpq.marshal (Python 3.11)

self.deviceList.clear()
self.scan_serials.clear()
self.device_list_additions.clear()
restore_scans = { }
if connected_serial:
    scan = self._get_placeholder_scan(connected_serial, connected_bootloader)
    scan.scan_strength = None
    restore_scans[connected_serial] = scan
if self.controller.default_remote_target and self.controller.default_remote_target != connected_serial:
    scan = self._get_placeholder_scan(self.controller.default_remote_target, False)
    scan.scan_strength = None
    scan.bootloader = False
    restore_scans[self.controller.default_remote_target] = scan
for i, serial_number in enumerate(sorted(restore_scans.keys())):
    scan = restore_scans[serial_number]
    list_item = QtWidgets.QListWidgetItem()
    self.update_list_item(list_item, scan)
    self.scan_serials.append(scan.serial_number)
    self.deviceList.insertItem(i, list_item)
    if serial_number == connected_serial:
        self.deviceList.setCurrentRow(i)
    self.update_scan_count()
    return None
