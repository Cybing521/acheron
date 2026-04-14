# Source Generated with Decompyle++
# File: tmprmj_e90z.marshal (Python 3.11)

reconnect_info = {
    'type': 'remote',
    'serial_number': serial_number_str }
parent_sn = controller.serial_number
serial_numbers = (parent_sn, serial_number_str)
new_controller = self._update_or_create_controller(serial_numbers, None, reconnect_info, controller, parties)
self._start_proxy(subproxy, new_controller)
return new_controller
