# Source Generated with Decompyle++
# File: tmpuqxyaw0r.marshal (Python 3.11)

self.load_device_function('asphodel_get_stream_count', [
    POINTER(c_int),
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_stream', [
    c_int,
    POINTER(POINTER(AsphodelStreamInfo))])
self.load_library_function('asphodel_free_stream', None, [
    POINTER(AsphodelStreamInfo)], None)
self.load_device_function('asphodel_get_stream_channels', [
    c_int,
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_stream_format', [
    c_int,
    POINTER(AsphodelStreamInfo)])
self.load_device_function('asphodel_enable_stream', [
    c_int,
    c_int])
self.load_device_function('asphodel_warm_up_stream', [
    c_int,
    c_int])
self.load_device_function('asphodel_get_stream_status', [
    c_int,
    POINTER(c_int),
    POINTER(c_int)])
self.load_device_function('asphodel_get_stream_rate_info', [
    c_int,
    POINTER(c_int),
    POINTER(c_int),
    POINTER(c_int),
    POINTER(c_float),
    POINTER(c_float)])
self.load_device_function('asphodel_get_channel_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_channel', [
    c_int,
    POINTER(POINTER(AsphodelChannelInfo))])
self.load_library_function('asphodel_free_channel', None, [
    POINTER(AsphodelChannelInfo)], None)
self.load_device_function('asphodel_get_channel_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_channel_info', [
    c_int,
    POINTER(AsphodelChannelInfo)])
self.load_device_function('asphodel_get_channel_coefficients', [
    c_int,
    POINTER(c_float),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_channel_chunk', [
    c_int,
    c_uint8,
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_channel_specific', [
    c_int,
    POINTER(c_uint8),
    c_uint8,
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_channel_calibration', [
    c_int,
    POINTER(c_int),
    POINTER(self.AsphodelChannelCalibration)])
