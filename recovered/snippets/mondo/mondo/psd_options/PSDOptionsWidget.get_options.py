# Source Generated with Decompyle++
# File: tmpoxsmly_a.marshal (Python 3.11)

index = self.fftPoints.currentIndex()
window_size = self.fft_points_by_index[index]
index = self.windowFunction.currentIndex()
window_function = self.window_functions[index][1]
window = window_function(numpy.ones(window_size, dtype = numpy.double))
index = self.detrendMethod.currentIndex()
detrend = self.detrend_options[index][1]
return {
    'Fs': self.sampling_rate,
    'NFFT': window_size,
    'noverlap': self.overlapPoints.value(),
    'window': window,
    'detrend': detrend }
