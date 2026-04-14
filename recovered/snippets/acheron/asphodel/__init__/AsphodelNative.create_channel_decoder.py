# Source Generated with Decompyle++
# File: tmpn_cgpkdk.marshal (Python 3.11)

decoder_ptr = POINTER(self.AsphodelChannelDecoder)()
self.lib.asphodel_create_channel_decoder(channel_info, bit_offset, byref(decoder_ptr))
return AsphodelNativeChannelDecoder(self, decoder_ptr.contents, channel_info)
