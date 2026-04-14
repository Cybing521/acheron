# Source Generated with Decompyle++
# File: tmpiq52qjyl.marshal (Python 3.11)

scan = self.scans.get(serial_number)
if scan:
    return scan
now = None.datetime.now(datetime.timezone.utc)
scan = ScanResult(serial_number = serial_number, last_seen = now, bootloader = bootloader, asphodel_type = 0, device_mode = 0, scan_strength = None, board_info = None)
self.scans[serial_number] = scan
return scan
