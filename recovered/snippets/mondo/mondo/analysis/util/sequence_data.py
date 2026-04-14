# Source Generated with Decompyle++
# File: tmpkrgx6bs2.marshal (Python 3.11)

sequence_info = { }
unit_info = { }
for channel_index, channel_data in sorted(batch_info.items()):
    indexes = channel_data.indexes - channel_data.indexes[0]
    repeated_indexes = numpy.repeat(indexes.astype(numpy.double), channel_data.samples)
    fractional_section = numpy.array(range(channel_data.samples), dtype = numpy.double) / channel_data.samples
    fractional_indexes = numpy.tile(fractional_section, channel_data.length)
    orig_time = (repeated_indexes + fractional_indexes) / channel_data.stream.rate
    orig_data = channel_data.data
    if raw_units:
        unit_formatter = asphodel.nativelib.create_unit_formatter(channel_data.channel.unit_type, 0, 0, channel_data.channel.resolution, use_metric = True)
    elif unscaled_units:
        ch_min = 0
        ch_max = 0
    else:
        ch_min = numpy.nanmin(orig_data).item()
        ch_max = numpy.nanmax(orig_data).item()
    settings = QtCore.QSettings()
    unit_formatter = hyperborea.unit_preferences.create_unit_formatter(settings, channel_data.channel.unit_type, ch_min, ch_max, channel_data.channel.resolution)
    unit_info[channel_index] = UnitInfo(unit_formatter.unit_ascii, unit_formatter.unit_html, unit_formatter.unit_utf8, unit_formatter)
    orig_data = orig_data * unit_formatter.conversion_scale + unit_formatter.conversion_offset
    if chunk:
        chunk_list = []
        last_data_index = 0
        last_timestamp_index = 0
        for _x, _y, index in enumerate(channel_data.lost_packet_list):
            data_index = index * channel_data.samples
            new_data = orig_data[last_data_index:data_index]
            new_time = orig_time[last_data_index:data_index]
            start = channel_data.timestamps[last_timestamp_index]
            end = channel_data.timestamps[index - 1]
            last_data_index = data_index
            last_timestamp_index = index
            chunk_list.append((new_time, new_data, start, end))
            new_data = orig_data[last_data_index:]
            new_time = orig_time[last_data_index:]
            start = channel_data.timestamps[last_timestamp_index]
            end = channel_data.timestamps[-1]
            chunk_list.append((new_time, new_data, start, end))
            sequence_info[channel_index] = chunk_list
            nan_count = len(channel_data.lost_packet_list)
            new_shape = (orig_data.shape[0] + nan_count, orig_data.shape[1])
            new_data = numpy.empty(new_shape)
            nan_slice = numpy.full((), numpy.nan, dtype = numpy.double)
            new_time = numpy.empty((new_shape[0],))
            last = 0
            for _x, _y, index in enumerate(channel_data.lost_packet_list):
                index *= channel_data.samples
                new_data[last + i:index + i] = orig_data[last:index]
                new_data[index + i] = nan_slice
                new_time[last + i:index + i] = orig_time[last:index]
                new_time[index + i] = orig_time[index - 1] + 1 / (channel_data.stream.rate * channel_data.samples)
                last = index
                new_data[last + nan_count:] = orig_data[last:]
                new_time[last + nan_count:] = orig_time[last:]
                start_time = channel_data.timestamps[0]
                end_time = channel_data.timestamps[-1]
                sequence_info[channel_index] = [
                    (new_time, new_data, start_time, end_time)]
                return (sequence_info, unit_info)
