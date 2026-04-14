# Source Generated with Decompyle++
# File: tmptjnggg66.marshal (Python 3.11)

self.load_device_function('asphodel_get_protocol_version', [
    POINTER(c_uint16)])
self.load_device_function('asphodel_get_protocol_version_string', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_board_info', [
    POINTER(c_uint8),
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_user_tag_locations', [
    c_size_t * 6])
self.load_device_function('asphodel_get_build_info', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_build_date', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_commit_id', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_repo_branch', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_repo_name', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_chip_family', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_chip_model', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_chip_id', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_nvm_size', [
    POINTER(c_size_t)])
self.load_device_function('asphodel_erase_nvm', [])
self.load_device_function('asphodel_write_nvm_raw', [
    c_size_t,
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_write_nvm_section', [
    c_size_t,
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_read_nvm_raw', [
    c_size_t,
    POINTER(c_uint8),
    POINTER(c_size_t)])
self.load_device_function('asphodel_read_nvm_section', [
    c_size_t,
    POINTER(c_uint8),
    c_size_t])
self.load_device_function('asphodel_read_user_tag_string', [
    c_size_t,
    c_size_t,
    c_char_p])
self.load_device_function('asphodel_write_user_tag_string', [
    c_size_t,
    c_size_t,
    c_char_p])
self.load_device_function('asphodel_get_nvm_modified', [
    POINTER(c_uint8)])
self.load_device_function('asphodel_get_nvm_hash', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_get_setting_hash', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_flush', [])
self.load_device_function('asphodel_reset', [])
self.load_device_function('asphodel_get_bootloader_info', [
    c_char_p,
    c_size_t])
self.load_device_function('asphodel_bootloader_jump', [])
self.load_device_function('asphodel_get_reset_flag', [
    POINTER(c_uint8)])
self.load_device_function('asphodel_clear_reset_flag', [])
self.load_device_function('asphodel_get_rgb_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_rgb_values', [
    c_int,
    c_uint8 * 3])
self.load_device_function('asphodel_set_rgb_values', [
    c_int,
    c_uint8 * 3,
    c_int])
self.load_device_function('asphodel_set_rgb_values_hex', [
    c_int,
    c_uint32,
    c_int])
self.load_device_function('asphodel_get_led_count', [
    POINTER(c_int)])
self.load_device_function('asphodel_get_led_value', [
    c_int,
    POINTER(c_uint8)])
self.load_device_function('asphodel_set_led_value', [
    c_int,
    c_uint8,
    c_int])
self.load_device_function('asphodel_set_device_mode', [
    c_uint8])
self.load_device_function('asphodel_get_device_mode', [
    POINTER(c_uint8)])
