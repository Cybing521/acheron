# Source Generated with Decompyle++
# File: tmpxt5wwn08.marshal (Python 3.11)


try:
    self.load_library_function('asphodel_usb_devices_supported', c_int, [], None, ignore_missing = False)
    s = self.lib.asphodel_usb_devices_supported()
    self.usb_devices_supported = s
except AttributeError:
    self.usb_devices_supported = True

self.load_library_function('asphodel_usb_init', c_int, [], self.asphodel_error_check)
self.load_library_function('asphodel_usb_deinit', None, [], None)
self.load_library_function('asphodel_usb_find_devices', c_int, [
    POINTER(POINTER(self.AsphodelDeviceStruct)),
    POINTER(c_size_t)], self.asphodel_error_check)
self.load_library_function('asphodel_usb_get_backend_version', c_char_p, [], None)
