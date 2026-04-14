# Source Generated with Decompyle++
# File: tmp0gwpfptk.marshal (Python 3.11)

socket_transmitter = self.socket_transmitters.get(serial_number)
if socket_transmitter:
    return socket_transmitter.callback
device_logger = None(logger, serial_number)
device_prefs = get_device_preferences(serial_number)
desired_channel_ports = device_prefs.get_all_channel_ports()
channel_ports = { }
for channel_id, subchannel_id in desired_channel_ports.items():
    port = None
    other_device = self.used_ports.get(port)
    if other_device:
        device_logger.warning('Port %s already in use by %s!', port, other_device)
        continue
    info = channel_info.get(channel_id)
    if not info:
        continue
    subchannel_count = len(info.subchannel_names)
    if subchannel_id >= subchannel_count:
        continue
    channel_ports[(channel_id, subchannel_id)] = port
    self.used_ports[port] = serial_number
    if not channel_ports:
        return None
    self.device_ports[serial_number] = None(channel_ports.values())
    socket_transmitter = DeviceSocketTransmitter(self.preferences.socket_buffer_size, channel_ports, self.selector, device_logger)
    self.socket_transmitters[serial_number] = socket_transmitter
    return socket_transmitter.callback
