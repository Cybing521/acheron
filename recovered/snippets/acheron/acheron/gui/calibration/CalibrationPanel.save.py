# Source Generated with Decompyle++
# File: tmpkwng6rum.marshal (Python 3.11)

settings = self.device_info.settings
unit_settings = { }
float_settings = { }
event_data = {
    'board_type': self.device_info.board_info[0],
    'board_rev': self.device_info.board_info[1],
    'computer': platform.node() }
for _name, channel_widget in self.channel_widgets:
    if channel_widget.calibrationEnabled.isChecked():
        results = channel_widget.get_results()
        if results:
            (unit_type, scale, offset, channel_event_data) = results
            (u, f) = get_channel_setting_values(len(settings), channel_widget.cal.calibration_info, unit_type, scale, offset)
            unit_settings.update(u)
            float_settings.update(f)
            event_data.update(channel_event_data)
    new_nvm = update_nvm(self.device_info.nvm, settings, unit_settings, float_settings, self.logger)
    self.event_uploader.calibration_finished(self.device_info.serial_number, event_data)
    self.write_nvm(new_nvm)
    return None
