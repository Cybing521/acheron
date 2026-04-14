# Source Generated with Decompyle++
# File: tmphyb4sin7.marshal (Python 3.11)


try:
    (value, result_flags) = device.check_supply(supply_id)
except Exception:
    return 

info.nominal * info.scale + info.offset = value * info.scale + info.offset
if scaled_nominal != 0:
    percent = (scaled_value / scaled_nominal) * 100
else:
    percent = 0
formatted = asphodel.format_value_ascii(info.unit_type, info.scale, scaled_value)
success = True if result_flags == 0 else False
passfail = 'pass' if success else 'FAIL'
message = '{}: {} ({:.0f}%), result=0x{:02x}, {}'.format(name, formatted, percent, result_flags, passfail)
return (success, message)
