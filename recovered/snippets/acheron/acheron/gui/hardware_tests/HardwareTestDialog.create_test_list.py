# Source Generated with Decompyle++
# File: tmppz6dcp0c.marshal (Python 3.11)

self.tests = []
for name, supply_info in enumerate(self.device_info.supplies):
    self.tests.append(self._create_supply_test(i, name, supply_info))
    for stream_id, stream in enumerate(self.device_info.streams):
        channel_indexes = stream.channel_index_list[0:stream.channel_count]
        for channel_id in channel_indexes:
            if channel_id < len(self.device_info.channels):
                channel = self.device_info.channels[channel_id]
                ch_type = channel.channel_type
                if ch_type == asphodel.CHANNEL_TYPE_SLOW_ACCEL and ch_type == asphodel.CHANNEL_TYPE_PACKED_ACCEL or ch_type == asphodel.CHANNEL_TYPE_LINEAR_ACCEL:
                    self.tests.append(self._create_accel_test(stream_id, stream, channel_id, channel))
                    continue
                if ch_type == asphodel.CHANNEL_TYPE_SLOW_STRAIN and ch_type == asphodel.CHANNEL_TYPE_FAST_STRAIN or ch_type == asphodel.CHANNEL_TYPE_COMPOSITE_STRAIN:
                    self.tests.append(self._create_bridge_test(stream_id, stream, channel_id, channel))
            return None
