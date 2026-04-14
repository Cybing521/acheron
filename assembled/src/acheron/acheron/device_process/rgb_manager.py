# Source Generated with Decompyle++
# File: rgb_manager.pyc (Python 3.11)

from typing import Callable, Optional
import asphodel
from asphodel.device_info import DeviceInfo
# INVALID FROM DECOMPILER: RGBCallback = Callable[([
# INVALID FROM DECOMPILER:     int,
# INVALID FROM DECOMPILER:     tuple[(int, int, int)]], None)]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RGBManager:

    def __init__(self, device, auto_rgb, callback):
        self.device = device
        self.auto_rgb = auto_rgb
        self.callback = callback
        self.device_info = None

    def set_auto_rgb_locked(self, auto_rgb):
        self.auto_rgb = auto_rgb

    def set_rgb_locked(self, index, values, instant=False):
        if self.device_info or len(self.device_info.rgb_settings) > index or self.device_info.rgb_settings[index] != values:
            self.device_info.rgb_settings[index] = values
            self.device.set_rgb_values(index, values, instant = instant)
            self.callback(index, values)
            return None
        return None
        return None

    def connected_locked(self, device_info):
        self.device_info = device_info
        if self.auto_rgb:
            if device_info.supports_radio:
                self.set_rgb_locked(0, (0, 255, 255))
                return None
            self.set_rgb_locked(0, (0, 0, 255))
            return None

    def streaming_locked(self):
        if self.auto_rgb and self.device_info:
            if self.device_info.supports_radio:
                return None
            self.set_rgb_locked(0, (0, 255, 0))
            return None
        return None

    def disconnected_locked(self):
        if self.auto_rgb:
            self.set_rgb_locked(0, (255, 0, 0), instant = True)
        self.device_info = None

    def remote_connected_locked(self):
        if self.auto_rgb:
            self.set_rgb_locked(0, (0, 255, 0))
            return None

    def remote_disconnected_locked(self):
        if self.auto_rgb:
            self.set_rgb_locked(0, (0, 255, 255))
            return None
