# Source Generated with Decompyle++
# File: tmpcc5q__j7.marshal (Python 3.11)

stream_ids = sorted(active_streams)
for stream_id in stream_ids:
    self.device.warm_up_stream(stream_id, True)
    warm_up_time = 0
    for stream_id in stream_ids:
        stream = device_info.streams[stream_id]
        if stream.warm_up_delay > warm_up_time:
            warm_up_time = stream.warm_up_delay
        if warm_up_time > 0:
            time.sleep(warm_up_time)
for stream_id in stream_ids:
    self.device.enable_stream(stream_id, True)
    self.device.warm_up_stream(stream_id, False)
    return None
