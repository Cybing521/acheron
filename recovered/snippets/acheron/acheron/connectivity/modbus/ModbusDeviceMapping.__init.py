# Source Generated with Decompyle++
# File: tmpm77y9q8p.marshal (Python 3.11)

self.serial_number = serial_number
self.channel_info = channel_info
self.logger = DeviceLoggerAdapter(logger, serial_number)
self.mean_ringbuffers = { }
self.instant_ringbuffers = []
self.last_instant_value = []
self.channel_modbus_index = { }
self.modbus_index_channel = { }
for channel_id, info in sorted(channel_info.items()):
    subchannel_count = len(info.subchannel_names)
    self.mean_ringbuffers[channel_id] = RingBuffer(info.mean_len, subchannel_count)
    modbus_index = len(self.instant_ringbuffers)
    self.channel_modbus_index[channel_id] = modbus_index
    for i in range(subchannel_count):
        self.instant_ringbuffers.append(RingBuffer(info.mean_len, 1))
        self.last_instant_value.append(0)
        self.modbus_index_channel[modbus_index + i] = (channel_id, i)
        self.channel_count = len(self.instant_ringbuffers)
        self.numeric_serial = get_numeric_serial(serial_number)
        return None
