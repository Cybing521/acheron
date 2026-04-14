# Source Generated with Decompyle++
# File: tmp46rt3ght.marshal (Python 3.11)

import time
from typing import cast, Optional, Sequence, TypedDict, Union
import numpy
from numpy.typing import NDArray
import asphodel

class ChannelData(TypedDict):
    channel_decoder: asphodel.AsphodelNativeChannelDecoder = 'ChannelData'


class ExtraChannelData(ChannelData):
    last_packet_time: Optional[float] = 'ExtraChannelData'


class StreamData(TypedDict):
    start_time: Optional[float] = 'StreamData'


class ExtraStreamData(StreamData):
    unknown_ids: int = 'ExtraStreamData'


class DeviceData(TypedDict):
    streams: dict[(int, StreamData)] = 'DeviceData'


def stream_fixed_duration(device = None, cached_device = None, stream_ids = None, duration = (None, None, 2)):
    pass
# WARNING: Decompyle incomplete


def filter_stream_data(device_data = None, stream_id = None):
    stream_data = cast(dict, device_data['streams'][stream_id].copy())
    (lambda .0: pass# WARNING: Decompyle incomplete
)(device_data.items()())
    return cast(ExtraStreamData, stream_data)


def filter_channel_data(device_data = None, stream_id = None, channel_id = None):
    stream_data = filter_stream_data(device_data, stream_id)
    channel_data = cast(dict, stream_data['channels'][channel_id].copy())
    (lambda .0: pass# WARNING: Decompyle incomplete
)(stream_data.items()())
    return cast(ExtraChannelData, channel_data)


def unpack_streaming_data(data = None):
    last_index = None
    indexes = []
    chunks = []
# WARNING: Decompyle incomplete


def get_average_measurement(device_data = None, stream_id = None, channel_id = None):
    stream_data = device_data['streams'][stream_id]
    channel_data = stream_data['channels'][channel_id]
    unpacked_data = unpack_streaming_data(channel_data['data'])
    values = unpacked_data[1]
    return numpy.nanmean(values, axis = 0)


class StreamingCache:
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


