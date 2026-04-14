# Source Generated with Decompyle++
# File: streamutil.pyc (Python 3.11)

import time
from typing import cast, Optional, Sequence, TypedDict, Union
import numpy
from numpy.typing import NDArray
import asphodel

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ChannelData(TypedDict):

    channel: asphodel.AsphodelChannelInfo

    channel_decoder: asphodel.AsphodelNativeChannelDecoder

class ExtraChannelData(ChannelData):

    unknown_ids: int

    lost_packets: int

    stream: asphodel.AsphodelStreamInfo

    stream_decoder: asphodel.AsphodelNativeStreamDecoder

class StreamData(TypedDict):

    lost_packets: int

    stream: asphodel.AsphodelStreamInfo

    stream_decoder: asphodel.AsphodelNativeStreamDecoder

class ExtraStreamData(StreamData):

    unknown_ids: int

class DeviceData(TypedDict):

    unknown_ids: int

def stream_fixed_duration(device, cached_device, stream_ids, duration):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device_data
    #    2 MAKE_CELL device_decoder
    #    4 MAKE_CELL error_code
    #    6 MAKE_CELL start_time
    #    8 RESUME
    #   10 LOAD_CONST 0.005
    #   12 STORE_FAST response_time
    #   14 LOAD_CONST 0.05
    #   16 STORE_FAST buffer_time
    #   18 LOAD_CONST 1000
    #   20 STORE_FAST timeout
    #   22 LOAD_CONST 0
    #   24 BUILD_MAP
    #   26 LOAD_CONST ('unknown_ids', 'streams')
    #   28 BUILD_CONST_KEY_MAP
    #   30 STORE_DEREF device_data
    #   32 LOAD_FAST cached_device
    #   34 POP_JUMP_FORWARD_IF_NOT_NONE to 40
    #   36 LOAD_FAST device
    #   38 STORE_FAST cached_device
    #   40 LOAD_FAST cached_device
    #   42 LOAD_METHOD get_stream_count
    #   64 PRECALL
    #   68 CALL
    #   78 UNPACK_SEQUENCE
    #   82 STORE_FAST stream_count
    #   84 STORE_FAST filler_bits
    #   86 STORE_FAST id_bits
    #   88 LOAD_FAST stream_ids
    #   90 POP_JUMP_FORWARD_IF_NOT_NONE to 148
    #   92 LOAD_GLOBAL NULL + list
    #  104 LOAD_GLOBAL NULL + range
    #  116 LOAD_FAST stream_count
    #  118 PRECALL
    #  122 CALL
    #  132 PRECALL
    #  136 CALL
    #  146 STORE_FAST stream_ids
    #  148 LOAD_CONST 0.0
    #  150 STORE_FAST max_warm_up
    #  152 BUILD_LIST
    #  154 STORE_FAST info_list
    #  156 BUILD_LIST
    #  158 STORE_FAST streams
    #  160 LOAD_FAST stream_ids
    #  162 GET_ITER
    #  164 FOR_ITER to 482
    #  166 STORE_FAST stream_id
    #  168 LOAD_FAST cached_device
    #  170 LOAD_METHOD get_stream
    #  192 LOAD_FAST stream_id
    #  194 PRECALL
    #  198 CALL
    #  208 STORE_FAST stream_struct
    #  210 LOAD_FAST streams
    #  212 LOAD_METHOD append
    #  234 LOAD_FAST stream_struct
    #  236 PRECALL
    #  240 CALL
    #  250 POP_TOP
    #  252 LOAD_GLOBAL NULL + max
    #  264 LOAD_FAST max_warm_up
    #  266 LOAD_FAST stream_struct
    #  268 LOAD_ATTR warm_up_delay
    #  278 PRECALL
    #  282 CALL
    #  292 STORE_FAST max_warm_up
    #  294 BUILD_LIST
    #  296 STORE_FAST channel_info_list
    #  298 LOAD_FAST stream_struct
    #  300 LOAD_ATTR channel_count
    #  310 STORE_FAST channels
    #  312 LOAD_FAST stream_struct
    #  314 LOAD_ATTR channel_index_list
    #  324 LOAD_CONST 0
    #  326 LOAD_FAST channels
    #  328 BUILD_SLICE
    #  330 BINARY_SUBSCR
    #  340 STORE_FAST indexes
    #  342 LOAD_FAST indexes
    # ... bytecode truncated ...
    pass

def filter_stream_data(device_data, stream_id):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + cast
    #   14 LOAD_GLOBAL dict
    #   26 LOAD_FAST device_data
    #   28 LOAD_CONST 'streams'
    #   30 BINARY_SUBSCR
    #   40 LOAD_FAST stream_id
    #   42 BINARY_SUBSCR
    #   52 LOAD_METHOD copy
    #   74 PRECALL
    #   78 CALL
    #   88 PRECALL
    #   92 CALL
    #  102 STORE_FAST stream_data
    #  104 LOAD_FAST stream_data
    #  106 LOAD_METHOD update
    #  128 LOAD_CONST <code object <dictcomp> at 0x105aabdd0, file "asphodel\streamutil.py", line 205>
    #  130 MAKE_FUNCTION
    #  132 LOAD_FAST device_data
    #  134 LOAD_METHOD items
    #  156 PRECALL
    #  160 CALL
    #  170 GET_ITER
    #  172 PRECALL
    #  176 CALL
    #  186 PRECALL
    #  190 CALL
    #  200 POP_TOP
    #  202 LOAD_GLOBAL NULL + cast
    #  214 LOAD_GLOBAL ExtraStreamData
    #  226 LOAD_FAST stream_data
    #  228 PRECALL
    #  232 CALL
    #  242 RETURN_VALUE
    pass

def filter_channel_data(device_data, stream_id, channel_id):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + filter_stream_data
    #   14 LOAD_FAST device_data
    #   16 LOAD_FAST stream_id
    #   18 PRECALL
    #   22 CALL
    #   32 STORE_FAST stream_data
    #   34 LOAD_GLOBAL NULL + cast
    #   46 LOAD_GLOBAL dict
    #   58 LOAD_FAST stream_data
    #   60 LOAD_CONST 'channels'
    #   62 BINARY_SUBSCR
    #   72 LOAD_FAST channel_id
    #   74 BINARY_SUBSCR
    #   84 LOAD_METHOD copy
    #  106 PRECALL
    #  110 CALL
    #  120 PRECALL
    #  124 CALL
    #  134 STORE_FAST channel_data
    #  136 LOAD_FAST channel_data
    #  138 LOAD_METHOD update
    #  160 LOAD_CONST <code object <dictcomp> at 0x105aabcc0, file "asphodel\streamutil.py", line 214>
    #  162 MAKE_FUNCTION
    #  164 LOAD_FAST stream_data
    #  166 LOAD_METHOD items
    #  188 PRECALL
    #  192 CALL
    #  202 GET_ITER
    #  204 PRECALL
    #  208 CALL
    #  218 PRECALL
    #  222 CALL
    #  232 POP_TOP
    #  234 LOAD_GLOBAL NULL + cast
    #  246 LOAD_GLOBAL ExtraChannelData
    #  258 LOAD_FAST channel_data
    #  260 PRECALL
    #  264 CALL
    #  274 RETURN_VALUE
    pass

def unpack_streaming_data(data):
    last_index = None
    indexes = []
    chunks = []

def get_average_measurement(device_data, stream_id, channel_id):
    stream_data = device_data['streams'][stream_id]
    channel_data = stream_data['channels'][channel_id]
    unpacked_data = unpack_streaming_data(channel_data['data'])
    values = unpacked_data[1]
    return numpy.nanmean(values, axis = 0)

class StreamingCache:

    def __init__(self, cached_device, stream, stream_id, channel, channel_id):
        self.cached_device = cached_device
        self.stream = stream
        self.stream_id = stream_id
        self.channel = channel
        self.channel_id = channel_id

    def __call__(self, device):
        device_data = self.caches.get(self.cached_device, None)
