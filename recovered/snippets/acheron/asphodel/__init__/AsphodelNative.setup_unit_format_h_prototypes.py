# Source Generated with Decompyle++
# File: tmpubzge0r4.marshal (Python 3.11)

self.load_library_function('asphodel_create_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
    c_uint8,
    c_double,
    c_double,
    c_double,
    c_int], None)
self.load_library_function('asphodel_create_custom_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
    c_double,
    c_double,
    c_double,
    c_char_p,
    c_char_p,
    c_char_p], None)
self.load_library_function('asphodel_format_value_ascii', c_int, [
    c_char_p,
    c_size_t,
    c_uint8,
    c_double,
    c_int,
    c_double], None)
self.load_library_function('asphodel_format_value_utf8', c_int, [
    c_char_p,
    c_size_t,
    c_uint8,
    c_double,
    c_int,
    c_double], None)
self.load_library_function('asphodel_format_value_html', c_int, [
    c_char_p,
    c_size_t,
    c_uint8,
    c_double,
    c_int,
    c_double], None)
