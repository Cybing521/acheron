# Source Generated with Decompyle++
# File: tmpsdv_many.marshal (Python 3.11)

(stream_count, filler_bits, id_bits) = self.get_stream_count()
info_list = []
for i in range(stream_count):
    stream_struct = self.get_stream(i)
    channel_info_list = []
    channels = stream_struct.channel_count
    indexes = stream_struct.channel_index_list[0:channels]
    for ch_index in indexes:
        channel_info_list.append(self.get_channel(ch_index))
        info_list.append((i, stream_struct, channel_info_list))
        return self.lib.create_device_decoder(info_list, filler_bits, id_bits)
