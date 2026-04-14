# Source Generated with Decompyle++
# File: tmpif4mised.marshal (Python 3.11)

mean_formatter = asphodel.nativelib.create_custom_unit_formatter(self.unit_formatter.conversion_scale, self.unit_formatter.conversion_offset, 0, self.unit_formatter.unit_ascii, self.unit_formatter.unit_utf8, self.unit_formatter.unit_html)
std_formatter = asphodel.nativelib.create_custom_unit_formatter(self.unit_formatter.conversion_scale, 0, 0, self.unit_formatter.unit_ascii, self.unit_formatter.unit_utf8, self.unit_formatter.unit_html)
self.meanHigh.set_unit_formatter(mean_formatter)
self.meanLow.set_unit_formatter(mean_formatter)
self.stdHigh.set_unit_formatter(std_formatter)
self.stdLow.set_unit_formatter(std_formatter)
self.meanHigh.setMaximum(math.inf)
self.meanHigh.setMinimum(-(math.inf))
self.meanLow.setMaximum(math.inf)
self.meanLow.setMinimum(-(math.inf))
self.stdHigh.setMaximum(math.inf)
self.stdHigh.setMinimum(0)
self.stdLow.setMaximum(math.inf)
self.stdLow.setMinimum(0)
self.limit_type_widgets = ((LimitType.MEAN_HIGH_LIMIT, self.meanHighEnabled, self.meanHigh), (LimitType.MEAN_LOW_LIMIT, self.meanLowEnabled, self.meanLow), (LimitType.STD_HIGH_LIMIT, self.stdHighEnabled, self.stdHigh), (LimitType.STD_LOW_LIMIT, self.stdLowEnabled, self.stdLow))
# WARNING: Decompyle incomplete
