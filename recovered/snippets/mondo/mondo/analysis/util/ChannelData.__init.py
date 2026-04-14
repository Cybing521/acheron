# Source Generated with Decompyle++
# File: tmpjg5j33h5.marshal (Python 3.11)

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
