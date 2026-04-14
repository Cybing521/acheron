# Source Generated with Decompyle++
# File: tmpl5ndeeud.marshal (Python 3.11)

self.lib = lib
self._decoder = decoder
self._info_list = info_list
self._filler_bits = filler_bits
self._id_bits = id_bits
bit_offset = self._filler_bits + self._id_bits
self.id_byte_offset = self._decoder.id_byte_offset
self.used_bits = self._decoder.used_bits
self.streams = self._decoder.streams
self.stream_ids = self._decoder.stream_ids[0:self.streams]
self.decoders = []
for i in range(self.streams):
    d = AsphodelNativeStreamDecoder(self.lib, self._decoder.decoders[i].contents, info_list[i][1], info_list[i][2], bit_offset, self)
    self.decoders.append(d)
    return None
