# Source Generated with Decompyle++
# File: tmphy2171wx.marshal (Python 3.11)

start_index = max(0, numpy.searchsorted(x, start_time, side = 'right').item() - 1)
end_index = min(len(x), numpy.searchsorted(x, end_time, side = 'left').item() + 1)
data = y[start_index:end_index]
mean = numpy.mean(data, axis = 0).item()
std_dev = numpy.std(data, axis = 0).item()
return (mean, std_dev)
