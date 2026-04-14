# Source Generated with Decompyle++
# File: tmp03rcg5ks.marshal (Python 3.11)

info = self.get_ctrl_var_info(index)
(unit_type, minimum, maximum, scale, offset) = info
return self.lib.create_unit_formatter(unit_type, minimum * scale + offset, maximum * scale + offset, scale, use_metric)
