# Source Generated with Decompyle++
# File: tmprmgugn8o.marshal (Python 3.11)

self.logger.debug('Jumping to app from bootloader')
serial_number = self.device.get_serial_number()
self.device.bootloader_start_program()
self.device.reconnect(application = True, serial_number = serial_number)
