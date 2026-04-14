# Source Generated with Decompyle++
# File: tmp9xn5ph8r.marshal (Python 3.11)

self.load_device_function('asphodel_bootloader_start_program', [])
self.load_device_function('asphodel_get_bootloader_page_info', [
    POINTER(c_uint32),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_bootloader_block_sizes', [
    POINTER(c_uint16),
    POINTER(c_uint8)])
self.load_device_function('asphodel_start_bootloader_page', [
    c_uint32,
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_write_bootloader_code_block', [
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_write_bootloader_page', [
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint16),
    c_uint8])
self.load_device_function('asphodel_finish_bootloader_page', [
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_verify_bootloader_page', [
    POINTER(c_uint8),
    c_size_t])
