# Source Generated with Decompyle++
# File: tmpho6m62jj.marshal (Python 3.11)

ret = self.device.poll_device(self.device, milliseconds, None)
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
