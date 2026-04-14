# Source Generated with Decompyle++
# File: tmp9232_8g3.marshal (Python 3.11)

count = c_size_t(0)
self.lib.asphodel_usb_find_devices(None, byref(count))
array_size = count.value
if array_size == 0:
    return []
array = POINTER(self.AsphodelDeviceStruct) * array_size()
array_ptr = cast(byref(array), POINTER(POINTER(self.AsphodelDeviceStruct)))
self.lib.asphodel_usb_find_devices(array_ptr, byref(count))
array_entries = min(array_size, count.value)
device_list = []
for i in range(array_entries):
    device_list.append(AsphodelNativeDevice(self, array[i].contents))
    return device_list
