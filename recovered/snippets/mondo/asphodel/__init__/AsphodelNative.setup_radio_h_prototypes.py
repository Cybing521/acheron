# Source Generated with Decompyle++
# File: tmpb98axlsz.marshal (Python 3.11)

self.load_device_function('asphodel_stop_radio', [])
self.load_device_function('asphodel_start_radio_scan', [])
self.load_device_function('asphodel_get_raw_radio_scan_results', [
    POINTER(c_uint32),
    POINTER(c_size_t)])
self.load_device_function('asphodel_get_radio_scan_results', [
    POINTER(POINTER(c_uint32)),
    POINTER(c_size_t)])
self.load_library_function('asphodel_free_radio_scan_results', None, [
    POINTER(c_uint32)], None)
self.load_device_function('asphodel_get_raw_radio_extra_scan_results', [
    POINTER(self.AsphodelExtraScanResult),
    POINTER(c_size_t)])
self.load_device_function('asphodel_get_radio_extra_scan_results', [
    POINTER(POINTER(self.AsphodelExtraScanResult)),
    POINTER(c_size_t)])
self.load_library_function('asphodel_free_radio_extra_scan_results', None, [
    POINTER(self.AsphodelExtraScanResult)], None)
self.load_device_function('asphodel_get_radio_scan_power', [
    POINTER(c_uint32),
    POINTER(c_int8),
    c_size_t])
self.load_device_function('asphodel_connect_radio', [
    c_uint32])
self.load_device_function('asphodel_get_radio_status', [
    POINTER(c_int),
    POINTER(c_uint32),
    POINTER(c_uint8),
    POINTER(c_int)])
self.load_device_function('asphodel_get_radio_ctrl_vars', [
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_radio_default_serial', [
    POINTER(c_uint32)])
self.load_device_function('asphodel_start_radio_scan_boot', [])
self.load_device_function('asphodel_connect_radio_boot', [
    c_uint32])
self.load_device_function('asphodel_stop_remote', [])
self.load_device_function('asphodel_restart_remote', [])
self.load_device_function('asphodel_get_remote_status', [
    POINTER(c_int),
    POINTER(c_uint32),
    POINTER(c_uint8)])
self.load_device_function('asphodel_restart_remote_app', [])
self.load_device_function('asphodel_restart_remote_boot', [])
