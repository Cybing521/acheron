# Source Generated with Decompyle++
# File: tmp24uxd0di.marshal (Python 3.11)

nvm_array = bytearray(nvm)
for key, value in device_config:
    setting_name = key.encode('UTF-8')
    for setting in device_info.settings:
        if setting.name == setting_name:
            configure_setting(setting, value, device_info, nvm_array)
        raise KeyError('No setting {}'.format(key))
        return bytes(nvm_array)
