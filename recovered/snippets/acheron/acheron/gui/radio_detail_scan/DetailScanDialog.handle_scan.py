# Source Generated with Decompyle++
# File: tmpmjmrtjrq.marshal (Python 3.11)

row_info = self.row_info.get(scan.serial_number)
if not row_info:
    table_items = self.add_row(scan.serial_number)
    self.update_table_items(table_items, scan, None)
    row_info = RowInformation(table_items, scan, None, None)
    self.row_info[scan.serial_number] = row_info
    self.update_scan_count()
    controller = self.active_scan_database.get_remote_controller(scan.serial_number)
    if controller:
        self.update_controller(scan.serial_number, controller)
    active_scan = self.active_scan_database.get_active_scan(scan.serial_number)
    if active_scan:
        self.update_active_scan_info(scan.serial_number, active_scan)
    self.update_last_seen(row_info)
    return None
None.scans_to_process.append(scan)
