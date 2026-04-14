# Source Generated with Decompyle++
# File: tmp0xdkbss7.marshal (Python 3.11)

if new_settings == self.settings:
    return False
if None.response_time != self.settings.response_time and new_settings.buffer_time != self.settings.buffer_time and new_settings.timeout != self.settings.timeout or new_settings.default_output_config != self.settings.default_output_config:
    self.settings = new_settings
    return True
None.device_lock
self.rgb_manager.set_auto_rgb_locked(new_settings.auto_rgb)
None(None, None)
