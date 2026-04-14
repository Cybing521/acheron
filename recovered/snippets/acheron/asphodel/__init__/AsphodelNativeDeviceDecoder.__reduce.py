# Source Generated with Decompyle++
# File: tmp6ta6x139.marshal (Python 3.11)

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
