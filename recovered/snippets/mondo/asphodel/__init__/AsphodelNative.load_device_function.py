# Source Generated with Decompyle++
# File: tmp7xnyokyp.marshal (Python 3.11)

non_blocking_name = base_name
blocking_name = base_name + '_blocking'
blocking_argtypes = [
    POINTER(self.AsphodelDeviceStruct)]
blocking_argtypes.extend(argtypes)
non_blocking_argtypes = list(blocking_argtypes)
non_blocking_argtypes.append(self.AsphodelCommandCallback)
non_blocking_argtypes.append(c_void_p)
self.load_library_function(non_blocking_name, c_int, non_blocking_argtypes, self.asphodel_error_check)
self.load_library_function(blocking_name, c_int, blocking_argtypes, self.asphodel_error_check)
