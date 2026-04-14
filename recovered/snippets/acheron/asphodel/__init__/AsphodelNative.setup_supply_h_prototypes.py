# Source Generated with Decompyle++
# File: tmpgc62h6l8.marshal (Python 3.11)

self.load_device_function('asphodel_get_supply_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_supply_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_supply_info', [
    c_int,
    POINTER(self.AsphodelSupplyInfo)])
self.load_device_function('asphodel_check_supply', [
    c_int,
    POINTER(c_int32),
    POINTER(c_uint8),
    c_uint])
