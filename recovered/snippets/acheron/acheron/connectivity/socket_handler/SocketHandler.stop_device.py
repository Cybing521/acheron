# Source Generated with Decompyle++
# File: tmpea82v9i_.marshal (Python 3.11)

socket_transmitter = self.socket_transmitters.pop(serial_number, None)
if socket_transmitter:
    socket_transmitter.stop()
ports = self.device_ports.pop(serial_number, None)
if ports:
    for port in ports:
        del self.used_ports[port]
        return None
        return None
