# Source Generated with Decompyle++
# File: tmpxmbfg3v5.marshal (Python 3.11)


def _handle_pending(self = None):
    if self.pending:
        array = numpy.concatenate(self.pending)
        self.pending.clear()
        if len(array) + self.index > self.maxlen:
            if len(array) >= self.maxlen:
                self.data = array[-(self.maxlen):]
                self.index = 0
                return None
            end_length = None.maxlen - self.index
            start_length = len(array) - end_length
            self.data[self.index:] = array[0:end_length]
            self.data[0:start_length] = array[end_length:]
            self.index = start_length
            return None
        self.data[self.index:self.index + len(array)] = None
        return None


def clear(self = None):
    self.lock
    self.pending.clear()
    self.length = 0
    self.index = 0
    self.__class__ = RingBuffer
    None(None, None)
    return None
    with None:
        if not None:
            pass


def get_contents(self = None):
    self.lock
    self._handle_pending()
    None(None, None)
    return 
    with None:
        if not None, numpy.roll(self.data, -(self.index), axis = 0):
            pass


def append(self = None, value = None):
    self.lock
    self.data[self.index] = value
    if self.index == self.maxlen:
        0 = self, self.index += 1, .index
    None(None, None)
    return None
    with None:
        if not None:
            pass


def extend(self = None, array = None):
    self.lock
    self.pending.append(array)
    None(None, None)
    return None
    with None:
        if not None:
            pass

