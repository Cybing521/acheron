# Source Generated with Decompyle++
# File: tmp72dp5icn.marshal (Python 3.11)

stream_info = self.get_stream(index)
channel_info_list = []
indexes = stream_info.channel_index_list[0:stream_info.channel_count]
for ch_index in indexes:
    channel_info_list.append(self.get_channel(ch_index))
    return self.lib.create_stream_decoder(stream_info, channel_info_list, bit_offset)
