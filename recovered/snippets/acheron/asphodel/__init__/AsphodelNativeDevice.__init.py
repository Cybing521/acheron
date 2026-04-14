# Source Generated with Decompyle++
# File: tmpwrfahj80.marshal (Python 3.11)

self.lib = lib
self.device = device
self._callbacks = []
self._remote = None
if self.get_transport_type() == 'usb':
    self.reconnect_time = 5
else:
    self.reconnect_time = 10
if self.lib:
    self.lib.device_list.add(self)
    return None
