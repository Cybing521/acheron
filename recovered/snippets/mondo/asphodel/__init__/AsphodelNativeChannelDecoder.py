# Source Generated with Decompyle++
# File: tmp4fmy5vvp.marshal (Python 3.11)


def __init__(self, lib, decoder, channel_info, stream_decoder = (None,)):
    self.lib = lib
    self._decoder = decoder
    self.channel_info = channel_info
    self.stream_decoder = stream_decoder
    self.auto_free = False if stream_decoder else True
    self.channel_bit_offset = self._decoder.channel_bit_offset
    self.samples = self._decoder.samples
    
    try:
        self.channel_name = self._decoder.channel_name.decode('UTF-8')
    except UnicodeDecodeError:
        self.channel_name = '<ERROR>'

    self.subchannels = self._decoder.subchannels
    self.subchannel_names = []
    for i in range(self.subchannels):
        s = self._decoder.subchannel_names[i].decode('UTF-8')
        self.subchannel_names.append(s)
        except UnicodeDecodeError:
            self.subchannel_names.append('<ERROR>')
            continue
        return None


def __del__(self):
    if self.auto_free:
        self.free()
        return None


def __reduce__(self):
    if self._decoder.callback:
        raise Exception('Cannot reduce channel decoder with callback')
    args = (self.channel_info, self._decoder.channel_bit_offset)
    return (recreate_channel_decoder, args)


def free(self):
    if self._decoder:
        self._decoder.free_decoder(self._decoder)
        self._decoder = None
        return None


def reset(self):
    self._decoder.reset(self._decoder)


def decode(self, counter, buffer):
    b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
    self._decoder.decode(self._decoder, counter, cast(b, POINTER(c_uint8)))


def set_conversion_factor(self, scale, offset):
    self._decoder.set_conversion_factor(self._decoder, scale, offset)


def set_callback(self, cb):
    pass
# WARNING: Decompyle incomplete

