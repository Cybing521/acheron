# Source Generated with Decompyle++
# File: tmp1b_sfopm.marshal (Python 3.11)

_fields_ = [
    ('channel_index_list', POINTER(c_uint8)),
    ('channel_count', c_uint8),
    ('filler_bits', c_uint8),
    ('counter_bits', c_uint8),
    ('rate', c_float),
    ('rate_error', c_float),
    ('warm_up_delay', c_float)]
__reduce__ = object.__reduce__

def __del__(self):
    
    try:
        self._free_func(self)
        return None
    except AttributeError:
        return None



def __repr__(self):
    channel_index_list = self.channel_index_list[:self.channel_count]
    items = [
        ('channel_index_list', channel_index_list),
        ('channel_count', self.channel_count),
        ('filler_bits', self.filler_bits),
        ('counter_bits', self.counter_bits),
        ('rate', self.rate),
        ('rate_error', self.rate_error),
        ('warm_up_delay', self.warm_up_delay)]
    contents = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
    return '<AsphodelStreamInfo {' + contents + '}>'


def __getstate__(self):
    return {
        '_channel_array': self.channel_index_list[:self.channel_count],
        'channel_count': self.channel_count,
        'filler_bits': self.filler_bits,
        'counter_bits': self.counter_bits,
        'rate': self.rate,
        'rate_error': self.rate_error,
        'warm_up_delay': self.warm_up_delay }


def __setstate__(self, state):
    pass
# WARNING: Decompyle incomplete


def to_json_obj(self):
    return self.__getstate__()

from_json_obj = (lambda cls, obj: instance = cls.__new__(cls)instance.__setstate__(obj)instance)()
