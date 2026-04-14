# Source Generated with Decompyle++
# File: tmpn89gxrso.marshal (Python 3.11)

import time
import numpy
import asphodel
from asphodel import AsphodelNativeDevice, AsphodelStreamInfo, AsphodelChannelInfo, SupplyInfo
from asphodel.streamutil import stream_fixed_duration
from asphodel.streamutil import filter_channel_data
from asphodel.streamutil import unpack_streaming_data

def supply_test(device = None, supply_id = None, name = None, info = ('device', AsphodelNativeDevice, 'supply_id', int, 'name', str, 'info', SupplyInfo, 'return', tuple[(bool, str)])):
    
    try:
        (value, result_flags) = device.check_supply(supply_id)
    except Exception:
        return 

    info.nominal * info.scale + info.offset = value * info.scale + info.offset
    if scaled_nominal != 0:
        percent = (scaled_value / scaled_nominal) * 100
    else:
        percent = 0
    formatted = asphodel.format_value_ascii(info.unit_type, info.scale, scaled_value)
    success = True if result_flags == 0 else False
    passfail = 'pass' if success else 'FAIL'
    message = '{}: {} ({:.0f}%), result=0x{:02x}, {}'.format(name, formatted, percent, result_flags, passfail)
    return (success, message)


def bridge_test(device, stream_id = None, stream = None, channel_id = None, channel = ('device', AsphodelNativeDevice, 'stream_id', int, 'stream', AsphodelStreamInfo, 'channel_id', int, 'channel', AsphodelChannelInfo, 'return', tuple[(bool, str)])):
    pass
# WARNING: Decompyle incomplete


def accel_test(device, stream_id = None, stream = None, channel_id = None, channel = ('device', AsphodelNativeDevice, 'stream_id', int, 'stream', AsphodelStreamInfo, 'channel_id', int, 'channel', AsphodelChannelInfo, 'return', tuple[(bool, str)])):
    pass
# WARNING: Decompyle incomplete

