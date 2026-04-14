# Source Generated with Decompyle++
# File: tmp8eb05j76.marshal (Python 3.11)


def __init__(self, lib, decoder, stream_info, channel_info_list, bit_offset, device_decoder = (None,)):
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


def __del__(self):
    if self.auto_free:
        self.free()
        return None


def __reduce__(self):
    if self._decoder.lost_packet_callback:
        raise Exception('Cannot reduce stream decoder with callback')
    for d in self.decoders:
        if d._decoder.callback:
            raise Exception('Cannot reduce channel decoder with callback')
        args = (self.stream_info, self._channel_info_list, self.bit_offset)
        return (recreate_stream_decoder, args)


def free(self):
    if self._decoder:
        self._decoder.free_decoder(self._decoder)
        self._decoder = None
        return None


def reset(self):
    self._decoder.reset(self._decoder)

last_count = (lambda self: self._decoder.last_count)()

def decode(self, buffer):
    b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
    self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))


def set_lost_packet_callback(self, cb):
    pass
# WARNING: Decompyle incomplete

