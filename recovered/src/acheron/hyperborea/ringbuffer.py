# Source Generated with Decompyle++
# File: ringbuffer.pyc (Python 3.11)

import collections
import threading
import numpy
from numpy.typing import NDArray

class RingBuffer:
    
    def __init__(self = None, maxlen = None, element_size = None):
        self.maxlen = maxlen
        self.element_size = element_size
        self.lock = threading.Lock()
        self.length = 0
        self.index = 0
        shape = (maxlen, element_size)
        self.data = numpy.empty(shape, dtype = numpy.float64)
        self.pending = collections.deque(maxlen = maxlen)

    
    def _handle_pending(self = None):
        pass

    
    def __len__(self = None):
        self.lock
        None(None, None)
        return 
        with None:
            if not None, self.length:
                pass

    
    def clear(self = None):
        self.lock
        self.length = 0
        self.index = 0
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get_contents(self = None):
        self.lock
        None(None, None)
        return 
        with None:
            if not None, self.data[0:self.length]:
                pass

    
    def append(self = None, value = None):
        self.lock
        self.data[self.index] = value
        if self.length == self.maxlen:
            0 = self, self.length += 1, .length
            self.__class__ = RingBufferFull
        None(None, None)
        return None
        with None:
            if not self, self.index += 1, .index:
                pass

    
    def extend(self = None, array = None):
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



class RingBufferFull(RingBuffer):
    
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


