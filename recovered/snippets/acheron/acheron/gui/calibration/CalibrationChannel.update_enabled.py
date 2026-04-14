# Source Generated with Decompyle++
# File: tmpp7h5ssez.marshal (Python 3.11)

enabled = self.calibrationEnabled.isChecked()
self.unitLabel.setEnabled(enabled)
self.unit.setEnabled(enabled)
self.selectUnit.setEnabled(enabled)
if enabled:
    unit_ready = self.unit_info is not None
else:
    unit_ready = False
self.linearPage.setEnabled(unit_ready)
self.acPage.setEnabled(unit_ready)
self.scaleLabel.setEnabled(unit_ready)
self.scale.setEnabled(unit_ready)
self.offsetLabel.setEnabled(unit_ready)
self.offset.setEnabled(unit_ready)
