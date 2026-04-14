# Source Generated with Decompyle++
# File: hardware_test_funcs.pyc (Python 3.11)

import time
import numpy
import asphodel
from asphodel import AsphodelNativeDevice, AsphodelStreamInfo, AsphodelChannelInfo, SupplyInfo
from asphodel.streamutil import stream_fixed_duration
from asphodel.streamutil import filter_channel_data
from asphodel.streamutil import unpack_streaming_data

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def supply_test(device, supply_id, name, info):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 NOP
    #    4 LOAD_FAST device
    #    6 LOAD_METHOD check_supply
    #   28 LOAD_FAST supply_id
    #   30 PRECALL
    #   34 CALL
    #   44 UNPACK_SEQUENCE
    #   48 STORE_FAST value
    #   50 STORE_FAST result_flags
    #   52 JUMP_FORWARD to 100
    #   54 PUSH_EXC_INFO
    #   56 LOAD_GLOBAL Exception
    #   68 CHECK_EXC_MATCH
    #   70 POP_JUMP_FORWARD_IF_FALSE to 92
    #   72 POP_TOP
    #   74 LOAD_CONST False
    #   76 LOAD_FAST name
    #   78 FORMAT_VALUE
    #   80 LOAD_CONST ' check aborted!'
    #   82 BUILD_STRING
    #   84 BUILD_TUPLE
    #   86 SWAP
    #   88 POP_EXCEPT
    #   90 RETURN_VALUE
    #   92 RERAISE
    #   94 COPY
    #   96 POP_EXCEPT
    #   98 RERAISE
    #  100 LOAD_FAST value
    #  102 LOAD_FAST info
    #  104 LOAD_ATTR scale
    #  114 BINARY_OP *
    #  118 LOAD_FAST info
    #  120 LOAD_ATTR offset
    #  130 BINARY_OP +
    #  134 STORE_FAST scaled_value
    #  136 LOAD_FAST info
    #  138 LOAD_ATTR nominal
    #  148 LOAD_FAST info
    #  150 LOAD_ATTR scale
    #  160 BINARY_OP *
    #  164 LOAD_FAST info
    #  166 LOAD_ATTR offset
    #  176 BINARY_OP +
    #  180 STORE_FAST scaled_nominal
    #  182 LOAD_FAST scaled_nominal
    #  184 LOAD_CONST 0.0
    #  186 COMPARE_OP !=
    #  192 POP_JUMP_FORWARD_IF_FALSE to 212
    #  194 LOAD_FAST scaled_value
    #  196 LOAD_FAST scaled_nominal
    #  198 BINARY_OP /
    #  202 LOAD_CONST 100.0
    #  204 BINARY_OP *
    #  208 STORE_FAST percent
    #  210 JUMP_FORWARD to 216
    #  212 LOAD_CONST 0.0
    #  214 STORE_FAST percent
    #  216 LOAD_GLOBAL NULL + asphodel
    #  228 LOAD_ATTR format_value_ascii
    #  238 LOAD_FAST info
    #  240 LOAD_ATTR unit_type
    #  250 LOAD_FAST info
    #  252 LOAD_ATTR scale
    #  262 LOAD_FAST scaled_value
    #  264 PRECALL
    #  268 CALL
    #  278 STORE_FAST formatted
    #  280 LOAD_FAST result_flags
    #  282 LOAD_CONST 0
    #  284 COMPARE_OP ==
    #  290 POP_JUMP_FORWARD_IF_FALSE to 296
    #  292 LOAD_CONST True
    #  294 JUMP_FORWARD to 298
    #  296 LOAD_CONST False
    #  298 STORE_FAST success
    #  300 LOAD_FAST success
    #  302 POP_JUMP_FORWARD_IF_FALSE to 308
    #  304 LOAD_CONST 'pass'
    # ... bytecode truncated ...
    pass

def bridge_test(device, stream_id, stream, channel_id, channel):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 MAKE_CELL stream_id
    #    4 MAKE_CELL channel_id
    #    6 RESUME
    #    8 LOAD_FAST channel
    #   10 LOAD_ATTR name
    #   20 LOAD_METHOD decode
    #   42 LOAD_CONST 'utf-8'
    #   44 PRECALL
    #   48 CALL
    #   58 STORE_FAST channel_name
    #   60 LOAD_DEREF device
    #   62 LOAD_METHOD get_strain_bridge_count
    #   84 LOAD_FAST channel
    #   86 PRECALL
    #   90 CALL
    #  100 STORE_FAST bridge_count
    #  102 LOAD_CONST 'subchannel_index'
    #  104 LOAD_GLOBAL int
    #  116 LOAD_CONST 'return'
    #  118 LOAD_GLOBAL tuple
    #  130 LOAD_GLOBAL float
    #  142 LOAD_GLOBAL str
    #  154 BUILD_TUPLE
    #  156 BINARY_SUBSCR
    #  166 BUILD_TUPLE
    #  168 LOAD_CLOSURE channel_id
    #  170 LOAD_CLOSURE device
    #  172 LOAD_CLOSURE stream_id
    #  174 BUILD_TUPLE
    #  176 LOAD_CONST <code object get_mean_value at 0x100b03290, file "acheron\device_process\hardware_test_funcs.py", line 46>
    #  178 MAKE_FUNCTION annotations, closure
    #  180 STORE_FAST get_mean_value
    #  182 NOP
    #  184 LOAD_DEREF device
    #  186 LOAD_METHOD warm_up_stream
    #  208 LOAD_DEREF stream_id
    #  210 LOAD_CONST True
    #  212 PRECALL
    #  216 CALL
    #  226 POP_TOP
    #  228 LOAD_GLOBAL NULL + time
    #  240 LOAD_ATTR sleep
    #  250 LOAD_CONST 0.1
    #  252 PRECALL
    #  256 CALL
    #  266 POP_TOP
    #  268 BUILD_LIST
    #  270 STORE_FAST lines
    #  272 LOAD_CONST True
    #  274 STORE_FAST success
    #  276 NOP
    #  278 LOAD_GLOBAL NULL + range
    #  290 LOAD_FAST bridge_count
    #  292 PRECALL
    #  296 CALL
    #  306 GET_ITER
    #  308 EXTENDED_ARG
    #  310 FOR_ITER to 890
    #  312 STORE_FAST bridge_index
    #  314 LOAD_DEREF device
    #  316 LOAD_METHOD get_strain_bridge_subchannel
    #  338 LOAD_FAST channel
    #  340 LOAD_FAST bridge_index
    #  342 PRECALL
    #  346 CALL
    #  356 STORE_FAST subchannel_index
    #  358 LOAD_DEREF device
    #  360 LOAD_METHOD set_strain_outputs
    #  382 LOAD_DEREF channel_id
    #  384 LOAD_FAST bridge_index
    #  386 LOAD_CONST 1
    #  388 LOAD_CONST 0
    #  390 PRECALL
    #  394 CALL
    #  404 POP_TOP
    #  406 PUSH_NULL
    #  408 LOAD_FAST get_mean_value
    #  410 LOAD_FAST subchannel_index
    #  412 PRECALL
    # ... bytecode truncated ...
    pass

def accel_test(device, stream_id, stream, channel_id, channel):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 MAKE_CELL stream_id
    #    4 MAKE_CELL stream
    #    6 MAKE_CELL channel_id
    #    8 RESUME
    #   10 LOAD_FAST channel
    #   12 LOAD_ATTR name
    #   22 LOAD_METHOD decode
    #   44 LOAD_CONST 'utf-8'
    #   46 PRECALL
    #   50 CALL
    #   60 STORE_FAST channel_name
    #   62 LOAD_CONST 'return'
    #   64 LOAD_GLOBAL tuple
    #   76 LOAD_GLOBAL float
    #   88 LOAD_GLOBAL float
    #  100 LOAD_GLOBAL float
    #  112 BUILD_TUPLE
    #  114 BINARY_SUBSCR
    #  124 BUILD_TUPLE
    #  126 LOAD_CLOSURE channel_id
    #  128 LOAD_CLOSURE device
    #  130 LOAD_CLOSURE stream
    #  132 LOAD_CLOSURE stream_id
    #  134 BUILD_TUPLE
    #  136 LOAD_CONST <code object get_mean_value at 0x105a86040, file "acheron\device_process\hardware_test_funcs.py", line 106>
    #  138 MAKE_FUNCTION annotations, closure
    #  140 STORE_FAST get_mean_value
    #  142 NOP
    #  144 LOAD_DEREF device
    #  146 LOAD_METHOD warm_up_stream
    #  168 LOAD_DEREF stream_id
    #  170 LOAD_CONST True
    #  172 PRECALL
    #  176 CALL
    #  186 POP_TOP
    #  188 LOAD_GLOBAL NULL + time
    #  200 LOAD_ATTR sleep
    #  210 LOAD_CONST 0.1
    #  212 PRECALL
    #  216 CALL
    #  226 POP_TOP
    #  228 NOP
    #  230 LOAD_DEREF device
    #  232 LOAD_METHOD enable_accel_self_test
    #  254 LOAD_DEREF channel_id
    #  256 LOAD_CONST True
    #  258 PRECALL
    #  262 CALL
    #  272 POP_TOP
    #  274 PUSH_NULL
    #  276 LOAD_FAST get_mean_value
    #  278 PRECALL
    #  282 CALL
    #  292 STORE_FAST enabled_mean
    #  294 LOAD_DEREF device
    #  296 LOAD_METHOD enable_accel_self_test
    #  318 LOAD_DEREF channel_id
    #  320 LOAD_CONST False
    #  322 PRECALL
    #  326 CALL
    #  336 POP_TOP
    #  338 PUSH_NULL
    #  340 LOAD_FAST get_mean_value
    #  342 PRECALL
    #  346 CALL
    #  356 STORE_FAST disabled_mean
    #  358 LOAD_DEREF device
    #  360 LOAD_METHOD warm_up_stream
    #  382 LOAD_DEREF stream_id
    #  384 LOAD_CONST False
    #  386 PRECALL
    #  390 CALL
    #  400 POP_TOP
    #  402 JUMP_FORWARD to 458
    #  404 PUSH_EXC_INFO
    #  406 LOAD_DEREF device
    #  408 LOAD_METHOD warm_up_stream
    #  430 LOAD_DEREF stream_id
    #  432 LOAD_CONST False
    # ... bytecode truncated ...
    pass
