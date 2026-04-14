# Source Generated with Decompyle++
# File: tmp74luhya4.marshal (Python 3.11)

ret = self.device.poll_device(self.device, milliseconds, None)
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
