# Source Generated with Decompyle++
# File: tmpw9jto123.marshal (Python 3.11)


def __init__(self, lib, decoder, info_list, filler_bits, id_bits):
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


def __del__(self):
    self.free()


def __reduce__(self):
    if self._decoder.unknown_id_callback:
        raise Exception('Cannot reduce device decoder with callback')
    for d in self.decoders:
        if d._decoder.lost_packet_callback:
            raise Exception('Cannot reduce stream decoder with callback')
        for cd in d.decoders:
            if cd._decoder.callback:
                raise Exception('Cannot reduce channel decoder with callback')
            args = (self._info_list, self._filler_bits, self._id_bits)
            return (recreate_device_decoder, args)


def free(self):
    if self._decoder:
        self._decoder.free_decoder(self._decoder)
        self._decoder = None
        return None


def reset(self):
    self._decoder.reset(self._decoder)


def decode(self, buffer):
    b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
    self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))


def set_unknown_id_callback(self, cb):
    pass
# WARNING: Decompyle incomplete

