# Source Generated with Decompyle++
# File: tmp9a89hrr4.marshal (Python 3.11)

self.handle_device_list_additions()
row = self.deviceList.currentRow()
if row == -1:
    return None
serial_number = None.scan_serials[row]
return self.scans.get(serial_number)
