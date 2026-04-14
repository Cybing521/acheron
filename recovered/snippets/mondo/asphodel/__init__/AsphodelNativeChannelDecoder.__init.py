# Source Generated with Decompyle++
# File: tmpu15ster6.marshal (Python 3.11)

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
