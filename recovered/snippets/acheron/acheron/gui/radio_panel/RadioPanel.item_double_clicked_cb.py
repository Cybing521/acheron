# Source Generated with Decompyle++
# File: tmp3kgapvyc.marshal (Python 3.11)

self.handle_device_list_additions()
row = self.deviceList.row(item)
if row != -1:
    serial_number = self.scan_serials[row]
    scan = self.scans.get(serial_number)
    if scan:
        self.controller.set_remote_target(scan.serial_number, scan.bootloader)
        return None
    return None
