# Source Generated with Decompyle++
# File: tmp_rmcsyfz.marshal (Python 3.11)

self.logger.debug('Resetting device')
serial_number = self.device.get_serial_number()
self.device.reset()
self._reconnect_device_locked(serial_number = serial_number)
