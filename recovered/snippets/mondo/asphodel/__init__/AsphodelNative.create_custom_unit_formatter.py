# Source Generated with Decompyle++
# File: tmpxl2bvvd6.marshal (Python 3.11)

formatter = self.lib.asphodel_create_custom_unit_formatter(scale, offset, resolution, unit_ascii.encode('ascii'), unit_utf8.encode('UTF-8'), unit_html.encode('ascii'))
if not formatter:
    raise AsphodelError(0, 'asphodel_create_custom_unit_formatter returned NULL')
recreate = (recreate_custom_unit_formatter, (scale, offset, resolution, unit_ascii, unit_utf8, unit_html))
return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)
