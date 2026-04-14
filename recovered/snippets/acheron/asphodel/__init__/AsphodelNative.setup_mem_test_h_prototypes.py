# Source Generated with Decompyle++
# File: tmpmdjeracd.marshal (Python 3.11)


try:
    self.load_library_function('asphodel_mem_test_supported', c_int, [], None, ignore_missing = False)
    self.mem_test_supported = self.lib.asphodel_mem_test_supported()
except AttributeError:
    self.mem_test_supported = False

self.load_library_function('asphodel_mem_test_set_limit', None, [
    c_int], None)
self.load_library_function('asphodel_mem_test_get_limit', c_int, [], None)
