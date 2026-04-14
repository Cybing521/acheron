# Source Generated with Decompyle++
# File: tmpfz1s6cpi.marshal (Python 3.11)

d = { }
for stream_index, stream in enumerate(self.streams):
    stream_channels = stream.channel_index_list[:stream.channel_count]
    d[min(stream_channels)] = stream_index
    for _sort_key, stream_index in sorted(d.items()):
        stream = self.streams[stream_index]
        stream_channels = stream.channel_index_list[:stream.channel_count]
        if not stream_channels:
            continue
        radio_button = QtWidgets.QRadioButton('Stream {}'.format(stream_index), parent = self)
        self.stream_buttons.append(radio_button)
        self.verticalLayout.addWidget(radio_button)
        group_widget = QtWidgets.QWidget(parent = self)
        layout = QtWidgets.QVBoxLayout(group_widget)
        channel_group = { }
        self.channel_groups.append(channel_group)
        for channel_index in sorted(stream_channels):
            channel = self.channels[channel_index]
            channel_name = channel.name.decode('utf-8')
            check_box = QtWidgets.QCheckBox(channel_name, parent = group_widget)
            channel_group[channel_index] = check_box
            check_box.setChecked(False)
            layout.addWidget(check_box)
            self.verticalLayout.addWidget(group_widget)
            group_widget.setEnabled(False)
            radio_button.toggled.connect(group_widget.setEnabled)
            self.stream_buttons[0].setChecked(True)
            return None
