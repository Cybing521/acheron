# Source Generated with Decompyle++
# File: tmpcd_hxssp.marshal (Python 3.11)

scan = self.get_selected_scan()
if scan:
    self.controller.set_remote_target(scan.serial_number, scan.bootloader, streaming = False)
    return None
