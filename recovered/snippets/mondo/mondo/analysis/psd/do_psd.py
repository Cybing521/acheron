# Source Generated with Decompyle++
# File: tmpbyms4lul.marshal (Python 3.11)

freqs = numpy.fft.rfftfreq(NFFT, 1 / Fs)
windows = 0
sums = numpy.zeros(freqs.shape)
for _time, data, _start, _end in sequence:
    x = numpy.asarray(data[(:, subchannel_index)])
    if len(x) < NFFT:
        continue
    result = _stride_windows(x, NFFT, noverlap)
    result = mlab.detrend(result, detrend, axis = 0)
    result = numpy.asarray(result) * window.reshape((-1, 1))
    result = numpy.fft.rfft(result, n = NFFT, axis = 0)
    result = (numpy.conjugate(result) * result).real
    result /= (numpy.abs(window) ** 2).sum()
    windows += result.shape[1]
    result = result.sum(axis = 1)
    sums += result
    del result
    sums /= Fs = None
    sums /= windows
    return (sums, freqs)
