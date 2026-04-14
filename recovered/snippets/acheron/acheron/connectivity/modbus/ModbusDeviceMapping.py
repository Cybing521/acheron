# Source Generated with Decompyle++
# File: tmpzcym_ofa.marshal (Python 3.11)


def __init__(self = None, serial_number = None, channel_info = None):
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


def callback(self = None, channel_id = None, data = None):
    self.mean_ringbuffers[channel_id].extend(data)
    modbus_index = self.channel_modbus_index[channel_id]
    for i, subchannel_data in enumerate(data.T):
        self.instant_ringbuffers[modbus_index + i].extend(subchannel_data[(:, None)])
        return None


def _mean_to_16bit(self = None, value = None, channel = None):
    
    try:
        if value >= channel.maximum:
            return 65535
        if None <= channel.minimum:
            return 0
        ratio = (None - channel.minimum) / (channel.maximum - channel.minimum)
        return round(65535 * ratio)
    except ValueError:
        return 0



def _std_to_16bit(self = None, value = None, channel = None):
    
    try:
        if value <= 0:
            return 0
        std_max = (None.maximum - channel.minimum) / 2
        if value >= std_max:
            return 65535
        return None((value / std_max) * 65535)
    except ValueError:
        return 0



def _get_mean(self = None, modbus_index = None):
    
    try:
        (channel_id, subchannel) = self.modbus_index_channel[modbus_index]
    except KeyError:
        return None

    ringbuffer = self.mean_ringbuffers[channel_id]
    data = ringbuffer.get_contents()[(:, subchannel)]
    value = numpy.mean(data).item()
    return (value, channel_id)


def get_mean_float(self = None, modbus_index = None):
    result = self._get_mean(modbus_index)
# WARNING: Decompyle incomplete


def get_mean_16bit(self = None, modbus_index = None):
    result = self._get_mean(modbus_index)
# WARNING: Decompyle incomplete


def _get_std(self = None, modbus_index = None):
    
    try:
        (channel_id, subchannel) = self.modbus_index_channel[modbus_index]
    except KeyError:
        return None

    ringbuffer = self.mean_ringbuffers[channel_id]
    data = ringbuffer.get_contents()[(:, subchannel)]
    value = numpy.std(data).item()
    return (value, channel_id)


def get_std_float(self = None, modbus_index = None):
    result = self._get_std(modbus_index)
# WARNING: Decompyle incomplete


def get_std_16bit(self = None, modbus_index = None):
    result = self._get_std(modbus_index)
# WARNING: Decompyle incomplete


def get_instant_float(self = None, modbus_index = None):
    
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


def get_instant_16bit(self = None, modbus_index = None):
    value = self.get_instant_float(modbus_index)
# WARNING: Decompyle incomplete

