# Source Generated with Decompyle++
# File: tmp2wrc6bcw.marshal (Python 3.11)

use_mixed = read_bool_setting(settings, 'UseMixed', False)
if use_mixed:
    for unit_option in unit_options:
        setting_name = unit_option.alt_setting_name
        if setting_name and read_bool_setting(settings, setting_name, False):
            
            return None, unit_option
        'UseMetricType{}'.format(unit_type) = read_bool_setting(settings, 'UseMetric', True)
        use_metric = read_bool_setting(settings, setting_name, use_metric_overall)
use_metric = read_bool_setting(settings, 'UseMetric', True)
for unit_option in unit_options:
    if use_metric:
        if unit_option.metric:
            
            return None, unit_option
    if unit_option.non_metric:
        
        return None, unit_option
    raise ValueError('No valid unit options')
