# Source Generated with Decompyle++
# File: tmpo3gtckyw.marshal (Python 3.11)

packet_count = c_int()
transfer_count = c_int()
timeout = c_uint(timeout)
array_size = len(streams)
info_array = self.AsphodelStreamAndChannels * array_size()
for i, stream_info in enumerate(streams):
    info_array[i].stream_info = pointer(stream_info)
    self.lib.asphodel_get_streaming_counts(cast(info_array, POINTER(self.AsphodelStreamAndChannels)), array_size, response_time, buffer_time, byref(packet_count), byref(transfer_count), byref(timeout))
    return (packet_count.value, transfer_count.value, timeout.value)
