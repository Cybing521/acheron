# Source Generated with Decompyle++
# File: tmp4mv9sxvb.marshal (Python 3.11)

caches: dict[(asphodel.AsphodelNativeDevice, DeviceData)] = { }

def __init__(self, cached_device = None, stream = None, stream_id = None, channel = (None, None, None, None), channel_id = ('cached_device', asphodel.AsphodelNativeDevice, 'stream', Optional[asphodel.AsphodelStreamInfo], 'stream_id', Optional[int], 'channel', Optional[asphodel.AsphodelChannelInfo], 'channel_id', Optional[int], 'return', None)):
    self.cached_device = cached_device
    self.stream = stream
    self.stream_id = stream_id
    self.channel = channel
    self.channel_id = channel_id


def __call__(self = None, device = None):
    device_data = self.caches.get(self.cached_device, None)
# WARNING: Decompyle incomplete

