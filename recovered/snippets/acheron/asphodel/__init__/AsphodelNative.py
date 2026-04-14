# Source Generated with Decompyle++
# File: tmpmrs17wkc.marshal (Python 3.11)

AsphodelTransferCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_void_p)
AsphodelStreamingCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_size_t, c_void_p)
AsphodelConnectCallback = CFUNCTYPE(None, c_int, c_int, c_void_p)
AsphodelCommandCallback = CFUNCTYPE(None, c_int, c_void_p)
AsphodelDecodeCallback = CFUNCTYPE(None, c_uint64, POINTER(c_double), c_size_t, c_size_t, c_void_p)
AsphodelCounterDecoderFunc = CFUNCTYPE(c_uint64, POINTER(c_uint8), c_uint64)
AsphodelLostPacketCallback = CFUNCTYPE(None, c_uint64, c_uint64, c_void_p)
AsphodelIDDecoderFunc = CFUNCTYPE(c_uint8, POINTER(c_uint8))
AsphodelUnknownIDCallback = CFUNCTYPE(None, c_uint8, c_void_p)

class AsphodelDeviceStruct(Structure):
    pass

AsphodelDeviceStruct._fields_ = [
    ('protocol_type', c_int),
    ('location_string', c_char_p),
    ('open_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct))),
    ('close_device', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
    ('free_device', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
    ('get_serial_number', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_char_p, c_size_t)),
    ('do_transfer', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint8, POINTER(c_uint8), c_size_t, AsphodelTransferCallback, c_void_p)),
    ('do_transfer_reset', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint8, POINTER(c_uint8), c_size_t, AsphodelTransferCallback, c_void_p)),
    ('start_streaming_packets', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_int, c_int, c_uint, AsphodelStreamingCallback, c_void_p)),
    ('stop_streaming_packets', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
    ('get_stream_packets_blocking', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(c_uint8), POINTER(c_int), c_uint)),
    ('get_max_incoming_param_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
    ('get_max_outgoing_param_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
    ('get_stream_packet_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
    ('poll_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_int, POINTER(c_int))),
    ('set_connect_callback', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), AsphodelConnectCallback, c_void_p)),
    ('wait_for_connect', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint)),
    ('get_remote_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
    ('reconnect_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
    ('error_callback', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct), c_int, c_void_p)),
    ('error_closure', c_void_p),
    ('reconnect_device_bootloader', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
    ('reconnect_device_application', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
    ('implementation_info', c_void_p),
    ('transport_type', c_char_p),
    ('_reserved', c_void_p * 9)]

class AsphodelChannelCalibration(Structure):
    _fields_ = [
        ('base_setting_index', c_int),
        ('resolution_setting_index', c_int),
        ('scale', c_float),
        ('offset', c_float),
        ('minimum', c_float),
        ('maximum', c_float)]


class AsphodelSupplyInfo(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('name_length', c_uint8),
        ('unit_type', c_uint8),
        ('is_battery', c_uint8),
        ('nominal', c_int32),
        ('scale', c_float),
        ('offset', c_float)]


class AsphodelCtrlVarInfo(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('name_length', c_uint8),
        ('unit_type', c_uint8),
        ('minimum', c_int32),
        ('maximum', c_int32),
        ('scale', c_float),
        ('offset', c_float)]


class AsphodelExtraScanResult(Structure):
    _fields_ = [
        ('serial_number', c_uint32),
        ('asphodel_type', c_uint8),
        ('device_mode', c_uint8),
        ('_reserved', c_uint16)]


class AsphodelGPIOPortInfo(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('name_length', c_uint8),
        ('input_pins', c_uint32),
        ('output_pins', c_uint32),
        ('floating_pins', c_uint32),
        ('loaded_pins', c_uint32),
        ('overridden_pins', c_uint32)]


class AsphodelStreamAndChannels(Structure):
    _fields_ = [
        ('stream_id', c_uint8),
        ('stream_info', POINTER(AsphodelStreamInfo)),
        ('channel_info', POINTER(POINTER(AsphodelChannelInfo)))]


class AsphodelChannelDecoder(Structure):
    pass

AsphodelChannelDecoder._fields_ = [
    ('decode', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder), c_uint64, POINTER(c_uint8))),
    ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder))),
    ('reset', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder))),
    ('set_conversion_factor', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder), c_double, c_double)),
    ('channel_bit_offset', c_uint16),
    ('samples', c_size_t),
    ('channel_name', c_char_p),
    ('subchannels', c_size_t),
    ('subchannel_names', POINTER(c_char_p)),
    ('callback', AsphodelDecodeCallback),
    ('closure', c_void_p)]

class AsphodelStreamDecoder(Structure):
    pass

AsphodelStreamDecoder._fields_ = [
    ('decode', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder), POINTER(c_uint8))),
    ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder))),
    ('reset', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder))),
    ('last_count', c_uint64),
    ('counter_byte_offset', c_size_t),
    ('counter_decoder', AsphodelCounterDecoderFunc),
    ('channels', c_size_t),
    ('decoders', POINTER(POINTER(AsphodelChannelDecoder))),
    ('lost_packet_callback', AsphodelLostPacketCallback),
    ('lost_packet_closure', c_void_p),
    ('used_bits', c_uint16)]

class AsphodelDeviceDecoder(Structure):
    pass

AsphodelDeviceDecoder._fields_ = [
    ('decode', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder), POINTER(c_uint8))),
    ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder))),
    ('reset', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder))),
    ('id_byte_offset', c_size_t),
    ('id_decoder', AsphodelIDDecoderFunc),
    ('streams', c_size_t),
    ('stream_ids', POINTER(c_uint8)),
    ('decoders', POINTER(POINTER(AsphodelStreamDecoder))),
    ('unknown_id_callback', AsphodelUnknownIDCallback),
    ('unknown_id_closure', c_void_p),
    ('used_bits', c_uint16)]

class AsphodelTCPAdvInfo(Structure):
    _fields_ = [
        ('tcp_version', c_uint8),
        ('connected', c_uint8),
        ('max_incoming_param_length', c_size_t),
        ('max_outgoing_param_length', c_size_t),
        ('stream_packet_length', c_size_t),
        ('protocol_type', c_int),
        ('serial_number', c_char_p),
        ('board_rev', c_uint8),
        ('board_type', c_char_p),
        ('build_info', c_char_p),
        ('build_date', c_char_p),
        ('user_tag1', c_char_p),
        ('user_tag2', c_char_p),
        ('remote_max_incoming_param_length', c_size_t),
        ('remote_max_outgoing_param_length', c_size_t),
        ('remote_stream_packet_length', c_size_t)]


class AsphodelUnitFormatter(Structure):
    pass

AsphodelUnitFormatter._fields_ = [
    ('format_bare', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
    ('format_ascii', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
    ('format_utf8', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
    ('format_html', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
    ('free', CFUNCTYPE(None, POINTER(AsphodelUnitFormatter))),
    ('unit_ascii', c_char_p),
    ('unit_utf8', c_char_p),
    ('unit_html', c_char_p),
    ('conversion_scale', c_double),
    ('conversion_offset', c_double)]

def __init__(self):
    pass
# WARNING: Decompyle incomplete


def free(self):
    if self.device_list:
        for device in self.device_list:
            device.free()
            self.device_list = None
            if self.lib:
                if self.usb_devices_supported:
                    self.lib.asphodel_usb_deinit()
                if self.tcp_devices_supported:
                    self.lib.asphodel_tcp_deinit()
                self.lib = None
                return None
            return None


def __del__(self):
    self.free()


def asphodel_error_check(self, result, func, arguments = (None, None)):
    if result != 0:
        error_name = self.lib.asphodel_error_name(result)
        raise AsphodelError(result, error_name)


def asphodel_string_decode_check(self, result, func, arguments):
    return result.decode('UTF-8')


def load_library_function(self, name, restype, argtypes, errcheck, ignore_missing = (True,)):
    pass
# WARNING: Decompyle incomplete


def load_device_function(self, base_name, argtypes):
    non_blocking_name = base_name
    blocking_name = base_name + '_blocking'
    blocking_argtypes = [
        POINTER(self.AsphodelDeviceStruct)]
    blocking_argtypes.extend(argtypes)
    non_blocking_argtypes = list(blocking_argtypes)
    non_blocking_argtypes.append(self.AsphodelCommandCallback)
    non_blocking_argtypes.append(c_void_p)
    self.load_library_function(non_blocking_name, c_int, non_blocking_argtypes, self.asphodel_error_check)
    self.load_library_function(blocking_name, c_int, blocking_argtypes, self.asphodel_error_check)


def setup_api_h_prototypes(self):
    string_decode = self.asphodel_string_decode_check
    self.load_library_function('asphodel_error_name', c_char_p, [
        c_int], string_decode)
    self.load_library_function('asphodel_unit_type_name', c_char_p, [
        c_uint8], string_decode)
    self.load_library_function('asphodel_get_unit_type_count', c_uint8, [], None)
    self.load_library_function('asphodel_channel_type_name', c_char_p, [
        c_uint8], string_decode)
    self.load_library_function('asphodel_get_channel_type_count', c_uint8, [], None)
    self.load_library_function('asphodel_setting_type_name', c_char_p, [
        c_uint8], string_decode)
    self.load_library_function('asphodel_get_setting_type_count', c_uint8, [], None)


def setup_bootloader_h_prototypes(self):
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


def setup_channel_specific_h_prototypes(self):
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


def setup_ctrl_var_h_prototypes(self):
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


def setup_decode_h_prototypes(self):
    self.load_library_function('asphodel_create_channel_decoder', c_int, [
        POINTER(AsphodelChannelInfo),
        c_uint16,
        POINTER(POINTER(self.AsphodelChannelDecoder))], self.asphodel_error_check)
    self.load_library_function('asphodel_create_stream_decoder', c_int, [
        POINTER(self.AsphodelStreamAndChannels),
        c_uint16,
        POINTER(POINTER(self.AsphodelStreamDecoder))], self.asphodel_error_check)
    self.load_library_function('asphodel_create_device_decoder', c_int, [
        POINTER(self.AsphodelStreamAndChannels),
        c_uint8,
        c_uint8,
        c_uint8,
        POINTER(POINTER(self.AsphodelDeviceDecoder))], self.asphodel_error_check)
    self.load_library_function('asphodel_get_streaming_counts', c_int, [
        POINTER(self.AsphodelStreamAndChannels),
        c_uint8,
        c_double,
        c_double,
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_uint)], self.asphodel_error_check)


def setup_device_h_prototypes(self):
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


def setup_device_type_h_prototypes(self):
    self.load_library_function('asphodel_supports_rf_power_commands', c_int, [
        POINTER(self.AsphodelDeviceStruct)], None)
    self.load_library_function('asphodel_supports_radio_commands', c_int, [
        POINTER(self.AsphodelDeviceStruct)], None)
    self.load_library_function('asphodel_supports_remote_commands', c_int, [
        POINTER(self.AsphodelDeviceStruct)], None)
    self.load_library_function('asphodel_supports_bootloader_commands', c_int, [
        POINTER(self.AsphodelDeviceStruct)], None)


def setup_low_level_h_prototypes(self):
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


def setup_mem_test_h_prototypes(self):
    
    try:
        self.load_library_function('asphodel_mem_test_supported', c_int, [], None, ignore_missing = False)
        self.mem_test_supported = self.lib.asphodel_mem_test_supported()
    except AttributeError:
        self.mem_test_supported = False

    self.load_library_function('asphodel_mem_test_set_limit', None, [
        c_int], None)
    self.load_library_function('asphodel_mem_test_get_limit', c_int, [], None)


def setup_radio_h_prototypes(self):
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


def setup_rf_power_h_prototypes(self):
    self.load_device_function('asphodel_enable_rf_power', [
        c_int])
    self.load_device_function('asphodel_get_rf_power_status', [
        POINTER(c_int)])
    self.load_device_function('asphodel_get_rf_power_ctrl_vars', [
        POINTER(c_uint8),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_reset_rf_power_timeout', [
        c_uint32])


def setup_setting_h_prototypes(self):
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


def setup_stream_h_prototypes(self):
    self.load_device_function('asphodel_get_stream_count', [
        POINTER(c_int),
        POINTER(c_uint8),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_get_stream', [
        c_int,
        POINTER(POINTER(AsphodelStreamInfo))])
    self.load_library_function('asphodel_free_stream', None, [
        POINTER(AsphodelStreamInfo)], None)
    self.load_device_function('asphodel_get_stream_channels', [
        c_int,
        POINTER(c_uint8),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_get_stream_format', [
        c_int,
        POINTER(AsphodelStreamInfo)])
    self.load_device_function('asphodel_enable_stream', [
        c_int,
        c_int])
    self.load_device_function('asphodel_warm_up_stream', [
        c_int,
        c_int])
    self.load_device_function('asphodel_get_stream_status', [
        c_int,
        POINTER(c_int),
        POINTER(c_int)])
    self.load_device_function('asphodel_get_stream_rate_info', [
        c_int,
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_int),
        POINTER(c_float),
        POINTER(c_float)])
    self.load_device_function('asphodel_get_channel_count', [
        POINTER(c_int)])
    self.load_device_function('asphodel_get_channel', [
        c_int,
        POINTER(POINTER(AsphodelChannelInfo))])
    self.load_library_function('asphodel_free_channel', None, [
        POINTER(AsphodelChannelInfo)], None)
    self.load_device_function('asphodel_get_channel_name', [
        c_int,
        c_char_p,
        POINTER(c_uint8)])
    self.load_device_function('asphodel_get_channel_info', [
        c_int,
        POINTER(AsphodelChannelInfo)])
    self.load_device_function('asphodel_get_channel_coefficients', [
        c_int,
        POINTER(c_float),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_get_channel_chunk', [
        c_int,
        c_uint8,
        POINTER(c_uint8),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_channel_specific', [
        c_int,
        POINTER(c_uint8),
        c_uint8,
        POINTER(c_uint8),
        POINTER(c_uint8)])
    self.load_device_function('asphodel_get_channel_calibration', [
        c_int,
        POINTER(c_int),
        POINTER(self.AsphodelChannelCalibration)])


def setup_supply_h_prototypes(self):
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


def setup_tcp_h_prototypes(self):
    
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


def setup_unit_format_h_prototypes(self):
    self.load_library_function('asphodel_create_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
        c_uint8,
        c_double,
        c_double,
        c_double,
        c_int], None)
    self.load_library_function('asphodel_create_custom_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
        c_double,
        c_double,
        c_double,
        c_char_p,
        c_char_p,
        c_char_p], None)
    self.load_library_function('asphodel_format_value_ascii', c_int, [
        c_char_p,
        c_size_t,
        c_uint8,
        c_double,
        c_int,
        c_double], None)
    self.load_library_function('asphodel_format_value_utf8', c_int, [
        c_char_p,
        c_size_t,
        c_uint8,
        c_double,
        c_int,
        c_double], None)
    self.load_library_function('asphodel_format_value_html', c_int, [
        c_char_p,
        c_size_t,
        c_uint8,
        c_double,
        c_int,
        c_double], None)


def setup_usb_h_prototypes(self):
    
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


def setup_version_h_prototypes(self):
    self.load_library_function('asphodel_get_library_protocol_version', c_uint16, [], None)
    self.load_library_function('asphodel_get_library_protocol_version_string', c_char_p, [], None)
    self.load_library_function('asphodel_get_library_build_info', c_char_p, [], None)
    self.load_library_function('asphodel_get_library_build_date', c_char_p, [], None)


def find_usb_devices(self):
    count = c_size_t(0)
    self.lib.asphodel_usb_find_devices(None, byref(count))
    array_size = count.value
    if array_size == 0:
        return []
    array = POINTER(self.AsphodelDeviceStruct) * array_size()
    array_ptr = cast(byref(array), POINTER(POINTER(self.AsphodelDeviceStruct)))
    self.lib.asphodel_usb_find_devices(array_ptr, byref(count))
    array_entries = min(array_size, count.value)
    device_list = []
    for i in range(array_entries):
        device_list.append(AsphodelNativeDevice(self, array[i].contents))
        return device_list


def find_tcp_devices(self, flags = (None,)):
    pass
# WARNING: Decompyle incomplete


def create_tcp_device(self, host, port, timeout, serial = (None,)):
    device_ptr = POINTER(self.AsphodelDeviceStruct)()
    if serial:
        serial_bytes = serial.encode('UTF-8')
    else:
        serial_bytes = None
    self.lib.asphodel_tcp_create_device(host.encode('UTF-8'), port, timeout, serial_bytes, byref(device_ptr))
    return AsphodelNativeDevice(self, device_ptr.contents)


def tcp_get_advertisement(self, device):
    adv_ptr = self.lib.asphodel_tcp_get_advertisement(device)
    adv = adv_ptr.contents
    
    def decode_safe(b):
        
        try:
            return b.decode('UTF-8')
        except UnicodeDecodeError:
            return 'ERROR'


    return TCPAdvInfo(adv.tcp_version, bool(adv.connected), adv.max_incoming_param_length, adv.max_outgoing_param_length, adv.stream_packet_length, adv.protocol_type, decode_safe(adv.serial_number), adv.board_rev, decode_safe(adv.board_type), decode_safe(adv.build_info), decode_safe(adv.build_date), decode_safe(adv.user_tag1), decode_safe(adv.user_tag2), adv.remote_max_incoming_param_length, adv.remote_max_outgoing_param_length, adv.remote_stream_packet_length)


def create_channel_decoder(self, channel_info, bit_offset):
    decoder_ptr = POINTER(self.AsphodelChannelDecoder)()
    self.lib.asphodel_create_channel_decoder(channel_info, bit_offset, byref(decoder_ptr))
    return AsphodelNativeChannelDecoder(self, decoder_ptr.contents, channel_info)


def create_stream_decoder(self, stream_info, channel_info_list, bit_offset):
    decoder_ptr = POINTER(self.AsphodelStreamDecoder)()
    array_type = POINTER(AsphodelChannelInfo) * len(channel_info_list)
# WARNING: Decompyle incomplete


def create_device_decoder(self, info_list, filler_bits, id_bits):
    '''
        info_list is a sequence of tuples of (stream_id, stream_info,
        channel_info_list).
        '''
    decoder_ptr = POINTER(self.AsphodelDeviceDecoder)()
    array_size = len(info_list)
    info_array = self.AsphodelStreamAndChannels * array_size()
# WARNING: Decompyle incomplete


def get_streaming_counts(self, streams, response_time, buffer_time, timeout):
    '''
        returns (packet_count, transfer_count, timeout)
        '''
    packet_count = c_int()
    transfer_count = c_int()
    timeout = c_uint(timeout)
    array_size = len(streams)
    info_array = self.AsphodelStreamAndChannels * array_size()
    for i, stream_info in enumerate(streams):
        info_array[i].stream_info = pointer(stream_info)
        self.lib.asphodel_get_streaming_counts(cast(info_array, POINTER(self.AsphodelStreamAndChannels)), array_size, response_time, buffer_time, byref(packet_count), byref(transfer_count), byref(timeout))
        return (packet_count.value, transfer_count.value, timeout.value)


def create_unit_formatter(self, unit_type, minimum, maximum, resolution, use_metric = (True,)):
    use_metric_int = 1 if use_metric else 0
    formatter = self.lib.asphodel_create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric_int)
    if not formatter:
        raise AsphodelError(0, 'asphodel_create_unit_formatter returned NULL')
    recreate = (recreate_unit_formatter, (unit_type, minimum, maximum, resolution, use_metric))
    return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)


def create_custom_unit_formatter(self, scale, offset, resolution, unit_ascii, unit_utf8, unit_html):
    formatter = self.lib.asphodel_create_custom_unit_formatter(scale, offset, resolution, unit_ascii.encode('ascii'), unit_utf8.encode('UTF-8'), unit_html.encode('ascii'))
    if not formatter:
        raise AsphodelError(0, 'asphodel_create_custom_unit_formatter returned NULL')
    recreate = (recreate_custom_unit_formatter, (scale, offset, resolution, unit_ascii, unit_utf8, unit_html))
    return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)


def _format_value(self, lib_func, unit_type, resolution, value, use_metric):
    use_metric_int = 1 if use_metric else 0
    buffer = create_string_buffer(256)
    lib_func(buffer, len(buffer), unit_type, resolution, use_metric_int, value)
    return buffer.value


def format_value_ascii(self, unit_type, resolution, value, use_metric = (True,)):
    b = self._format_value(self.lib.asphodel_format_value_ascii, unit_type, resolution, value, use_metric)
    return b.decode('ascii')


def format_value_utf8(self, unit_type, resolution, value, use_metric = (True,)):
    b = self._format_value(self.lib.asphodel_format_value_utf8, unit_type, resolution, value, use_metric)
    return b.decode('UTF-8')


def format_value_html(self, unit_type, resolution, value, use_metric = (True,)):
    b = self._format_value(self.lib.asphodel_format_value_html, unit_type, resolution, value, use_metric)
    return b.decode('ascii')


def mem_test_set_limit(self, limit):
    self.lib.asphodel_mem_test_set_limit(limit)


def mem_test_get_limit(self):
    return self.lib.asphodel_mem_test_get_limit()

