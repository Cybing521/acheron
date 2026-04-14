# Source Generated with Decompyle++
# File: tmptit5kda7.marshal (Python 3.11)


try:
    (channel_id, subchannel) = self.modbus_index_channel[modbus_index]
except KeyError:
    return None

ringbuffer = self.mean_ringbuffers[channel_id]
data = ringbuffer.get_contents()[(:, subchannel)]
value = numpy.mean(data).item()
return (value, channel_id)
