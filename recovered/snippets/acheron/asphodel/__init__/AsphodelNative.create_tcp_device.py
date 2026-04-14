# Source Generated with Decompyle++
# File: tmp72p_qd5w.marshal (Python 3.11)

device_ptr = POINTER(self.AsphodelDeviceStruct)()
if serial:
    serial_bytes = serial.encode('UTF-8')
else:
    serial_bytes = None
self.lib.asphodel_tcp_create_device(host.encode('UTF-8'), port, timeout, serial_bytes, byref(device_ptr))
return AsphodelNativeDevice(self, device_ptr.contents)
