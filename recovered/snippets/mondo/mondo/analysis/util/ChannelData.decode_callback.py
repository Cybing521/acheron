# Source Generated with Decompyle++
# File: tmpdi4vf1jv.marshal (Python 3.11)

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
