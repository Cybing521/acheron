# Source Generated with Decompyle++
# File: tmp1_vv60se.marshal (Python 3.11)

text_elements = []
active_scan = self.active_scan_database.get_active_scan(scan.serial_number)
if scan.serial_number != 0xFFFFFFFF:
    text_elements.append(str(scan.serial_number))
else:
    text_elements.append('Any')
if scan.serial_number == self.controller.default_remote_target:
    text_elements.append('<Auto>')
# WARNING: Decompyle incomplete
