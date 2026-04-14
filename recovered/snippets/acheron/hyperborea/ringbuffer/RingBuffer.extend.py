# Source Generated with Decompyle++
# File: tmpjs10b_l_.marshal (Python 3.11)

self.lock
if len(array) >= self.maxlen:
    self.data = array[-(self.maxlen):]
    self.index = 0
    self.length = self.maxlen
    self.pending.clear()
    self.__class__ = RingBufferFull
elif len(array) + self.index >= self.maxlen:
    end_length = self.maxlen - self.index
    start_length = len(array) - end_length
    self.data[self.index:] = array[0:end_length]
    self.data[0:start_length] = array[end_length:]
    self.index = start_length
    self.length = self.maxlen
    self.pending.clear()
    self.__class__ = RingBufferFull
else:
    self.data[self.index:self.index + len(array)] = array
    self.length = self, self.length += len(array), .length
None(None, None)
return None
with None:
    if not None:
        pass
