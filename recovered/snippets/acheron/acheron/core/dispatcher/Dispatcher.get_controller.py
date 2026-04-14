# Source Generated with Decompyle++
# File: tmp6lpdj9aa.marshal (Python 3.11)

if len(serial_numbers) > 1:
    party = f'''parent-{serial_numbers[-1]}'''
    parent_controller = self.get_controller(serial_numbers[:-1], party)
else:
    parent_controller = None
controller = self._update_or_create_controller(serial_numbers, None, None, parent_controller, {
    registration_str})
return controller
