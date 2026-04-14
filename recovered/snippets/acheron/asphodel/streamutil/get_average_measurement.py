# Source Generated with Decompyle++
# File: tmpgwtajchz.marshal (Python 3.11)

stream_data = device_data['streams'][stream_id]
channel_data = stream_data['channels'][channel_id]
unpacked_data = unpack_streaming_data(channel_data['data'])
values = unpacked_data[1]
return numpy.nanmean(values, axis = 0)
