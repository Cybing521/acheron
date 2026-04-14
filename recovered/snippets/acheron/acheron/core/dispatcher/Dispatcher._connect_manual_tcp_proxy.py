# Source Generated with Decompyle++
# File: tmpbzrvgi8v.marshal (Python 3.11)


try:
    device = asphodel.create_tcp_device(hostname, port, timeout, serial_number)
except asphodel.AsphodelError:
    logger.exception('Could not connect to TCP device.')
    if err_cb:
        err_cb()
    return None

adv = device.tcp_get_advertisement()
found_serial_number = adv.serial_number
location = device.get_location_string()
reconnect_info = {
    'type': 'manual_tcp',
    'location': location,
    'serial_number': found_serial_number,
    'hostname': hostname,
    'port': port,
    'timeout': timeout }
f = functools.partial(self._create_proxy, found_serial_number, location, reconnect_info, connect_and_open_tcp_device, hostname, port, timeout, found_serial_number)
self._create_signal.emit(f)
