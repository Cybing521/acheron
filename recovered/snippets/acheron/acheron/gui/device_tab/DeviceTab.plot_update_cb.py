# Source Generated with Decompyle++
# File: tmp68wt0i_i.marshal (Python 3.11)

selected_channel_id = self.get_current_channel_id()
if channel_id != selected_channel_id:
    return None

try:
    channel_info = self.controller.channel_info[channel_id]
except KeyError:
    return None

if self.last_channel_id != channel_id:
    self.last_channel_id = channel_id
    if channel_info.downsample_factor == 1:
        self.timePlot.setTitle('Time Domain')
    else:
        s = 'Time Domain (Downsampled {}x)'.format(channel_info.downsample_factor)
        self.timePlot.setTitle(s)
unit_formatter = self.channel_unit[channel_id].unit_formatter
data = data * unit_formatter.conversion_scale + unit_formatter.conversion_offset
for array, curve in zip(data.transpose(), self.time_curves):
    curve.setData(time, array.flatten())
    return None
