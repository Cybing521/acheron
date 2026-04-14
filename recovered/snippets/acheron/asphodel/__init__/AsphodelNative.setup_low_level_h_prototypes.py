# Source Generated with Decompyle++
# File: tmpprzve6wl.marshal (Python 3.11)

self.load_device_function('asphodel_get_gpio_port_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_gpio_port_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_gpio_port_info', [
    c_int,
    POINTER(self.AsphodelGPIOPortInfo)])
self.load_device_function('asphodel_get_gpio_port_values', [
    c_int,
    POINTER(c_uint32)])
self.load_device_function('asphodel_set_gpio_port_modes', [
    c_int,
    c_uint8,
    c_uint32])
self.load_device_function('asphodel_disable_gpio_overrides', [])
self.load_device_function('asphodel_get_bus_counts', [
    POINTER(c_int),
    POINTER(c_int)])
self.load_device_function('asphodel_set_spi_cs_mode', [
    c_int,
    c_uint8])
self.load_device_function('asphodel_do_spi_transfer', [
    c_int,
    POINTER(c_uint8),
    POINTER(c_uint8),
    c_uint8])
self.load_device_function('asphodel_do_i2c_write', [
    c_int,
    c_uint8,
    POINTER(c_uint8),
    c_uint8])
self.load_device_function('asphodel_do_i2c_read', [
    c_int,
    c_uint8,
    POINTER(c_uint8),
    c_uint8])
self.load_device_function('asphodel_do_radio_fixed_test', [
    c_int,
    c_uint8,
    POINTER(c_uint8),
    c_uint8,
    POINTER(c_uint8),
    c_uint8])
self.load_device_function('asphodel_do_radio_fixed_test', [
    c_uint16,
    c_uint16,
    c_uint8])
self.load_device_function('asphodel_do_radio_sweep_test', [
    c_uint16,
    c_uint16,
    c_uint16,
    c_uint16,
    c_uint8])
self.load_device_function('asphodel_get_info_region_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_info_region_name', [
    c_int,
    c_char_p,
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_info_region', [
    c_int,
    POINTER(c_uint8),
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_stack_info', [
    c_uint32 * 2])
self.load_device_function('asphodel_echo_raw', [
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint8),
    POINTER(c_size_t)])
self.load_device_function('asphodel_echo_transaction', [
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint8),
    POINTER(c_size_t)])
self.load_device_function('asphodel_echo_params', [
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint8),
    POINTER(c_size_t)])
