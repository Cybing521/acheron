# Source Generated with Decompyle++
# File: tmpbu9vgsss.marshal (Python 3.11)

scaled_min = self.ctrl_var_info.minimum * self.ctrl_var_info.scale + self.ctrl_var_info.offset
scaled_max = self.ctrl_var_info.maximum * self.ctrl_var_info.scale + self.ctrl_var_info.offset
unit_formatter = asphodel.nativelib.create_unit_formatter(self.ctrl_var_info.unit_type, scaled_min, scaled_max, self.ctrl_var_info.scale)
self.spinBox = UnitFormatterSpinBox(self)
self.spinBox.set_unit_formatter(unit_formatter)
self.horizontalLayout.addWidget(self.spinBox)
self.spinBox.setMinimum(minimum)
self.spinBox.setMaximum(maximum)
self.spinBox.setValue(value)
self.slider.setMinimum(minimum)
self.slider.setMaximum(maximum)
self.slider.setValue(value)
self.spinBox.valueChanged.connect(self.slider.setValue)
self.slider.valueChanged.connect(self.spinBox.setValue)
