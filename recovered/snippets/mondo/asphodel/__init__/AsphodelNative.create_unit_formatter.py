# Source Generated with Decompyle++
# File: tmp5pqbezvm.marshal (Python 3.11)

use_metric_int = 1 if use_metric else 0
formatter = self.lib.asphodel_create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric_int)
if not formatter:
    raise AsphodelError(0, 'asphodel_create_unit_formatter returned NULL')
recreate = (recreate_unit_formatter, (unit_type, minimum, maximum, resolution, use_metric))
return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)
