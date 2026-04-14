# Source Generated with Decompyle++
# File: tmp41ayrz4v.marshal (Python 3.11)

QtCore.QCoreApplication.processEvents()
tcp_scanned = False
tcp_devices = []
if self.preferences.initial_connect_usb or self.preferences.rescan_connect_usb:
    self.rescan_usb()
if (self.preferences.initial_connect_tcp or self.preferences.rescan_connect_tcp) and asphodel.nativelib.tcp_devices_supported:
    tcp_devices = asphodel.find_tcp_devices()
    tcp_scanned = True
    locations = self.get_proxy_locations()
    for device in tcp_devices:
        adv = device.tcp_get_advertisement()
        if adv.connected:
            continue
        serial_number = adv.serial_number
        location = device.get_location_string()
        if location not in locations:
            logger.debug('Connecting TCP device %s', serial_number)
            self.create_tcp_proxy(serial_number, location)
        create = set()
        self.lock
        for serial_number in self.preferences.initial_serials:
            serial_number = serial_number.strip()
            if not serial_number:
                continue
            if serial_number not in self.controllers:
                create.add(serial_number)
            None(None, None)
        with None:
            if not None:
                pass
for serial_number in create:
    controller = self._update_or_create_controller((serial_number,), None, None, None, set())
    self.lock
    self.disconnected_controllers.add(controller)
    None(None, None)
with None:
    if not None:
        pass
continue
self.initial_devices_connected.emit(tcp_scanned, tcp_devices)
self.background_connect_thread.start()
