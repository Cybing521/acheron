# Source Generated with Decompyle++
# File: tmphzemmt_v.marshal (Python 3.11)

show_rf_test = self.preferences.show_rf_test
self.actionRFTestSeparator.setVisible(show_rf_test)
self.actionRFTest.setVisible(show_rf_test)
device_info = self.controller.device_info
if device_info:
    self.update_supply_display(device_info)
for channel_id, unit_options in self.channel_unit_options.items():
    unit_type = self.channel_unit_type[channel_id]
    new_default = get_default_option(self.settings, unit_type, unit_options)
    old_default = self.channel_unit_default[channel_id]
    if new_default != old_default:
        if old_default == self.channel_unit[channel_id]:
            self.channel_unit[channel_id] = new_default
            index = unit_options.index(new_default)
            action = self.channel_unit_actions[channel_id][index]
            action.setChecked(True)
        self.channel_unit_default[channel_id] = new_default
    self.update_alert_action_icons()
    self.graph_channel_changed()
    return None
