# Source Generated with Decompyle++
# File: tmpyqzmx1xm.marshal (Python 3.11)


def __init__(self = None, stream = None, channel = None, channel_decoder = ('stream', asphodel.AsphodelStreamInfo, 'channel', asphodel.AsphodelChannelInfo, 'channel_decoder', asphodel.AsphodelNativeChannelDecoder)):
    self.stream = stream
    self.channel = channel
    self.channel_decoder = channel_decoder
    self.samples = self.channel.samples
    self.subchannels = self.channel_decoder.subchannels
    if self.samples == 0 and self.subchannels == 0 or stream.rate == 0:
        raise ValueError('Invalid channel configuration')
    self.last_counter = -1
    self.lost_packet_list = []
    self.lost_packet_file_boundary_list = []
    self.file_boundary = False
    self.next_timestamp = 0
    self.allocated = 1000
    self.length = 0
    self.data = numpy.empty((self.allocated * self.samples, self.subchannels), dtype = numpy.double)
    self.indexes = numpy.empty((self.allocated,), dtype = numpy.uint64)
    self.timestamps = numpy.empty((self.allocated,), dtype = numpy.double)


def set_file_boundary(self = None):
    self.file_boundary = True


def set_next_timestamp(self = None, timestamp = None):
    self.next_timestamp = timestamp


def trim(self = None):
    self.allocated = self.length
    self.data = self.data[0:self.length * self.samples]
    self.indexes = self.indexes[0:self.length]
    self.timestamps = self.timestamps[0:self.length]


def decode_callback(self, counter = None, data = None, samples = None, subchannels = ('counter', int, 'data', list[float], 'samples', int, 'subchannels', int, 'return', None)):
    if self.samples != samples:
        raise ValueError('Bad sample count in callback!')
    if self.subchannels != subchannels:
        raise ValueError('Bad subchannel count in callback!')
    if self.last_counter + 1 != counter and self.length != 0:
        lost_tuple = (self.last_counter, counter, self.length)
        self.lost_packet_list.append(lost_tuple)
        if self.file_boundary:
            self.lost_packet_file_boundary_list.append(lost_tuple)
    self.last_counter = counter
    if self.length == self.allocated:
        self.allocated = self.allocated * 2
        new_data = numpy.empty((self.allocated * self.samples, self.subchannels), dtype = numpy.double)
        new_data[0:self.length * self.samples] = self.data
        self.data = new_data
        new_indexes = numpy.empty((self.allocated,), dtype = numpy.uint64)
        new_indexes[0:self.length] = self.indexes
        self.indexes = new_indexes
        new_timestamps = numpy.empty((self.allocated,), dtype = numpy.double)
        new_timestamps[0:self.length] = self.timestamps
        self.timestamps = new_timestamps
    d = numpy.array(data).reshape(samples, subchannels)
    self.indexes[self.length] = counter
    self.timestamps[self.length] = self.next_timestamp
    self.data[self.length * samples:(self.length + 1) * samples] = d
    if self.file_boundary:
        False = self, self.length += 1, .length
        return None
    return self, self.length += 1, .length

