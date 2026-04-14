# Source Generated with Decompyle++
# File: tmpnv3ve90i.marshal (Python 3.11)

self.device_info = device_info
if self.auto_rgb:
    if device_info.supports_radio:
        self.set_rgb_locked(0, (0, 255, 255))
        return None
    None.set_rgb_locked(0, (0, 0, 255))
    return None
