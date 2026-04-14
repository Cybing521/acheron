# Source Generated with Decompyle++
# File: tmprj2r7zcq.marshal (Python 3.11)

scan = self.get_selected_scan()
if scan:
    self.controller.set_remote_target(scan.serial_number, scan.bootloader)
    return None
