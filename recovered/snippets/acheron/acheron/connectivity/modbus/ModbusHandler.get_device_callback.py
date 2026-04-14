# Source Generated with Decompyle++
# File: tmp74gw7s04.marshal (Python 3.11)

device_prefs = get_device_preferences(serial_number)
if not device_prefs.modbus_enable:
    return None
device_logger = None(logger, serial_number)
register_offset = device_prefs.modbus_register_offset
# WARNING: Decompyle incomplete
