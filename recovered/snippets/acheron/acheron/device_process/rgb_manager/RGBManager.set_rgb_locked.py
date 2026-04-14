# Source Generated with Decompyle++
# File: tmpiik8wvpf.marshal (Python 3.11)

if self.device_info or len(self.device_info.rgb_settings) > index or self.device_info.rgb_settings[index] != values:
    self.device_info.rgb_settings[index] = values
    self.device.set_rgb_values(index, values, instant = instant)
    self.callback(index, values)
    return None
return None
return None
