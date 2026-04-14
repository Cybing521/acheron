# Source Generated with Decompyle++
# File: tmp3r0z3v6_.marshal (Python 3.11)

devices = asphodel.find_usb_devices()
for device in devices:
    device_location_string = device.get_location_string()
    if device_location_string == location:
        device.open()
        
        return None, device
    return None
