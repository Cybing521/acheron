# Source Generated with Decompyle++
# File: tmpq778_uug.marshal (Python 3.11)

buffer = create_string_buffer(64)
ret = self.device.get_serial_number(self.device, buffer, len(buffer))
if ret != 0:
    error_name = self.lib.lib.asphodel_error_name(ret)
    raise AsphodelError(ret, error_name)
return buffer.value.decode('UTF-8')
