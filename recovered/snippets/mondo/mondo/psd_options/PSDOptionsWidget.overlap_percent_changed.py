# Source Generated with Decompyle++
# File: tmpq7in2pyo.marshal (Python 3.11)

if self.changing_overlap:
    return None

try:
    self.changing_overlap = True
    index = self.fftPoints.currentIndex()
    window_size = self.fft_points_by_index[index]
    percent = self.overlapPercent.value()
    points = math.floor(window_size * percent / 100)
    if points >= window_size:
        points = window_size - 1
    self.overlapPoints.setValue(points)
    self.update_window_count(window_size, points)
    self.changing_overlap = False
    return None
except:
    self.changing_overlap = False

