# Source Generated with Decompyle++
# File: tmp87ehu5lg.marshal (Python 3.11)

if len(sequence) == 1:
    return sequence[0]
str_list = None
str_indexes = { }
max_points = 0
max_index = 0
for time, _data, start_time, _end_time in enumerate(sequence):
    points = len(time)
    if max_points < points:
        max_points = points
        max_index = i
    duration = time[-1] - time[0]
    start_dt = datetime.datetime.fromtimestamp(start_time, datetime.timezone.utc)
    start_str = start_dt.strftime('%Y-%m-%d %H:%M:%S (UTC)')
    s = '{} points ({} s), starting {}'.format(points, duration, start_str)
    if s not in str_list:
        str_list.append(s)
        str_indexes[s] = i
    (value, ok) = QtWidgets.QInputDialog.getItem(parent, 'Select Contiguous Section', 'Select Section', str_list, max_index, editable = False)
    if not ok:
        return None
    return None[str_indexes[value]]
