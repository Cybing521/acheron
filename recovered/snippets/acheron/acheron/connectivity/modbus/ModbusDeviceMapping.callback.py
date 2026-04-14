# Source Generated with Decompyle++
# File: tmpkrd19rv3.marshal (Python 3.11)

self.mean_ringbuffers[channel_id].extend(data)
modbus_index = self.channel_modbus_index[channel_id]
for i, subchannel_data in enumerate(data.T):
    self.instant_ringbuffers[modbus_index + i].extend(subchannel_data[(:, None)])
    return None
