# Source Generated with Decompyle++
# File: writer.pyc (Python 3.11)

import binascii
import ctypes
from dataclasses import fields
import datetime
import json
import logging
import os
from queue import Empty, Queue
import re
import struct
import subprocess
import sys
import threading
import time
from typing import Any, IO, Iterable, Optional, Protocol
import unicodedata
from asphodel.device_info import DeviceInfo
from compressor import open_compressor
from schedule import OutputConfig, ScheduleItem
logger = logging.getLogger(__name__)
UPLOAD_EXTENSION = '.upload'

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class WriterStatusCallback(Protocol):

    def writer_file_started(self, filename, schedule_id, marked_for_upload):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def writer_file_finished(self, filename, schedule_id, marked_for_upload):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def writer_stopped(self, schedule_id, success):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

def _get_valid_filename(s):
    b = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    s = b.decode('ascii')
    s = s.strip().replace(' ', '_')
    s = re.sub('[^-\\w.]', '', s)
    s = re.sub('[.]{2,}', '.', s)
    s = s.strip('.')
    return s

class StreamWriter:

    def __init__(self, logger, device_info, extra_info, schedule_item, default_output_config, writer_status_callback):
        self.logger = logger
        self.device_info = device_info
        self.extra_info = extra_info
        self.schedule_item = schedule_item
        self.default_output_config = default_output_config
        self.writer_status_callback = writer_status_callback

    def calc_filename_parts(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR device_info
        #   14 LOAD_ATTR user_tag_1
        #   24 POP_JUMP_FORWARD_IF_NOT_NONE to 62
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR device_info
        #   38 LOAD_ATTR serial_number
        #   48 LOAD_FAST self
        #   50 STORE_ATTR display_name
        #   60 JUMP_FORWARD to 170
        #   62 LOAD_GLOBAL NULL + _get_valid_filename
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR device_info
        #   86 LOAD_ATTR user_tag_1
        #   96 PRECALL
        #  100 CALL
        #  110 LOAD_FAST self
        #  112 STORE_ATTR display_name
        #  122 LOAD_FAST self
        #  124 LOAD_ATTR display_name
        #  134 POP_JUMP_FORWARD_IF_TRUE to 170
        #  136 LOAD_FAST self
        #  138 LOAD_ATTR device_info
        #  148 LOAD_ATTR serial_number
        #  158 LOAD_FAST self
        #  160 STORE_ATTR display_name
        #  170 LOAD_FAST self
        #  172 LOAD_ATTR output_config
        #  182 LOAD_ATTR base_name
        #  192 STORE_FAST base_name
        #  194 LOAD_FAST base_name
        #  196 POP_JUMP_FORWARD_IF_FALSE to 214
        #  198 LOAD_FAST base_name
        #  200 LOAD_FAST self
        #  202 STORE_ATTR base_name
        #  212 JUMP_FORWARD to 238
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR display_name
        #  226 LOAD_FAST self
        #  228 STORE_ATTR base_name
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR output_config
        #  250 LOAD_ATTR device_directory
        #  260 STORE_FAST device_directory
        #  262 LOAD_FAST device_directory
        #  264 LOAD_CONST False
        #  266 IS_OP
        #  268 POP_JUMP_FORWARD_IF_FALSE to 288
        #  270 LOAD_CONST ''
        #  272 LOAD_FAST self
        #  274 STORE_ATTR device_directory
        #  284 LOAD_CONST None
        #  286 RETURN_VALUE
        #  288 LOAD_FAST device_directory
        #  290 LOAD_CONST True
        #  292 IS_OP
        #  294 POP_JUMP_FORWARD_IF_FALSE to 324
        #  296 LOAD_FAST self
        #  298 LOAD_ATTR display_name
        #  308 LOAD_FAST self
        #  310 STORE_ATTR device_directory
        #  320 LOAD_CONST None
        #  322 RETURN_VALUE
        #  324 LOAD_FAST device_directory
        #  326 LOAD_FAST self
        #  328 STORE_ATTR device_directory
        #  338 LOAD_CONST None
        #  340 RETURN_VALUE
        pass

    def create_header(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL type_convert
        #    2 RESUME
        #    4 LOAD_GLOBAL datetime
        #   16 LOAD_ATTR datetime
        #   26 LOAD_METHOD now
        #   48 LOAD_GLOBAL datetime
        #   60 LOAD_ATTR timezone
        #   70 LOAD_ATTR utc
        #   80 PRECALL
        #   84 CALL
        #   94 LOAD_METHOD timestamp
        #  116 PRECALL
        #  120 CALL
        #  130 STORE_FAST timestamp
        #  132 BUILD_MAP
        #  134 STORE_FAST header_dict
        #  136 LOAD_GLOBAL NULL + fields
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR device_info
        #  160 PRECALL
        #  164 CALL
        #  174 GET_ITER
        #  176 FOR_ITER to 254
        #  178 STORE_FAST field
        #  180 LOAD_GLOBAL NULL + getattr
        #  192 LOAD_FAST self
        #  194 LOAD_ATTR device_info
        #  204 LOAD_FAST field
        #  206 LOAD_ATTR name
        #  216 PRECALL
        #  220 CALL
        #  230 STORE_FAST item
        #  232 LOAD_FAST item
        #  234 LOAD_FAST header_dict
        #  236 LOAD_FAST field
        #  238 LOAD_ATTR name
        #  248 STORE_SUBSCR
        #  252 JUMP_BACKWARD to 176
        #  254 LOAD_FAST header_dict
        #  256 LOAD_METHOD update
        #  278 LOAD_FAST self
        #  280 LOAD_ATTR extra_info
        #  290 PRECALL
        #  294 CALL
        #  304 POP_TOP
        #  306 LOAD_FAST self
        #  308 LOAD_ATTR schedule_item
        #  318 LOAD_ATTR id
        #  328 LOAD_FAST header_dict
        #  330 LOAD_CONST 'schedule_id'
        #  332 STORE_SUBSCR
        #  336 LOAD_CONST 't'
        #  338 LOAD_GLOBAL Any
        #  350 LOAD_CONST 'return'
        #  352 LOAD_GLOBAL Any
        #  364 BUILD_TUPLE
        #  366 LOAD_CLOSURE type_convert
        #  368 BUILD_TUPLE
        #  370 LOAD_CONST <code object type_convert at 0xacd202a00, file "acheron\device_process\writer.py", line 141>
        #  372 MAKE_FUNCTION annotations, closure
        #  374 STORE_DEREF type_convert
        #  376 PUSH_NULL
        #  378 LOAD_DEREF type_convert
        #  380 LOAD_FAST header_dict
        #  382 PRECALL
        #  386 CALL
        #  396 STORE_FAST d
        #  398 LOAD_GLOBAL NULL + json
        #  410 LOAD_ATTR dumps
        #  420 LOAD_FAST d
        #  422 LOAD_CONST True
        #  424 KW_NAMES
        #  426 PRECALL
        #  430 CALL
        #  440 LOAD_METHOD encode
        #  462 LOAD_CONST 'ascii'
        #  464 PRECALL
        #  468 CALL
        #  478 STORE_FAST hb
        #  480 LOAD_GLOBAL NULL + struct
        # ... bytecode truncated ...
        pass

    def get_filename(self, dt):
        if self.output_config.date_dir_structure:
            date_dir = dt.strftime('%Y_%m_%d')
        else:
            date_dir = ''
        directory = os.path.join(self.output_config.base_directory, date_dir, self.device_directory)
        os.makedirs(directory, exist_ok = True)
        if self.output_config.datetime_filename:
            base_name = dt.strftime('%Y%m%dT%H%MZ_') + self.base_name
        else:
            base_name = self.base_name
        base_name = os.path.join(directory, base_name)
        filename = base_name + '.apd'
        index = 1

    def open_compressor(self, dt):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD get_filename
        #   26 LOAD_FAST dt
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST filename
        #   44 LOAD_FAST filename
        #   46 LOAD_FAST self
        #   48 STORE_ATTR current_filename
        #   58 LOAD_GLOBAL NULL + open_compressor
        #   70 LOAD_FAST filename
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR output_config
        #   84 LOAD_ATTR compression_level
        #   94 PRECALL
        #   98 CALL
        #  108 UNPACK_SEQUENCE
        #  112 STORE_FAST pipe
        #  114 STORE_FAST process
        #  116 LOAD_FAST pipe
        #  118 LOAD_FAST self
        #  120 STORE_ATTR compressor_pipe
        #  130 LOAD_FAST process
        #  132 POP_JUMP_FORWARD_IF_FALSE to 216
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR compressor_lock
        #  146 BEFORE_WITH
        #  148 POP_TOP
        #  150 LOAD_FAST process
        #  152 LOAD_FAST self
        #  154 LOAD_ATTR compressors
        #  164 LOAD_FAST filename
        #  166 STORE_SUBSCR
        #  170 LOAD_CONST None
        #  172 LOAD_CONST None
        #  174 LOAD_CONST None
        #  176 PRECALL
        #  180 CALL
        #  190 POP_TOP
        #  192 JUMP_FORWARD to 216
        #  194 PUSH_EXC_INFO
        #  196 WITH_EXCEPT_START
        #  198 POP_JUMP_FORWARD_IF_TRUE to 208
        #  200 RERAISE
        #  202 COPY
        #  204 POP_EXCEPT
        #  206 RERAISE
        #  208 POP_TOP
        #  210 POP_EXCEPT
        #  212 POP_TOP
        #  214 POP_TOP
        #  216 LOAD_FAST pipe
        #  218 LOAD_METHOD write
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR header_bytes
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_FAST self
        #  270 LOAD_ATTR output_config
        #  280 LOAD_ATTR upload_marker
        #  290 POP_JUMP_FORWARD_IF_FALSE to 678
        #  292 LOAD_GLOBAL os
        #  304 LOAD_ATTR path
        #  314 LOAD_METHOD split
        #  336 LOAD_FAST filename
        #  338 PRECALL
        #  342 CALL
        #  352 UNPACK_SEQUENCE
        #  356 STORE_FAST path
        #  358 STORE_FAST name
        #  360 LOAD_GLOBAL os
        #  372 LOAD_ATTR path
        #  382 LOAD_METHOD join
        #  404 LOAD_FAST path
        #  406 LOAD_CONST '.'
        #  408 LOAD_FAST name
        #  410 BINARY_OP +
        #  414 LOAD_GLOBAL UPLOAD_EXTENSION
        # ... bytecode truncated ...
        pass

    def close_compressor(self):
        if self.compressor_pipe:
            self.compressor_pipe.close()
            self.compressor_pipe = None
            return None

    def mark_finished(self, filename):
        if filename:
            self.finished_queue.put(filename)
            return None

    def write(self, stream_packets):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.write_queue.put((b''.join(stream_packets), now))

    def calc_stop_time_target(self):
        t = None
        if self.collection_time_actual and self.schedule_item.duration:
            t = self.collection_time_actual + self.schedule_item.duration
        if self.schedule_item.stop_time:
            if t:
                t = min(t, self.schedule_item.stop_time)
            else:
                t = self.schedule_item.stop_time
        if self.schedule_item.failure_time:
            if t:
                t = min(t, self.schedule_item.failure_time)
            else:
                t = self.schedule_item.stop_time
        self.stop_time_target = t

    def calc_next_boundary(self, dt):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR output_config
        #   14 LOAD_ATTR roll_over_interval
        #   24 POP_JUMP_FORWARD_IF_FALSE to 262
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR output_config
        #   38 LOAD_ATTR roll_over_interval
        #   48 LOAD_METHOD total_seconds
        #   70 PRECALL
        #   74 CALL
        #   84 STORE_FAST interval
        #   86 LOAD_FAST dt
        #   88 LOAD_ATTR hour
        #   98 LOAD_CONST 60
        #  100 BINARY_OP *
        #  104 LOAD_FAST dt
        #  106 LOAD_ATTR minute
        #  116 BINARY_OP +
        #  120 LOAD_CONST 60
        #  122 BINARY_OP *
        #  126 LOAD_FAST dt
        #  128 LOAD_ATTR second
        #  138 BINARY_OP +
        #  142 STORE_FAST seconds
        #  144 LOAD_GLOBAL NULL + datetime
        #  156 LOAD_ATTR timedelta
        #  166 LOAD_FAST seconds
        #  168 LOAD_FAST interval
        #  170 BINARY_OP %
        #  174 LOAD_FAST dt
        #  176 LOAD_ATTR microsecond
        #  186 KW_NAMES
        #  188 PRECALL
        #  192 CALL
        #  202 STORE_FAST partial
        #  204 LOAD_FAST dt
        #  206 LOAD_FAST partial
        #  208 BINARY_OP -
        #  212 LOAD_GLOBAL NULL + datetime
        #  224 LOAD_ATTR timedelta
        #  234 LOAD_FAST interval
        #  236 KW_NAMES
        #  238 PRECALL
        #  242 CALL
        #  252 BINARY_OP +
        #  256 STORE_FAST boundary
        #  258 LOAD_FAST boundary
        #  260 RETURN_VALUE
        #  262 LOAD_GLOBAL datetime
        #  274 LOAD_ATTR datetime
        #  284 LOAD_ATTR max
        #  294 RETURN_VALUE
        pass

    def handle_write(self, stream_packets, dt):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR stop_time_target
        #   14 POP_JUMP_FORWARD_IF_FALSE to 338
        #   16 LOAD_FAST dt
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR stop_time_target
        #   30 COMPARE_OP >
        #   36 POP_JUMP_FORWARD_IF_FALSE to 338
        #   38 LOAD_FAST self
        #   40 LOAD_ATTR stop_time_reached
        #   50 POP_JUMP_FORWARD_IF_TRUE to 334
        #   52 LOAD_CONST True
        #   54 LOAD_FAST self
        #   56 STORE_ATTR stop_time_reached
        #   66 LOAD_FAST self
        #   68 LOAD_METHOD close_compressor
        #   90 PRECALL
        #   94 CALL
        #  104 POP_TOP
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR schedule_item
        #  118 LOAD_ATTR failure_time
        #  128 POP_JUMP_FORWARD_IF_FALSE to 168
        #  130 LOAD_FAST dt
        #  132 LOAD_FAST self
        #  134 LOAD_ATTR schedule_item
        #  144 LOAD_ATTR failure_time
        #  154 COMPARE_OP >
        #  160 POP_JUMP_FORWARD_IF_FALSE to 168
        #  162 LOAD_CONST False
        #  164 STORE_FAST success
        #  166 JUMP_FORWARD to 172
        #  168 LOAD_CONST True
        #  170 STORE_FAST success
        #  172 NOP
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR writer_status_callback
        #  186 LOAD_METHOD writer_stopped
        #  208 LOAD_FAST self
        #  210 LOAD_ATTR schedule_item
        #  220 LOAD_ATTR id
        #  230 LOAD_FAST success
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 JUMP_FORWARD to 754
        #  250 PUSH_EXC_INFO
        #  252 LOAD_GLOBAL Exception
        #  264 CHECK_EXC_MATCH
        #  266 POP_JUMP_FORWARD_IF_FALSE to 326
        #  268 POP_TOP
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR logger
        #  282 LOAD_METHOD exception
        #  304 LOAD_CONST 'Exception in writer_stopped callback'
        #  306 PRECALL
        #  310 CALL
        #  320 POP_TOP
        #  322 POP_EXCEPT
        #  324 JUMP_FORWARD to 754
        #  326 RERAISE
        #  328 COPY
        #  330 POP_EXCEPT
        #  332 RERAISE
        #  334 LOAD_CONST None
        #  336 RETURN_VALUE
        #  338 LOAD_FAST self
        #  340 LOAD_ATTR next_boundary
        #  350 POP_JUMP_FORWARD_IF_NOT_NONE to 542
        #  352 LOAD_FAST self
        #  354 LOAD_ATTR collection_time_target
        #  364 POP_JUMP_FORWARD_IF_NONE to 388
        #  366 LOAD_FAST dt
        #  368 LOAD_FAST self
        #  370 LOAD_ATTR collection_time_target
        #  380 COMPARE_OP >
        #  386 POP_JUMP_FORWARD_IF_FALSE to 538
        #  388 LOAD_FAST dt
        #  390 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def write_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + time
        #   16 LOAD_ATTR monotonic
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST last_log
        #   42 LOAD_CONST False
        #   44 STORE_FAST slowdown_logged
        #   46 NOP
        #   48 NOP
        #   50 LOAD_FAST self
        #   52 LOAD_ATTR write_queue
        #   62 LOAD_METHOD get
        #   84 LOAD_CONST True
        #   86 LOAD_CONST 0.1
        #   88 PRECALL
        #   92 CALL
        #  102 STORE_FAST data
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR write_queue
        #  116 LOAD_METHOD qsize
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST qsize
        #  154 LOAD_GLOBAL NULL + time
        #  166 LOAD_ATTR monotonic
        #  176 PRECALL
        #  180 CALL
        #  190 STORE_FAST now
        #  192 LOAD_FAST qsize
        #  194 LOAD_CONST 100
        #  196 COMPARE_OP >=
        #  202 POP_JUMP_FORWARD_IF_FALSE to 290
        #  204 LOAD_FAST now
        #  206 LOAD_FAST last_log
        #  208 BINARY_OP -
        #  212 LOAD_CONST 10.0
        #  214 COMPARE_OP >=
        #  220 POP_JUMP_FORWARD_IF_FALSE to 288
        #  222 LOAD_CONST True
        #  224 STORE_FAST slowdown_logged
        #  226 LOAD_CONST 'Write queue slow down: %d elements'
        #  228 STORE_FAST msg
        #  230 LOAD_FAST self
        #  232 LOAD_ATTR logger
        #  242 LOAD_METHOD info
        #  264 LOAD_FAST msg
        #  266 LOAD_FAST qsize
        #  268 PRECALL
        #  272 CALL
        #  282 POP_TOP
        #  284 LOAD_FAST now
        #  286 STORE_FAST last_log
        #  288 JUMP_FORWARD to 366
        #  290 LOAD_FAST qsize
        #  292 LOAD_CONST 0
        #  294 COMPARE_OP ==
        #  300 POP_JUMP_FORWARD_IF_FALSE to 366
        #  302 LOAD_FAST slowdown_logged
        #  304 POP_JUMP_FORWARD_IF_FALSE to 366
        #  306 LOAD_CONST False
        #  308 STORE_FAST slowdown_logged
        #  310 LOAD_FAST self
        #  312 LOAD_ATTR logger
        #  322 LOAD_METHOD info
        #  344 LOAD_CONST 'Write queue has caught up'
        #  346 PRECALL
        #  350 CALL
        #  360 POP_TOP
        #  362 LOAD_FAST now
        #  364 STORE_FAST last_log
        #  366 PUSH_NULL
        #  368 LOAD_FAST self
        #  370 LOAD_ATTR handle_write
        #  380 LOAD_FAST data
        #  382 CALL_FUNCTION_EX
        #  384 POP_TOP
        #  386 JUMP_FORWARD to 852
        #  388 PUSH_EXC_INFO
        # ... bytecode truncated ...
        pass

    def monitor_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 NOP
        #    6 NOP
        #    8 LOAD_FAST self
        #   10 LOAD_ATTR finished_queue
        #   20 LOAD_METHOD get
        #   42 LOAD_CONST True
        #   44 LOAD_CONST 0.1
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST filename
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR compressor_lock
        #   74 BEFORE_WITH
        #   76 POP_TOP
        #   78 LOAD_FAST self
        #   80 LOAD_ATTR compressors
        #   90 LOAD_METHOD get
        #  112 LOAD_FAST filename
        #  114 PRECALL
        #  118 CALL
        #  128 STORE_FAST compressor
        #  130 LOAD_CONST None
        #  132 LOAD_CONST None
        #  134 LOAD_CONST None
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 JUMP_FORWARD to 176
        #  154 PUSH_EXC_INFO
        #  156 WITH_EXCEPT_START
        #  158 POP_JUMP_FORWARD_IF_TRUE to 168
        #  160 RERAISE
        #  162 COPY
        #  164 POP_EXCEPT
        #  166 RERAISE
        #  168 POP_TOP
        #  170 POP_EXCEPT
        #  172 POP_TOP
        #  174 POP_TOP
        #  176 LOAD_FAST compressor
        #  178 POP_JUMP_FORWARD_IF_FALSE to 404
        #  180 LOAD_FAST compressor
        #  182 LOAD_METHOD wait
        #  204 PRECALL
        #  208 CALL
        #  218 STORE_FAST ret_val
        #  220 LOAD_FAST ret_val
        #  222 LOAD_CONST 0
        #  224 COMPARE_OP !=
        #  230 POP_JUMP_FORWARD_IF_FALSE to 326
        #  232 LOAD_CONST 'Compressor exited with error {}'
        #  234 STORE_FAST msg
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR logger
        #  248 LOAD_METHOD warning
        #  270 LOAD_FAST msg
        #  272 LOAD_METHOD format
        #  294 LOAD_FAST ret_val
        #  296 PRECALL
        #  300 CALL
        #  310 PRECALL
        #  314 CALL
        #  324 POP_TOP
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR compressor_lock
        #  338 BEFORE_WITH
        #  340 POP_TOP
        #  342 LOAD_FAST self
        #  344 LOAD_ATTR compressors
        #  354 LOAD_FAST filename
        #  356 DELETE_SUBSCR
        #  358 LOAD_CONST None
        #  360 LOAD_CONST None
        #  362 LOAD_CONST None
        #  364 PRECALL
        #  368 CALL
        #  378 POP_TOP
        #  380 JUMP_FORWARD to 404
        # ... bytecode truncated ...
        pass

    def close(self):
        self.is_finished.set()

    def join(self):
        self.write_thread.join()
        self.monitor_thread.join()

    def update(self, schedule_item):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR schedule_item
        #   14 LOAD_FAST schedule_item
        #   16 COMPARE_OP ==
        #   22 POP_JUMP_FORWARD_IF_FALSE to 28
        #   24 LOAD_CONST None
        #   26 RETURN_VALUE
        #   28 LOAD_FAST self
        #   30 LOAD_ATTR output_config
        #   40 LOAD_FAST schedule_item
        #   42 LOAD_ATTR output_config
        #   52 COMPARE_OP !=
        #   58 POP_JUMP_FORWARD_IF_FALSE to 90
        #   60 LOAD_GLOBAL NULL + ValueError
        #   72 LOAD_CONST "Can't update output configuration while running"
        #   74 PRECALL
        #   78 CALL
        #   88 RAISE_VARARGS
        #   90 LOAD_FAST schedule_item
        #   92 LOAD_FAST self
        #   94 STORE_ATTR schedule_item
        #  104 LOAD_FAST schedule_item
        #  106 LOAD_ATTR collection_time
        #  116 LOAD_FAST self
        #  118 STORE_ATTR collection_time_target
        #  128 LOAD_FAST self
        #  130 LOAD_METHOD calc_stop_time_target
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_CONST None
        #  170 RETURN_VALUE
        pass
