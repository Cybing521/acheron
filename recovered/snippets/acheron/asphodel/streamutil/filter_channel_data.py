# Source Generated with Decompyle++
# File: tmp673mko3w.marshal (Python 3.11)

stream_data = filter_stream_data(device_data, stream_id)
channel_data = cast(dict, stream_data['channels'][channel_id].copy())
(lambda .0: pass# WARNING: Decompyle incomplete
)(stream_data.items()())
return cast(ExtraChannelData, channel_data)
