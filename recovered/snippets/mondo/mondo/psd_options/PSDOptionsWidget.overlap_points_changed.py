# Source Generated with Decompyle++
# File: tmppvlqdm3p.marshal (Python 3.11)

if self.changing_overlap:
    return None

try:
    self.changing_overlap = True
    index = self.fftPoints.currentIndex()
    window_size = self.fft_points_by_index[index]
    points = self.overlapPoints.value()
    percent = (points / window_size) * 100
    self.overlapPercent.setValue(percent)
    self.update_window_count(window_size, points)
    self.changing_overlap = False
    return None
except:
    self.changing_overlap = False

