# Source Generated with Decompyle++
# File: tmp97_x_efk.marshal (Python 3.11)

start_index = max(0, numpy.searchsorted(freqs, start_freq, side = 'right').item() - 1)
end_index = min(len(freqs), numpy.searchsorted(freqs, end_freq, side = 'left').item() + 1)
dfreq = freqs[1] - freqs[0]
integrated = numpy.sum(pxx[start_index:end_index]) * dfreq
return integrated.item()
