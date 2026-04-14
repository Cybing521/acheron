# Source Generated with Decompyle++
# File: tmpsi4olctw.marshal (Python 3.11)

alert_limits = { }
for limit_type, enabled, spinbox in self.limit_type_widgets:
    if enabled.isChecked():
        alert_limits[limit_type] = spinbox.value()
    return alert_limits
