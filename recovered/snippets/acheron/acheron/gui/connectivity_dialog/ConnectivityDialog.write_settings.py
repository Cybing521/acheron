# Source Generated with Decompyle++
# File: tmpfaqcngph.marshal (Python 3.11)

self.device_prefs.modbus_enable = self.modbusCheckBox.isChecked()
self.device_prefs.modbus_register_offset = self.modbusOffset.value()
for checkbox, spinbox in self.setting_names.items():
    if checkbox.isChecked():
        port = spinbox.value()
        self.settings.setValue(setting_name, port)
        continue
    self.settings.remove(setting_name)
    return None
