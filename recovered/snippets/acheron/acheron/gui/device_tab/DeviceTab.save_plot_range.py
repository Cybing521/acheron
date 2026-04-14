# Source Generated with Decompyle++
# File: tmp8wpix2r3.marshal (Python 3.11)

save_dict = self.saved_plot_ranges.setdefault(channel_id, { })
time_vb = self.timePlot.getViewBox()
if not isinstance(time_vb, pyqtgraph.ViewBox):
    return None
time_autorange = None.autoRangeEnabled()
time_range = time_vb.targetRange()
save_dict['time'] = (time_autorange, time_range)
# WARNING: Decompyle incomplete
