# Source Generated with Decompyle++
# File: tmpo764h54w.marshal (Python 3.11)


try:
    self.load_library_function('asphodel_tcp_devices_supported', c_int, [], None, ignore_missing = False)
    s = self.lib.asphodel_tcp_devices_supported()
    self.tcp_devices_supported = s
except AttributeError:
    self.tcp_devices_supported = False

self.load_library_function('asphodel_tcp_init', c_int, [], self.asphodel_error_check)
self.load_library_function('asphodel_tcp_deinit', None, [], None)
self.load_library_function('asphodel_tcp_find_devices', c_int, [
    POINTER(POINTER(self.AsphodelDeviceStruct)),
    POINTER(c_size_t)], self.asphodel_error_check)
self.load_library_function('asphodel_tcp_find_devices_filter', c_int, [
    POINTER(POINTER(self.AsphodelDeviceStruct)),
    POINTER(c_size_t),
    c_uint32], self.asphodel_error_check)
self.load_library_function('asphodel_tcp_get_advertisement', POINTER(self.AsphodelTCPAdvInfo), [
    POINTER(self.AsphodelDeviceStruct)], None)
self.load_library_function('asphodel_tcp_create_device', c_int, [
    c_char_p,
    c_uint16,
    c_int,
    c_char_p,
    POINTER(POINTER(self.AsphodelDeviceStruct))], self.asphodel_error_check)
