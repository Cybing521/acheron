# Source Generated with Decompyle++
# File: tmp7iar8nvx.marshal (Python 3.11)

device_info_dict = get_device_info_dict(remote, device_logger, False, diskcache, None, active_scan_setting_getters, [
    get_nvm_active_scan])
if 'nvm' not in device_info_dict:
    device_info_dict['nvm'] = None
return ActiveScanInfo.from_dict(device_info_dict)
