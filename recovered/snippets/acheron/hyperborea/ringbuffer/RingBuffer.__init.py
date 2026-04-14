# Source Generated with Decompyle++
# File: tmpd85hxr2k.marshal (Python 3.11)

self.maxlen = maxlen
self.element_size = element_size
self.lock = threading.Lock()
self.length = 0
self.index = 0
shape = (maxlen, element_size)
self.data = numpy.empty(shape, dtype = numpy.float64)
self.pending = collections.deque(maxlen = maxlen)
