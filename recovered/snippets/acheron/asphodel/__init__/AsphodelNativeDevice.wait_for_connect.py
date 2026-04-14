# Source Generated with Decompyle++
# File: tmp64pkzp2s.marshal (Python 3.11)

ret = self.device.wait_for_connect(self.device, timeout)
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
