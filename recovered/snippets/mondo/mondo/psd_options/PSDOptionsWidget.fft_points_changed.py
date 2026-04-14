# Source Generated with Decompyle++
# File: tmpiifepzt2.marshal (Python 3.11)

index = self.fftPoints.currentIndex()
window_size = self.fft_points_by_index[index]
original_percent = self.overlapPercent.value()
if self.overlapPoints.value() >= window_size:
    self.overlapPoints.setValue(window_size - 1)
self.overlapPoints.setMaximum(window_size - 1)
self.overlapPercent.setMaximum(100 * (window_size - 1) / window_size)
self.changing_overlap = True
self.overlapPercent.setValue(original_percent)
self.changing_overlap = False
self.overlap_percent_changed()
window_duration = window_size / self.sampling_rate
self.duration.setText('{:.3f} s'.format(window_duration))
frequency_resolution = self.sampling_rate / window_size
self.resolution.setText('{:.3f} Hz'.format(frequency_resolution))
