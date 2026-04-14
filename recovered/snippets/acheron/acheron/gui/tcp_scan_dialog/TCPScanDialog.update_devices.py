# Source Generated with Decompyle++
# File: tmp8yqi9i_2.marshal (Python 3.11)

connected_location_strs = self.dispatcher.get_proxy_locations()
existing_serials = set()
for device in devices:
    adv = device.tcp_get_advertisement()
    serial_number = adv.serial_number
    existing_serials.add(serial_number)
    location_str = device.get_location_string()
    connected = location_str in connected_location_strs
    row_info = self.row_info.get(serial_number)
    if not row_info:
        table_items = self.add_row(serial_number)
        row_info = RowInformation(table_items)
        self.row_info[serial_number] = row_info
    self.update_row_with_device(row_info, device, connected)
    old_serials = set(self.row_info.keys())
    old_serials.difference_update(existing_serials)
    for serial_number in old_serials:
        self.remove_row(serial_number)
        self.selection_changed()
        return None
