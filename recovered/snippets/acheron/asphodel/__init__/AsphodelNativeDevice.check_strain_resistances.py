# Source Generated with Decompyle++
# File: tmpvf3yzym9.marshal (Python 3.11)

passed = c_int(0)
pos_res = c_double()
neg_res = c_double()
self.lib.lib.asphodel_check_strain_resistances(channel_info, bridge_index, baseline, pos_high, neg_high, byref(pos_res), byref(neg_res), byref(passed))
return (bool(passed.value), pos_res.value, neg_res.value)
