# Source Generated with Decompyle++
# File: tmp9m3i00yq.marshal (Python 3.11)

if self._decoder.lost_packet_callback:
    raise Exception('Cannot reduce stream decoder with callback')
for d in self.decoders:
    if d._decoder.callback:
        raise Exception('Cannot reduce channel decoder with callback')
    args = (self.stream_info, self._channel_info_list, self.bit_offset)
    return (recreate_stream_decoder, args)
