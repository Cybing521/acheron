# Source Generated with Decompyle++
# File: tmp12tymqfx.marshal (Python 3.11)

self.finished.set()
for socket_transmitter in self.socket_transmitters.values():
    socket_transmitter.stop()
    self.socket_transmitters.clear()
    self.device_ports.clear()
    self.used_ports.clear()
    return None
