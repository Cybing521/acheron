# Source Generated with Decompyle++
# File: tmp897sx6s3.marshal (Python 3.11)

metric_formatter = asphodel.nativelib.create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric = True)
us_formatter = asphodel.nativelib.create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric = False)
metric_scale = None
base_str = metric_formatter.unit_utf8
if metric_formatter.conversion_offset == 0:
    uf_1000x = asphodel.nativelib.create_unit_formatter(unit_type, minimum * 1000, maximum * 1000, resolution, use_metric = True)
    ratio = metric_formatter.conversion_scale / uf_1000x.conversion_scale
    if math.isclose(1000, ratio):
        metric_scale = 1 / metric_formatter.conversion_scale
        uf_base = asphodel.nativelib.create_unit_formatter(unit_type, 1, 1, 1, use_metric = True)
        base_str = uf_base.unit_utf8
unit_options = [
    UnitOption(unit_formatter = metric_formatter, metric = True, non_metric = metric_formatter == us_formatter, alt_setting_name = None, base_str = base_str, metric_scale = metric_scale, metric_relation = None)]
if metric_formatter != us_formatter:
    metric_relation = asphodel.nativelib.format_value_utf8(unit_type, 0, 1 / us_formatter.conversion_scale, use_metric = True)
    unit_options.append(UnitOption(unit_formatter = us_formatter, metric = False, non_metric = True, alt_setting_name = None, base_str = us_formatter.unit_utf8, metric_scale = None, metric_relation = metric_relation))
# WARNING: Decompyle incomplete
