# Source Generated with Decompyle++
# File: tmpr8gy219f.marshal (Python 3.11)

adv = tcp_device.tcp_get_advertisement()
serial_number = adv.serial_number
location = tcp_device.get_location_string()
self.create_tcp_proxy(serial_number, location)
