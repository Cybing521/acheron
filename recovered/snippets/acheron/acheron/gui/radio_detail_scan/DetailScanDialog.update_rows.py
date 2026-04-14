# Source Generated with Decompyle++
# File: tmp6okostp5.marshal (Python 3.11)

self.tableWidget.setUpdatesEnabled(False)
header = self.tableWidget.horizontalHeader()
header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)

try:
    scan = self.scans_to_process.popleft()
    row_info = self.row_info.get(scan.serial_number)
    if row_info:
        old_scan = row_info.scan
        self.update_table_items(row_info.table_items, scan, old_scan)
        row_info.scan = scan
    continue
except IndexError:
    pass

now = datetime.datetime.now(datetime.timezone.utc)
for row_info in self.row_info.values():
    if row_info.connected_radio:
        continue
    self.update_last_seen(row_info, now)
    header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
    self.tableWidget.setUpdatesEnabled(True)
    return None
