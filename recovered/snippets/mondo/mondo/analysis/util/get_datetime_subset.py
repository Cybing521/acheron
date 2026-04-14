# Source Generated with Decompyle++
# File: tmpqee_ls5k.marshal (Python 3.11)

for _channel_index, channel_data in sorted(batch_info.items()):
    channel_name = channel_data.channel_decoder.channel_name
    d = numpy.diff(channel_data.timestamps)
    if numpy.min(d) < 0:
        s = 'Timestamps are not monotonic on channel {}! Continue?'
        message = s.format(channel_name)
        logger.warning(message)
        ret = QtWidgets.QMessageBox.warning(parent, 'Warning', message, buttons = QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, defaultButton = QtWidgets.QMessageBox.StandardButton.Yes)
        if ret == QtWidgets.QMessageBox.StandardButton.No:
            return None
        starts = batch_info.values()()
        ends = batch_info.values()()
        start = datetime.datetime.fromtimestamp(numpy.floor(min(starts)), datetime.timezone.utc)
        end = datetime.datetime.fromtimestamp(numpy.ceil(max(ends)), datetime.timezone.utc)
        start_qdt = QtCore.QDateTime(start)
        end_qdt = QtCore.QDateTime(end)
        dialog = DateTimeSubsetDialog(start_qdt, end_qdt, parent)
        dialog_ret = dialog.exec()
        if dialog_ret == 0:
            return None
        if (lambda .0: [ d.timestamps[-1] for d in .0 ]).should_use_all():
            return batch_info
        (start_qdt, end_qdt) = (lambda .0: [ d.timestamps[0] for d in .0 ]).get_subset()
        utc = datetime.timezone.utc
        start = cast(datetime.datetime, start_qdt.toPython()).replace(tzinfo = utc).timestamp()
        end = cast(datetime.datetime, end_qdt.toPython()).replace(tzinfo = utc).timestamp()
        new_indexes = { }
        some_empty = False
        for channel_index, channel_data in batch_info.items():
            start_index = bisect.bisect_left(channel_data.timestamps, start)
            end_index = bisect.bisect_right(channel_data.timestamps, end)
            if start_index >= end_index:
                some_empty = True
            new_indexes[channel_index] = (start_index, end_index)
            if some_empty:
                message = 'No data is present within this interval on one or more channels.'
                logger.warning(message)
                QtWidgets.QMessageBox.warning(parent, 'Warning', message)
                continue
for channel_index, channel_data in batch_info.items():
    (start_index, end_index) = new_indexes[channel_index]
    if start_index >= end_index:
        start_index = 0
        end_index = 0
    data_start = start_index * channel_data.samples
    data_end = end_index * channel_data.samples
    channel_data.data = channel_data.data[data_start:data_end]
    channel_data.indexes = channel_data.indexes[start_index:end_index]
    channel_data.timestamps = channel_data.timestamps[start_index:end_index]
    
    def trim_list(lost_packet_list = None, start_index = None, end_index = None):
        new_lost_packet_list = []
        for last, current, index in lost_packet_list:
            if index > start_index and index < end_index:
                new_lost_packet_list.append((last, current, index - start_index))
            return new_lost_packet_list

    channel_data.lost_packet_list = trim_list(channel_data.lost_packet_list, start_index, end_index)
    channel_data.lost_packet_file_boundary_list = trim_list(channel_data.lost_packet_file_boundary_list, start_index, end_index)
    channel_data.length = end_index - start_index
    channel_data.allocated = channel_data.length
    return batch_info
