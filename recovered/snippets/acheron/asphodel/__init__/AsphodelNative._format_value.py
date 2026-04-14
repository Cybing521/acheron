# Source Generated with Decompyle++
# File: tmp58p0war3.marshal (Python 3.11)

use_metric_int = 1 if use_metric else 0
buffer = create_string_buffer(256)
lib_func(buffer, len(buffer), unit_type, resolution, use_metric_int, value)
return buffer.value
