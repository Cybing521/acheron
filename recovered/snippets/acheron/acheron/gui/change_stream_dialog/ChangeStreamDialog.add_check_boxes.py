# Source Generated with Decompyle++
# File: tmptorgdecc.marshal (Python 3.11)

d = { }
for index, stream in enumerate(self.streams):
    check_box = QtWidgets.QCheckBox(self)
    check_box.setChecked(index in self.active_streams)
    self.check_boxes[index] = check_box
    stream_channels = stream.channel_index_list[:stream.channel_count]
    channel_names = []
    for ch_index in stream_channels:
        channel = self.channels[ch_index]
        channel_names.append(channel.name.decode('utf-8'))
        stream_text = 'Stream {} ({})'.format(index, ', '.join(channel_names))
        check_box.setText(stream_text)
        d[min(stream_channels)] = check_box
        for ch_index in sorted(d.keys()):
            check_box = d[ch_index]
            self.verticalLayout.addWidget(check_box)
            return None
