# Source Generated with Decompyle++
# File: tmp1n3r38_2.marshal (Python 3.11)


try:
    ringbuffer = self.instant_ringbuffers[modbus_index]
except IndexError:
    return None

data = ringbuffer.get_contents()
if data.size != 0:
    value = numpy.mean(data).item()
    self.last_instant_value[modbus_index] = value
    ringbuffer.clear()
else:
    value = self.last_instant_value[modbus_index]
return value
