# Source Generated with Decompyle++
# File: tmpsumzkfva.marshal (Python 3.11)

self.load_library_function('asphodel_get_strain_bridge_count', c_int, [
    POINTER(AsphodelChannelInfo),
    POINTER(c_int)], self.asphodel_error_check)
self.load_library_function('asphodel_get_strain_bridge_subchannel', c_int, [
    POINTER(AsphodelChannelInfo),
    c_int,
    POINTER(c_size_t)], self.asphodel_error_check)
self.load_library_function('asphodel_get_strain_bridge_values', c_int, [
    POINTER(AsphodelChannelInfo),
    c_int,
    c_float * 5], self.asphodel_error_check)
self.load_device_function('asphodel_set_strain_outputs', [
    c_int,
    c_int,
    c_int,
    c_int])
self.load_library_function('asphodel_check_strain_resistances', c_int, [
    POINTER(AsphodelChannelInfo),
    c_int,
    c_double,
    c_double,
    c_double,
    POINTER(c_double),
    POINTER(c_double),
    POINTER(c_int)], self.asphodel_error_check)
self.load_library_function('asphodel_get_accel_self_test_limits', c_int, [
    POINTER(AsphodelChannelInfo),
    c_float * 6], self.asphodel_error_check)
self.load_device_function('asphodel_enable_accel_self_test', [
    c_int,
    c_int])
self.load_library_function('asphodel_check_accel_self_test', c_int, [
    POINTER(AsphodelChannelInfo),
    c_double * 3,
    c_double * 3,
    POINTER(c_int)], self.asphodel_error_check)
