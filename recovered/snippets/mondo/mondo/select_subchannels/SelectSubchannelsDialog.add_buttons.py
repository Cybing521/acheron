# Source Generated with Decompyle++
# File: tmpkya5m6lg.marshal (Python 3.11)

for channel_id, channel_name, subchannel_names in sorted(self.names):
    if len(subchannel_names) > 1:
        channel_label = QtWidgets.QLabel(channel_name, parent = self)
        self.verticalLayout.addWidget(channel_label)
        group_widget = QtWidgets.QWidget(parent = self)
        layout = QtWidgets.QVBoxLayout(group_widget)
        for i, subchannel_name in enumerate(subchannel_names):
            check_box = QtWidgets.QCheckBox(subchannel_name, parent = group_widget)
            self.subchannel_buttons[(channel_id, i)] = check_box
            check_box.setChecked(False)
            layout.addWidget(check_box)
            self.verticalLayout.addWidget(group_widget)
            check_box = QtWidgets.QCheckBox(subchannel_names[0], parent = self)
            self.subchannel_buttons[(channel_id, 0)] = check_box
            check_box.setChecked(False)
            self.verticalLayout.addWidget(check_box)
            return None
