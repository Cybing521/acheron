# Source Generated with Decompyle++
# File: tmp74xe3nki.marshal (Python 3.11)

self.logger.debug('Jumping to bootloader')
serial_number = self.device.get_serial_number()
self.device.bootloader_jump()
self.device.reconnect(bootloader = True, serial_number = serial_number)
