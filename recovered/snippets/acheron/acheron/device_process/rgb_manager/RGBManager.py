# Source Generated with Decompyle++
# File: tmpgqnsgiu4.marshal (Python 3.11)


def __init__(self = None, device = None, auto_rgb = None, callback = ('device', asphodel.AsphodelNativeDevice, 'auto_rgb', bool, 'callback', RGBCallback)):
    self.device = device
    self.auto_rgb = auto_rgb
    self.callback = callback
    self.device_info = None


def set_auto_rgb_locked(self = None, auto_rgb = None):
    self.auto_rgb = auto_rgb


def set_rgb_locked(self = None, index = None, values = None, instant = (False,)):
    if self.device_info or len(self.device_info.rgb_settings) > index or self.device_info.rgb_settings[index] != values:
        self.device_info.rgb_settings[index] = values
        self.device.set_rgb_values(index, values, instant = instant)
        self.callback(index, values)
        return None
    return None
    return None


def connected_locked(self = None, device_info = None):
    self.device_info = device_info
    if self.auto_rgb:
        if device_info.supports_radio:
            self.set_rgb_locked(0, (0, 255, 255))
            return None
        None.set_rgb_locked(0, (0, 0, 255))
        return None


def streaming_locked(self = None):
    if self.auto_rgb or self.device_info:
        if self.device_info.supports_radio:
            return None
        None.set_rgb_locked(0, (0, 255, 0))
        return None
    return None


def disconnected_locked(self = None):
    if self.auto_rgb:
        self.set_rgb_locked(0, (255, 0, 0), instant = True)
    self.device_info = None


def remote_connected_locked(self = None):
    if self.auto_rgb:
        self.set_rgb_locked(0, (0, 255, 0))
        return None


def remote_disconnected_locked(self = None):
    if self.auto_rgb:
        self.set_rgb_locked(0, (0, 255, 255))
        return None

