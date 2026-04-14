# Source Generated with Decompyle++
# File: tmp773ak4sk.marshal (Python 3.11)

buffer = c_uint8 * byte_count()
count_int = c_int(byte_count)
ret = self.device.get_stream_packets_blocking(self.device, buffer, byref(count_int), timeout)
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
return bytes(buffer[0:count_int.value])
