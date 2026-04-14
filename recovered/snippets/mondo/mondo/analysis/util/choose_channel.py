# Source Generated with Decompyle++
# File: tmp01utkku7.marshal (Python 3.11)

channel_indexes = set()
for stream_id in header['streams_to_activate']:
    stream = header['streams'][stream_id]
    for index in stream.channel_index_list[0:stream.channel_count]:
        channel_indexes.add(index)
        channel_names = []
        name_dict = { }
        for channel_index in sorted(channel_indexes):
            channel = header['channels'][channel_index]
            channel_name = channel.name[0:channel.name_length].decode('UTF-8')
            channel_names.append(channel_name)
            name_dict[channel_name] = channel_index
            (value, ok) = QtWidgets.QInputDialog.getItem(parent, 'Select Channel', 'Select Channel', channel_names, 0, editable = False)
            if not ok:
                return None
            return None[value]
