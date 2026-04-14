# Source Generated with Decompyle++
# File: tmp0zplsnx7.marshal (Python 3.11)

channel = channel_info.channel
unit_options = get_unit_options(channel.unit_type, channel.minimum, channel.maximum, channel.resolution)
default = get_default_option(self.settings, channel.unit_type, unit_options)
action_group = QtGui.QActionGroup(self)
unit_actions = []
for unit_option in unit_options:
    action = QtGui.QAction(action_group)
    if unit_option.metric_relation:
        action.setText('{} ({})'.format(unit_option.base_str, unit_option.metric_relation))
    else:
        action.setText(unit_option.base_str)
    action.setCheckable(True)
    if unit_option == default:
        action.setChecked(True)
    action_cb = functools.partial(self._unit_selected, channel_id, unit_option)
    action.triggered.connect(action_cb)
    unit_actions.append(action)
    self.channel_unit_options[channel_id] = unit_options
    self.channel_unit_actions[channel_id] = unit_actions
    self.channel_unit_action_group[channel_id] = action_group
    self.channel_unit_type[channel_id] = channel.unit_type
    self.channel_unit_default[channel_id] = default
    self.channel_unit[channel_id] = default
    field_list = []
    alert_actions = []
    for i, subchannel_name in enumerate(channel_info.subchannel_names):
        label = QtWidgets.QLabel(subchannel_name)
        mean_field = MeasurementLineEdit(unit_actions)
        std_dev_field = MeasurementLineEdit(unit_actions)
        sampling_rate_field = MeasurementLineEdit(None)
        sampling_rate = '{:g} sps'.format(channel_info.rate)
        sampling_rate_field.setText(sampling_rate)
        edit_alert_button = QtWidgets.QToolButton()
        edit_alert_action = EditAlertAction(channel_id, i, subchannel_name, self, edit_alert_button)
        edit_alert_button.setDefaultAction(edit_alert_action)
        alert_actions.append(edit_alert_action)
        row = self.channelLayout.rowCount()
        self.channelLayout.addWidget(label, row, 0)
        self.channelLayout.addWidget(mean_field, row, 1)
        self.channelLayout.addWidget(std_dev_field, row, 2)
        self.channelLayout.addWidget(sampling_rate_field, row, 3)
        self.channelLayout.addWidget(edit_alert_button, row, 4)
        field_list.append((mean_field, std_dev_field))
        self.subchannel_fields[channel_id] = field_list
        self.channel_alert_actions[channel_id] = alert_actions
        return None
