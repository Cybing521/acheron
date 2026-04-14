# Source Generated with Decompyle++
# File: tmp867cqlnp.marshal (Python 3.11)

remote_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
ret = self.device.get_remote_device(self.device, byref(remote_ptr))
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
return remote_ptr.contents
