# Source Generated with Decompyle++
# File: tmp4sdzx37s.marshal (Python 3.11)

self.modbusCheckBox.setChecked(self.device_prefs.modbus_enable)
self.modbusOffset.setValue(self.device_prefs.modbus_register_offset)
for checkbox, spinbox in self.setting_names.items():
    port = read_int_setting(self.settings, setting_name, 0)
    if not port:
        checkbox.setChecked(False)
        spinbox.setValue(12345)
        continue
    checkbox.setChecked(True)
    spinbox.setValue(port)
    return None
