# Source Generated with Decompyle++
# File: tmpeqba7027.marshal (Python 3.11)

if self._decoder.callback:
    raise Exception('Cannot reduce channel decoder with callback')
args = (self.channel_info, self._decoder.channel_bit_offset)
return (recreate_channel_decoder, args)
