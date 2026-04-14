# Source Generated with Decompyle++
# File: tmplotpcjft.marshal (Python 3.11)

reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
ret = self.device.reconnect_device_bootloader(self.device, byref(reconnected_ptr))
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
self._reconnect_helper(reconnected_ptr.contents, reopen)
