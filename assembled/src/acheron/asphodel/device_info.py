# Source Generated with Decompyle++
# File: device_info.pyc (Python 3.11)

from collections.abc import Generator
from dataclasses import dataclass
import inspect
import logging
import math
from typing import Any, Callable, cast, Optional, ParamSpec, TypeVar, TYPE_CHECKING, Union
import asphodel
if TYPE_CHECKING:
    from diskcache import Cache
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: ProgressCallback = Callable[([
# INVALID FROM DECOMPILER:     int,
# INVALID FROM DECOMPILER:     int,
# INVALID FROM DECOMPILER:     str], None)]
LoggerType = Union[(logging.Logger, logging.LoggerAdapter[logging.Logger])]
P = ParamSpec('P')
T = TypeVar('T')
GetterFirst = tuple[(int, int, dict[(str, Any)])]
GetterFirstGenerator = Generator[(GetterFirst, None, None)]
GetterSecond = dict[(str, Any)]
GetterSecondGenerator = Generator[(GetterSecond, None, None)]
GetterGenerator = Generator[(Union[(GetterFirst, GetterSecond)], None, None)]
# INVALID FROM DECOMPILER: Getter = Callable[([
# INVALID FROM DECOMPILER:     asphodel.AsphodelNativeDevice,
# INVALID FROM DECOMPILER:     dict[(str, Any)],
# INVALID FROM DECOMPILER:     'Incrementer'], GetterGenerator)]
# INVALID FROM DECOMPILER: ActiveScanInfo = <NODE:12>()
# INVALID FROM DECOMPILER: DeviceInfo = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ActiveScanInfo:

    bootloader_info: str

    build_date: str

    build_info: str

    library_build_date: str

    library_build_info: str

    library_protocol_version: str

    location_string: str

    max_incoming_param_length: int

    max_outgoing_param_length: int

    serial_number: str

    stream_packet_length: int

    supports_bootloader: bool

    supports_radio: bool

    supports_remote: bool

    supports_rf_power: bool

    def from_dict(cls, device_info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL cls
        #    2 RESUME
        #    4 PUSH_NULL
        #    6 LOAD_DEREF cls
        #    8 LOAD_CONST ()
        #   10 BUILD_MAP
        #   12 LOAD_CLOSURE cls
        #   14 BUILD_TUPLE
        #   16 LOAD_CONST <code object <dictcomp> at 0x105aabcc0, file "asphodel\device_info.py", line 61>
        #   18 MAKE_FUNCTION closure
        #   20 LOAD_FAST device_info
        #   22 LOAD_METHOD items
        #   44 PRECALL
        #   48 CALL
        #   58 GET_ITER
        #   60 PRECALL
        #   64 CALL
        #   74 DICT_MERGE
        #   76 CALL_FUNCTION_EX
        #   78 RETURN_VALUE
        pass

class DeviceInfo:

    nvm: bytes

    chip_family: str

    chip_id: str

    chip_model: str

    protocol_version: str

    stream_filler_bits: int

    stream_id_bits: int

    supports_device_mode: bool

    device_mode = None

    radio_ctrl_vars = None

    radio_default_serial = None

    radio_scan_power = None

    rf_power_ctrl_vars = None

    rf_power_status = None

def try_optional(func, *args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 NOP
    #    4 PUSH_NULL
    #    6 LOAD_FAST func
    #    8 LOAD_FAST args
    #   10 BUILD_MAP
    #   12 LOAD_FAST kwargs
    #   14 DICT_MERGE
    #   16 CALL_FUNCTION_EX
    #   18 RETURN_VALUE
    #   20 PUSH_EXC_INFO
    #   22 LOAD_GLOBAL asphodel
    #   34 LOAD_ATTR AsphodelError
    #   44 CHECK_EXC_MATCH
    #   46 POP_JUMP_FORWARD_IF_FALSE to 106
    #   48 STORE_FAST e
    #   50 LOAD_FAST e
    #   52 LOAD_ATTR args
    #   62 LOAD_CONST 1
    #   64 BINARY_SUBSCR
    #   74 LOAD_CONST 'ERROR_CODE_UNIMPLEMENTED_COMMAND'
    #   76 COMPARE_OP ==
    #   82 POP_JUMP_FORWARD_IF_FALSE to 96
    #   84 POP_EXCEPT
    #   86 LOAD_CONST None
    #   88 STORE_FAST e
    #   90 DELETE_FAST e
    #   92 LOAD_CONST None
    #   94 RETURN_VALUE
    #   96 RAISE_VARARGS
    #   98 LOAD_CONST None
    #  100 STORE_FAST e
    #  102 DELETE_FAST e
    #  104 RERAISE
    #  106 RERAISE
    #  108 COPY
    #  110 POP_EXCEPT
    #  112 RERAISE
    pass

class Incrementer:

    def __init__(self, progress_callback, logger):
        self.progress_callback = progress_callback
        self.logger = logger
        self.finished = None
        self.total = None

    def increment(self, difference, section_name):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR finished
        #   14 POP_JUMP_FORWARD_IF_NONE to 30
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR total
        #   28 POP_JUMP_FORWARD_IF_NOT_NONE to 88
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR logger
        #   42 LOAD_METHOD warning
        #   64 LOAD_CONST 'Incrementing %s before ready'
        #   66 LOAD_FAST section_name
        #   68 PRECALL
        #   72 CALL
        #   82 POP_TOP
        #   84 LOAD_CONST None
        #   86 RETURN_VALUE
        #   88 LOAD_FAST self
        #   90 COPY
        #   92 LOAD_ATTR finished
        #  102 LOAD_FAST difference
        #  104 BINARY_OP +=
        #  108 SWAP
        #  110 STORE_ATTR finished
        #  120 LOAD_FAST self
        #  122 LOAD_ATTR progress_callback
        #  132 POP_JUMP_FORWARD_IF_FALSE to 312
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR finished
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR total
        #  158 COMPARE_OP >
        #  164 POP_JUMP_FORWARD_IF_FALSE to 242
        #  166 LOAD_FAST self
        #  168 LOAD_ATTR logger
        #  178 LOAD_METHOD warning
        #  200 LOAD_CONST 'Finished count (%s) exceeds total (%s)'
        #  202 LOAD_FAST self
        #  204 LOAD_ATTR finished
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR total
        #  226 PRECALL
        #  230 CALL
        #  240 POP_TOP
        #  242 LOAD_FAST self
        #  244 LOAD_METHOD progress_callback
        #  266 LOAD_FAST self
        #  268 LOAD_ATTR finished
        #  278 LOAD_FAST self
        #  280 LOAD_ATTR total
        #  290 LOAD_FAST section_name
        #  292 PRECALL
        #  296 CALL
        #  306 POP_TOP
        #  308 LOAD_CONST None
        #  310 RETURN_VALUE
        #  312 LOAD_CONST None
        #  314 RETURN_VALUE
        pass

    def set_values(self, finished, total):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR finished
        #   14 POP_JUMP_FORWARD_IF_NONE to 104
        #   16 LOAD_FAST finished
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR finished
        #   30 COMPARE_OP !=
        #   36 POP_JUMP_FORWARD_IF_FALSE to 104
        #   38 LOAD_FAST self
        #   40 LOAD_ATTR logger
        #   50 LOAD_METHOD warning
        #   72 LOAD_CONST 'Finished count has been changed %s -> %s'
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR finished
        #   86 LOAD_FAST finished
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_FAST finished
        #  106 LOAD_FAST self
        #  108 STORE_ATTR finished
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR total
        #  130 POP_JUMP_FORWARD_IF_NONE to 220
        #  132 LOAD_FAST self
        #  134 LOAD_ATTR total
        #  144 LOAD_FAST total
        #  146 COMPARE_OP !=
        #  152 POP_JUMP_FORWARD_IF_FALSE to 220
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR logger
        #  166 LOAD_METHOD warning
        #  188 LOAD_CONST 'Total count has been changed %s -> %s'
        #  190 LOAD_FAST self
        #  192 LOAD_ATTR total
        #  202 LOAD_FAST total
        #  204 PRECALL
        #  208 CALL
        #  218 POP_TOP
        #  220 LOAD_FAST total
        #  222 LOAD_FAST self
        #  224 STORE_ATTR total
        #  234 LOAD_CONST None
        #  236 RETURN_VALUE
        pass

def single_call(key_name, func_name, optional):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL key_name
    #    2 MAKE_CELL func_name
    #    4 MAKE_CELL optional
    #    6 RESUME
    #    8 LOAD_CONST 'device'
    #   10 LOAD_GLOBAL asphodel
    #   22 LOAD_ATTR AsphodelNativeDevice
    #   32 LOAD_CONST 'device_info'
    #   34 LOAD_GLOBAL dict
    #   46 LOAD_GLOBAL str
    #   58 LOAD_GLOBAL Any
    #   70 BUILD_TUPLE
    #   72 BINARY_SUBSCR
    #   82 LOAD_CONST 'incrementer'
    #   84 LOAD_GLOBAL Incrementer
    #   96 LOAD_CONST 'return'
    #   98 LOAD_GLOBAL GetterGenerator
    #  110 BUILD_TUPLE
    #  112 LOAD_CLOSURE func_name
    #  114 LOAD_CLOSURE key_name
    #  116 LOAD_CLOSURE optional
    #  118 BUILD_TUPLE
    #  120 LOAD_CONST <code object func at 0x105aeda10, file "asphodel\device_info.py", line 153>
    #  122 MAKE_FUNCTION annotations, closure
    #  124 STORE_FAST func
    #  126 LOAD_FAST func
    #  128 RETURN_VALUE
    pass

def array_call(key, device_info, incrementer, count_fn, element_fn, count_key, element_cost, skippable):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_FAST count_fn
    #    8 POP_JUMP_FORWARD_IF_NOT_NONE to 44
    #   10 LOAD_FAST count_key
    #   12 POP_JUMP_FORWARD_IF_NOT_NONE to 44
    #   14 LOAD_GLOBAL NULL + ValueError
    #   26 LOAD_CONST 'Must use count_fn or count_key'
    #   28 PRECALL
    #   32 CALL
    #   42 RAISE_VARARGS
    #   44 LOAD_FAST count_key
    #   46 POP_JUMP_FORWARD_IF_NONE to 128
    #   48 LOAD_FAST skippable
    #   50 POP_JUMP_FORWARD_IF_FALSE to 64
    #   52 LOAD_FAST key
    #   54 LOAD_FAST device_info
    #   56 CONTAINS_OP
    #   58 POP_JUMP_FORWARD_IF_FALSE to 64
    #   60 LOAD_CONST None
    #   62 RETURN_VALUE
    #   64 LOAD_GLOBAL NULL + len
    #   76 LOAD_FAST device_info
    #   78 LOAD_FAST count_key
    #   80 BINARY_SUBSCR
    #   90 PRECALL
    #   94 CALL
    #  104 STORE_FAST array_length
    #  106 LOAD_CONST 0
    #  108 LOAD_FAST element_cost
    #  110 LOAD_FAST array_length
    #  112 BINARY_OP *
    #  116 BUILD_MAP
    #  118 BUILD_TUPLE
    #  120 YIELD_VALUE
    #  122 RESUME
    #  124 POP_TOP
    #  126 JUMP_FORWARD to 314
    #  128 LOAD_FAST key
    #  130 LOAD_FAST device_info
    #  132 CONTAINS_OP
    #  134 POP_JUMP_FORWARD_IF_FALSE to 262
    #  136 LOAD_FAST device_info
    #  138 LOAD_FAST key
    #  140 BINARY_SUBSCR
    #  150 STORE_FAST array
    #  152 LOAD_FAST skippable
    #  154 POP_JUMP_FORWARD_IF_FALSE to 210
    #  156 LOAD_GLOBAL NULL + all
    #  168 LOAD_CONST <code object <genexpr> at 0x105af90d0, file "asphodel\device_info.py", line 191>
    #  170 MAKE_FUNCTION
    #  172 LOAD_FAST array
    #  174 GET_ITER
    #  176 PRECALL
    #  180 CALL
    #  190 PRECALL
    #  194 CALL
    #  204 POP_JUMP_FORWARD_IF_TRUE to 210
    #  206 LOAD_CONST None
    #  208 RETURN_VALUE
    #  210 LOAD_GLOBAL NULL + len
    #  222 LOAD_FAST array
    #  224 PRECALL
    #  228 CALL
    #  238 STORE_FAST array_length
    #  240 LOAD_CONST 0
    #  242 LOAD_FAST element_cost
    #  244 LOAD_FAST array_length
    #  246 BINARY_OP *
    #  250 BUILD_MAP
    #  252 BUILD_TUPLE
    #  254 YIELD_VALUE
    #  256 RESUME
    #  258 POP_TOP
    #  260 JUMP_FORWARD to 314
    #  262 PUSH_NULL
    #  264 LOAD_FAST count_fn
    #  266 PRECALL
    #  270 CALL
    # ... bytecode truncated ...
    pass

def get_custom_enums(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 MAKE_CELL d
    #    4 MAKE_CELL i
    #    6 RETURN_GENERATOR
    #    8 POP_TOP
    #   10 RESUME
    #   12 LOAD_CONST 'custom_enums'
    #   14 LOAD_FAST device_info
    #   16 CONTAINS_OP
    #   18 POP_JUMP_FORWARD_IF_FALSE to 278
    #   20 LOAD_FAST device_info
    #   22 LOAD_CONST 'custom_enums'
    #   24 BINARY_SUBSCR
    #   34 STORE_DEREF d
    #   36 LOAD_GLOBAL NULL + any
    #   48 LOAD_CONST <code object <genexpr> at 0x105af8b90, file "asphodel\device_info.py", line 216>
    #   50 MAKE_FUNCTION
    #   52 LOAD_DEREF d
    #   54 LOAD_METHOD values
    #   76 PRECALL
    #   80 CALL
    #   90 GET_ITER
    #   92 PRECALL
    #   96 CALL
    #  106 PRECALL
    #  110 CALL
    #  120 POP_JUMP_FORWARD_IF_FALSE to 274
    #  122 LOAD_GLOBAL NULL + tuple
    #  134 LOAD_CLOSURE d
    #  136 BUILD_TUPLE
    #  138 LOAD_CONST <code object <genexpr> at 0x105ba0030, file "asphodel\device_info.py", line 218>
    #  140 MAKE_FUNCTION closure
    #  142 LOAD_GLOBAL NULL + range
    #  154 LOAD_GLOBAL NULL + len
    #  166 LOAD_DEREF d
    #  168 PRECALL
    #  172 CALL
    #  182 PRECALL
    #  186 CALL
    #  196 GET_ITER
    #  198 PRECALL
    #  202 CALL
    #  212 PRECALL
    #  216 CALL
    #  226 STORE_FAST custom_enum_counts
    #  228 LOAD_GLOBAL NULL + sum
    #  240 LOAD_FAST custom_enum_counts
    #  242 PRECALL
    #  246 CALL
    #  256 STORE_FAST custom_enum_commands
    #  258 LOAD_CONST 0
    #  260 LOAD_FAST custom_enum_commands
    #  262 BUILD_MAP
    #  264 BUILD_TUPLE
    #  266 YIELD_VALUE
    #  268 RESUME
    #  270 POP_TOP
    #  272 JUMP_FORWARD to 416
    #  274 LOAD_CONST None
    #  276 RETURN_VALUE
    #  278 LOAD_DEREF device
    #  280 LOAD_METHOD get_custom_enum_counts
    #  302 PRECALL
    #  306 CALL
    #  316 STORE_FAST custom_enum_counts
    #  318 LOAD_GLOBAL NULL + sum
    #  330 LOAD_FAST custom_enum_counts
    #  332 PRECALL
    #  336 CALL
    #  346 STORE_FAST custom_enum_commands
    #  348 LOAD_CONST <code object <dictcomp> at 0x105af88f0, file "asphodel\device_info.py", line 227>
    #  350 MAKE_FUNCTION
    #  352 LOAD_GLOBAL NULL + enumerate
    #  364 LOAD_FAST custom_enum_counts
    #  366 PRECALL
    #  370 CALL
    #  380 GET_ITER
    #  382 PRECALL
    #  386 CALL
    #  396 STORE_FAST empty
    # ... bytecode truncated ...
    pass

def get_setting_categories(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 RETURN_GENERATOR
    #    4 POP_TOP
    #    6 RESUME
    #    8 LOAD_CONST 'i'
    #   10 LOAD_GLOBAL int
    #   22 LOAD_CONST 'return'
    #   24 LOAD_GLOBAL tuple
    #   36 LOAD_GLOBAL str
    #   48 LOAD_GLOBAL tuple
    #   60 LOAD_GLOBAL int
    #   72 LOAD_CONST Ellipsis
    #   74 BUILD_TUPLE
    #   76 BINARY_SUBSCR
    #   86 BUILD_TUPLE
    #   88 BINARY_SUBSCR
    #   98 BUILD_TUPLE
    #  100 LOAD_CLOSURE device
    #  102 BUILD_TUPLE
    #  104 LOAD_CONST <code object element_fn at 0x105a732d0, file "asphodel\device_info.py", line 240>
    #  106 MAKE_FUNCTION annotations, closure
    #  108 STORE_FAST element_fn
    #  110 LOAD_GLOBAL NULL + array_call
    #  122 LOAD_CONST 'setting_categories'
    #  124 LOAD_FAST device_info
    #  126 LOAD_FAST incrementer
    #  128 LOAD_DEREF device
    #  130 LOAD_ATTR get_setting_category_count
    #  140 LOAD_FAST element_fn
    #  142 LOAD_CONST 2
    #  144 KW_NAMES
    #  146 PRECALL
    #  150 CALL
    #  160 GET_YIELD_FROM_ITER
    #  162 LOAD_CONST None
    #  164 SEND to 172
    #  166 YIELD_VALUE
    #  168 RESUME
    #  170 JUMP_BACKWARD_NO_INTERRUPT to 164
    #  172 POP_TOP
    #  174 LOAD_CONST None
    #  176 RETURN_VALUE
    pass

def get_streams(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'stream_rate_info'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 18
    #   14 LOAD_CONST None
    #   16 RETURN_VALUE
    #   18 LOAD_CONST 'streams'
    #   20 LOAD_FAST device_info
    #   22 CONTAINS_OP
    #   24 POP_JUMP_FORWARD_IF_FALSE to 90
    #   26 LOAD_GLOBAL NULL + len
    #   38 LOAD_FAST device_info
    #   40 LOAD_CONST 'streams'
    #   42 BINARY_SUBSCR
    #   52 PRECALL
    #   56 CALL
    #   66 STORE_FAST stream_count
    #   68 LOAD_CONST 0
    #   70 LOAD_CONST 3
    #   72 LOAD_FAST stream_count
    #   74 BINARY_OP *
    #   78 BUILD_MAP
    #   80 BUILD_TUPLE
    #   82 YIELD_VALUE
    #   84 RESUME
    #   86 POP_TOP
    #   88 JUMP_FORWARD to 178
    #   90 LOAD_FAST device
    #   92 LOAD_METHOD get_stream_count
    #  114 PRECALL
    #  118 CALL
    #  128 UNPACK_SEQUENCE
    #  132 STORE_FAST stream_count
    #  134 STORE_FAST filler_bits
    #  136 STORE_FAST id_bits
    #  138 LOAD_FAST filler_bits
    #  140 LOAD_FAST id_bits
    #  142 LOAD_CONST None
    #  144 BUILD_LIST
    #  146 LOAD_FAST stream_count
    #  148 BINARY_OP *
    #  152 LOAD_CONST ('stream_filler_bits', 'stream_id_bits', 'streams')
    #  154 BUILD_CONST_KEY_MAP
    #  156 STORE_FAST d
    #  158 LOAD_CONST 1
    #  160 LOAD_CONST 3
    #  162 LOAD_FAST stream_count
    #  164 BINARY_OP *
    #  168 LOAD_FAST d
    #  170 BUILD_TUPLE
    #  172 YIELD_VALUE
    #  174 RESUME
    #  176 POP_TOP
    #  178 BUILD_LIST
    #  180 STORE_FAST streams
    #  182 BUILD_LIST
    #  184 STORE_FAST stream_rate_info
    #  186 LOAD_GLOBAL NULL + range
    #  198 LOAD_FAST stream_count
    #  200 PRECALL
    #  204 CALL
    #  214 GET_ITER
    #  216 FOR_ITER to 426
    #  218 STORE_FAST i
    #  220 LOAD_FAST streams
    #  222 LOAD_METHOD append
    #  244 LOAD_FAST device
    #  246 LOAD_METHOD get_stream
    #  268 LOAD_FAST i
    #  270 PRECALL
    #  274 CALL
    #  284 PRECALL
    #  288 CALL
    #  298 POP_TOP
    #  300 LOAD_FAST stream_rate_info
    #  302 LOAD_METHOD append
    #  324 LOAD_FAST device
    # ... bytecode truncated ...
    pass

def get_channels(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_GLOBAL NULL + array_call
    #   18 LOAD_CONST 'channels'
    #   20 LOAD_FAST device_info
    #   22 LOAD_FAST incrementer
    #   24 LOAD_FAST device
    #   26 LOAD_ATTR get_channel_count
    #   36 LOAD_FAST device
    #   38 LOAD_ATTR get_channel
    #   48 LOAD_CONST 3
    #   50 KW_NAMES
    #   52 PRECALL
    #   56 CALL
    #   66 GET_YIELD_FROM_ITER
    #   68 LOAD_CONST None
    #   70 SEND to 78
    #   72 YIELD_VALUE
    #   74 RESUME
    #   76 JUMP_BACKWARD_NO_INTERRUPT to 70
    #   78 POP_TOP
    #   80 LOAD_CONST None
    #   82 RETURN_VALUE
    pass

def get_channel_calibrations(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 MAKE_CELL supports_calibration
    #    4 RETURN_GENERATOR
    #    6 POP_TOP
    #    8 RESUME
    #   10 LOAD_CONST True
    #   12 STORE_DEREF supports_calibration
    #   14 LOAD_CONST 'i'
    #   16 LOAD_GLOBAL int
    #   28 LOAD_CONST 'return'
    #   30 LOAD_GLOBAL Optional
    #   42 LOAD_GLOBAL asphodel
    #   54 LOAD_ATTR ChannelCalibration
    #   64 BINARY_SUBSCR
    #   74 BUILD_TUPLE
    #   76 LOAD_CLOSURE device
    #   78 LOAD_CLOSURE supports_calibration
    #   80 BUILD_TUPLE
    #   82 LOAD_CONST <code object element_fn at 0x100acfcb0, file "asphodel\device_info.py", line 288>
    #   84 MAKE_FUNCTION annotations, closure
    #   86 STORE_FAST element_fn
    #   88 LOAD_GLOBAL NULL + array_call
    #  100 LOAD_CONST 'channel_calibration'
    #  102 LOAD_FAST device_info
    #  104 LOAD_FAST incrementer
    #  106 LOAD_CONST None
    #  108 LOAD_CONST 'channels'
    #  110 LOAD_FAST element_fn
    #  112 LOAD_CONST 1
    #  114 KW_NAMES
    #  116 PRECALL
    #  120 CALL
    #  130 GET_YIELD_FROM_ITER
    #  132 LOAD_CONST None
    #  134 SEND to 142
    #  136 YIELD_VALUE
    #  138 RESUME
    #  140 JUMP_BACKWARD_NO_INTERRUPT to 134
    #  142 POP_TOP
    #  144 LOAD_CONST None
    #  146 RETURN_VALUE
    pass

def get_supplies(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 RETURN_GENERATOR
    #    4 POP_TOP
    #    6 RESUME
    #    8 LOAD_CONST 'i'
    #   10 LOAD_GLOBAL int
    #   22 LOAD_CONST 'return'
    #   24 LOAD_GLOBAL tuple
    #   36 LOAD_GLOBAL str
    #   48 LOAD_GLOBAL asphodel
    #   60 LOAD_ATTR SupplyInfo
    #   70 BUILD_TUPLE
    #   72 BINARY_SUBSCR
    #   82 BUILD_TUPLE
    #   84 LOAD_CLOSURE device
    #   86 BUILD_TUPLE
    #   88 LOAD_CONST <code object element_fn at 0x105a73870, file "asphodel\device_info.py", line 309>
    #   90 MAKE_FUNCTION annotations, closure
    #   92 STORE_FAST element_fn
    #   94 LOAD_GLOBAL NULL + array_call
    #  106 LOAD_CONST 'supplies'
    #  108 LOAD_FAST device_info
    #  110 LOAD_FAST incrementer
    #  112 LOAD_DEREF device
    #  114 LOAD_ATTR get_supply_count
    #  124 LOAD_FAST element_fn
    #  126 LOAD_CONST 2
    #  128 KW_NAMES
    #  130 PRECALL
    #  134 CALL
    #  144 GET_YIELD_FROM_ITER
    #  146 LOAD_CONST None
    #  148 SEND to 156
    #  150 YIELD_VALUE
    #  152 RESUME
    #  154 JUMP_BACKWARD_NO_INTERRUPT to 148
    #  156 POP_TOP
    #  158 LOAD_CONST None
    #  160 RETURN_VALUE
    pass

def get_supply_results(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 RETURN_GENERATOR
    #    4 POP_TOP
    #    6 RESUME
    #    8 LOAD_CONST 'i'
    #   10 LOAD_GLOBAL int
    #   22 LOAD_CONST 'return'
    #   24 LOAD_GLOBAL Optional
    #   36 LOAD_GLOBAL tuple
    #   48 LOAD_GLOBAL int
    #   60 LOAD_GLOBAL int
    #   72 BUILD_TUPLE
    #   74 BINARY_SUBSCR
    #   84 BINARY_SUBSCR
    #   94 BUILD_TUPLE
    #   96 LOAD_CLOSURE device
    #   98 BUILD_TUPLE
    #  100 LOAD_CONST <code object element_fn at 0x105a733f0, file "asphodel\device_info.py", line 322>
    #  102 MAKE_FUNCTION annotations, closure
    #  104 STORE_FAST element_fn
    #  106 LOAD_GLOBAL NULL + array_call
    #  118 LOAD_CONST 'supply_results'
    #  120 LOAD_FAST device_info
    #  122 LOAD_FAST incrementer
    #  124 LOAD_CONST None
    #  126 LOAD_CONST 'supplies'
    #  128 LOAD_FAST element_fn
    #  130 LOAD_CONST False
    #  132 KW_NAMES
    #  134 PRECALL
    #  138 CALL
    #  148 GET_YIELD_FROM_ITER
    #  150 LOAD_CONST None
    #  152 SEND to 160
    #  154 YIELD_VALUE
    #  156 RESUME
    #  158 JUMP_BACKWARD_NO_INTERRUPT to 152
    #  160 POP_TOP
    #  162 LOAD_CONST None
    #  164 RETURN_VALUE
    pass

def get_ctrl_vars(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL device
    #    2 RETURN_GENERATOR
    #    4 POP_TOP
    #    6 RESUME
    #    8 LOAD_CONST 'i'
    #   10 LOAD_GLOBAL int
    #   22 LOAD_CONST 'return'
    #   24 LOAD_GLOBAL tuple
    #   36 LOAD_GLOBAL str
    #   48 LOAD_GLOBAL asphodel
    #   60 LOAD_ATTR CtrlVarInfo
    #   70 LOAD_CONST None
    #   72 BUILD_TUPLE
    #   74 BINARY_SUBSCR
    #   84 BUILD_TUPLE
    #   86 LOAD_CLOSURE device
    #   88 BUILD_TUPLE
    #   90 LOAD_CONST <code object element_fn at 0x105a73ab0, file "asphodel\device_info.py", line 336>
    #   92 MAKE_FUNCTION annotations, closure
    #   94 STORE_FAST element_fn
    #   96 LOAD_GLOBAL NULL + array_call
    #  108 LOAD_CONST 'ctrl_vars'
    #  110 LOAD_FAST device_info
    #  112 LOAD_FAST incrementer
    #  114 LOAD_DEREF device
    #  116 LOAD_ATTR get_ctrl_var_count
    #  126 LOAD_FAST element_fn
    #  128 LOAD_CONST 2
    #  130 KW_NAMES
    #  132 PRECALL
    #  136 CALL
    #  146 GET_YIELD_FROM_ITER
    #  148 LOAD_CONST None
    #  150 SEND to 158
    #  152 YIELD_VALUE
    #  154 RESUME
    #  156 JUMP_BACKWARD_NO_INTERRUPT to 150
    #  158 POP_TOP
    #  160 LOAD_CONST None
    #  162 RETURN_VALUE
    pass

def get_ctrl_var_settings(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_GLOBAL NULL + len
    #   18 LOAD_FAST device_info
    #   20 LOAD_CONST 'ctrl_vars'
    #   22 BINARY_SUBSCR
    #   32 PRECALL
    #   36 CALL
    #   46 STORE_FAST ctrl_var_count
    #   48 LOAD_CONST 0
    #   50 LOAD_FAST ctrl_var_count
    #   52 BUILD_MAP
    #   54 BUILD_TUPLE
    #   56 YIELD_VALUE
    #   58 RESUME
    #   60 POP_TOP
    #   62 LOAD_FAST device_info
    #   64 LOAD_CONST 'ctrl_vars'
    #   66 BINARY_SUBSCR
    #   76 STORE_FAST old_ctrl_vars
    #   78 BUILD_LIST
    #   80 STORE_FAST new_ctrl_vars
    #   82 LOAD_GLOBAL NULL + enumerate
    #   94 LOAD_FAST old_ctrl_vars
    #   96 PRECALL
    #  100 CALL
    #  110 GET_ITER
    #  112 FOR_ITER to 266
    #  114 UNPACK_SEQUENCE
    #  118 STORE_FAST i
    #  120 UNPACK_SEQUENCE
    #  124 STORE_FAST name
    #  126 STORE_FAST info
    #  128 STORE_FAST _old_setting
    #  130 LOAD_FAST device
    #  132 LOAD_METHOD get_ctrl_var
    #  154 LOAD_FAST i
    #  156 PRECALL
    #  160 CALL
    #  170 STORE_FAST new_setting
    #  172 LOAD_FAST new_ctrl_vars
    #  174 LOAD_METHOD append
    #  196 LOAD_FAST name
    #  198 LOAD_FAST info
    #  200 LOAD_FAST new_setting
    #  202 BUILD_TUPLE
    #  204 PRECALL
    #  208 CALL
    #  218 POP_TOP
    #  220 LOAD_FAST incrementer
    #  222 LOAD_METHOD increment
    #  244 LOAD_CONST 1
    #  246 LOAD_CONST 'ctrl_var_settings'
    #  248 PRECALL
    #  252 CALL
    #  262 POP_TOP
    #  264 JUMP_BACKWARD to 112
    #  266 LOAD_CONST 'ctrl_vars'
    #  268 LOAD_FAST new_ctrl_vars
    #  270 BUILD_MAP
    #  272 YIELD_VALUE
    #  274 RESUME
    #  276 POP_TOP
    #  278 LOAD_CONST None
    #  280 RETURN_VALUE
    pass

def get_settings(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_GLOBAL NULL + array_call
    #   18 LOAD_CONST 'settings'
    #   20 LOAD_FAST device_info
    #   22 LOAD_FAST incrementer
    #   24 LOAD_FAST device
    #   26 LOAD_ATTR get_setting_count
    #   36 LOAD_FAST device
    #   38 LOAD_ATTR get_setting
    #   48 LOAD_CONST 3
    #   50 KW_NAMES
    #   52 PRECALL
    #   56 CALL
    #   66 GET_YIELD_FROM_ITER
    #   68 LOAD_CONST None
    #   70 SEND to 78
    #   72 YIELD_VALUE
    #   74 RESUME
    #   76 JUMP_BACKWARD_NO_INTERRUPT to 70
    #   78 POP_TOP
    #   80 LOAD_CONST None
    #   82 RETURN_VALUE
    pass

def get_nvm(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL nvm_bytes
    #    2 RETURN_GENERATOR
    #    4 POP_TOP
    #    6 RESUME
    #    8 LOAD_CONST 'nvm'
    #   10 LOAD_FAST device_info
    #   12 CONTAINS_OP
    #   14 POP_JUMP_FORWARD_IF_FALSE to 20
    #   16 LOAD_CONST None
    #   18 RETURN_VALUE
    #   20 LOAD_FAST device
    #   22 LOAD_METHOD get_nvm_size
    #   44 PRECALL
    #   48 CALL
    #   58 STORE_FAST nvm_size
    #   60 LOAD_FAST device
    #   62 LOAD_METHOD get_max_incoming_param_length
    #   84 PRECALL
    #   88 CALL
    #   98 LOAD_CONST 4
    #  100 BINARY_OP //
    #  104 LOAD_CONST 4
    #  106 BINARY_OP *
    #  110 STORE_FAST nvm_bpc
    #  112 LOAD_GLOBAL NULL + math
    #  124 LOAD_ATTR ceil
    #  134 LOAD_FAST nvm_size
    #  136 LOAD_FAST nvm_bpc
    #  138 BINARY_OP /
    #  142 PRECALL
    #  146 CALL
    #  156 STORE_FAST nvm_commands
    #  158 LOAD_CONST 1
    #  160 LOAD_CONST 1
    #  162 LOAD_FAST nvm_commands
    #  164 BINARY_OP +
    #  168 BUILD_MAP
    #  170 BUILD_TUPLE
    #  172 YIELD_VALUE
    #  174 RESUME
    #  176 POP_TOP
    #  178 LOAD_FAST device
    #  180 LOAD_METHOD read_nvm_section
    #  202 LOAD_CONST 0
    #  204 LOAD_FAST nvm_size
    #  206 PRECALL
    #  210 CALL
    #  220 STORE_DEREF nvm_bytes
    #  222 LOAD_FAST incrementer
    #  224 LOAD_METHOD increment
    #  246 LOAD_FAST nvm_commands
    #  248 LOAD_CONST 'nvm'
    #  250 PRECALL
    #  254 CALL
    #  264 POP_TOP
    #  266 LOAD_FAST device
    #  268 LOAD_METHOD get_user_tag_locations
    #  290 PRECALL
    #  294 CALL
    #  304 STORE_FAST tag_locations
    #  306 LOAD_FAST incrementer
    #  308 LOAD_METHOD increment
    #  330 LOAD_CONST 1
    #  332 LOAD_CONST 'tag_locations'
    #  334 PRECALL
    #  338 CALL
    #  348 POP_TOP
    #  350 LOAD_CONST 'offset'
    #  352 LOAD_GLOBAL int
    #  364 LOAD_CONST 'length'
    #  366 LOAD_GLOBAL int
    #  378 LOAD_CONST 'return'
    #  380 LOAD_GLOBAL Optional
    #  392 LOAD_GLOBAL str
    #  404 BINARY_SUBSCR
    #  414 BUILD_TUPLE
    #  416 LOAD_CLOSURE nvm_bytes
    #  418 BUILD_TUPLE
    #  420 LOAD_CONST <code object read_user_tag_string at 0x105acd920, file "asphodel\device_info.py", line 387>
    #  422 MAKE_FUNCTION annotations, closure
    # ... bytecode truncated ...
    pass

def get_nvm_active_scan(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_FAST device_info
    #    8 LOAD_CONST 'nvm_hash'
    #   10 BINARY_SUBSCR
    #   20 POP_JUMP_FORWARD_IF_FALSE to 72
    #   22 LOAD_GLOBAL NULL + get_nvm
    #   34 LOAD_FAST device
    #   36 LOAD_FAST device_info
    #   38 LOAD_FAST incrementer
    #   40 PRECALL
    #   44 CALL
    #   54 GET_YIELD_FROM_ITER
    #   56 LOAD_CONST None
    #   58 SEND to 66
    #   60 YIELD_VALUE
    #   62 RESUME
    #   64 JUMP_BACKWARD_NO_INTERRUPT to 58
    #   66 POP_TOP
    #   68 LOAD_CONST None
    #   70 RETURN_VALUE
    #   72 LOAD_CONST 0
    #   74 LOAD_CONST 3
    #   76 BUILD_MAP
    #   78 BUILD_TUPLE
    #   80 YIELD_VALUE
    #   82 RESUME
    #   84 POP_TOP
    #   86 LOAD_FAST device
    #   88 LOAD_METHOD get_user_tag_locations
    #  110 PRECALL
    #  114 CALL
    #  124 STORE_FAST tag_locations
    #  126 LOAD_FAST incrementer
    #  128 LOAD_METHOD increment
    #  150 LOAD_CONST 1
    #  152 LOAD_CONST 'tag_locations'
    #  154 PRECALL
    #  158 CALL
    #  168 POP_TOP
    #  170 NOP
    #  172 PUSH_NULL
    #  174 LOAD_FAST device
    #  176 LOAD_ATTR read_user_tag_string
    #  186 LOAD_FAST tag_locations
    #  188 LOAD_CONST 0
    #  190 BINARY_SUBSCR
    #  200 CALL_FUNCTION_EX
    #  202 STORE_FAST t1
    #  204 JUMP_FORWARD to 242
    #  206 PUSH_EXC_INFO
    #  208 LOAD_GLOBAL UnicodeDecodeError
    #  220 CHECK_EXC_MATCH
    #  222 POP_JUMP_FORWARD_IF_FALSE to 234
    #  224 POP_TOP
    #  226 LOAD_CONST None
    #  228 STORE_FAST t1
    #  230 POP_EXCEPT
    #  232 JUMP_FORWARD to 242
    #  234 RERAISE
    #  236 COPY
    #  238 POP_EXCEPT
    #  240 RERAISE
    #  242 LOAD_FAST incrementer
    #  244 LOAD_METHOD increment
    #  266 LOAD_CONST 1
    #  268 LOAD_CONST 'user_tag_1'
    #  270 PRECALL
    #  274 CALL
    #  284 POP_TOP
    #  286 NOP
    #  288 PUSH_NULL
    #  290 LOAD_FAST device
    #  292 LOAD_ATTR read_user_tag_string
    #  302 LOAD_FAST tag_locations
    #  304 LOAD_CONST 1
    #  306 BINARY_SUBSCR
    #  316 CALL_FUNCTION_EX
    #  318 STORE_FAST t2
    # ... bytecode truncated ...
    pass

def get_led_settings(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_GLOBAL NULL + array_call
    #   18 LOAD_CONST 'led_settings'
    #   20 LOAD_FAST device_info
    #   22 LOAD_FAST incrementer
    #   24 LOAD_FAST device
    #   26 LOAD_ATTR get_led_count
    #   36 LOAD_FAST device
    #   38 LOAD_ATTR get_led_value
    #   48 LOAD_CONST False
    #   50 KW_NAMES
    #   52 PRECALL
    #   56 CALL
    #   66 GET_YIELD_FROM_ITER
    #   68 LOAD_CONST None
    #   70 SEND to 78
    #   72 YIELD_VALUE
    #   74 RESUME
    #   76 JUMP_BACKWARD_NO_INTERRUPT to 70
    #   78 POP_TOP
    #   80 LOAD_CONST None
    #   82 RETURN_VALUE
    pass

def get_rgb_settings(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_GLOBAL NULL + array_call
    #   18 LOAD_CONST 'rgb_settings'
    #   20 LOAD_FAST device_info
    #   22 LOAD_FAST incrementer
    #   24 LOAD_FAST device
    #   26 LOAD_ATTR get_rgb_count
    #   36 LOAD_FAST device
    #   38 LOAD_ATTR get_rgb_values
    #   48 LOAD_CONST False
    #   50 KW_NAMES
    #   52 PRECALL
    #   56 CALL
    #   66 GET_YIELD_FROM_ITER
    #   68 LOAD_CONST None
    #   70 SEND to 78
    #   72 YIELD_VALUE
    #   74 RESUME
    #   76 JUMP_BACKWARD_NO_INTERRUPT to 70
    #   78 POP_TOP
    #   80 LOAD_CONST None
    #   82 RETURN_VALUE
    pass

def get_rf_power_status(device, _device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_FAST device
    #    8 LOAD_METHOD supports_rf_power_commands
    #   30 PRECALL
    #   34 CALL
    #   44 POP_JUMP_FORWARD_IF_TRUE to 50
    #   46 LOAD_CONST None
    #   48 RETURN_VALUE
    #   50 LOAD_CONST 0
    #   52 LOAD_CONST 1
    #   54 BUILD_MAP
    #   56 BUILD_TUPLE
    #   58 YIELD_VALUE
    #   60 RESUME
    #   62 POP_TOP
    #   64 LOAD_FAST device
    #   66 LOAD_METHOD get_rf_power_status
    #   88 PRECALL
    #   92 CALL
    #  102 STORE_FAST rf_power_status
    #  104 LOAD_FAST incrementer
    #  106 LOAD_METHOD increment
    #  128 LOAD_CONST 1
    #  130 LOAD_CONST 'rf_power_status'
    #  132 PRECALL
    #  136 CALL
    #  146 POP_TOP
    #  148 LOAD_CONST 'rf_power_status'
    #  150 LOAD_FAST rf_power_status
    #  152 BUILD_MAP
    #  154 YIELD_VALUE
    #  156 RESUME
    #  158 POP_TOP
    #  160 LOAD_CONST None
    #  162 RETURN_VALUE
    pass

def get_rf_power_ctrl_vars(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'rf_power_ctrl_vars'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 18
    #   14 LOAD_CONST None
    #   16 RETURN_VALUE
    #   18 LOAD_FAST device
    #   20 LOAD_METHOD supports_rf_power_commands
    #   42 PRECALL
    #   46 CALL
    #   56 POP_JUMP_FORWARD_IF_TRUE to 62
    #   58 LOAD_CONST None
    #   60 RETURN_VALUE
    #   62 LOAD_CONST 0
    #   64 LOAD_CONST 1
    #   66 BUILD_MAP
    #   68 BUILD_TUPLE
    #   70 YIELD_VALUE
    #   72 RESUME
    #   74 POP_TOP
    #   76 LOAD_FAST device
    #   78 LOAD_METHOD get_rf_power_ctrl_vars
    #  100 PRECALL
    #  104 CALL
    #  114 STORE_FAST rf_power_ctrl_vars
    #  116 LOAD_FAST incrementer
    #  118 LOAD_METHOD increment
    #  140 LOAD_CONST 1
    #  142 LOAD_CONST 'rf_power_ctrl_vars'
    #  144 PRECALL
    #  148 CALL
    #  158 POP_TOP
    #  160 LOAD_CONST 'rf_power_ctrl_vars'
    #  162 LOAD_FAST rf_power_ctrl_vars
    #  164 BUILD_MAP
    #  166 YIELD_VALUE
    #  168 RESUME
    #  170 POP_TOP
    #  172 LOAD_CONST None
    #  174 RETURN_VALUE
    pass

def get_radio_ctrl_vars(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'radio_ctrl_vars'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 18
    #   14 LOAD_CONST None
    #   16 RETURN_VALUE
    #   18 LOAD_FAST device
    #   20 LOAD_METHOD supports_radio_commands
    #   42 PRECALL
    #   46 CALL
    #   56 POP_JUMP_FORWARD_IF_TRUE to 62
    #   58 LOAD_CONST None
    #   60 RETURN_VALUE
    #   62 LOAD_CONST 0
    #   64 LOAD_CONST 1
    #   66 BUILD_MAP
    #   68 BUILD_TUPLE
    #   70 YIELD_VALUE
    #   72 RESUME
    #   74 POP_TOP
    #   76 LOAD_FAST device
    #   78 LOAD_METHOD get_radio_ctrl_vars
    #  100 PRECALL
    #  104 CALL
    #  114 STORE_FAST radio_ctrl_vars
    #  116 LOAD_FAST incrementer
    #  118 LOAD_METHOD increment
    #  140 LOAD_CONST 1
    #  142 LOAD_CONST 'radio_ctrl_vars'
    #  144 PRECALL
    #  148 CALL
    #  158 POP_TOP
    #  160 LOAD_CONST 'radio_ctrl_vars'
    #  162 LOAD_FAST radio_ctrl_vars
    #  164 BUILD_MAP
    #  166 YIELD_VALUE
    #  168 RESUME
    #  170 POP_TOP
    #  172 LOAD_CONST None
    #  174 RETURN_VALUE
    pass

def get_radio_scan_power(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'radio_scan_power'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 18
    #   14 LOAD_CONST None
    #   16 RETURN_VALUE
    #   18 LOAD_FAST device
    #   20 LOAD_METHOD supports_radio_commands
    #   42 PRECALL
    #   46 CALL
    #   56 POP_JUMP_FORWARD_IF_TRUE to 62
    #   58 LOAD_CONST None
    #   60 RETURN_VALUE
    #   62 LOAD_CONST 0
    #   64 LOAD_CONST 1
    #   66 BUILD_MAP
    #   68 BUILD_TUPLE
    #   70 YIELD_VALUE
    #   72 RESUME
    #   74 POP_TOP
    #   76 NOP
    #   78 LOAD_FAST device
    #   80 LOAD_METHOD get_radio_scan_power
    #  102 LOAD_CONST 0
    #  104 BUILD_LIST
    #  106 PRECALL
    #  110 CALL
    #  120 POP_TOP
    #  122 LOAD_CONST True
    #  124 STORE_FAST radio_scan_power
    #  126 JUMP_FORWARD to 164
    #  128 PUSH_EXC_INFO
    #  130 LOAD_GLOBAL Exception
    #  142 CHECK_EXC_MATCH
    #  144 POP_JUMP_FORWARD_IF_FALSE to 156
    #  146 POP_TOP
    #  148 LOAD_CONST False
    #  150 STORE_FAST radio_scan_power
    #  152 POP_EXCEPT
    #  154 JUMP_FORWARD to 164
    #  156 RERAISE
    #  158 COPY
    #  160 POP_EXCEPT
    #  162 RERAISE
    #  164 LOAD_FAST incrementer
    #  166 LOAD_METHOD increment
    #  188 LOAD_CONST 1
    #  190 LOAD_CONST 'radio_scan_power'
    #  192 PRECALL
    #  196 CALL
    #  206 POP_TOP
    #  208 LOAD_CONST 'radio_scan_power'
    #  210 LOAD_FAST radio_scan_power
    #  212 BUILD_MAP
    #  214 YIELD_VALUE
    #  216 RESUME
    #  218 POP_TOP
    #  220 LOAD_CONST None
    #  222 RETURN_VALUE
    pass

def get_radio_default_serial(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'radio_default_serial'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 18
    #   14 LOAD_CONST None
    #   16 RETURN_VALUE
    #   18 LOAD_FAST device
    #   20 LOAD_METHOD supports_radio_commands
    #   42 PRECALL
    #   46 CALL
    #   56 POP_JUMP_FORWARD_IF_TRUE to 62
    #   58 LOAD_CONST None
    #   60 RETURN_VALUE
    #   62 LOAD_CONST 0
    #   64 LOAD_CONST 1
    #   66 BUILD_MAP
    #   68 BUILD_TUPLE
    #   70 YIELD_VALUE
    #   72 RESUME
    #   74 POP_TOP
    #   76 LOAD_FAST device
    #   78 LOAD_METHOD get_radio_default_serial
    #  100 PRECALL
    #  104 CALL
    #  114 STORE_FAST radio_default_serial
    #  116 LOAD_FAST incrementer
    #  118 LOAD_METHOD increment
    #  140 LOAD_CONST 1
    #  142 LOAD_CONST 'radio_default_serial'
    #  144 PRECALL
    #  148 CALL
    #  158 POP_TOP
    #  160 LOAD_CONST 'radio_default_serial'
    #  162 LOAD_FAST radio_default_serial
    #  164 BUILD_MAP
    #  166 YIELD_VALUE
    #  168 RESUME
    #  170 POP_TOP
    #  172 LOAD_CONST None
    #  174 RETURN_VALUE
    pass

def get_device_mode(device, device_info, incrementer):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RETURN_GENERATOR
    #    2 POP_TOP
    #    4 RESUME
    #    6 LOAD_CONST 'supports_device_mode'
    #    8 LOAD_FAST device_info
    #   10 CONTAINS_OP
    #   12 POP_JUMP_FORWARD_IF_FALSE to 34
    #   14 LOAD_FAST device_info
    #   16 LOAD_CONST 'supports_device_mode'
    #   18 BINARY_SUBSCR
    #   28 POP_JUMP_FORWARD_IF_TRUE to 34
    #   30 LOAD_CONST None
    #   32 RETURN_VALUE
    #   34 LOAD_CONST 0
    #   36 LOAD_CONST 1
    #   38 BUILD_MAP
    #   40 BUILD_TUPLE
    #   42 YIELD_VALUE
    #   44 RESUME
    #   46 POP_TOP
    #   48 NOP
    #   50 LOAD_FAST device
    #   52 LOAD_METHOD get_device_mode
    #   74 PRECALL
    #   78 CALL
    #   88 STORE_FAST device_mode
    #   90 LOAD_FAST device_mode
    #   92 LOAD_CONST True
    #   94 LOAD_CONST ('device_mode', 'supports_device_mode')
    #   96 BUILD_CONST_KEY_MAP
    #   98 STORE_FAST d
    #  100 JUMP_FORWARD to 204
    #  102 PUSH_EXC_INFO
    #  104 LOAD_GLOBAL asphodel
    #  116 LOAD_ATTR AsphodelError
    #  126 CHECK_EXC_MATCH
    #  128 POP_JUMP_FORWARD_IF_FALSE to 196
    #  130 STORE_FAST e
    #  132 LOAD_FAST e
    #  134 LOAD_ATTR args
    #  144 LOAD_CONST 1
    #  146 BINARY_SUBSCR
    #  156 LOAD_CONST 'ERROR_CODE_UNIMPLEMENTED_COMMAND'
    #  158 COMPARE_OP ==
    #  164 POP_JUMP_FORWARD_IF_FALSE to 176
    #  166 LOAD_CONST 'supports_device_mode'
    #  168 LOAD_CONST False
    #  170 BUILD_MAP
    #  172 STORE_FAST d
    #  174 JUMP_FORWARD to 178
    #  176 RAISE_VARARGS
    #  178 POP_EXCEPT
    #  180 LOAD_CONST None
    #  182 STORE_FAST e
    #  184 DELETE_FAST e
    #  186 JUMP_FORWARD to 204
    #  188 LOAD_CONST None
    #  190 STORE_FAST e
    #  192 DELETE_FAST e
    #  194 RERAISE
    #  196 RERAISE
    #  198 COPY
    #  200 POP_EXCEPT
    #  202 RERAISE
    #  204 LOAD_FAST incrementer
    #  206 LOAD_METHOD increment
    #  228 LOAD_CONST 1
    #  230 LOAD_CONST 'device_mode'
    #  232 PRECALL
    #  236 CALL
    #  246 POP_TOP
    #  248 LOAD_FAST d
    #  250 YIELD_VALUE
    #  252 RESUME
    #  254 POP_TOP
    #  256 LOAD_CONST None
    #  258 RETURN_VALUE
    pass

def hash_is_valid(h):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_FAST h
    #    4 POP_JUMP_FORWARD_IF_TRUE to 10
    #    6 LOAD_CONST False
    #    8 RETURN_VALUE
    #   10 LOAD_FAST h
    #   12 LOAD_METHOD lower
    #   34 PRECALL
    #   38 CALL
    #   48 STORE_FAST lowercase_string
    #   50 LOAD_GLOBAL NULL + all
    #   62 LOAD_CONST <code object <genexpr> at 0x105af9ed0, file "asphodel\device_info.py", line 543>
    #   64 MAKE_FUNCTION
    #   66 LOAD_FAST lowercase_string
    #   68 GET_ITER
    #   70 PRECALL
    #   74 CALL
    #   84 PRECALL
    #   88 CALL
    #   98 POP_JUMP_FORWARD_IF_FALSE to 104
    #  100 LOAD_CONST False
    #  102 RETURN_VALUE
    #  104 LOAD_GLOBAL NULL + all
    #  116 LOAD_CONST <code object <genexpr> at 0x105af91b0, file "asphodel\device_info.py", line 545>
    #  118 MAKE_FUNCTION
    #  120 LOAD_FAST lowercase_string
    #  122 GET_ITER
    #  124 PRECALL
    #  128 CALL
    #  138 PRECALL
    #  142 CALL
    #  152 POP_JUMP_FORWARD_IF_FALSE to 158
    #  154 LOAD_CONST False
    #  156 RETURN_VALUE
    #  158 LOAD_CONST True
    #  160 RETURN_VALUE
    pass

def get_device_info_dict(device, device_logger, allow_reconnect, diskcache, progress_callback, setting_getters, nvm_getters):
    incrementer = Incrementer(progress_callback, device_logger)
    serial_number = device.get_serial_number()
    if not serial_number:
        raise asphodel.AsphodelError('No serial number when fetching device info')
    protocol_type = device.device.protocol_type
    build_info = device.get_build_info()
    build_date = device.get_build_date()
    nvm_hash = try_optional(device.get_nvm_hash)
    nvm_modified = try_optional(device.get_nvm_modified)
    setting_hash = try_optional(device.get_setting_hash)
    finished_commands = 4
    total_commands = 4
    board_info_key = None
    if device.supports_remote_commands():
        (connected, remote_serial_number, _protocol) = device.get_remote_status()
        if connected:
            board_info_key = remote_serial_number
    setting_key = (serial_number, protocol_type, build_info, build_date, setting_hash)
    if not hash_is_valid(setting_hash) and allow_reconnect:
        setting_info = { }

def get_active_scan_info(remote, device_logger, diskcache):
    device_info_dict = get_device_info_dict(remote, device_logger, False, diskcache, None, active_scan_setting_getters, [
        get_nvm_active_scan])
    if 'nvm' not in device_info_dict:
        device_info_dict['nvm'] = None
    return ActiveScanInfo.from_dict(device_info_dict)

def get_device_info(device, allow_reconnect, device_logger, diskcache, progress_callback):
    device_info_dict = get_device_info_dict(device, device_logger, allow_reconnect, diskcache, progress_callback, default_setting_getters, [
        get_nvm])

def get_remote_board_info(serial_number, diskcache):
    return diskcache.get(serial_number, default = None)
