# Source Generated with Decompyle++
# File: tmpm7vmnyjk.marshal (Python 3.11)

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
