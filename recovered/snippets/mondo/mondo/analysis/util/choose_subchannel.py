# Source Generated with Decompyle++
# File: tmpeigjdvl9.marshal (Python 3.11)

options = list(channel_data.channel_decoder.subchannel_names)
if len(options) == 1:
    return 0
if None:
    options.insert(0, 'All Subchannels')
(value, ok) = QtWidgets.QInputDialog.getItem(parent, 'Select Subchannel', 'Select Subchannel', options, 0, editable = False)
if not ok:
    return None

try:
    return channel_data.channel_decoder.subchannel_names.index(value)
except ValueError:
    return -1

