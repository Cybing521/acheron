# Source Generated with Decompyle++
# File: tmppbvcibbl.marshal (Python 3.11)

keys = set()
for device in asphodel.find_tcp_devices():
    adv = device.tcp_get_advertisement()
    if adv.connected:
        continue
    location = device.get_location_string()
    serial_number = adv.serial_number
    if location not in locations:
        keys.add((serial_number, location))
    return keys
