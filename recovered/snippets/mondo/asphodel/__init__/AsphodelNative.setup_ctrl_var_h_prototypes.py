# Source Generated with Decompyle++
# File: tmp7mbqvrw0.marshal (Python 3.11)

self.load_device_function('asphodel_get_ctrl_var_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_ctrl_var_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_ctrl_var_info', [
    c_int,
    POINTER(self.AsphodelCtrlVarInfo)])
self.load_device_function('asphodel_get_ctrl_var', [
    c_int,
    POINTER(c_int32)])
self.load_device_function('asphodel_set_ctrl_var', [
    c_int,
    c_int32])
