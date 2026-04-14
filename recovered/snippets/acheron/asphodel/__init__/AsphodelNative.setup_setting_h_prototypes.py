# Source Generated with Decompyle++
# File: tmpq_b9hjiu.marshal (Python 3.11)

self.load_device_function('asphodel_get_setting_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_setting_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_setting_info', [
    c_int,
    POINTER(AsphodelSettingInfo)])
self.load_device_function('asphodel_get_setting_default', [
    c_int,
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_custom_enum_counts', [
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_custom_enum_value_name', [
    c_int,
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_setting_category_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_setting_category_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_setting_category_settings', [
    c_int,
    POINTER(c_uint8),
    POINTER(c_uint8)])
