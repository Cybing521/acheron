# Source Generated with Decompyle++
# File: tmpoinjf1sy.marshal (Python 3.11)

dialog = self.unit_selection_dialog
ret = dialog.exec()
if ret == 0:
    return None
unit_info = None.get_unit_info()
if not unit_info:
    return None
self.unit_info = None
unit_formatter = self.unit_info[1]
self.unit.setText(unit_formatter.unit_utf8)
rms_formatter = asphodel.nativelib.create_custom_unit_formatter(unit_formatter.conversion_scale, 0, 0, unit_formatter.unit_ascii, unit_formatter.unit_utf8, unit_formatter.unit_html)
self.actualMagnitude.set_unit_formatter(rms_formatter)
self.actualOffset.set_unit_formatter(unit_formatter)
row_count = self.linearTable.rowCount()
for row in range(row_count):
    actual = cast(UnitFormatterDoubleSpinBox, self.linearTable.cellWidget(row, 1))
    actual.set_unit_formatter(unit_formatter)
    self.plot.setLabel('left', unit_formatter.unit_html)
    self.update_all()
    return None
