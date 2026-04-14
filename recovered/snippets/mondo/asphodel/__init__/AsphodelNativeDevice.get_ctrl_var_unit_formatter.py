# Source Generated with Decompyle++
# File: tmp2x9gfhpy.marshal (Python 3.11)

info = self.get_ctrl_var_info(index)
(unit_type, minimum, maximum, scale, offset) = info
return self.lib.create_unit_formatter(unit_type, minimum * scale + offset, maximum * scale + offset, scale, use_metric)
