# Source Generated with Decompyle++
# File: tmppzz2b0ex.marshal (Python 3.11)

unit_settings = {
    cal.base_setting_index: unit_type }
float_settings = {
    cal.base_setting_index + 2: offset,
    cal.base_setting_index + 1: scale }
if math.isfinite(cal.minimum):
    minimum = cal.minimum * scale + offset
    float_settings[cal.base_setting_index + 3] = minimum
if math.isfinite(cal.maximum):
    maximum = cal.maximum * scale + offset
    float_settings[cal.base_setting_index + 4] = maximum
if cal.resolution_setting_index < settings_len:
    float_settings[cal.resolution_setting_index] = scale
return (unit_settings, float_settings)
