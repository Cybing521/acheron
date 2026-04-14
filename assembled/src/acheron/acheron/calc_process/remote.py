# Source Generated with Decompyle++
# File: remote.pyc (Python 3.11)

from collections import deque
import datetime
import logging
from logging.handlers import QueueHandler
import math
import multiprocessing
from multiprocessing.connection import Connection, wait
import os
import signal
import sys
import threading
import time
from typing import Any, Callable, Optional
import numpy
from numpy.typing import NDArray
import psutil
from asphodel import AsphodelChannelInfo, AsphodelNativeChannelDecoder, AsphodelNativeDeviceDecoder, AsphodelStreamInfo, StreamRateInfo
import asphodel
from asphodel.device_info import DeviceInfo
from hyperborea.ringbuffer import RingBuffer
from ..device_logging import DeviceLoggerAdapter
from .types import CalcControl, CalcData, CalcSettings, ChannelInformation, LimitType, Trigger
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class CalcDataProcessor:

    def __init__(self, decoder, channel_info, data_pipe, logger, is_shown, channel_interval, plot_interval, fft_interval, triggers):
        self.device_decoder = decoder
        self.channel_info = channel_info
        self.data_pipe = data_pipe
        self.logger = logger
        self.is_shown = is_shown
        self.channel_interval = channel_interval
        self.plot_interval = plot_interval
        self.fft_interval = fft_interval
        self.current_channel_id = None
        self.current_subchannel_index = None
        self.mean_ringbuffers = { }
        self.plot_ringbuffers = { }
        self.fft_ringbuffers = { }
        self.connectivity_pipe = None
        self.connectivity_deques = { }
        self.data_lock = threading.Lock()
        self.trigger_lock = threading.Lock()
        self.triggers_by_channel = { }
        self.active_triggers = set()
        self.change_triggers(triggers)
        self.lost_packet_lock = threading.Lock()
        self.lost_packet_count = 0
        self.lost_packet_last_time = None
        self.recent_lost_packet_count = 0
        self.lost_packet_deque = deque()
        self.last_lost_packet_update = None
        self.stopped = threading.Event()
        self.setup_decoder()
        self.update_thread = threading.Thread(target = self.update_thread_run)
        self.update_thread.start()

    def stop_and_join(self):
        self.stopped.set()
        self.update_thread.join()

    def set_connectivity_pipe(self, pipe):
        self.connectivity_pipe = pipe

    def process_connectivity(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR connectivity_pipe
        #   14 POP_JUMP_FORWARD_IF_NONE to 314
        #   16 BUILD_LIST
        #   18 STORE_FAST messages
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR connectivity_deques
        #   32 LOAD_METHOD items
        #   54 PRECALL
        #   58 CALL
        #   68 GET_ITER
        #   70 FOR_ITER to 258
        #   72 UNPACK_SEQUENCE
        #   76 STORE_FAST channel_id
        #   78 STORE_FAST d
        #   80 BUILD_LIST
        #   82 STORE_FAST values
        #   84 LOAD_FAST d
        #   86 POP_JUMP_FORWARD_IF_FALSE to 170
        #   88 LOAD_FAST values
        #   90 LOAD_METHOD append
        #  112 LOAD_FAST d
        #  114 LOAD_METHOD popleft
        #  136 PRECALL
        #  140 CALL
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 LOAD_FAST d
        #  168 POP_JUMP_BACKWARD_IF_TRUE to 88
        #  170 LOAD_FAST values
        #  172 POP_JUMP_FORWARD_IF_FALSE to 256
        #  174 LOAD_FAST messages
        #  176 LOAD_METHOD append
        #  198 LOAD_FAST channel_id
        #  200 LOAD_GLOBAL NULL + numpy
        #  212 LOAD_ATTR concatenate
        #  222 LOAD_FAST values
        #  224 PRECALL
        #  228 CALL
        #  238 BUILD_TUPLE
        #  240 PRECALL
        #  244 CALL
        #  254 POP_TOP
        #  256 JUMP_BACKWARD to 70
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR connectivity_pipe
        #  270 LOAD_METHOD send
        #  292 LOAD_FAST messages
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 LOAD_CONST None
        #  312 RETURN_VALUE
        #  314 LOAD_CONST None
        #  316 RETURN_VALUE
        pass

    def setup_decoder(self):
        self.device_decoder.set_unknown_id_callback(self.unknown_id_cb)
        channel_decoders = { }
        for i, stream_decoder in enumerate(self.device_decoder.decoders):
            stream_id = self.device_decoder.stream_ids[i]
            lost_packet_cb = self.create_lost_packet_callback(stream_id)
            stream_decoder.set_lost_packet_callback(lost_packet_cb)
            for j, channel_decoder in enumerate(stream_decoder.decoders):
                channel_id = stream_decoder.stream_info.channel_index_list[j]
                channel_decoders[channel_id] = channel_decoder
                for channel_id in sorted(channel_decoders.keys()):
                    channel_decoder = channel_decoders[channel_id]
                    self.setup_channel(channel_id, channel_decoder)
                    return None

    def setup_channel(self, channel_id, channel_decoder):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL channel_id
        #    4 MAKE_CELL downsample
        #    6 MAKE_CELL fft_rb
        #    8 MAKE_CELL mean_rb
        #   10 MAKE_CELL plot_rb
        #   12 RESUME
        #   14 LOAD_DEREF self
        #   16 LOAD_ATTR channel_info
        #   26 LOAD_DEREF channel_id
        #   28 BINARY_SUBSCR
        #   38 STORE_FAST channel_info
        #   40 LOAD_GLOBAL NULL + RingBuffer
        #   52 LOAD_FAST channel_info
        #   54 LOAD_ATTR mean_len
        #   64 LOAD_FAST channel_decoder
        #   66 LOAD_ATTR subchannels
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_DEREF mean_rb
        #   92 LOAD_DEREF mean_rb
        #   94 LOAD_DEREF self
        #   96 LOAD_ATTR mean_ringbuffers
        #  106 LOAD_DEREF channel_id
        #  108 STORE_SUBSCR
        #  112 LOAD_GLOBAL NULL + RingBuffer
        #  124 LOAD_FAST channel_info
        #  126 LOAD_ATTR plot_len
        #  136 LOAD_FAST channel_decoder
        #  138 LOAD_ATTR subchannels
        #  148 PRECALL
        #  152 CALL
        #  162 STORE_DEREF plot_rb
        #  164 LOAD_DEREF plot_rb
        #  166 LOAD_DEREF self
        #  168 LOAD_ATTR plot_ringbuffers
        #  178 LOAD_DEREF channel_id
        #  180 STORE_SUBSCR
        #  184 LOAD_GLOBAL NULL + RingBuffer
        #  196 LOAD_FAST channel_info
        #  198 LOAD_ATTR fft_sample_len
        #  208 LOAD_FAST channel_decoder
        #  210 LOAD_ATTR subchannels
        #  220 PRECALL
        #  224 CALL
        #  234 STORE_DEREF fft_rb
        #  236 LOAD_DEREF fft_rb
        #  238 LOAD_DEREF self
        #  240 LOAD_ATTR fft_ringbuffers
        #  250 LOAD_DEREF channel_id
        #  252 STORE_SUBSCR
        #  256 LOAD_FAST channel_info
        #  258 LOAD_ATTR downsample_factor
        #  268 LOAD_CONST 1
        #  270 COMPARE_OP !=
        #  276 STORE_DEREF downsample
        #  278 LOAD_CONST '_counter'
        #  280 LOAD_GLOBAL int
        #  292 LOAD_CONST 'data'
        #  294 LOAD_GLOBAL list
        #  306 LOAD_GLOBAL float
        #  318 BINARY_SUBSCR
        #  328 LOAD_CONST 'samples'
        #  330 LOAD_GLOBAL int
        #  342 LOAD_CONST 'subchannels'
        #  344 LOAD_GLOBAL int
        #  356 LOAD_CONST 'return'
        #  358 LOAD_CONST None
        #  360 BUILD_TUPLE
        #  362 LOAD_CLOSURE channel_id
        #  364 LOAD_CLOSURE downsample
        #  366 LOAD_CLOSURE fft_rb
        #  368 LOAD_CLOSURE mean_rb
        #  370 LOAD_CLOSURE plot_rb
        #  372 LOAD_CLOSURE self
        #  374 BUILD_TUPLE
        #  376 LOAD_CONST <code object callback at 0xacd202a00, file "acheron\calc_process\remote.py", line 142>
        #  378 MAKE_FUNCTION annotations, closure
        #  380 STORE_FAST callback
        #  382 LOAD_FAST channel_decoder
        # ... bytecode truncated ...
        pass

    def create_lost_packet_callback(self, stream_id):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL stream_id
        #    4 RESUME
        #    6 LOAD_CONST 'current'
        #    8 LOAD_GLOBAL int
        #   20 LOAD_CONST 'last'
        #   22 LOAD_GLOBAL int
        #   34 LOAD_CONST 'return'
        #   36 LOAD_CONST None
        #   38 BUILD_TUPLE
        #   40 LOAD_CLOSURE self
        #   42 LOAD_CLOSURE stream_id
        #   44 BUILD_TUPLE
        #   46 LOAD_CONST <code object lost_packet_callback at 0xacd220000, file "acheron\calc_process\remote.py", line 165>
        #   48 MAKE_FUNCTION annotations, closure
        #   50 STORE_FAST lost_packet_callback
        #   52 LOAD_FAST lost_packet_callback
        #   54 RETURN_VALUE
        pass

    def update_lost_packets(self):
        lost_count_too_old = 0
        now = datetime.datetime.now(datetime.timezone.utc)
        twenty_secs_ago = now - datetime.timedelta(seconds = 20)
        if len(self.lost_packet_deque):
            (lost_dt, lost) = self.lost_packet_deque[0]
            if lost_dt < twenty_secs_ago:
                lost_count_too_old += lost
                self.lost_packet_deque.popleft()

    def get_stream_rate(self, rate_info):
        if rate_info.available:
            rate_channel_id = rate_info.channel_index
            ringbuffer = self.fft_ringbuffers[rate_channel_id]
            if len(ringbuffer) != 0:
                rate_data = ringbuffer.get_contents()
                raw_rate = numpy.average(rate_data)
                if not math.isfinite(raw_rate):
                    return None
                stream_rate = None * rate_info.scale + rate_info.offset
                if rate_info.invert:
                    if stream_rate != 0:
                        stream_rate = 1 / stream_rate
                    else:
                        stream_rate = 0
                return stream_rate
            return None

    def change_triggers(self, triggers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 BUILD_MAP
        #    4 STORE_FAST triggers_by_channel
        #    6 LOAD_FAST triggers
        #    8 GET_ITER
        #   10 FOR_ITER to 164
        #   12 STORE_FAST trigger
        #   14 LOAD_FAST triggers_by_channel
        #   16 LOAD_METHOD get
        #   38 LOAD_FAST trigger
        #   40 LOAD_ATTR channel_id
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST channel_triggers
        #   66 LOAD_FAST channel_triggers
        #   68 POP_JUMP_FORWARD_IF_FALSE to 114
        #   70 LOAD_FAST channel_triggers
        #   72 LOAD_METHOD add
        #   94 LOAD_FAST trigger
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 JUMP_BACKWARD to 10
        #  114 LOAD_GLOBAL NULL + set
        #  126 LOAD_FAST trigger
        #  128 BUILD_TUPLE
        #  130 PRECALL
        #  134 CALL
        #  144 LOAD_FAST triggers_by_channel
        #  146 LOAD_FAST trigger
        #  148 LOAD_ATTR channel_id
        #  158 STORE_SUBSCR
        #  162 JUMP_BACKWARD to 10
        #  164 LOAD_GLOBAL NULL + set
        #  176 LOAD_CONST <code object <genexpr> at 0x105af8810, file "acheron\calc_process\remote.py", line 253>
        #  178 MAKE_FUNCTION
        #  180 LOAD_FAST triggers
        #  182 GET_ITER
        #  184 PRECALL
        #  188 CALL
        #  198 PRECALL
        #  202 CALL
        #  212 STORE_FAST available_ids
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR trigger_lock
        #  226 BEFORE_WITH
        #  228 POP_TOP
        #  230 LOAD_FAST triggers_by_channel
        #  232 LOAD_FAST self
        #  234 STORE_ATTR triggers_by_channel
        #  244 LOAD_GLOBAL NULL + len
        #  256 LOAD_FAST self
        #  258 LOAD_ATTR active_triggers
        #  268 PRECALL
        #  272 CALL
        #  282 STORE_FAST active_count
        #  284 LOAD_FAST self
        #  286 LOAD_ATTR active_triggers
        #  296 LOAD_METHOD intersection_update
        #  318 LOAD_FAST available_ids
        #  320 PRECALL
        #  324 CALL
        #  334 POP_TOP
        #  336 LOAD_GLOBAL NULL + len
        #  348 LOAD_FAST self
        #  350 LOAD_ATTR active_triggers
        #  360 PRECALL
        #  364 CALL
        #  374 LOAD_FAST active_count
        #  376 COMPARE_OP !=
        #  382 POP_JUMP_FORWARD_IF_FALSE to 532
        #  384 LOAD_FAST self
        #  386 LOAD_ATTR data_lock
        #  396 BEFORE_WITH
        #  398 POP_TOP
        #  400 LOAD_FAST self
        #  402 LOAD_ATTR data_pipe
        #  412 LOAD_METHOD send
        #  434 LOAD_GLOBAL CalcData
        #  446 LOAD_ATTR ACTIVE_TRIGGERS_CHANGED
        # ... bytecode truncated ...
        pass

    def check_triggers(self, triggers, mean, std):
        for trigger in triggers:
            was_active = trigger.id in self.active_triggers
            if trigger.subchannel_index >= len(mean):
                continue
            if trigger.limit_type == LimitType.MEAN_HIGH_LIMIT:
                value = mean[trigger.subchannel_index]
                if was_active:
                    active = value >= trigger.deactivate_limit
                else:
                    active = value > trigger.activate_limit
            elif trigger.limit_type == LimitType.MEAN_LOW_LIMIT:
                value = mean[trigger.subchannel_index]
                if was_active:
                    active = value <= trigger.deactivate_limit
                else:
                    active = value < trigger.activate_limit
            elif trigger.limit_type == LimitType.STD_HIGH_LIMIT:
                value = std[trigger.subchannel_index]
                if was_active:
                    active = value >= trigger.deactivate_limit
                else:
                    active = value > trigger.activate_limit
            else:
                value = std[trigger.subchannel_index]
                if was_active:
                    active = value <= trigger.deactivate_limit
                else:
                    active = value < trigger.activate_limit
            if not active and was_active:
                self.active_triggers.add(trigger.id)
                self.triggers_changed = True
                continue
            if active and was_active:
                self.active_triggers.remove(trigger.id)
                self.triggers_changed = True
            return None

    def update_channels(self):
        self.trigger_lock
        self.triggers_changed = False

    def update_plots(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR is_shown
        #   14 POP_JUMP_FORWARD_IF_TRUE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR current_channel_id
        #   32 STORE_FAST channel_id
        #   34 LOAD_FAST channel_id
        #   36 POP_JUMP_FORWARD_IF_NOT_NONE to 42
        #   38 LOAD_CONST None
        #   40 RETURN_VALUE
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR channel_info
        #   54 LOAD_FAST channel_id
        #   56 BINARY_SUBSCR
        #   66 STORE_FAST channel_info
        #   68 LOAD_FAST self
        #   70 LOAD_METHOD get_stream_rate
        #   92 LOAD_FAST channel_info
        #   94 LOAD_ATTR rate_info
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST stream_rate
        #  120 LOAD_FAST stream_rate
        #  122 POP_JUMP_FORWARD_IF_TRUE to 140
        #  124 LOAD_FAST channel_info
        #  126 LOAD_ATTR rate
        #  136 STORE_FAST channel_rate
        #  138 JUMP_FORWARD to 160
        #  140 LOAD_FAST stream_rate
        #  142 LOAD_FAST channel_info
        #  144 LOAD_ATTR samples
        #  154 BINARY_OP *
        #  158 STORE_FAST channel_rate
        #  160 LOAD_FAST channel_rate
        #  162 LOAD_FAST channel_info
        #  164 LOAD_ATTR downsample_factor
        #  174 BINARY_OP /
        #  178 STORE_FAST plot_rate
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR plot_ringbuffers
        #  192 LOAD_FAST channel_id
        #  194 BINARY_SUBSCR
        #  204 LOAD_METHOD get_contents
        #  226 PRECALL
        #  230 CALL
        #  240 STORE_FAST plot_array
        #  242 LOAD_GLOBAL NULL + len
        #  254 LOAD_FAST plot_array
        #  256 PRECALL
        #  260 CALL
        #  270 LOAD_CONST 0
        #  272 COMPARE_OP >
        #  278 POP_JUMP_FORWARD_IF_FALSE to 520
        #  280 LOAD_GLOBAL NULL + len
        #  292 LOAD_FAST plot_array
        #  294 PRECALL
        #  298 CALL
        #  308 STORE_FAST length
        #  310 LOAD_FAST length
        #  312 LOAD_CONST 1
        #  314 BINARY_OP -
        #  318 UNARY_NEGATIVE
        #  320 LOAD_FAST plot_rate
        #  322 BINARY_OP /
        #  326 STORE_FAST start
        #  328 LOAD_GLOBAL NULL + numpy
        #  340 LOAD_ATTR linspace
        #  350 LOAD_FAST start
        #  352 LOAD_CONST 0
        #  354 LOAD_FAST length
        #  356 PRECALL
        #  360 CALL
        #  370 STORE_FAST time_axis
        #  372 LOAD_FAST self
        #  374 LOAD_ATTR data_lock
        #  384 BEFORE_WITH
        #  386 POP_TOP
        # ... bytecode truncated ...
        pass

    def update_ffts(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR is_shown
        #   14 POP_JUMP_FORWARD_IF_TRUE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR current_channel_id
        #   32 STORE_FAST channel_id
        #   34 LOAD_FAST channel_id
        #   36 POP_JUMP_FORWARD_IF_NOT_NONE to 42
        #   38 LOAD_CONST None
        #   40 RETURN_VALUE
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR current_subchannel_index
        #   54 STORE_FAST subchannel_index
        #   56 LOAD_FAST subchannel_index
        #   58 POP_JUMP_FORWARD_IF_NOT_NONE to 64
        #   60 LOAD_CONST None
        #   62 RETURN_VALUE
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR channel_info
        #   76 LOAD_FAST channel_id
        #   78 BINARY_SUBSCR
        #   88 STORE_FAST channel_info
        #   90 LOAD_FAST self
        #   92 LOAD_METHOD get_stream_rate
        #  114 LOAD_FAST channel_info
        #  116 LOAD_ATTR rate_info
        #  126 PRECALL
        #  130 CALL
        #  140 STORE_FAST stream_rate
        #  142 LOAD_FAST stream_rate
        #  144 POP_JUMP_FORWARD_IF_TRUE to 162
        #  146 LOAD_FAST channel_info
        #  148 LOAD_ATTR fft_freq_axis
        #  158 STORE_FAST fft_freq_axis
        #  160 JUMP_FORWARD to 262
        #  162 LOAD_FAST stream_rate
        #  164 LOAD_FAST channel_info
        #  166 LOAD_ATTR samples
        #  176 BINARY_OP *
        #  180 STORE_FAST channel_rate
        #  182 LOAD_GLOBAL numpy
        #  194 LOAD_ATTR fft
        #  204 LOAD_METHOD rfftfreq
        #  226 LOAD_FAST channel_info
        #  228 LOAD_ATTR fft_size
        #  238 LOAD_CONST 1
        #  240 LOAD_FAST channel_rate
        #  242 BINARY_OP /
        #  246 PRECALL
        #  250 CALL
        #  260 STORE_FAST fft_freq_axis
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR fft_ringbuffers
        #  274 LOAD_FAST channel_id
        #  276 BINARY_SUBSCR
        #  286 STORE_FAST ringbuffer
        #  288 LOAD_FAST ringbuffer
        #  290 LOAD_METHOD get_contents
        #  312 PRECALL
        #  316 CALL
        #  326 STORE_FAST fft_array
        #  328 LOAD_FAST ringbuffer
        #  330 LOAD_ATTR maxlen
        #  340 LOAD_GLOBAL NULL + len
        #  352 LOAD_FAST fft_array
        #  354 PRECALL
        #  358 CALL
        #  368 COMPARE_OP !=
        #  374 POP_JUMP_FORWARD_IF_FALSE to 572
        #  376 LOAD_GLOBAL NULL + len
        #  388 LOAD_FAST fft_array
        #  390 PRECALL
        #  394 CALL
        #  404 LOAD_FAST ringbuffer
        #  406 LOAD_ATTR maxlen
        #  416 BINARY_OP /
        #  420 STORE_FAST buffering_progress
        # ... bytecode truncated ...
        pass

    def set_is_shown(self, is_shown):
        self.is_shown = is_shown
        if is_shown:
            self.update_plots()
            self.update_ffts()
            return None

    def plot_change(self, channel_id, subchannel_index):
        if channel_id == -1:
            channel_id = None
        if subchannel_index == -1:
            subchannel_index = None
        self.current_channel_id = channel_id
        self.current_subchannel_index = subchannel_index

    def reset_lost_packets(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lost_packet_deque
        #   14 LOAD_METHOD clear
        #   36 PRECALL
        #   40 CALL
        #   50 POP_TOP
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR lost_packet_lock
        #   64 BEFORE_WITH
        #   66 POP_TOP
        #   68 LOAD_CONST 0
        #   70 LOAD_FAST self
        #   72 STORE_ATTR recent_lost_packet_count
        #   82 LOAD_CONST None
        #   84 LOAD_CONST None
        #   86 LOAD_CONST None
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        #  108 PUSH_EXC_INFO
        #  110 WITH_EXCEPT_START
        #  112 POP_JUMP_FORWARD_IF_TRUE to 122
        #  114 RERAISE
        #  116 COPY
        #  118 POP_EXCEPT
        #  120 RERAISE
        #  122 POP_TOP
        #  124 POP_EXCEPT
        #  126 POP_TOP
        #  128 POP_TOP
        #  130 LOAD_CONST None
        #  132 RETURN_VALUE
        pass

    def unknown_id_cb(self, unknown_id):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR data_lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR data_pipe
        #   30 LOAD_METHOD send
        #   52 LOAD_GLOBAL CalcData
        #   64 LOAD_ATTR UNKNOWN_ID
        #   74 LOAD_FAST unknown_id
        #   76 BUILD_TUPLE
        #   78 PRECALL
        #   82 CALL
        #   92 POP_TOP
        #   94 LOAD_CONST None
        #   96 LOAD_CONST None
        #   98 LOAD_CONST None
        #  100 PRECALL
        #  104 CALL
        #  114 POP_TOP
        #  116 LOAD_CONST None
        #  118 RETURN_VALUE
        #  120 PUSH_EXC_INFO
        #  122 WITH_EXCEPT_START
        #  124 POP_JUMP_FORWARD_IF_TRUE to 134
        #  126 RERAISE
        #  128 COPY
        #  130 POP_EXCEPT
        #  132 RERAISE
        #  134 POP_TOP
        #  136 POP_EXCEPT
        #  138 POP_TOP
        #  140 POP_TOP
        #  142 LOAD_CONST None
        #  144 RETURN_VALUE
        pass

    def update_thread_run(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 BUILD_LIST
        #    4 STORE_FAST update_funcs
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR fft_interval
        #   18 POP_JUMP_FORWARD_IF_FALSE to 86
        #   20 LOAD_FAST update_funcs
        #   22 LOAD_METHOD append
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR update_ffts
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR fft_interval
        #   68 BUILD_TUPLE
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR plot_interval
        #   98 POP_JUMP_FORWARD_IF_FALSE to 166
        #  100 LOAD_FAST update_funcs
        #  102 LOAD_METHOD append
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR update_plots
        #  136 LOAD_FAST self
        #  138 LOAD_ATTR plot_interval
        #  148 BUILD_TUPLE
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 LOAD_FAST self
        #  168 LOAD_ATTR channel_interval
        #  178 POP_JUMP_FORWARD_IF_FALSE to 312
        #  180 LOAD_FAST update_funcs
        #  182 LOAD_METHOD append
        #  204 LOAD_FAST self
        #  206 LOAD_ATTR update_channels
        #  216 LOAD_FAST self
        #  218 LOAD_ATTR channel_interval
        #  228 BUILD_TUPLE
        #  230 PRECALL
        #  234 CALL
        #  244 POP_TOP
        #  246 LOAD_FAST update_funcs
        #  248 LOAD_METHOD append
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR update_lost_packets
        #  282 LOAD_FAST self
        #  284 LOAD_ATTR channel_interval
        #  294 BUILD_TUPLE
        #  296 PRECALL
        #  300 CALL
        #  310 POP_TOP
        #  312 LOAD_FAST update_funcs
        #  314 POP_JUMP_FORWARD_IF_TRUE to 320
        #  316 LOAD_CONST None
        #  318 RETURN_VALUE
        #  320 LOAD_GLOBAL NULL + time
        #  332 LOAD_ATTR monotonic
        #  342 PRECALL
        #  346 CALL
        #  356 BUILD_LIST
        #  358 LOAD_GLOBAL NULL + len
        #  370 LOAD_FAST update_funcs
        #  372 PRECALL
        #  376 CALL
        #  386 BINARY_OP *
        #  390 STORE_FAST next_run
        #  392 NOP
        #  394 NOP
        #  396 LOAD_GLOBAL NULL + time
        #  408 LOAD_ATTR monotonic
        #  418 PRECALL
        #  422 CALL
        #  432 STORE_FAST now
        #  434 LOAD_GLOBAL NULL + enumerate
        #  446 LOAD_FAST update_funcs
        #  448 PRECALL
        #  452 CALL
        #  462 GET_ITER
        #  464 FOR_ITER to 598
        # ... bytecode truncated ...
        pass

class CalcRunner:

    def __init__(self, packet_pipe, data_pipe, ctrl_pipe, serial_number, is_shown, settings, triggers):
        self.packet_pipe = packet_pipe
        self.data_pipe = data_pipe
        self.ctrl_pipe = ctrl_pipe
        self.serial_number = serial_number
        self.is_shown = is_shown
        self.settings = settings
        self.triggers = triggers
        self.logger = DeviceLoggerAdapter(logger, self.serial_number)
        self.decoder = None
        self.data_processor = None
        self
        self

    def create_decoder(self, device_info, active_streams):
        channel_info = { }
        streams = device_info.streams
        channels = device_info.channels
        info_list = []
        for i, stream in enumerate(streams):
            if i not in active_streams:
                continue
            channel_info_list = []
            ids = stream.channel_index_list[0:stream.channel_count]
            for channel_id in ids:
                channel_info_list.append(channels[channel_id])
                info_list.append((i, stream, channel_info_list))
                device_decoder = asphodel.nativelib.create_device_decoder(info_list, device_info.stream_filler_bits, device_info.stream_id_bits)
                for i, stream_decoder in enumerate(device_decoder.decoders):
                    stream_id = device_decoder.stream_ids[i]
                    for j, channel_decoder in enumerate(stream_decoder.decoders):
                        channel_id = stream_decoder.stream_info.channel_index_list[j]
                        channel = channels[channel_id]
                        channel_info[channel_id] = self.create_channel_info(device_info, stream_id, streams[stream_id], channel_id, channel, channel_decoder)
                        return (device_decoder, channel_info)

    def create_channel_info(self, device_info, stream_id, stream, channel_id, channel, channel_decoder):
        rate_info = device_info.stream_rate_info[stream_id]
        samples = channel.samples
        channel_rate = samples * stream.rate
        sample_len = math.ceil(10 * channel_rate)
        sample_len = 2 ** math.ceil(math.log2(sample_len))
        if self.settings.downsample and sample_len > 32768:
            downsample_factor = samples
        else:
            downsample_factor = 1
        fft_sample_len = min(sample_len, 32768)
        return ChannelInformation(name = channel_decoder.channel_name, channel_id = channel_id, stream_id = stream_id, channel = channel, subchannel_names = channel_decoder.subchannel_names, rate_info = rate_info, samples = samples, rate = channel_rate, downsample_factor = downsample_factor, mean_len = math.ceil(1 * channel_rate), plot_len = sample_len // downsample_factor, fft_shortened = fft_sample_len != sample_len, fft_sample_len = fft_sample_len, fft_freq_axis = numpy.fft.rfftfreq(fft_sample_len, 1 / channel_rate), fft_size = fft_sample_len)

    def stop_processing(self):
        self.decoder = None
        if self.data_processor:
            self.data_processor.stop_and_join()
            self.data_processor = None
            return None

    def start_processing(self):
        self.stop_processing()
        (self.decoder, channel_info) = self.create_decoder(self.device_info, self.active_streams)
        self.data_pipe.send((CalcData.PROCESSING_START, self.device_info, self.active_streams, channel_info))
        self.data_processor = CalcDataProcessor(self.decoder, channel_info, self.data_pipe, self.logger, self.is_shown, self.settings.channel_interval, self.settings.plot_interval, self.settings.fft_interval, self.triggers)

    def run(self):
        running = True

def run_calc_runner(log_queue, *args, **kwargs):
    sys.stdout = open(os.devnull)
    sys.stderr = open(os.devnull)
    handler = QueueHandler(log_queue)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)
    if sys.platform == 'win32':
        signal.signal(signal.SIGINT, signal.SIG_IGN)
    else:
        os.setpgrp()
