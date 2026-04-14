# Source Generated with Decompyle++
# File: tmpko52b18p.marshal (Python 3.11)

MAX_STRING_LENGTH = 128

def __init__(self, lib, device):
    self.lib = lib
    self.device = device
    self._callbacks = []
    self._remote = None
    if self.get_transport_type() == 'usb':
        self.reconnect_time = 5
    else:
        self.reconnect_time = 10
    if self.lib:
        self.lib.device_list.add(self)
        return None


def open(self):
    ret = self.device.open_device(self.device)
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)


def close(self):
    if self.device:
        self.device.close_device(self.device)
        return None


def free(self):
    self.close()
    if self.device:
        self.device.free_device(self.device)
    self.device = None
    self.lib = None


def __del__(self):
    self.free()


def get_location_string(self):
    return self.device.location_string.decode('UTF-8')


def get_transport_type(self):
    if self.lib.protocol_version >= 515:
        return self.device.transport_type.decode('UTF-8')


def get_serial_number(self):
    buffer = create_string_buffer(64)
    ret = self.device.get_serial_number(self.device, buffer, len(buffer))
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    return buffer.value.decode('UTF-8')


def do_transfer(self, cmd, params, callback):
    pass
# WARNING: Decompyle incomplete


def do_transfer_blocking(self, cmd, params = (None,)):
    '''
        This function is for testing purposes only!
        '''
    pass
# WARNING: Decompyle incomplete


def do_transfer_reset(self, cmd, params, callback):
    pass
# WARNING: Decompyle incomplete


def do_transfer_reset_blocking(self, cmd, params = (None,)):
    '''
        This function is for testing purposes only!
        '''
    pass
# WARNING: Decompyle incomplete


def start_streaming_packets(self, packet_count, transfer_count, timeout, callback):
    pass
# WARNING: Decompyle incomplete


def stop_streaming_packets(self):
    self.device.stop_streaming_packets(self.device)
    
    try:
        del self._streaming_callback
        return None
    except AttributeError:
        return None



def get_stream_packets_blocking(self, byte_count, timeout):
    buffer = c_uint8 * byte_count()
    count_int = c_int(byte_count)
    ret = self.device.get_stream_packets_blocking(self.device, buffer, byref(count_int), timeout)
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    return bytes(buffer[0:count_int.value])


def get_max_incoming_param_length(self):
    v = self.device.get_max_incoming_param_length(self.device)
    return v


def get_max_outgoing_param_length(self):
    v = self.device.get_max_outgoing_param_length(self.device)
    return v


def get_stream_packet_length(self):
    v = self.device.get_stream_packet_length(self.device)
    return v


def poll_device(self, milliseconds):
    ret = self.device.poll_device(self.device, milliseconds, None)
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)


def set_connect_callback(self, callback):
    pass
# WARNING: Decompyle incomplete


def wait_for_connect(self, timeout):
    ret = self.device.wait_for_connect(self.device, timeout)
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)


def _get_raw_remote_device(self):
    remote_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
    ret = self.device.get_remote_device(self.device, byref(remote_ptr))
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    return remote_ptr.contents


def get_remote_device(self):
    pass
# WARNING: Decompyle incomplete


def reconnect(self, bootloader, application, serial_number = (False, False, None)):
    if bootloader and application:
        raise ValueError('cannot set both application and bootloader')
    if bootloader:
        reconnect_func = self.reconnect_device_bootloader
    elif application:
        reconnect_func = self.reconnect_device_application
    else:
        reconnect_func = self.reconnect_device
    if not serial_number:
        
        try:
            serial_number = self.get_serial_number()
        except AsphodelError:
            pass

        end_time = time.monotonic() + self.reconnect_time
        time.sleep(0.5)
        
        try:
            reconnect_func(reopen = True)
        except AsphodelError:
            if time.monotonic() >= end_time:
                raise 

        if serial_number:
            device = find_device_by_serial(serial_number)
            if device:
                time.sleep(0.5)
                
                try:
                    reconnect_func(reopen = True)
                except AsphodelError:
                    pass

                time.sleep(0.5)
                
                try:
                    reconnect_func(reopen = True)
                except AsphodelError:
                    pass

                native_device = device.device
                device.device = None
                self._reconnect_helper(native_device, reopen = True)
            else:
                time.sleep(0.25)
            self.wait_for_connect(int(self.reconnect_time * 1000))
            return None


def _reconnect_helper(self, new_device, reopen):
    if addressof(new_device) == addressof(self.device):
        return None
    None.close()
    if self.device:
        self.device.free_device(self.device)
    self.device = new_device
    if reopen:
        self.open()
# WARNING: Decompyle incomplete


def reconnect_device(self, reopen = (False,)):
    reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
    ret = self.device.reconnect_device(self.device, byref(reconnected_ptr))
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    self._reconnect_helper(reconnected_ptr.contents, reopen)


def reconnect_device_bootloader(self, reopen = (False,)):
    reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
    ret = self.device.reconnect_device_bootloader(self.device, byref(reconnected_ptr))
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    self._reconnect_helper(reconnected_ptr.contents, reopen)


def reconnect_device_application(self, reopen = (False,)):
    reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
    ret = self.device.reconnect_device_application(self.device, byref(reconnected_ptr))
    if ret != 0:
        error_name = self.lib.lib.asphodel_error_name(ret)
        raise AsphodelError(ret, error_name)
    self._reconnect_helper(reconnected_ptr.contents, reopen)


def supports_rf_power_commands(self):
    v = self.lib.lib.asphodel_supports_rf_power_commands(self.device)
    return bool(v)


def supports_radio_commands(self):
    v = self.lib.lib.asphodel_supports_radio_commands(self.device)
    return bool(v)


def supports_remote_commands(self):
    v = self.lib.lib.asphodel_supports_remote_commands(self.device)
    return bool(v)


def supports_bootloader_commands(self):
    v = self.lib.lib.asphodel_supports_bootloader_commands(self.device)
    return bool(v)


def set_error_callback(self, callback):
    pass
# WARNING: Decompyle incomplete


def tcp_get_advertisement(self):
    return self.lib.tcp_get_advertisement(self.device)

get_protocol_version = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_protocol_version_string = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_board_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_user_tag_locations = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_build_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_build_date = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_commit_id = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_repo_branch = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_repo_name = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_chip_family = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_chip_model = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_chip_id = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_nvm_size = (lambda self: pass# WARNING: Decompyle incomplete
)()
erase_nvm = (lambda self: pass# WARNING: Decompyle incomplete
)()
write_nvm_raw = (lambda self, address, values: pass# WARNING: Decompyle incomplete
)()
write_nvm_section = (lambda self, address, values: pass# WARNING: Decompyle incomplete
)()
read_nvm_raw = (lambda self, address: pass# WARNING: Decompyle incomplete
)()
read_nvm_section = (lambda self, address, length: pass# WARNING: Decompyle incomplete
)()
read_user_tag_string = (lambda self, offset, length: pass# WARNING: Decompyle incomplete
)()
write_user_tag_string = (lambda self, offset, length, string: pass# WARNING: Decompyle incomplete
)()
get_nvm_modified = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_nvm_hash = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_setting_hash = (lambda self: pass# WARNING: Decompyle incomplete
)()
flush = (lambda self: pass# WARNING: Decompyle incomplete
)()
reset = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_bootloader_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
bootloader_jump = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_reset_flag = (lambda self: pass# WARNING: Decompyle incomplete
)()
clear_reset_flag = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_rgb_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_rgb_values = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
set_rgb_values = (lambda self, index, values, instant = (False,): pass# WARNING: Decompyle incomplete
)()
set_rgb_values_hex = (lambda self, index, hex_color, instant = (False,): pass# WARNING: Decompyle incomplete
)()
get_led_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_led_value = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
set_led_value = (lambda self, index, value, instant = (False,): pass# WARNING: Decompyle incomplete
)()
set_device_mode = (lambda self, mode: pass# WARNING: Decompyle incomplete
)()
get_device_mode = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_stream_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_stream = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_stream_channels = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_stream_format = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
enable_stream = (lambda self, index, enable = (True,): pass# WARNING: Decompyle incomplete
)()
warm_up_stream = (lambda self, index, enable = (True,): pass# WARNING: Decompyle incomplete
)()
get_stream_status = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_stream_rate_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_channel_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_channel = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_channel_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_channel_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_channel_coefficients = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_channel_chunk = (lambda self, index, chunk_number: pass# WARNING: Decompyle incomplete
)()
channel_specific = (lambda self, index, values: pass# WARNING: Decompyle incomplete
)()
get_channel_calibration = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_supply_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_supply_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_supply_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
check_supply = (lambda self, index, tries = (20,): pass# WARNING: Decompyle incomplete
)()
get_ctrl_var_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_ctrl_var_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_ctrl_var_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_ctrl_var = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
set_ctrl_var = (lambda self, index, value: pass# WARNING: Decompyle incomplete
)()
get_setting_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_setting_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_setting_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_setting_default = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_custom_enum_counts = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_custom_enum_value_name = (lambda self, index, value: pass# WARNING: Decompyle incomplete
)()
get_setting_category_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_setting_category_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_setting_category_settings = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_gpio_port_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_gpio_port_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_gpio_port_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_gpio_port_values = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
set_gpio_port_modes = (lambda self, index, mode, pins: pass# WARNING: Decompyle incomplete
)()
disable_gpio_overrides = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_bus_counts = (lambda self: pass# WARNING: Decompyle incomplete
)()
set_spi_cs_mode = (lambda self, index, mode: pass# WARNING: Decompyle incomplete
)()
do_spi_transfer = (lambda self, index, write_bytes: pass# WARNING: Decompyle incomplete
)()
do_i2c_write = (lambda self, index, addr, write_bytes: pass# WARNING: Decompyle incomplete
)()
do_i2c_read = (lambda self, index, addr, read_length: pass# WARNING: Decompyle incomplete
)()
do_i2c_write_read = (lambda self, index, addr, write_bytes, read_length: pass# WARNING: Decompyle incomplete
)()
do_radio_fixed_test = (lambda self, channel, duration, mode: pass# WARNING: Decompyle incomplete
)()
do_radio_sweep_test = (lambda self, start, stop, hop_interval, hop_count, mode: pass# WARNING: Decompyle incomplete
)()
get_info_region_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_info_region_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_info_region = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
get_stack_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
echo_raw = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
echo_transaction = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
echo_params = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
enable_rf_power = (lambda self, enable = (True,): pass# WARNING: Decompyle incomplete
)()
get_rf_power_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_rf_power_ctrl_vars = (lambda self: pass# WARNING: Decompyle incomplete
)()
reset_rf_power_timeout = (lambda self, timeout: pass# WARNING: Decompyle incomplete
)()
stop_radio = (lambda self: pass# WARNING: Decompyle incomplete
)()
start_radio_scan = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_raw_radio_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_radio_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_raw_radio_extra_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_radio_extra_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_radio_scan_power = (lambda self, serial_numbers: pass# WARNING: Decompyle incomplete
)()
connect_radio = (lambda self, serial_number: pass# WARNING: Decompyle incomplete
)()
get_radio_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_radio_ctrl_vars = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_radio_default_serial = (lambda self: pass# WARNING: Decompyle incomplete
)()
start_radio_scan_boot = (lambda self: pass# WARNING: Decompyle incomplete
)()
connect_radio_boot = (lambda self, serial_number: pass# WARNING: Decompyle incomplete
)()
stop_remote = (lambda self: pass# WARNING: Decompyle incomplete
)()
restart_remote = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_remote_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
restart_remote_app = (lambda self: pass# WARNING: Decompyle incomplete
)()
restart_remote_boot = (lambda self: pass# WARNING: Decompyle incomplete
)()
bootloader_start_program = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_bootloader_page_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
get_bootloader_block_sizes = (lambda self: pass# WARNING: Decompyle incomplete
)()
start_bootloader_page = (lambda self, page_number, nonce: pass# WARNING: Decompyle incomplete
)()
write_bootloader_code_block = (lambda self, data: pass# WARNING: Decompyle incomplete
)()
write_bootloader_page = (lambda self, data, block_sizes: pass# WARNING: Decompyle incomplete
)()
finish_bootloader_page = (lambda self, mac_tag = (None,): pass# WARNING: Decompyle incomplete
)()
verify_bootloader_page = (lambda self, mac_tag = (None,): pass# WARNING: Decompyle incomplete
)()

def get_strain_bridge_count(self, channel_info):
    count = c_int()
    self.lib.lib.asphodel_get_strain_bridge_count(channel_info, byref(count))
    return count.value


def get_strain_bridge_subchannel(self, channel_info, bridge_index):
    subchannel = c_size_t()
    self.lib.lib.asphodel_get_strain_bridge_subchannel(channel_info, bridge_index, byref(subchannel))
    return subchannel.value


def get_strain_bridge_values(self, channel_info, bridge_index):
    array = c_float * 5()
    self.lib.lib.asphodel_get_strain_bridge_values(channel_info, bridge_index, array)
# WARNING: Decompyle incomplete

set_strain_outputs = (lambda self, channel_index, bridge_index, pos, neg: pass# WARNING: Decompyle incomplete
)()

def check_strain_resistances(self, channel_info, bridge_index, baseline, pos_high, neg_high):
    '''
        Return (passed, pos_res, neg_res)
        '''
    passed = c_int(0)
    pos_res = c_double()
    neg_res = c_double()
    self.lib.lib.asphodel_check_strain_resistances(channel_info, bridge_index, baseline, pos_high, neg_high, byref(pos_res), byref(neg_res), byref(passed))
    return (bool(passed.value), pos_res.value, neg_res.value)


def get_accel_self_test_limits(self, channel_info):
    array = c_float * 6()
    self.lib.lib.asphodel_get_accel_self_test_limits(channel_info, array)
# WARNING: Decompyle incomplete

enable_accel_self_test = (lambda self, channel_index, enable = (True,): pass# WARNING: Decompyle incomplete
)()

def check_accel_self_test(self, channel_info, disabled, enabled):
    '''
        Return passed
        '''
    pass
# WARNING: Decompyle incomplete


def get_channel_decoder(self, index, bit_offset):
    channel_info = self.get_channel(index)
    return self.lib.create_channel_decoder(channel_info, bit_offset)


def get_stream_decoder(self, index, bit_offset):
    stream_info = self.get_stream(index)
    channel_info_list = []
    indexes = stream_info.channel_index_list[0:stream_info.channel_count]
    for ch_index in indexes:
        channel_info_list.append(self.get_channel(ch_index))
        return self.lib.create_stream_decoder(stream_info, channel_info_list, bit_offset)


def get_device_decoder(self):
    (stream_count, filler_bits, id_bits) = self.get_stream_count()
    info_list = []
    for i in range(stream_count):
        stream_struct = self.get_stream(i)
        channel_info_list = []
        channels = stream_struct.channel_count
        indexes = stream_struct.channel_index_list[0:channels]
        for ch_index in indexes:
            channel_info_list.append(self.get_channel(ch_index))
            info_list.append((i, stream_struct, channel_info_list))
            return self.lib.create_device_decoder(info_list, filler_bits, id_bits)


def get_streaming_counts(self, response_time, buffer_time, timeout):
    pass
# WARNING: Decompyle incomplete


def get_channel_unit_formatter(self, index, use_metric):
    info = self.get_channel_info(index)
    return self.lib.create_unit_formatter(info.unit_type, info.minimum, info.maximum, info.resolution, use_metric)


def get_ctrl_var_unit_formatter(self, index, use_metric):
    info = self.get_ctrl_var_info(index)
    (unit_type, minimum, maximum, scale, offset) = info
    return self.lib.create_unit_formatter(unit_type, minimum * scale + offset, maximum * scale + offset, scale, use_metric)


def get_setting(self, index):
    info = self.get_setting_info(index)
    name = self.get_setting_name(index)
    default = self.get_setting_default(index)
    name_bytes = name.encode('UTF-8')
    info.name = name_bytes
    info.name_length = len(name_bytes)
# WARNING: Decompyle incomplete

