# Source Generated with Decompyle++
# File: tmp1znfn659.marshal (Python 3.11)

self.lib = lib
self._decoder = decoder
self.stream_info = stream_info
self._channel_info_list = channel_info_list[:]
self.bit_offset = bit_offset
self.device_decoder = device_decoder
self.auto_free = False if device_decoder else True
self.counter_byte_offset = self._decoder.counter_byte_offset
self.used_bits = self._decoder.used_bits
self.channels = self._decoder.channels
self.decoders = []
for i in range(self.channels):
    d = AsphodelNativeChannelDecoder(self.lib, self._decoder.decoders[i].contents, channel_info_list[i], self)
    self.decoders.append(d)
    return None
