# Source Generated with Decompyle++
# File: tmpy1f005c_.marshal (Python 3.11)

ret = self.device.open_device(self.device)
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
