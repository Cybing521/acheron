# Source Generated with Decompyle++
# File: tmp74po_9hu.marshal (Python 3.11)

pad_size = downsample_factor - array.size % downsample_factor
if pad_size == downsample_factor:
    pad_size = 0
padded_array = numpy.append(array, numpy.zeros(pad_size) * numpy.nan)
reshaped = padded_array.reshape((-1, downsample_factor))
result = numpy.nanmean(reshaped, axis = 1)
return result
