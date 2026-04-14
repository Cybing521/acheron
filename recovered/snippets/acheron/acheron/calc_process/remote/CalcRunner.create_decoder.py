# Source Generated with Decompyle++
# File: tmpfb1tbka5.marshal (Python 3.11)

channel_info = { }
streams = device_info.streams
channels = device_info.channels
info_list = []
for i, stream in enumerate(streams):
    if i not in active_streams:
        continue
    channel_info_list = []
    ids = stream.channel_index_list[0:stream.channel_count]
    for channel_id in ids:
        channel_info_list.append(channels[channel_id])
        info_list.append((i, stream, channel_info_list))
        device_decoder = asphodel.nativelib.create_device_decoder(info_list, device_info.stream_filler_bits, device_info.stream_id_bits)
        for i, stream_decoder in enumerate(device_decoder.decoders):
            stream_id = device_decoder.stream_ids[i]
            for j, channel_decoder in enumerate(stream_decoder.decoders):
                channel_id = stream_decoder.stream_info.channel_index_list[j]
                channel = channels[channel_id]
                channel_info[channel_id] = self.create_channel_info(device_info, stream_id, streams[stream_id], channel_id, channel, channel_decoder)
                return (device_decoder, channel_info)
