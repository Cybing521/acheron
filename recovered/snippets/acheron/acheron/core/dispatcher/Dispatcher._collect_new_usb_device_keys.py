# Source Generated with Decompyle++
# File: tmph7uqcqv6.marshal (Python 3.11)

keys = set()
for device in asphodel.find_usb_devices():
    location = device.get_location_string()
    device.close()
device.close()
keys.add((serial_number, location))
continue
return keys
