# Source Generated with Decompyle++
# File: tmpbxtv8s4a.marshal (Python 3.11)

if not asphodel.nativelib.usb_devices_supported:
    return None
locations = None.get_proxy_locations()
usb_keys = self._collect_new_usb_device_keys(locations)
for serial_number, location in usb_keys:
    self.create_usb_proxy(serial_number, location)
    return None
