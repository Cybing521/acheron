# Source Generated with Decompyle++
# File: tmp3wkk_ypq.marshal (Python 3.11)

incrementer = Incrementer(progress_callback, device_logger)
serial_number = device.get_serial_number()
if not serial_number:
    raise asphodel.AsphodelError('No serial number when fetching device info')
protocol_type = device.device.protocol_type
build_info = device.get_build_info()
build_date = device.get_build_date()
nvm_hash = try_optional(device.get_nvm_hash)
nvm_modified = try_optional(device.get_nvm_modified)
setting_hash = try_optional(device.get_setting_hash)
finished_commands = 4
total_commands = 4
board_info_key = None
if device.supports_remote_commands():
    (connected, remote_serial_number, _protocol) = device.get_remote_status()
    if connected:
        board_info_key = remote_serial_number
setting_key = (serial_number, protocol_type, build_info, build_date, setting_hash)
if not hash_is_valid(setting_hash) and allow_reconnect:
    setting_info = { }
# WARNING: Decompyle incomplete
