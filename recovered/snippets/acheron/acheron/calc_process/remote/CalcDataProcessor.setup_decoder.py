# Source Generated with Decompyle++
# File: tmp1mywb5zd.marshal (Python 3.11)

self.device_decoder.set_unknown_id_callback(self.unknown_id_cb)
channel_decoders = { }
for i, stream_decoder in enumerate(self.device_decoder.decoders):
    stream_id = self.device_decoder.stream_ids[i]
    lost_packet_cb = self.create_lost_packet_callback(stream_id)
    stream_decoder.set_lost_packet_callback(lost_packet_cb)
    for j, channel_decoder in enumerate(stream_decoder.decoders):
        channel_id = stream_decoder.stream_info.channel_index_list[j]
        channel_decoders[channel_id] = channel_decoder
        for channel_id in sorted(channel_decoders.keys()):
            channel_decoder = channel_decoders[channel_id]
            self.setup_channel(channel_id, channel_decoder)
            return None
