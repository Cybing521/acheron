# Source Generated with Decompyle++
# File: tmpabcadwpx.marshal (Python 3.11)

self.load_library_function('asphodel_create_channel_decoder', c_int, [
    POINTER(AsphodelChannelInfo),
    c_uint16,
    POINTER(POINTER(self.AsphodelChannelDecoder))], self.asphodel_error_check)
self.load_library_function('asphodel_create_stream_decoder', c_int, [
    POINTER(self.AsphodelStreamAndChannels),
    c_uint16,
    POINTER(POINTER(self.AsphodelStreamDecoder))], self.asphodel_error_check)
self.load_library_function('asphodel_create_device_decoder', c_int, [
    POINTER(self.AsphodelStreamAndChannels),
    c_uint8,
    c_uint8,
    c_uint8,
    POINTER(POINTER(self.AsphodelDeviceDecoder))], self.asphodel_error_check)
self.load_library_function('asphodel_get_streaming_counts', c_int, [
    POINTER(self.AsphodelStreamAndChannels),
    c_uint8,
    c_double,
    c_double,
    POINTER(c_int),
    POINTER(c_int),
    POINTER(c_uint)], self.asphodel_error_check)
