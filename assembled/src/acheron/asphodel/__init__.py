# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import ast
import binascii
from collections import namedtuple
from ctypes import addressof, byref, c_char_p, c_double, c_float, c_int, c_int8, c_int16, c_int32, c_uint, c_uint8, c_uint16, c_uint32, c_uint64, c_size_t, c_void_p, cast, cdll, CFUNCTYPE, create_string_buffer, POINTER, pointer, Structure, Union
from ctypes.util import find_library
import functools
import os
import string
import sys
import time
import threading
from typing import Optional
import weakref

try:
    from version import version as __version__
except ImportError:
    __version__ = 'UNKNOWN'

ASPHODEL_PROTOCOL_TYPE_BASIC = 0
ASPHODEL_PROTOCOL_TYPE_RF_POWER = 1
ASPHODEL_PROTOCOL_TYPE_RADIO = 2
ASPHODEL_PROTOCOL_TYPE_REMOTE = 4
ASPHODEL_PROTOCOL_TYPE_BOOTLOADER = 8
GPIO_PIN_MODE_HI_Z = 0
GPIO_PIN_MODE_PULL_DOWN = 1
GPIO_PIN_MODE_PULL_UP = 2
GPIO_PIN_MODE_LOW = 3
GPIO_PIN_MODE_HIGH = 4
SPI_CS_MODE_LOW = 0
SPI_CS_MODE_HIGH = 1
SPI_CS_MODE_AUTO_TRANSFER = 2
SPI_CS_MODE_AUTO_BYTE = 3
ASPHODEL_SUPPLY_LOW_BATTERY = 1
ASPHODEL_SUPPLY_TOO_LOW = 2
ASPHODEL_SUPPLY_TOO_HIGH = 4
ASPHODEL_TCP_FILTER_DEFAULT = 0
ASPHODEL_TCP_FILTER_PREFER_IPV6 = 0
ASPHODEL_TCP_FILTER_PREFER_IPV4 = 1
ASPHODEL_TCP_FILTER_ONLY_IPV6 = 2
ASPHODEL_TCP_FILTER_ONLY_IPV4 = 3
ASPHODEL_TCP_FILTER_RETURN_ALL = 4
ChannelInfo = namedtuple('ChannelInfo', [
    'channel_type',
    'unit_type',
    'filler_bits',
    'data_bits',
    'samples',
    'bits_per_sample',
    'minimum',
    'maximum',
    'resolution',
    'chunk_count'])
ChannelCalibration = namedtuple('ChannelCalibration', [
    'base_setting_index',
    'resolution_setting_index',
    'scale',
    'offset',
    'minimum',
    'maximum'])
SupplyInfo = namedtuple('SupplyInfo', [
    'unit_type',
    'is_battery',
    'nominal',
    'scale',
    'offset'])
CtrlVarInfo = namedtuple('CtrlVarInfo', [
    'unit_type',
    'minimum',
    'maximum',
    'scale',
    'offset'])
ExtraScanResult = namedtuple('ExtraScanResult', [
    'serial_number',
    'asphodel_type',
    'device_mode'])
GPIOPortInfo = namedtuple('GPIOPortInfo', [
    'input_pins',
    'output_pins',
    'floating_pins',
    'loaded_pins',
    'overridden_pins'])
BridgeValues = namedtuple('BridgeValues', [
    'pos_sense',
    'neg_sense',
    'nominal',
    'minimum',
    'maximum'])
SelfTestLimits = namedtuple('SelfTestLimits', [
    'x_min',
    'x_max',
    'y_min',
    'y_max',
    'z_min',
    'z_max'])
StreamRateInfo = namedtuple('StreamRateInfo', [
    'available',
    'channel_index',
    'invert',
    'scale',
    'offset'])
TCPAdvInfo = namedtuple('TCPAdvInfo', [
    'tcp_version',
    'connected',
    'max_incoming_param_length',
    'max_outgoing_param_length',
    'stream_packet_length',
    'protocol_type',
    'serial_number',
    'board_rev',
    'board_type',
    'build_info',
    'build_date',
    'user_tag1',
    'user_tag2',
    'remote_max_incoming_param_length',
    'remote_max_outgoing_param_length',
    'remote_stream_packet_length'])

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class AsphodelError(IOError):

    pass

class AsphodelStreamInfo(Structure):

    __reduce__ = object.__reduce__

    def __del__(self):
        try:
            self._free_func(self)
            return None
        except AttributeError:
            return None

    def __repr__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR channel_index_list
        #   14 LOAD_CONST None
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR channel_count
        #   28 BUILD_SLICE
        #   30 BINARY_SUBSCR
        #   40 STORE_FAST channel_index_list
        #   42 LOAD_CONST 'channel_index_list'
        #   44 LOAD_FAST channel_index_list
        #   46 BUILD_TUPLE
        #   48 LOAD_CONST 'channel_count'
        #   50 LOAD_FAST self
        #   52 LOAD_ATTR channel_count
        #   62 BUILD_TUPLE
        #   64 LOAD_CONST 'filler_bits'
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR filler_bits
        #   78 BUILD_TUPLE
        #   80 LOAD_CONST 'counter_bits'
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR counter_bits
        #   94 BUILD_TUPLE
        #   96 LOAD_CONST 'rate'
        #   98 LOAD_FAST self
        #  100 LOAD_ATTR rate
        #  110 BUILD_TUPLE
        #  112 LOAD_CONST 'rate_error'
        #  114 LOAD_FAST self
        #  116 LOAD_ATTR rate_error
        #  126 BUILD_TUPLE
        #  128 LOAD_CONST 'warm_up_delay'
        #  130 LOAD_FAST self
        #  132 LOAD_ATTR warm_up_delay
        #  142 BUILD_TUPLE
        #  144 BUILD_LIST
        #  146 STORE_FAST items
        #  148 LOAD_CONST ', '
        #  150 LOAD_METHOD join
        #  172 LOAD_CONST <code object <genexpr> at 0x105abff00, file "asphodel\__init__.py", line 123>
        #  174 MAKE_FUNCTION
        #  176 LOAD_FAST items
        #  178 GET_ITER
        #  180 PRECALL
        #  184 CALL
        #  194 PRECALL
        #  198 CALL
        #  208 STORE_FAST contents
        #  210 LOAD_CONST '<AsphodelStreamInfo {'
        #  212 LOAD_FAST contents
        #  214 BINARY_OP +
        #  218 LOAD_CONST '}>'
        #  220 BINARY_OP +
        #  224 RETURN_VALUE
        pass

    def __getstate__(self):
        return {
            '_channel_array': self.channel_index_list[:self.channel_count],
            'channel_count': self.channel_count,
            'filler_bits': self.filler_bits,
            'counter_bits': self.counter_bits,
            'rate': self.rate,
            'rate_error': self.rate_error,
            'warm_up_delay': self.warm_up_delay }

    def __setstate__(self, state):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST state
        #    4 LOAD_METHOD items
        #   26 PRECALL
        #   30 CALL
        #   40 GET_ITER
        #   42 FOR_ITER to 88
        #   44 UNPACK_SEQUENCE
        #   48 STORE_FAST k
        #   50 STORE_FAST v
        #   52 LOAD_GLOBAL NULL + setattr
        #   64 LOAD_FAST self
        #   66 LOAD_FAST k
        #   68 LOAD_FAST v
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 JUMP_BACKWARD to 42
        #   88 LOAD_GLOBAL c_uint8
        #  100 LOAD_GLOBAL NULL + len
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR _channel_array
        #  124 PRECALL
        #  128 CALL
        #  138 BINARY_OP *
        #  142 STORE_FAST channel_array_type
        #  144 PUSH_NULL
        #  146 LOAD_FAST channel_array_type
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR _channel_array
        #  160 CALL_FUNCTION_EX
        #  162 LOAD_FAST self
        #  164 STORE_ATTR _channel_array
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR _channel_array
        #  186 LOAD_FAST self
        #  188 STORE_ATTR channel_index_list
        #  198 LOAD_CONST None
        #  200 RETURN_VALUE
        pass

    def to_json_obj(self):
        return self.__getstate__()

    def from_json_obj(cls, obj):
        instance = cls.__new__(cls)
        instance.__setstate__(obj)
        return instance

class AsphodelChannelInfo(Structure):

    __reduce__ = object.__reduce__

    def __getattribute__(self, name):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __getattribute__
        #   52 LOAD_FAST name
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST value
        #   70 LOAD_FAST name
        #   72 LOAD_CONST 'name'
        #   74 COMPARE_OP ==
        #   80 POP_JUMP_FORWARD_IF_FALSE to 90
        #   82 LOAD_FAST value
        #   84 POP_JUMP_FORWARD_IF_NOT_NONE to 90
        #   86 LOAD_CONST b''
        #   88 RETURN_VALUE
        #   90 LOAD_FAST value
        #   92 RETURN_VALUE
        pass

    def __del__(self):
        try:
            self._free_func(self)
            return None
        except AttributeError:
            return None

    def __repr__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR channel_type
        #   14 LOAD_GLOBAL NULL + len
        #   26 LOAD_GLOBAL channel_type_names
        #   38 PRECALL
        #   42 CALL
        #   52 COMPARE_OP <
        #   58 POP_JUMP_FORWARD_IF_FALSE to 152
        #   60 LOAD_GLOBAL channel_type_names
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR channel_type
        #   84 BINARY_SUBSCR
        #   94 STORE_FAST s
        #   96 LOAD_CONST '{} ({})'
        #   98 LOAD_METHOD format
        #  120 LOAD_FAST self
        #  122 LOAD_ATTR channel_type
        #  132 LOAD_FAST s
        #  134 PRECALL
        #  138 CALL
        #  148 STORE_FAST channel_type_str
        #  150 JUMP_FORWARD to 204
        #  152 LOAD_CONST '{}'
        #  154 LOAD_METHOD format
        #  176 LOAD_FAST self
        #  178 LOAD_ATTR channel_type
        #  188 PRECALL
        #  192 CALL
        #  202 STORE_FAST channel_type_str
        #  204 LOAD_FAST self
        #  206 LOAD_ATTR unit_type
        #  216 LOAD_GLOBAL NULL + len
        #  228 LOAD_GLOBAL unit_type_names
        #  240 PRECALL
        #  244 CALL
        #  254 COMPARE_OP <
        #  260 POP_JUMP_FORWARD_IF_FALSE to 354
        #  262 LOAD_GLOBAL unit_type_names
        #  274 LOAD_FAST self
        #  276 LOAD_ATTR unit_type
        #  286 BINARY_SUBSCR
        #  296 STORE_FAST s
        #  298 LOAD_CONST '{} ({})'
        #  300 LOAD_METHOD format
        #  322 LOAD_FAST self
        #  324 LOAD_ATTR unit_type
        #  334 LOAD_FAST s
        #  336 PRECALL
        #  340 CALL
        #  350 STORE_FAST unit_type_str
        #  352 JUMP_FORWARD to 406
        #  354 LOAD_CONST '{}'
        #  356 LOAD_METHOD format
        #  378 LOAD_FAST self
        #  380 LOAD_ATTR unit_type
        #  390 PRECALL
        #  394 CALL
        #  404 STORE_FAST unit_type_str
        #  406 LOAD_FAST self
        #  408 LOAD_ATTR coefficients
        #  418 LOAD_CONST None
        #  420 LOAD_FAST self
        #  422 LOAD_ATTR coefficients_length
        #  432 BUILD_SLICE
        #  434 BINARY_SUBSCR
        #  444 STORE_FAST coefficients
        #  446 LOAD_FAST self
        #  448 LOAD_ATTR chunk_lengths
        #  458 LOAD_CONST None
        #  460 LOAD_FAST self
        #  462 LOAD_ATTR chunk_count
        #  472 BUILD_SLICE
        #  474 BINARY_SUBSCR
        #  484 STORE_FAST chunk_lengths
        #  486 BUILD_LIST
        #  488 STORE_FAST chunks
        #  490 LOAD_GLOBAL NULL + enumerate
        #  502 LOAD_FAST self
        #  504 LOAD_ATTR chunks
        # ... bytecode truncated ...
        pass

    def __getstate__(self):
        coefficients = self.coefficients[:self.coefficients_length]
        chunk_lengths = self.chunk_lengths[:self.chunk_count]
        chunks = []

    def __setstate__(self, state):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST state
        #    4 LOAD_METHOD items
        #   26 PRECALL
        #   30 CALL
        #   40 GET_ITER
        #   42 FOR_ITER to 88
        #   44 UNPACK_SEQUENCE
        #   48 STORE_FAST k
        #   50 STORE_FAST v
        #   52 LOAD_GLOBAL NULL + setattr
        #   64 LOAD_FAST self
        #   66 LOAD_FAST k
        #   68 LOAD_FAST v
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 JUMP_BACKWARD to 42
        #   88 LOAD_GLOBAL NULL + c_char_p
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR _name_array
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_FAST self
        #  128 STORE_ATTR _name_array
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR _name_array
        #  150 LOAD_FAST self
        #  152 STORE_ATTR name
        #  162 LOAD_GLOBAL c_float
        #  174 LOAD_GLOBAL NULL + len
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR _coefficients_array
        #  198 PRECALL
        #  202 CALL
        #  212 BINARY_OP *
        #  216 STORE_FAST cf_array_type
        #  218 PUSH_NULL
        #  220 LOAD_FAST cf_array_type
        #  222 LOAD_FAST self
        #  224 LOAD_ATTR _coefficients_array
        #  234 CALL_FUNCTION_EX
        #  236 LOAD_FAST self
        #  238 STORE_ATTR _coefficients_array
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR _coefficients_array
        #  260 LOAD_FAST self
        #  262 STORE_ATTR coefficients
        #  272 LOAD_CONST <code object <listcomp> at 0x105ab7b30, file "asphodel\__init__.py", line 262>
        #  274 MAKE_FUNCTION
        #  276 LOAD_FAST self
        #  278 LOAD_ATTR _chunk_list
        #  288 GET_ITER
        #  290 PRECALL
        #  294 CALL
        #  304 LOAD_FAST self
        #  306 STORE_ATTR _chunk_list
        #  316 LOAD_GLOBAL c_uint8
        #  328 LOAD_FAST self
        #  330 LOAD_ATTR chunk_count
        #  340 BINARY_OP *
        #  344 STORE_FAST cl_array_type
        #  346 PUSH_NULL
        #  348 LOAD_FAST cl_array_type
        #  350 LOAD_FAST self
        #  352 LOAD_ATTR _chunk_length_array
        #  362 CALL_FUNCTION_EX
        #  364 LOAD_FAST self
        #  366 STORE_ATTR _chunk_length_array
        #  376 LOAD_FAST self
        #  378 LOAD_ATTR _chunk_length_array
        #  388 LOAD_FAST self
        #  390 STORE_ATTR chunk_lengths
        #  400 LOAD_GLOBAL NULL + POINTER
        #  412 LOAD_GLOBAL c_uint8
        #  424 PRECALL
        #  428 CALL
        #  438 LOAD_FAST self
        #  440 LOAD_ATTR chunk_count
        #  450 BINARY_OP *
        # ... bytecode truncated ...
        pass

    def to_json_obj(self):
        def to_hex(b):
            return binascii.b2a_hex(b).decode('ascii')

        d = self.__getstate__()
        d['_name_array'] = to_hex(d['_name_array'])
        return d

    def from_json_obj(cls, obj):
        def from_hex(h):
            return binascii.a2b_hex(h)

        d = obj.copy()
        d['_name_array'] = from_hex(d['_name_array'])
        instance = cls.__new__(cls)
        instance.__setstate__(d)
        return instance

class SettingStructure(Structure):

    def __repr__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_CLOSURE self
        #    6 BUILD_TUPLE
        #    8 LOAD_CONST <code object <listcomp> at 0x105b40cf0, file "asphodel\__init__.py", line 297>
        #   10 MAKE_FUNCTION closure
        #   12 LOAD_DEREF self
        #   14 LOAD_ATTR _fields_
        #   24 GET_ITER
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST items
        #   42 LOAD_GLOBAL NULL + enumerate
        #   54 LOAD_FAST items
        #   56 PRECALL
        #   60 CALL
        #   70 GET_ITER
        #   72 FOR_ITER to 244
        #   74 UNPACK_SEQUENCE
        #   78 STORE_FAST i
        #   80 UNPACK_SEQUENCE
        #   84 STORE_FAST name
        #   86 STORE_FAST value
        #   88 LOAD_FAST name
        #   90 LOAD_CONST 'unit_type'
        #   92 COMPARE_OP ==
        #   98 POP_JUMP_FORWARD_IF_FALSE to 242
        #  100 LOAD_FAST value
        #  102 LOAD_GLOBAL NULL + len
        #  114 LOAD_GLOBAL unit_type_names
        #  126 PRECALL
        #  130 CALL
        #  140 COMPARE_OP <
        #  146 POP_JUMP_FORWARD_IF_FALSE to 242
        #  148 LOAD_GLOBAL unit_type_names
        #  160 LOAD_DEREF self
        #  162 LOAD_ATTR unit_type
        #  172 BINARY_SUBSCR
        #  182 STORE_FAST s
        #  184 LOAD_CONST '{} ({})'
        #  186 LOAD_METHOD format
        #  208 LOAD_FAST value
        #  210 LOAD_FAST s
        #  212 PRECALL
        #  216 CALL
        #  226 STORE_FAST unit_type_str
        #  228 LOAD_FAST name
        #  230 LOAD_FAST unit_type_str
        #  232 BUILD_TUPLE
        #  234 LOAD_FAST items
        #  236 LOAD_FAST i
        #  238 STORE_SUBSCR
        #  242 JUMP_BACKWARD to 72
        #  244 LOAD_CONST ', '
        #  246 LOAD_METHOD join
        #  268 LOAD_CONST <code object <genexpr> at 0x105bc04e0, file "asphodel\__init__.py", line 306>
        #  270 MAKE_FUNCTION
        #  272 LOAD_FAST items
        #  274 GET_ITER
        #  276 PRECALL
        #  280 CALL
        #  290 PRECALL
        #  294 CALL
        #  304 STORE_FAST contents
        #  306 LOAD_CONST '<'
        #  308 LOAD_DEREF self
        #  310 LOAD_ATTR __class__
        #  320 LOAD_ATTR __name__
        #  330 BINARY_OP +
        #  334 LOAD_CONST ' {'
        #  336 BINARY_OP +
        #  340 LOAD_FAST contents
        #  342 BINARY_OP +
        #  346 LOAD_CONST '}>'
        #  348 BINARY_OP +
        #  352 RETURN_VALUE
        pass

class AsphodelByteSetting(SettingStructure):

    pass

class AsphodelByteArraySetting(SettingStructure):

    pass

class AsphodelStringSetting(SettingStructure):

    pass

class AsphodelInt32Setting(SettingStructure):

    pass

class AsphodelInt32ScaledSetting(SettingStructure):

    pass

class AsphodelFloatSetting(SettingStructure):

    pass

class AsphodelFloatArraySetting(SettingStructure):

    pass

class AsphodelCustomEnumSetting(SettingStructure):

    pass

class AsphodelSettingUnion(Union):

    pass

class AsphodelSettingInfo(Structure):

    __reduce__ = object.__reduce__

    def __repr__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR setting_type
        #   14 LOAD_GLOBAL NULL + len
        #   26 LOAD_GLOBAL setting_type_names
        #   38 PRECALL
        #   42 CALL
        #   52 COMPARE_OP <
        #   58 EXTENDED_ARG
        #   60 POP_JUMP_FORWARD_IF_FALSE to 706
        #   62 LOAD_GLOBAL setting_type_names
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR setting_type
        #   86 BINARY_SUBSCR
        #   96 STORE_FAST s
        #   98 LOAD_CONST '{} ({})'
        #  100 LOAD_METHOD format
        #  122 LOAD_FAST self
        #  124 LOAD_ATTR setting_type
        #  134 LOAD_FAST s
        #  136 PRECALL
        #  140 CALL
        #  150 STORE_FAST setting_type_str
        #  152 LOAD_FAST s
        #  154 LOAD_CONST 'SETTING_TYPE_BYTE'
        #  156 COMPARE_OP ==
        #  162 POP_JUMP_FORWARD_IF_TRUE to 200
        #  164 LOAD_FAST s
        #  166 LOAD_CONST 'SETTING_TYPE_BOOLEAN'
        #  168 COMPARE_OP ==
        #  174 POP_JUMP_FORWARD_IF_TRUE to 200
        #  176 LOAD_FAST s
        #  178 LOAD_CONST 'SETTING_TYPE_UNIT_TYPE'
        #  180 COMPARE_OP ==
        #  186 POP_JUMP_FORWARD_IF_TRUE to 200
        #  188 LOAD_FAST s
        #  190 LOAD_CONST 'SETTING_TYPE_CHANNEL_TYPE'
        #  192 COMPARE_OP ==
        #  198 POP_JUMP_FORWARD_IF_FALSE to 252
        #  200 LOAD_GLOBAL NULL + repr
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR u
        #  224 LOAD_ATTR byte_setting
        #  234 PRECALL
        #  238 CALL
        #  248 STORE_FAST u_str
        #  250 JUMP_FORWARD to 762
        #  252 LOAD_FAST s
        #  254 LOAD_CONST 'SETTING_TYPE_BYTE_ARRAY'
        #  256 COMPARE_OP ==
        #  262 POP_JUMP_FORWARD_IF_FALSE to 316
        #  264 LOAD_GLOBAL NULL + repr
        #  276 LOAD_FAST self
        #  278 LOAD_ATTR u
        #  288 LOAD_ATTR byte_array_setting
        #  298 PRECALL
        #  302 CALL
        #  312 STORE_FAST u_str
        #  314 JUMP_FORWARD to 762
        #  316 LOAD_FAST s
        #  318 LOAD_CONST 'SETTING_TYPE_STRING'
        #  320 COMPARE_OP ==
        #  326 POP_JUMP_FORWARD_IF_FALSE to 380
        #  328 LOAD_GLOBAL NULL + repr
        #  340 LOAD_FAST self
        #  342 LOAD_ATTR u
        #  352 LOAD_ATTR string_setting
        #  362 PRECALL
        #  366 CALL
        #  376 STORE_FAST u_str
        #  378 JUMP_FORWARD to 762
        #  380 LOAD_FAST s
        #  382 LOAD_CONST 'SETTING_TYPE_INT32'
        #  384 COMPARE_OP ==
        #  390 POP_JUMP_FORWARD_IF_FALSE to 444
        #  392 LOAD_GLOBAL NULL + repr
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR u
        #  416 LOAD_ATTR int32_setting
        #  426 PRECALL
        # ... bytecode truncated ...
        pass

    def __getstate__(self):
        default_bytes = self.default_bytes[:self.default_bytes_length]
        return {
            '_name_array': self.name,
            'name_length': self.name_length,
            '_default_bytes': default_bytes,
            'default_bytes_length': self.default_bytes_length,
            'setting_type': self.setting_type,
            'u': self.u }

    def __setstate__(self, state):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST state
        #    4 LOAD_METHOD items
        #   26 PRECALL
        #   30 CALL
        #   40 GET_ITER
        #   42 FOR_ITER to 88
        #   44 UNPACK_SEQUENCE
        #   48 STORE_FAST k
        #   50 STORE_FAST v
        #   52 LOAD_GLOBAL NULL + setattr
        #   64 LOAD_FAST self
        #   66 LOAD_FAST k
        #   68 LOAD_FAST v
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 JUMP_BACKWARD to 42
        #   88 LOAD_GLOBAL NULL + c_char_p
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR _name_array
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_FAST self
        #  128 STORE_ATTR _name_array
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR _name_array
        #  150 LOAD_FAST self
        #  152 STORE_ATTR name
        #  162 LOAD_GLOBAL c_uint8
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR default_bytes_length
        #  186 BINARY_OP *
        #  190 STORE_FAST array_type
        #  192 PUSH_NULL
        #  194 LOAD_FAST array_type
        #  196 LOAD_FAST self
        #  198 LOAD_ATTR _default_bytes
        #  208 CALL_FUNCTION_EX
        #  210 LOAD_FAST self
        #  212 STORE_ATTR _default_bytes
        #  222 LOAD_FAST self
        #  224 LOAD_ATTR _default_bytes
        #  234 LOAD_FAST self
        #  236 STORE_ATTR default_bytes
        #  246 LOAD_CONST None
        #  248 RETURN_VALUE
        pass

    def from_str(cls, s):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST <code object trim_prefix at 0x100acf9f0, file "asphodel\__init__.py", line 455>
        #    4 MAKE_FUNCTION
        #    6 STORE_FAST trim_prefix
        #    8 LOAD_CONST <code object trim_suffix at 0x100acf470, file "asphodel\__init__.py", line 461>
        #   10 MAKE_FUNCTION
        #   12 STORE_FAST trim_suffix
        #   14 PUSH_NULL
        #   16 LOAD_FAST trim_prefix
        #   18 LOAD_FAST s
        #   20 LOAD_CONST '<AsphodelSettingInfo {'
        #   22 PRECALL
        #   26 CALL
        #   36 STORE_FAST s
        #   38 PUSH_NULL
        #   40 LOAD_FAST trim_suffix
        #   42 LOAD_FAST s
        #   44 LOAD_CONST '}>'
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST s
        #   62 LOAD_GLOBAL NULL + AsphodelSettingUnion
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST u
        #   90 LOAD_FAST s
        #   92 LOAD_METHOD endswith
        #  114 LOAD_CONST 'UNKNOWN TYPE'
        #  116 PRECALL
        #  120 CALL
        #  130 EXTENDED_ARG
        #  132 POP_JUMP_FORWARD_IF_TRUE to 774
        #  134 PUSH_NULL
        #  136 LOAD_FAST trim_suffix
        #  138 LOAD_FAST s
        #  140 LOAD_CONST '}>'
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST s
        #  158 LOAD_FAST s
        #  160 LOAD_METHOD rsplit
        #  182 LOAD_CONST ' {'
        #  184 LOAD_CONST 1
        #  186 PRECALL
        #  190 CALL
        #  200 UNPACK_SEQUENCE
        #  204 STORE_FAST s
        #  206 STORE_FAST u_vals
        #  208 LOAD_FAST s
        #  210 LOAD_METHOD rsplit
        #  232 LOAD_CONST ', u=<'
        #  234 PRECALL
        #  238 CALL
        #  248 UNPACK_SEQUENCE
        #  252 STORE_FAST s
        #  254 STORE_FAST u_type
        #  256 LOAD_GLOBAL NULL + dict
        #  268 LOAD_GLOBAL NULL + map
        #  280 LOAD_CONST <code object <lambda> at 0x105bc0a80, file "asphodel\__init__.py", line 479>
        #  282 MAKE_FUNCTION
        #  284 LOAD_FAST u_vals
        #  286 LOAD_METHOD split
        #  308 LOAD_CONST ', '
        #  310 PRECALL
        #  314 CALL
        #  324 PRECALL
        #  328 CALL
        #  338 PRECALL
        #  342 CALL
        #  352 STORE_FAST u_dict
        #  354 LOAD_CONST 'unit_type'
        #  356 LOAD_FAST u_dict
        #  358 CONTAINS_OP
        #  360 POP_JUMP_FORWARD_IF_FALSE to 436
        #  362 LOAD_FAST u_dict
        #  364 LOAD_CONST 'unit_type'
        #  366 BINARY_SUBSCR
        #  376 LOAD_METHOD split
        #  398 LOAD_CONST ' '
        #  400 LOAD_CONST 1
        # ... bytecode truncated ...
        pass

class AsphodelNative:

    AsphodelTransferCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_void_p)

    AsphodelStreamingCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_size_t, c_void_p)

    AsphodelConnectCallback = CFUNCTYPE(None, c_int, c_int, c_void_p)

    AsphodelCommandCallback = CFUNCTYPE(None, c_int, c_void_p)

    AsphodelDecodeCallback = CFUNCTYPE(None, c_uint64, POINTER(c_double), c_size_t, c_size_t, c_void_p)

    AsphodelCounterDecoderFunc = CFUNCTYPE(c_uint64, POINTER(c_uint8), c_uint64)

    AsphodelLostPacketCallback = CFUNCTYPE(None, c_uint64, c_uint64, c_void_p)

    AsphodelIDDecoderFunc = CFUNCTYPE(c_uint8, POINTER(c_uint8))

    AsphodelUnknownIDCallback = CFUNCTYPE(None, c_uint8, c_void_p)

    class AsphodelDeviceStruct(Structure):

        pass

    class AsphodelChannelCalibration(Structure):

        pass

    class AsphodelSupplyInfo(Structure):

        pass

    class AsphodelCtrlVarInfo(Structure):

        pass

    class AsphodelExtraScanResult(Structure):

        pass

    class AsphodelGPIOPortInfo(Structure):

        pass

    class AsphodelStreamAndChannels(Structure):

        pass

    class AsphodelChannelDecoder(Structure):

        pass

    class AsphodelStreamDecoder(Structure):

        pass

    class AsphodelDeviceDecoder(Structure):

        pass

    class AsphodelTCPAdvInfo(Structure):

        pass

    class AsphodelUnitFormatter(Structure):

        pass

    def __init__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_CONST None
        #    6 LOAD_DEREF self
        #    8 STORE_ATTR lib
        #   18 BUILD_LIST
        #   20 LOAD_DEREF self
        #   22 STORE_ATTR missing_funcs
        #   32 LOAD_GLOBAL NULL + weakref
        #   44 LOAD_ATTR WeakSet
        #   54 PRECALL
        #   58 CALL
        #   68 LOAD_DEREF self
        #   70 STORE_ATTR device_list
        #   80 LOAD_GLOBAL sys
        #   92 LOAD_ATTR platform
        #  102 LOAD_CONST 'win32'
        #  104 COMPARE_OP ==
        #  110 EXTENDED_ARG
        #  112 POP_JUMP_FORWARD_IF_FALSE to 700
        #  114 LOAD_GLOBAL sys
        #  126 LOAD_ATTR maxsize
        #  136 LOAD_CONST 4294967296
        #  138 COMPARE_OP >
        #  144 STORE_FAST is_64bit
        #  146 LOAD_FAST is_64bit
        #  148 POP_JUMP_FORWARD_IF_FALSE to 288
        #  150 LOAD_CONST 'Asphodel64'
        #  152 STORE_FAST library_name
        #  154 LOAD_GLOBAL os
        #  166 LOAD_ATTR path
        #  176 LOAD_METHOD join
        #  198 LOAD_GLOBAL os
        #  210 LOAD_ATTR path
        #  220 LOAD_METHOD dirname
        #  242 LOAD_GLOBAL __file__
        #  254 PRECALL
        #  258 CALL
        #  268 LOAD_CONST 'lib64'
        #  270 PRECALL
        #  274 CALL
        #  284 STORE_FAST library_dir
        #  286 JUMP_FORWARD to 424
        #  288 LOAD_CONST 'Asphodel32'
        #  290 STORE_FAST library_name
        #  292 LOAD_GLOBAL os
        #  304 LOAD_ATTR path
        #  314 LOAD_METHOD join
        #  336 LOAD_GLOBAL os
        #  348 LOAD_ATTR path
        #  358 LOAD_METHOD dirname
        #  380 LOAD_GLOBAL __file__
        #  392 PRECALL
        #  396 CALL
        #  406 LOAD_CONST 'lib32'
        #  408 PRECALL
        #  412 CALL
        #  422 STORE_FAST library_dir
        #  424 LOAD_GLOBAL os
        #  436 LOAD_ATTR path
        #  446 LOAD_METHOD join
        #  468 LOAD_FAST library_dir
        #  470 LOAD_FAST library_name
        #  472 LOAD_CONST '.dll'
        #  474 BINARY_OP +
        #  478 PRECALL
        #  482 CALL
        #  492 STORE_FAST library_path
        #  494 LOAD_FAST library_dir
        #  496 LOAD_GLOBAL os
        #  508 LOAD_ATTR pathsep
        #  518 BINARY_OP +
        #  522 LOAD_GLOBAL os
        #  534 LOAD_ATTR path
        #  544 LOAD_METHOD dirname
        #  566 LOAD_GLOBAL sys
        #  578 LOAD_ATTR executable
        #  588 PRECALL
        #  592 CALL
        #  602 BINARY_OP +
        # ... bytecode truncated ...
        pass

    def free(self):
        if self.device_list:
            for device in self.device_list:
                device.free()
                self.device_list = None
                if self.lib:
                    if self.usb_devices_supported:
                        self.lib.asphodel_usb_deinit()
                    if self.tcp_devices_supported:
                        self.lib.asphodel_tcp_deinit()
                    self.lib = None
                    return None
                return None

    def __del__(self):
        self.free()

    def asphodel_error_check(self, result, func, arguments):
        if result != 0:
            error_name = self.lib.asphodel_error_name(result)
            raise AsphodelError(result, error_name)

    def asphodel_string_decode_check(self, result, func, arguments):
        return result.decode('UTF-8')

    def load_library_function(self, name, restype, argtypes, errcheck, ignore_missing):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL name
        #    2 RESUME
        #    4 NOP
        #    6 LOAD_GLOBAL NULL + getattr
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR lib
        #   30 LOAD_DEREF name
        #   32 PRECALL
        #   36 CALL
        #   46 STORE_FAST func
        #   48 JUMP_FORWARD to 196
        #   50 PUSH_EXC_INFO
        #   52 LOAD_GLOBAL AttributeError
        #   64 CHECK_EXC_MATCH
        #   66 POP_JUMP_FORWARD_IF_FALSE to 188
        #   68 POP_TOP
        #   70 LOAD_FAST ignore_missing
        #   72 POP_JUMP_FORWARD_IF_FALSE to 186
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR missing_funcs
        #   86 LOAD_METHOD append
        #  108 LOAD_DEREF name
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_CLOSURE name
        #  128 BUILD_TUPLE
        #  130 LOAD_CONST <code object missing_func at 0x105b408b0, file "asphodel\__init__.py", line 928>
        #  132 MAKE_FUNCTION closure
        #  134 STORE_FAST missing_func
        #  136 LOAD_GLOBAL NULL + setattr
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR lib
        #  160 LOAD_DEREF name
        #  162 LOAD_FAST missing_func
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 POP_EXCEPT
        #  182 LOAD_CONST None
        #  184 RETURN_VALUE
        #  186 RAISE_VARARGS
        #  188 RERAISE
        #  190 COPY
        #  192 POP_EXCEPT
        #  194 RERAISE
        #  196 LOAD_FAST restype
        #  198 LOAD_FAST func
        #  200 STORE_ATTR restype
        #  210 LOAD_FAST errcheck
        #  212 POP_JUMP_FORWARD_IF_NONE to 228
        #  214 LOAD_FAST errcheck
        #  216 LOAD_FAST func
        #  218 STORE_ATTR errcheck
        #  228 LOAD_FAST argtypes
        #  230 LOAD_FAST func
        #  232 STORE_ATTR argtypes
        #  242 LOAD_CONST None
        #  244 RETURN_VALUE
        pass

    def load_device_function(self, base_name, argtypes):
        non_blocking_name = base_name
        blocking_name = base_name + '_blocking'
        blocking_argtypes = [
            POINTER(self.AsphodelDeviceStruct)]
        blocking_argtypes.extend(argtypes)
        non_blocking_argtypes = list(blocking_argtypes)
        non_blocking_argtypes.append(self.AsphodelCommandCallback)
        non_blocking_argtypes.append(c_void_p)
        self.load_library_function(non_blocking_name, c_int, non_blocking_argtypes, self.asphodel_error_check)
        self.load_library_function(blocking_name, c_int, blocking_argtypes, self.asphodel_error_check)

    def setup_api_h_prototypes(self):
        string_decode = self.asphodel_string_decode_check
        self.load_library_function('asphodel_error_name', c_char_p, [
            c_int], string_decode)
        self.load_library_function('asphodel_unit_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_unit_type_count', c_uint8, [], None)
        self.load_library_function('asphodel_channel_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_channel_type_count', c_uint8, [], None)
        self.load_library_function('asphodel_setting_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_setting_type_count', c_uint8, [], None)

    def setup_bootloader_h_prototypes(self):
        self.load_device_function('asphodel_bootloader_start_program', [])
        self.load_device_function('asphodel_get_bootloader_page_info', [
            POINTER(c_uint32),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_bootloader_block_sizes', [
            POINTER(c_uint16),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_start_bootloader_page', [
            c_uint32,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_bootloader_code_block', [
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_bootloader_page', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint16),
            c_uint8])
        self.load_device_function('asphodel_finish_bootloader_page', [
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_verify_bootloader_page', [
            POINTER(c_uint8),
            c_size_t])

    def setup_channel_specific_h_prototypes(self):
        self.load_library_function('asphodel_get_strain_bridge_count', c_int, [
            POINTER(AsphodelChannelInfo),
            POINTER(c_int)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_strain_bridge_subchannel', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_strain_bridge_values', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            c_float * 5], self.asphodel_error_check)
        self.load_device_function('asphodel_set_strain_outputs', [
            c_int,
            c_int,
            c_int,
            c_int])
        self.load_library_function('asphodel_check_strain_resistances', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            c_double,
            c_double,
            c_double,
            POINTER(c_double),
            POINTER(c_double),
            POINTER(c_int)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_accel_self_test_limits', c_int, [
            POINTER(AsphodelChannelInfo),
            c_float * 6], self.asphodel_error_check)
        self.load_device_function('asphodel_enable_accel_self_test', [
            c_int,
            c_int])
        self.load_library_function('asphodel_check_accel_self_test', c_int, [
            POINTER(AsphodelChannelInfo),
            c_double * 3,
            c_double * 3,
            POINTER(c_int)], self.asphodel_error_check)

    def setup_ctrl_var_h_prototypes(self):
        self.load_device_function('asphodel_get_ctrl_var_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_ctrl_var_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_ctrl_var_info', [
            c_int,
            POINTER(self.AsphodelCtrlVarInfo)])
        self.load_device_function('asphodel_get_ctrl_var', [
            c_int,
            POINTER(c_int32)])
        self.load_device_function('asphodel_set_ctrl_var', [
            c_int,
            c_int32])

    def setup_decode_h_prototypes(self):
        self.load_library_function('asphodel_create_channel_decoder', c_int, [
            POINTER(AsphodelChannelInfo),
            c_uint16,
            POINTER(POINTER(self.AsphodelChannelDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_create_stream_decoder', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint16,
            POINTER(POINTER(self.AsphodelStreamDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_create_device_decoder', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint8,
            c_uint8,
            c_uint8,
            POINTER(POINTER(self.AsphodelDeviceDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_get_streaming_counts', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint8,
            c_double,
            c_double,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_uint)], self.asphodel_error_check)

    def setup_device_h_prototypes(self):
        self.load_device_function('asphodel_get_protocol_version', [
            POINTER(c_uint16)])
        self.load_device_function('asphodel_get_protocol_version_string', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_board_info', [
            POINTER(c_uint8),
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_user_tag_locations', [
            c_size_t * 6])
        self.load_device_function('asphodel_get_build_info', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_build_date', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_commit_id', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_repo_branch', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_repo_name', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_family', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_model', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_id', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_nvm_size', [
            POINTER(c_size_t)])
        self.load_device_function('asphodel_erase_nvm', [])
        self.load_device_function('asphodel_write_nvm_raw', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_nvm_section', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_read_nvm_raw', [
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_read_nvm_section', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_read_user_tag_string', [
            c_size_t,
            c_size_t,
            c_char_p])
        self.load_device_function('asphodel_write_user_tag_string', [
            c_size_t,
            c_size_t,
            c_char_p])
        self.load_device_function('asphodel_get_nvm_modified', [
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_nvm_hash', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_setting_hash', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_flush', [])
        self.load_device_function('asphodel_reset', [])
        self.load_device_function('asphodel_get_bootloader_info', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_bootloader_jump', [])
        self.load_device_function('asphodel_get_reset_flag', [
            POINTER(c_uint8)])
        self.load_device_function('asphodel_clear_reset_flag', [])
        self.load_device_function('asphodel_get_rgb_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_rgb_values', [
            c_int,
            c_uint8 * 3])
        self.load_device_function('asphodel_set_rgb_values', [
            c_int,
            c_uint8 * 3,
            c_int])
        self.load_device_function('asphodel_set_rgb_values_hex', [
            c_int,
            c_uint32,
            c_int])
        self.load_device_function('asphodel_get_led_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_led_value', [
            c_int,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_set_led_value', [
            c_int,
            c_uint8,
            c_int])
        self.load_device_function('asphodel_set_device_mode', [
            c_uint8])
        self.load_device_function('asphodel_get_device_mode', [
            POINTER(c_uint8)])

    def setup_device_type_h_prototypes(self):
        self.load_library_function('asphodel_supports_rf_power_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_radio_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_remote_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_bootloader_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)

    def setup_low_level_h_prototypes(self):
        self.load_device_function('asphodel_get_gpio_port_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_gpio_port_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_gpio_port_info', [
            c_int,
            POINTER(self.AsphodelGPIOPortInfo)])
        self.load_device_function('asphodel_get_gpio_port_values', [
            c_int,
            POINTER(c_uint32)])
        self.load_device_function('asphodel_set_gpio_port_modes', [
            c_int,
            c_uint8,
            c_uint32])
        self.load_device_function('asphodel_disable_gpio_overrides', [])
        self.load_device_function('asphodel_get_bus_counts', [
            POINTER(c_int),
            POINTER(c_int)])
        self.load_device_function('asphodel_set_spi_cs_mode', [
            c_int,
            c_uint8])
        self.load_device_function('asphodel_do_spi_transfer', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_i2c_write', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_i2c_read', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_radio_fixed_test', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_radio_fixed_test', [
            c_uint16,
            c_uint16,
            c_uint8])
        self.load_device_function('asphodel_do_radio_sweep_test', [
            c_uint16,
            c_uint16,
            c_uint16,
            c_uint16,
            c_uint8])
        self.load_device_function('asphodel_get_info_region_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_info_region_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_info_region', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stack_info', [
            c_uint32 * 2])
        self.load_device_function('asphodel_echo_raw', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_echo_transaction', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_echo_params', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])

    def setup_mem_test_h_prototypes(self):
        try:
            self.load_library_function('asphodel_mem_test_supported', c_int, [], None, ignore_missing = False)
            self.mem_test_supported = self.lib.asphodel_mem_test_supported()
        except AttributeError:
            self.mem_test_supported = False

        self.load_library_function('asphodel_mem_test_set_limit', None, [
            c_int], None)
        self.load_library_function('asphodel_mem_test_get_limit', c_int, [], None)

    def setup_radio_h_prototypes(self):
        self.load_device_function('asphodel_stop_radio', [])
        self.load_device_function('asphodel_start_radio_scan', [])
        self.load_device_function('asphodel_get_raw_radio_scan_results', [
            POINTER(c_uint32),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_get_radio_scan_results', [
            POINTER(POINTER(c_uint32)),
            POINTER(c_size_t)])
        self.load_library_function('asphodel_free_radio_scan_results', None, [
            POINTER(c_uint32)], None)
        self.load_device_function('asphodel_get_raw_radio_extra_scan_results', [
            POINTER(self.AsphodelExtraScanResult),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_get_radio_extra_scan_results', [
            POINTER(POINTER(self.AsphodelExtraScanResult)),
            POINTER(c_size_t)])
        self.load_library_function('asphodel_free_radio_extra_scan_results', None, [
            POINTER(self.AsphodelExtraScanResult)], None)
        self.load_device_function('asphodel_get_radio_scan_power', [
            POINTER(c_uint32),
            POINTER(c_int8),
            c_size_t])
        self.load_device_function('asphodel_connect_radio', [
            c_uint32])
        self.load_device_function('asphodel_get_radio_status', [
            POINTER(c_int),
            POINTER(c_uint32),
            POINTER(c_uint8),
            POINTER(c_int)])
        self.load_device_function('asphodel_get_radio_ctrl_vars', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_radio_default_serial', [
            POINTER(c_uint32)])
        self.load_device_function('asphodel_start_radio_scan_boot', [])
        self.load_device_function('asphodel_connect_radio_boot', [
            c_uint32])
        self.load_device_function('asphodel_stop_remote', [])
        self.load_device_function('asphodel_restart_remote', [])
        self.load_device_function('asphodel_get_remote_status', [
            POINTER(c_int),
            POINTER(c_uint32),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_restart_remote_app', [])
        self.load_device_function('asphodel_restart_remote_boot', [])

    def setup_rf_power_h_prototypes(self):
        self.load_device_function('asphodel_enable_rf_power', [
            c_int])
        self.load_device_function('asphodel_get_rf_power_status', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_rf_power_ctrl_vars', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_reset_rf_power_timeout', [
            c_uint32])

    def setup_setting_h_prototypes(self):
        self.load_device_function('asphodel_get_setting_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_setting_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_info', [
            c_int,
            POINTER(AsphodelSettingInfo)])
        self.load_device_function('asphodel_get_setting_default', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_custom_enum_counts', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_custom_enum_value_name', [
            c_int,
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_category_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_setting_category_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_category_settings', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])

    def setup_stream_h_prototypes(self):
        self.load_device_function('asphodel_get_stream_count', [
            POINTER(c_int),
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stream', [
            c_int,
            POINTER(POINTER(AsphodelStreamInfo))])
        self.load_library_function('asphodel_free_stream', None, [
            POINTER(AsphodelStreamInfo)], None)
        self.load_device_function('asphodel_get_stream_channels', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stream_format', [
            c_int,
            POINTER(AsphodelStreamInfo)])
        self.load_device_function('asphodel_enable_stream', [
            c_int,
            c_int])
        self.load_device_function('asphodel_warm_up_stream', [
            c_int,
            c_int])
        self.load_device_function('asphodel_get_stream_status', [
            c_int,
            POINTER(c_int),
            POINTER(c_int)])
        self.load_device_function('asphodel_get_stream_rate_info', [
            c_int,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_float),
            POINTER(c_float)])
        self.load_device_function('asphodel_get_channel_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_channel', [
            c_int,
            POINTER(POINTER(AsphodelChannelInfo))])
        self.load_library_function('asphodel_free_channel', None, [
            POINTER(AsphodelChannelInfo)], None)
        self.load_device_function('asphodel_get_channel_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_info', [
            c_int,
            POINTER(AsphodelChannelInfo)])
        self.load_device_function('asphodel_get_channel_coefficients', [
            c_int,
            POINTER(c_float),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_chunk', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_channel_specific', [
            c_int,
            POINTER(c_uint8),
            c_uint8,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_calibration', [
            c_int,
            POINTER(c_int),
            POINTER(self.AsphodelChannelCalibration)])

    def setup_supply_h_prototypes(self):
        self.load_device_function('asphodel_get_supply_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_supply_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_supply_info', [
            c_int,
            POINTER(self.AsphodelSupplyInfo)])
        self.load_device_function('asphodel_check_supply', [
            c_int,
            POINTER(c_int32),
            POINTER(c_uint8),
            c_uint])

    def setup_tcp_h_prototypes(self):
        try:
            self.load_library_function('asphodel_tcp_devices_supported', c_int, [], None, ignore_missing = False)
            s = self.lib.asphodel_tcp_devices_supported()
            self.tcp_devices_supported = s
        except AttributeError:
            self.tcp_devices_supported = False

        self.load_library_function('asphodel_tcp_init', c_int, [], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_deinit', None, [], None)
        self.load_library_function('asphodel_tcp_find_devices', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_find_devices_filter', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t),
            c_uint32], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_get_advertisement', POINTER(self.AsphodelTCPAdvInfo), [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_tcp_create_device', c_int, [
            c_char_p,
            c_uint16,
            c_int,
            c_char_p,
            POINTER(POINTER(self.AsphodelDeviceStruct))], self.asphodel_error_check)

    def setup_unit_format_h_prototypes(self):
        self.load_library_function('asphodel_create_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
            c_uint8,
            c_double,
            c_double,
            c_double,
            c_int], None)
        self.load_library_function('asphodel_create_custom_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
            c_double,
            c_double,
            c_double,
            c_char_p,
            c_char_p,
            c_char_p], None)
        self.load_library_function('asphodel_format_value_ascii', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)
        self.load_library_function('asphodel_format_value_utf8', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)
        self.load_library_function('asphodel_format_value_html', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)

    def setup_usb_h_prototypes(self):
        try:
            self.load_library_function('asphodel_usb_devices_supported', c_int, [], None, ignore_missing = False)
            s = self.lib.asphodel_usb_devices_supported()
            self.usb_devices_supported = s
        except AttributeError:
            self.usb_devices_supported = True

        self.load_library_function('asphodel_usb_init', c_int, [], self.asphodel_error_check)
        self.load_library_function('asphodel_usb_deinit', None, [], None)
        self.load_library_function('asphodel_usb_find_devices', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_usb_get_backend_version', c_char_p, [], None)

    def setup_version_h_prototypes(self):
        self.load_library_function('asphodel_get_library_protocol_version', c_uint16, [], None)
        self.load_library_function('asphodel_get_library_protocol_version_string', c_char_p, [], None)
        self.load_library_function('asphodel_get_library_build_info', c_char_p, [], None)
        self.load_library_function('asphodel_get_library_build_date', c_char_p, [], None)

    def find_usb_devices(self):
        count = c_size_t(0)
        self.lib.asphodel_usb_find_devices(None, byref(count))
        array_size = count.value
        if array_size == 0:
            return []
        array = POINTER(self.AsphodelDeviceStruct) * array_size()
        array_ptr = cast(byref(array), POINTER(POINTER(self.AsphodelDeviceStruct)))
        self.lib.asphodel_usb_find_devices(array_ptr, byref(count))
        array_entries = min(array_size, count.value)
        device_list = []
        for i in range(array_entries):
            device_list.append(AsphodelNativeDevice(self, array[i].contents))
            return device_list

    def find_tcp_devices(self, flags):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST flags
        #    4 POP_JUMP_FORWARD_IF_NOT_NONE to 20
        #    6 LOAD_GLOBAL ASPHODEL_TCP_FILTER_DEFAULT
        #   18 STORE_FAST flags
        #   20 LOAD_CONST 100
        #   22 STORE_FAST array_size
        #   24 LOAD_GLOBAL NULL + c_size_t
        #   36 LOAD_FAST array_size
        #   38 PRECALL
        #   42 CALL
        #   52 STORE_FAST count
        #   54 PUSH_NULL
        #   56 LOAD_GLOBAL NULL + POINTER
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR AsphodelDeviceStruct
        #   80 PRECALL
        #   84 CALL
        #   94 LOAD_FAST array_size
        #   96 BINARY_OP *
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST array
        #  116 LOAD_GLOBAL NULL + cast
        #  128 LOAD_GLOBAL NULL + byref
        #  140 LOAD_FAST array
        #  142 PRECALL
        #  146 CALL
        #  156 LOAD_GLOBAL NULL + POINTER
        #  168 LOAD_GLOBAL NULL + POINTER
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR AsphodelDeviceStruct
        #  192 PRECALL
        #  196 CALL
        #  206 PRECALL
        #  210 CALL
        #  220 PRECALL
        #  224 CALL
        #  234 STORE_FAST array_ptr
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR lib
        #  248 LOAD_METHOD asphodel_tcp_find_devices_filter
        #  270 LOAD_FAST array_ptr
        #  272 LOAD_GLOBAL NULL + byref
        #  284 LOAD_FAST count
        #  286 PRECALL
        #  290 CALL
        #  300 LOAD_FAST flags
        #  302 PRECALL
        #  306 CALL
        #  316 POP_TOP
        #  318 LOAD_FAST count
        #  320 LOAD_ATTR value
        #  330 LOAD_FAST array_size
        #  332 COMPARE_OP >
        #  338 POP_JUMP_FORWARD_IF_FALSE to 766
        #  340 LOAD_GLOBAL NULL + range
        #  352 LOAD_FAST array_size
        #  354 PRECALL
        #  358 CALL
        #  368 GET_ITER
        #  370 FOR_ITER to 444
        #  372 STORE_FAST i
        #  374 LOAD_FAST array
        #  376 LOAD_FAST i
        #  378 BINARY_SUBSCR
        #  388 LOAD_ATTR contents
        #  398 STORE_FAST device
        #  400 LOAD_FAST device
        #  402 LOAD_METHOD free_device
        #  424 LOAD_FAST device
        #  426 PRECALL
        #  430 CALL
        #  440 POP_TOP
        #  442 JUMP_BACKWARD to 370
        #  444 LOAD_FAST count
        #  446 LOAD_ATTR value
        #  456 STORE_FAST array_size
        #  458 PUSH_NULL
        #  460 LOAD_GLOBAL NULL + POINTER
        # ... bytecode truncated ...
        pass

    def create_tcp_device(self, host, port, timeout, serial):
        device_ptr = POINTER(self.AsphodelDeviceStruct)()
        if serial:
            serial_bytes = serial.encode('UTF-8')
        else:
            serial_bytes = None
        self.lib.asphodel_tcp_create_device(host.encode('UTF-8'), port, timeout, serial_bytes, byref(device_ptr))
        return AsphodelNativeDevice(self, device_ptr.contents)

    def tcp_get_advertisement(self, device):
        adv_ptr = self.lib.asphodel_tcp_get_advertisement(device)
        adv = adv_ptr.contents

        def decode_safe(b):
            
            try:
                return b.decode('UTF-8')
            except UnicodeDecodeError:
                return 'ERROR'


        return TCPAdvInfo(adv.tcp_version, bool(adv.connected), adv.max_incoming_param_length, adv.max_outgoing_param_length, adv.stream_packet_length, adv.protocol_type, decode_safe(adv.serial_number), adv.board_rev, decode_safe(adv.board_type), decode_safe(adv.build_info), decode_safe(adv.build_date), decode_safe(adv.user_tag1), decode_safe(adv.user_tag2), adv.remote_max_incoming_param_length, adv.remote_max_outgoing_param_length, adv.remote_stream_packet_length)

    def create_channel_decoder(self, channel_info, bit_offset):
        decoder_ptr = POINTER(self.AsphodelChannelDecoder)()
        self.lib.asphodel_create_channel_decoder(channel_info, bit_offset, byref(decoder_ptr))
        return AsphodelNativeChannelDecoder(self, decoder_ptr.contents, channel_info)

    def create_stream_decoder(self, stream_info, channel_info_list, bit_offset):
        decoder_ptr = POINTER(self.AsphodelStreamDecoder)()
        array_type = POINTER(AsphodelChannelInfo) * len(channel_info_list)

    def create_device_decoder(self, info_list, filler_bits, id_bits):
        decoder_ptr = POINTER(self.AsphodelDeviceDecoder)()
        array_size = len(info_list)
        info_array = self.AsphodelStreamAndChannels * array_size()

    def get_streaming_counts(self, streams, response_time, buffer_time, timeout):
        packet_count = c_int()
        transfer_count = c_int()
        timeout = c_uint(timeout)
        array_size = len(streams)
        info_array = self.AsphodelStreamAndChannels * array_size()
        for i, stream_info in enumerate(streams):
            info_array[i].stream_info = pointer(stream_info)
            self.lib.asphodel_get_streaming_counts(cast(info_array, POINTER(self.AsphodelStreamAndChannels)), array_size, response_time, buffer_time, byref(packet_count), byref(transfer_count), byref(timeout))
            return (packet_count.value, transfer_count.value, timeout.value)

    def create_unit_formatter(self, unit_type, minimum, maximum, resolution, use_metric):
        use_metric_int = 1 if use_metric else 0
        formatter = self.lib.asphodel_create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric_int)
        if not formatter:
            raise AsphodelError(0, 'asphodel_create_unit_formatter returned NULL')
        recreate = (recreate_unit_formatter, (unit_type, minimum, maximum, resolution, use_metric))
        return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)

    def create_custom_unit_formatter(self, scale, offset, resolution, unit_ascii, unit_utf8, unit_html):
        formatter = self.lib.asphodel_create_custom_unit_formatter(scale, offset, resolution, unit_ascii.encode('ascii'), unit_utf8.encode('UTF-8'), unit_html.encode('ascii'))
        if not formatter:
            raise AsphodelError(0, 'asphodel_create_custom_unit_formatter returned NULL')
        recreate = (recreate_custom_unit_formatter, (scale, offset, resolution, unit_ascii, unit_utf8, unit_html))
        return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)

    def _format_value(self, lib_func, unit_type, resolution, value, use_metric):
        use_metric_int = 1 if use_metric else 0
        buffer = create_string_buffer(256)
        lib_func(buffer, len(buffer), unit_type, resolution, use_metric_int, value)
        return buffer.value

    def format_value_ascii(self, unit_type, resolution, value, use_metric):
        b = self._format_value(self.lib.asphodel_format_value_ascii, unit_type, resolution, value, use_metric)
        return b.decode('ascii')

    def format_value_utf8(self, unit_type, resolution, value, use_metric):
        b = self._format_value(self.lib.asphodel_format_value_utf8, unit_type, resolution, value, use_metric)
        return b.decode('UTF-8')

    def format_value_html(self, unit_type, resolution, value, use_metric):
        b = self._format_value(self.lib.asphodel_format_value_html, unit_type, resolution, value, use_metric)
        return b.decode('ascii')

    def mem_test_set_limit(self, limit):
        self.lib.asphodel_mem_test_set_limit(limit)

    def mem_test_get_limit(self):
        return self.lib.asphodel_mem_test_get_limit()

def asphodel_command(func_base):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL func_base
    #    2 RESUME
    #    4 LOAD_CLOSURE func_base
    #    6 BUILD_TUPLE
    #    8 LOAD_CONST <code object decorator at 0x105b40e00, file "asphodel\__init__.py", line 2232>
    #   10 MAKE_FUNCTION closure
    #   12 STORE_FAST decorator
    #   14 LOAD_FAST decorator
    #   16 RETURN_VALUE
    pass

class AsphodelNativeDevice:

    MAX_STRING_LENGTH = 128

    def __init__(self, lib, device):
        self.lib = lib
        self.device = device
        self._callbacks = []
        self._remote = None
        if self.get_transport_type() == 'usb':
            self.reconnect_time = 5
        else:
            self.reconnect_time = 10
        if self.lib:
            self.lib.device_list.add(self)
            return None

    def open(self):
        ret = self.device.open_device(self.device)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    def close(self):
        if self.device:
            self.device.close_device(self.device)
            return None

    def free(self):
        self.close()
        if self.device:
            self.device.free_device(self.device)
        self.device = None
        self.lib = None

    def __del__(self):
        self.free()

    def get_location_string(self):
        return self.device.location_string.decode('UTF-8')

    def get_transport_type(self):
        if self.lib.protocol_version >= 515:
            return self.device.transport_type.decode('UTF-8')

    def get_serial_number(self):
        buffer = create_string_buffer(64)
        ret = self.device.get_serial_number(self.device, buffer, len(buffer))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return buffer.value.decode('UTF-8')

    def do_transfer(self, cmd, params, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL callback
        #    4 MAKE_CELL c_callback
        #    6 RESUME
        #    8 LOAD_FAST params
        #   10 POP_JUMP_FORWARD_IF_NOT_NONE to 16
        #   12 BUILD_LIST
        #   14 STORE_FAST params
        #   16 LOAD_GLOBAL c_uint8
        #   28 LOAD_GLOBAL NULL + len
        #   40 LOAD_FAST params
        #   42 PRECALL
        #   46 CALL
        #   56 BINARY_OP *
        #   60 STORE_FAST param_array_type
        #   62 LOAD_FAST param_array_type
        #   64 LOAD_METHOD from_buffer_copy
        #   86 LOAD_GLOBAL NULL + bytes
        #   98 LOAD_FAST params
        #  100 PRECALL
        #  104 CALL
        #  114 PRECALL
        #  118 CALL
        #  128 STORE_FAST param_array
        #  130 LOAD_CLOSURE c_callback
        #  132 LOAD_CLOSURE callback
        #  134 LOAD_CLOSURE self
        #  136 BUILD_TUPLE
        #  138 LOAD_CONST <code object cb at 0x105a85e90, file "asphodel\__init__.py", line 2341>
        #  140 MAKE_FUNCTION closure
        #  142 STORE_FAST cb
        #  144 LOAD_DEREF self
        #  146 LOAD_ATTR lib
        #  156 LOAD_METHOD AsphodelTransferCallback
        #  178 LOAD_FAST cb
        #  180 PRECALL
        #  184 CALL
        #  194 STORE_DEREF c_callback
        #  196 LOAD_DEREF self
        #  198 LOAD_ATTR _callbacks
        #  208 LOAD_METHOD append
        #  230 LOAD_DEREF c_callback
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_DEREF self
        #  250 LOAD_ATTR device
        #  260 LOAD_METHOD do_transfer
        #  282 LOAD_DEREF self
        #  284 LOAD_ATTR device
        #  294 LOAD_FAST cmd
        #  296 LOAD_FAST param_array
        #  298 LOAD_GLOBAL NULL + len
        #  310 LOAD_FAST param_array
        #  312 PRECALL
        #  316 CALL
        #  326 LOAD_DEREF c_callback
        #  328 LOAD_CONST None
        #  330 PRECALL
        #  334 CALL
        #  344 STORE_FAST ret
        #  346 LOAD_FAST ret
        #  348 LOAD_CONST 0
        #  350 COMPARE_OP !=
        #  356 POP_JUMP_FORWARD_IF_FALSE to 452
        #  358 LOAD_DEREF self
        #  360 LOAD_ATTR lib
        #  370 LOAD_ATTR lib
        #  380 LOAD_METHOD asphodel_error_name
        #  402 LOAD_FAST ret
        #  404 PRECALL
        #  408 CALL
        #  418 STORE_FAST error_name
        #  420 LOAD_GLOBAL NULL + AsphodelError
        #  432 LOAD_FAST ret
        #  434 LOAD_FAST error_name
        #  436 PRECALL
        #  440 CALL
        #  450 RAISE_VARARGS
        #  452 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def do_transfer_blocking(self, cmd, params):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL finished
        #    2 MAKE_CELL result
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + threading
        #   18 LOAD_ATTR Event
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_DEREF finished
        #   44 LOAD_CONST None
        #   46 STORE_DEREF result
        #   48 LOAD_CLOSURE finished
        #   50 LOAD_CLOSURE result
        #   52 BUILD_TUPLE
        #   54 LOAD_CONST <code object callback at 0x105bc15c0, file "asphodel\__init__.py", line 2369>
        #   56 MAKE_FUNCTION closure
        #   58 STORE_FAST callback
        #   60 LOAD_FAST self
        #   62 LOAD_METHOD do_transfer
        #   84 LOAD_FAST cmd
        #   86 LOAD_FAST params
        #   88 LOAD_FAST callback
        #   90 PRECALL
        #   94 CALL
        #  104 POP_TOP
        #  106 LOAD_DEREF finished
        #  108 LOAD_METHOD is_set
        #  130 PRECALL
        #  134 CALL
        #  144 POP_JUMP_FORWARD_IF_TRUE to 228
        #  146 LOAD_FAST self
        #  148 LOAD_METHOD poll_device
        #  170 LOAD_CONST 100
        #  172 PRECALL
        #  176 CALL
        #  186 POP_TOP
        #  188 LOAD_DEREF finished
        #  190 LOAD_METHOD is_set
        #  212 PRECALL
        #  216 CALL
        #  226 POP_JUMP_BACKWARD_IF_FALSE to 146
        #  228 LOAD_DEREF result
        #  230 UNPACK_SEQUENCE
        #  234 STORE_FAST ret
        #  236 STORE_FAST params
        #  238 LOAD_FAST ret
        #  240 LOAD_CONST 0
        #  242 COMPARE_OP !=
        #  248 POP_JUMP_FORWARD_IF_FALSE to 344
        #  250 LOAD_FAST self
        #  252 LOAD_ATTR lib
        #  262 LOAD_ATTR lib
        #  272 LOAD_METHOD asphodel_error_name
        #  294 LOAD_FAST ret
        #  296 PRECALL
        #  300 CALL
        #  310 STORE_FAST error_name
        #  312 LOAD_GLOBAL NULL + AsphodelError
        #  324 LOAD_FAST ret
        #  326 LOAD_FAST error_name
        #  328 PRECALL
        #  332 CALL
        #  342 RAISE_VARARGS
        #  344 LOAD_FAST params
        #  346 RETURN_VALUE
        pass

    def do_transfer_reset(self, cmd, params, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL callback
        #    4 MAKE_CELL c_callback
        #    6 RESUME
        #    8 LOAD_FAST params
        #   10 POP_JUMP_FORWARD_IF_NOT_NONE to 16
        #   12 BUILD_LIST
        #   14 STORE_FAST params
        #   16 LOAD_GLOBAL c_uint8
        #   28 LOAD_GLOBAL NULL + len
        #   40 LOAD_FAST params
        #   42 PRECALL
        #   46 CALL
        #   56 BINARY_OP *
        #   60 STORE_FAST param_array_type
        #   62 LOAD_FAST param_array_type
        #   64 LOAD_METHOD from_buffer_copy
        #   86 LOAD_GLOBAL NULL + bytes
        #   98 LOAD_FAST params
        #  100 PRECALL
        #  104 CALL
        #  114 PRECALL
        #  118 CALL
        #  128 STORE_FAST param_array
        #  130 LOAD_CLOSURE c_callback
        #  132 LOAD_CLOSURE callback
        #  134 LOAD_CLOSURE self
        #  136 BUILD_TUPLE
        #  138 LOAD_CONST <code object cb at 0x105a9ad50, file "asphodel\__init__.py", line 2392>
        #  140 MAKE_FUNCTION closure
        #  142 STORE_FAST cb
        #  144 LOAD_DEREF self
        #  146 LOAD_ATTR lib
        #  156 LOAD_METHOD AsphodelTransferCallback
        #  178 LOAD_FAST cb
        #  180 PRECALL
        #  184 CALL
        #  194 STORE_DEREF c_callback
        #  196 LOAD_DEREF self
        #  198 LOAD_ATTR _callbacks
        #  208 LOAD_METHOD append
        #  230 LOAD_DEREF c_callback
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_DEREF self
        #  250 LOAD_ATTR device
        #  260 LOAD_METHOD do_transfer_reset
        #  282 LOAD_DEREF self
        #  284 LOAD_ATTR device
        #  294 LOAD_FAST cmd
        #  296 LOAD_FAST param_array
        #  298 LOAD_GLOBAL NULL + len
        #  310 LOAD_FAST param_array
        #  312 PRECALL
        #  316 CALL
        #  326 LOAD_DEREF c_callback
        #  328 LOAD_CONST None
        #  330 PRECALL
        #  334 CALL
        #  344 STORE_FAST ret
        #  346 LOAD_FAST ret
        #  348 LOAD_CONST 0
        #  350 COMPARE_OP !=
        #  356 POP_JUMP_FORWARD_IF_FALSE to 452
        #  358 LOAD_DEREF self
        #  360 LOAD_ATTR lib
        #  370 LOAD_ATTR lib
        #  380 LOAD_METHOD asphodel_error_name
        #  402 LOAD_FAST ret
        #  404 PRECALL
        #  408 CALL
        #  418 STORE_FAST error_name
        #  420 LOAD_GLOBAL NULL + AsphodelError
        #  432 LOAD_FAST ret
        #  434 LOAD_FAST error_name
        #  436 PRECALL
        #  440 CALL
        #  450 RAISE_VARARGS
        #  452 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def do_transfer_reset_blocking(self, cmd, params):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL finished
        #    2 MAKE_CELL ret
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + threading
        #   18 LOAD_ATTR Event
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_DEREF finished
        #   44 LOAD_CONST None
        #   46 STORE_DEREF ret
        #   48 LOAD_CLOSURE finished
        #   50 LOAD_CLOSURE ret
        #   52 BUILD_TUPLE
        #   54 LOAD_CONST <code object callback at 0x105bc17a0, file "asphodel\__init__.py", line 2415>
        #   56 MAKE_FUNCTION closure
        #   58 STORE_FAST callback
        #   60 LOAD_FAST self
        #   62 LOAD_METHOD do_transfer_reset
        #   84 LOAD_FAST cmd
        #   86 LOAD_FAST params
        #   88 LOAD_FAST callback
        #   90 PRECALL
        #   94 CALL
        #  104 POP_TOP
        #  106 LOAD_DEREF finished
        #  108 LOAD_METHOD is_set
        #  130 PRECALL
        #  134 CALL
        #  144 POP_JUMP_FORWARD_IF_TRUE to 228
        #  146 LOAD_FAST self
        #  148 LOAD_METHOD poll_device
        #  170 LOAD_CONST 100
        #  172 PRECALL
        #  176 CALL
        #  186 POP_TOP
        #  188 LOAD_DEREF finished
        #  190 LOAD_METHOD is_set
        #  212 PRECALL
        #  216 CALL
        #  226 POP_JUMP_BACKWARD_IF_FALSE to 146
        #  228 LOAD_DEREF ret
        #  230 LOAD_CONST 0
        #  232 COMPARE_OP !=
        #  238 POP_JUMP_FORWARD_IF_FALSE to 334
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR lib
        #  252 LOAD_ATTR lib
        #  262 LOAD_METHOD asphodel_error_name
        #  284 LOAD_DEREF ret
        #  286 PRECALL
        #  290 CALL
        #  300 STORE_FAST error_name
        #  302 LOAD_GLOBAL NULL + AsphodelError
        #  314 LOAD_DEREF ret
        #  316 LOAD_FAST error_name
        #  318 PRECALL
        #  322 CALL
        #  332 RAISE_VARARGS
        #  334 LOAD_CONST None
        #  336 RETURN_VALUE
        pass

    def start_streaming_packets(self, packet_count, transfer_count, timeout, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL callback
        #    2 RESUME
        #    4 LOAD_DEREF callback
        #    6 POP_JUMP_FORWARD_IF_FALSE to 266
        #    8 LOAD_CLOSURE callback
        #   10 BUILD_TUPLE
        #   12 LOAD_CONST <code object cb at 0x105bdc030, file "asphodel\__init__.py", line 2431>
        #   14 MAKE_FUNCTION closure
        #   16 STORE_FAST cb
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR lib
        #   30 LOAD_METHOD AsphodelStreamingCallback
        #   52 LOAD_FAST cb
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST c_callback
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_METHOD start_streaming_packets
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR device
        #  116 LOAD_FAST packet_count
        #  118 LOAD_FAST transfer_count
        #  120 LOAD_FAST timeout
        #  122 LOAD_FAST c_callback
        #  124 LOAD_CONST None
        #  126 PRECALL
        #  130 CALL
        #  140 STORE_FAST ret
        #  142 LOAD_FAST c_callback
        #  144 LOAD_FAST self
        #  146 STORE_ATTR _streaming_callback
        #  156 LOAD_FAST ret
        #  158 LOAD_CONST 0
        #  160 COMPARE_OP !=
        #  166 POP_JUMP_FORWARD_IF_FALSE to 262
        #  168 LOAD_FAST self
        #  170 LOAD_ATTR lib
        #  180 LOAD_ATTR lib
        #  190 LOAD_METHOD asphodel_error_name
        #  212 LOAD_FAST ret
        #  214 PRECALL
        #  218 CALL
        #  228 STORE_FAST error_name
        #  230 LOAD_GLOBAL NULL + AsphodelError
        #  242 LOAD_FAST ret
        #  244 LOAD_FAST error_name
        #  246 PRECALL
        #  250 CALL
        #  260 RAISE_VARARGS
        #  262 LOAD_CONST None
        #  264 RETURN_VALUE
        #  266 NOP
        #  268 LOAD_FAST self
        #  270 DELETE_ATTR _streaming_callback
        #  272 JUMP_FORWARD to 306
        #  274 PUSH_EXC_INFO
        #  276 LOAD_GLOBAL AttributeError
        #  288 CHECK_EXC_MATCH
        #  290 POP_JUMP_FORWARD_IF_FALSE to 298
        #  292 POP_TOP
        #  294 POP_EXCEPT
        #  296 JUMP_FORWARD to 306
        #  298 RERAISE
        #  300 COPY
        #  302 POP_EXCEPT
        #  304 RERAISE
        #  306 LOAD_FAST self
        #  308 LOAD_ATTR lib
        #  318 LOAD_METHOD AsphodelStreamingCallback
        #  340 PRECALL
        #  344 CALL
        #  354 STORE_FAST c_callback
        #  356 LOAD_FAST self
        #  358 LOAD_ATTR device
        #  368 LOAD_METHOD start_streaming_packets
        #  390 LOAD_FAST self
        #  392 LOAD_ATTR device
        #  402 LOAD_FAST packet_count
        #  404 LOAD_FAST transfer_count
        # ... bytecode truncated ...
        pass

    def stop_streaming_packets(self):
        self.device.stop_streaming_packets(self.device)

        try:
            del self._streaming_callback
            return None
        except AttributeError:
            return None

    def get_stream_packets_blocking(self, byte_count, timeout):
        buffer = c_uint8 * byte_count()
        count_int = c_int(byte_count)
        ret = self.device.get_stream_packets_blocking(self.device, buffer, byref(count_int), timeout)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return bytes(buffer[0:count_int.value])

    def get_max_incoming_param_length(self):
        v = self.device.get_max_incoming_param_length(self.device)
        return v

    def get_max_outgoing_param_length(self):
        v = self.device.get_max_outgoing_param_length(self.device)
        return v

    def get_stream_packet_length(self):
        v = self.device.get_stream_packet_length(self.device)
        return v

    def poll_device(self, milliseconds):
        ret = self.device.poll_device(self.device, milliseconds, None)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    def set_connect_callback(self, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL callback
        #    2 RESUME
        #    4 LOAD_DEREF callback
        #    6 POP_JUMP_FORWARD_IF_FALSE to 86
        #    8 LOAD_CLOSURE callback
        #   10 BUILD_TUPLE
        #   12 LOAD_CONST <code object cb at 0x105bb1430, file "asphodel\__init__.py", line 2506>
        #   14 MAKE_FUNCTION closure
        #   16 STORE_FAST cb
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR lib
        #   30 LOAD_METHOD AsphodelConnectCallback
        #   52 LOAD_FAST cb
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST c_callback
        #   70 LOAD_FAST c_callback
        #   72 LOAD_FAST self
        #   74 STORE_ATTR _connect_callback
        #   84 JUMP_FORWARD to 150
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR lib
        #   98 LOAD_METHOD AsphodelConnectCallback
        #  120 PRECALL
        #  124 CALL
        #  134 STORE_FAST c_callback
        #  136 LOAD_CONST None
        #  138 LOAD_FAST self
        #  140 STORE_ATTR _connect_callback
        #  150 LOAD_FAST self
        #  152 LOAD_ATTR device
        #  162 LOAD_METHOD set_connect_callback
        #  184 LOAD_FAST self
        #  186 LOAD_ATTR device
        #  196 LOAD_FAST c_callback
        #  198 LOAD_CONST None
        #  200 PRECALL
        #  204 CALL
        #  214 STORE_FAST ret
        #  216 LOAD_FAST ret
        #  218 LOAD_CONST 0
        #  220 COMPARE_OP !=
        #  226 POP_JUMP_FORWARD_IF_FALSE to 322
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR lib
        #  240 LOAD_ATTR lib
        #  250 LOAD_METHOD asphodel_error_name
        #  272 LOAD_FAST ret
        #  274 PRECALL
        #  278 CALL
        #  288 STORE_FAST error_name
        #  290 LOAD_GLOBAL NULL + AsphodelError
        #  302 LOAD_FAST ret
        #  304 LOAD_FAST error_name
        #  306 PRECALL
        #  310 CALL
        #  320 RAISE_VARARGS
        #  322 LOAD_CONST None
        #  324 RETURN_VALUE
        pass

    def wait_for_connect(self, timeout):
        ret = self.device.wait_for_connect(self.device, timeout)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    def _get_raw_remote_device(self):
        remote_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.get_remote_device(self.device, byref(remote_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return remote_ptr.contents

    def get_remote_device(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR _remote
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 22
        #   16 LOAD_CONST None
        #   18 STORE_FAST remote
        #   20 JUMP_FORWARD to 62
        #   22 LOAD_FAST self
        #   24 LOAD_METHOD _remote
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST remote
        #   62 LOAD_FAST remote
        #   64 POP_JUMP_FORWARD_IF_NOT_NONE to 198
        #   66 LOAD_FAST self
        #   68 LOAD_METHOD _get_raw_remote_device
        #   90 PRECALL
        #   94 CALL
        #  104 STORE_FAST remote_dev
        #  106 LOAD_GLOBAL NULL + AsphodelNativeDevice
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR lib
        #  130 LOAD_FAST remote_dev
        #  132 PRECALL
        #  136 CALL
        #  146 STORE_FAST remote
        #  148 LOAD_GLOBAL NULL + weakref
        #  160 LOAD_ATTR ref
        #  170 LOAD_FAST remote
        #  172 PRECALL
        #  176 CALL
        #  186 LOAD_FAST self
        #  188 STORE_ATTR _remote
        #  198 LOAD_FAST remote
        #  200 RETURN_VALUE
        pass

    def reconnect(self, bootloader, application, serial_number):
        if bootloader and application:
            raise ValueError('cannot set both application and bootloader')
        if bootloader:
            reconnect_func = self.reconnect_device_bootloader
        elif application:
            reconnect_func = self.reconnect_device_application
        else:
            reconnect_func = self.reconnect_device
        if not serial_number:
            
            try:
                serial_number = self.get_serial_number()
            except AsphodelError:
                pass

            end_time = time.monotonic() + self.reconnect_time
            time.sleep(0.5)
            
            try:
                reconnect_func(reopen = True)
            except AsphodelError:
                if time.monotonic() >= end_time:
                    raise 

            if serial_number:
                device = find_device_by_serial(serial_number)
                if device:
                    time.sleep(0.5)
                    
                    try:
                        reconnect_func(reopen = True)
                    except AsphodelError:
                        pass

                    time.sleep(0.5)
                    
                    try:
                        reconnect_func(reopen = True)
                    except AsphodelError:
                        pass

                    native_device = device.device
                    device.device = None
                    self._reconnect_helper(native_device, reopen = True)
                else:
                    time.sleep(0.25)
                self.wait_for_connect(int(self.reconnect_time * 1000))
                return None

    def _reconnect_helper(self, new_device, reopen):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + addressof
        #   14 LOAD_FAST new_device
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_GLOBAL NULL + addressof
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR device
        #   54 PRECALL
        #   58 CALL
        #   68 COMPARE_OP ==
        #   74 POP_JUMP_FORWARD_IF_FALSE to 80
        #   76 LOAD_CONST None
        #   78 RETURN_VALUE
        #   80 LOAD_FAST self
        #   82 LOAD_METHOD close
        #  104 PRECALL
        #  108 CALL
        #  118 POP_TOP
        #  120 LOAD_FAST self
        #  122 LOAD_ATTR device
        #  132 POP_JUMP_FORWARD_IF_FALSE to 196
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR device
        #  146 LOAD_METHOD free_device
        #  168 LOAD_FAST self
        #  170 LOAD_ATTR device
        #  180 PRECALL
        #  184 CALL
        #  194 POP_TOP
        #  196 LOAD_FAST new_device
        #  198 LOAD_FAST self
        #  200 STORE_ATTR device
        #  210 LOAD_FAST reopen
        #  212 POP_JUMP_FORWARD_IF_FALSE to 254
        #  214 LOAD_FAST self
        #  216 LOAD_METHOD open
        #  238 PRECALL
        #  242 CALL
        #  252 POP_TOP
        #  254 LOAD_FAST self
        #  256 LOAD_ATTR _remote
        #  266 POP_JUMP_FORWARD_IF_NONE to 548
        #  268 LOAD_FAST self
        #  270 LOAD_METHOD _remote
        #  292 PRECALL
        #  296 CALL
        #  306 STORE_FAST remote
        #  308 LOAD_FAST remote
        #  310 POP_JUMP_FORWARD_IF_FALSE to 548
        #  312 NOP
        #  314 LOAD_FAST self
        #  316 LOAD_METHOD _get_raw_remote_device
        #  338 PRECALL
        #  342 CALL
        #  352 STORE_FAST remote_dev
        #  354 LOAD_FAST remote
        #  356 LOAD_METHOD close
        #  378 PRECALL
        #  382 CALL
        #  392 POP_TOP
        #  394 LOAD_FAST remote
        #  396 LOAD_ATTR device
        #  406 LOAD_METHOD free_device
        #  428 LOAD_FAST remote
        #  430 LOAD_ATTR device
        #  440 PRECALL
        #  444 CALL
        #  454 POP_TOP
        #  456 LOAD_FAST remote_dev
        #  458 LOAD_FAST remote
        #  460 STORE_ATTR device
        #  470 LOAD_FAST reopen
        #  472 POP_JUMP_FORWARD_IF_FALSE to 514
        #  474 LOAD_FAST remote
        #  476 LOAD_METHOD open
        #  498 PRECALL
        #  502 CALL
        #  512 POP_TOP
        #  514 JUMP_FORWARD to 548
        # ... bytecode truncated ...
        pass

    def reconnect_device(self, reopen):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    def reconnect_device_bootloader(self, reopen):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device_bootloader(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    def reconnect_device_application(self, reopen):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device_application(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    def supports_rf_power_commands(self):
        v = self.lib.lib.asphodel_supports_rf_power_commands(self.device)
        return bool(v)

    def supports_radio_commands(self):
        v = self.lib.lib.asphodel_supports_radio_commands(self.device)
        return bool(v)

    def supports_remote_commands(self):
        v = self.lib.lib.asphodel_supports_remote_commands(self.device)
        return bool(v)

    def supports_bootloader_commands(self):
        v = self.lib.lib.asphodel_supports_bootloader_commands(self.device)
        return bool(v)

    def set_error_callback(self, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL callback
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + CFUNCTYPE
        #   18 LOAD_CONST None
        #   20 LOAD_GLOBAL NULL + POINTER
        #   32 LOAD_DEREF self
        #   34 LOAD_ATTR lib
        #   44 LOAD_ATTR AsphodelDeviceStruct
        #   54 PRECALL
        #   58 CALL
        #   68 LOAD_GLOBAL c_int
        #   80 LOAD_GLOBAL c_void_p
        #   92 PRECALL
        #   96 CALL
        #  106 STORE_FAST error_cb_type
        #  108 LOAD_DEREF callback
        #  110 POP_JUMP_FORWARD_IF_FALSE to 188
        #  112 LOAD_CLOSURE callback
        #  114 LOAD_CLOSURE self
        #  116 BUILD_TUPLE
        #  118 LOAD_CONST <code object cb at 0x105bb1530, file "asphodel\__init__.py", line 2689>
        #  120 MAKE_FUNCTION closure
        #  122 STORE_FAST cb
        #  124 PUSH_NULL
        #  126 LOAD_FAST error_cb_type
        #  128 LOAD_FAST cb
        #  130 PRECALL
        #  134 CALL
        #  144 STORE_FAST c_callback
        #  146 LOAD_FAST c_callback
        #  148 LOAD_DEREF self
        #  150 LOAD_ATTR device
        #  160 STORE_ATTR error_callback
        #  170 LOAD_FAST c_callback
        #  172 LOAD_DEREF self
        #  174 STORE_ATTR _error_callback
        #  184 LOAD_CONST None
        #  186 RETURN_VALUE
        #  188 PUSH_NULL
        #  190 LOAD_FAST error_cb_type
        #  192 PRECALL
        #  196 CALL
        #  206 LOAD_DEREF self
        #  208 LOAD_ATTR device
        #  218 STORE_ATTR error_callback
        #  228 LOAD_CONST None
        #  230 LOAD_DEREF self
        #  232 STORE_ATTR _error_callback
        #  242 LOAD_CONST None
        #  244 RETURN_VALUE
        pass

    def tcp_get_advertisement(self):
        return self.lib.tcp_get_advertisement(self.device)

    def get_protocol_version(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint16
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST version
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST version
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST version
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_protocol_version_string(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_board_info(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST rev
        #   34 LOAD_GLOBAL NULL + create_string_buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR MAX_STRING_LENGTH
        #   58 PRECALL
        #   62 CALL
        #   72 STORE_FAST buffer
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR device
        #   86 LOAD_GLOBAL NULL + byref
        #   98 LOAD_FAST rev
        #  100 PRECALL
        #  104 CALL
        #  114 LOAD_GLOBAL NULL + cast
        #  126 LOAD_GLOBAL NULL + byref
        #  138 LOAD_FAST buffer
        #  140 PRECALL
        #  144 CALL
        #  154 LOAD_GLOBAL c_char_p
        #  166 PRECALL
        #  170 CALL
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR MAX_STRING_LENGTH
        #  192 BUILD_TUPLE
        #  194 YIELD_VALUE
        #  196 RESUME
        #  198 POP_TOP
        #  200 LOAD_FAST buffer
        #  202 LOAD_ATTR value
        #  212 LOAD_METHOD decode
        #  234 LOAD_CONST 'UTF-8'
        #  236 PRECALL
        #  240 CALL
        #  250 LOAD_FAST rev
        #  252 LOAD_ATTR value
        #  262 BUILD_TUPLE
        #  264 RETURN_VALUE
        pass

    def get_user_tag_locations(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_size_t
        #   18 LOAD_CONST 6
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST array
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR device
        #   52 LOAD_FAST array
        #   54 BUILD_TUPLE
        #   56 YIELD_VALUE
        #   58 RESUME
        #   60 POP_TOP
        #   62 LOAD_GLOBAL NULL + tuple
        #   74 LOAD_FAST array
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST values
        #   92 LOAD_GLOBAL NULL + tuple
        #  104 LOAD_GLOBAL NULL + zip
        #  116 LOAD_FAST values
        #  118 LOAD_CONST 0
        #  120 LOAD_CONST None
        #  122 LOAD_CONST 2
        #  124 BUILD_SLICE
        #  126 BINARY_SUBSCR
        #  136 LOAD_FAST values
        #  138 LOAD_CONST 1
        #  140 LOAD_CONST None
        #  142 LOAD_CONST 2
        #  144 BUILD_SLICE
        #  146 BINARY_SUBSCR
        #  156 PRECALL
        #  160 CALL
        #  170 PRECALL
        #  174 CALL
        #  184 RETURN_VALUE
        pass

    def get_build_info(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_build_date(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_commit_id(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_repo_branch(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_repo_name(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_chip_family(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_chip_model(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_chip_id(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_nvm_size(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_size_t
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST size
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST size
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST size
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def erase_nvm(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def write_nvm_raw(self, address, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL c_uint8
        #   18 LOAD_GLOBAL NULL + len
        #   30 LOAD_FAST values
        #   32 PRECALL
        #   36 CALL
        #   46 BINARY_OP *
        #   50 LOAD_METHOD from_buffer_copy
        #   72 LOAD_GLOBAL NULL + bytes
        #   84 LOAD_FAST values
        #   86 PRECALL
        #   90 CALL
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST data
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR device
        #  128 LOAD_FAST address
        #  130 LOAD_GLOBAL NULL + cast
        #  142 LOAD_GLOBAL NULL + byref
        #  154 LOAD_FAST data
        #  156 PRECALL
        #  160 CALL
        #  170 LOAD_GLOBAL NULL + POINTER
        #  182 LOAD_GLOBAL c_uint8
        #  194 PRECALL
        #  198 CALL
        #  208 PRECALL
        #  212 CALL
        #  222 LOAD_GLOBAL NULL + len
        #  234 LOAD_FAST values
        #  236 PRECALL
        #  240 CALL
        #  250 BUILD_TUPLE
        #  252 YIELD_VALUE
        #  254 RESUME
        #  256 POP_TOP
        #  258 LOAD_CONST None
        #  260 RETURN_VALUE
        pass

    def write_nvm_section(self, address, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL c_uint8
        #   18 LOAD_GLOBAL NULL + len
        #   30 LOAD_FAST values
        #   32 PRECALL
        #   36 CALL
        #   46 BINARY_OP *
        #   50 LOAD_METHOD from_buffer_copy
        #   72 LOAD_GLOBAL NULL + bytes
        #   84 LOAD_FAST values
        #   86 PRECALL
        #   90 CALL
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST data
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR device
        #  128 LOAD_FAST address
        #  130 LOAD_GLOBAL NULL + cast
        #  142 LOAD_GLOBAL NULL + byref
        #  154 LOAD_FAST data
        #  156 PRECALL
        #  160 CALL
        #  170 LOAD_GLOBAL NULL + POINTER
        #  182 LOAD_GLOBAL c_uint8
        #  194 PRECALL
        #  198 CALL
        #  208 PRECALL
        #  212 CALL
        #  222 LOAD_GLOBAL NULL + len
        #  234 LOAD_FAST values
        #  236 PRECALL
        #  240 CALL
        #  250 BUILD_TUPLE
        #  252 YIELD_VALUE
        #  254 RESUME
        #  256 POP_TOP
        #  258 LOAD_CONST None
        #  260 RETURN_VALUE
        pass

    def read_nvm_raw(self, address):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_METHOD get_max_incoming_param_length
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST max_length
        #   46 LOAD_GLOBAL NULL + c_uint8
        #   58 LOAD_FAST max_length
        #   60 BINARY_OP *
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST data
        #   80 LOAD_GLOBAL NULL + c_size_t
        #   92 LOAD_FAST max_length
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST data_length
        #  110 LOAD_FAST self
        #  112 LOAD_ATTR device
        #  122 LOAD_FAST address
        #  124 LOAD_GLOBAL NULL + cast
        #  136 LOAD_GLOBAL NULL + byref
        #  148 LOAD_FAST data
        #  150 PRECALL
        #  154 CALL
        #  164 LOAD_GLOBAL NULL + POINTER
        #  176 LOAD_GLOBAL c_uint8
        #  188 PRECALL
        #  192 CALL
        #  202 PRECALL
        #  206 CALL
        #  216 LOAD_GLOBAL NULL + byref
        #  228 LOAD_FAST data_length
        #  230 PRECALL
        #  234 CALL
        #  244 BUILD_TUPLE
        #  246 YIELD_VALUE
        #  248 RESUME
        #  250 POP_TOP
        #  252 LOAD_GLOBAL NULL + min
        #  264 LOAD_FAST max_length
        #  266 LOAD_FAST data_length
        #  268 LOAD_ATTR value
        #  278 PRECALL
        #  282 CALL
        #  292 STORE_FAST actual_length
        #  294 LOAD_GLOBAL NULL + bytes
        #  306 LOAD_FAST data
        #  308 LOAD_CONST 0
        #  310 LOAD_FAST actual_length
        #  312 BUILD_SLICE
        #  314 BINARY_SUBSCR
        #  324 PRECALL
        #  328 CALL
        #  338 RETURN_VALUE
        pass

    def read_nvm_section(self, address, length):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_FAST length
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST data
        #   40 LOAD_GLOBAL NULL + c_size_t
        #   52 LOAD_FAST length
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST data_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST address
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST data
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_uint8
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_FAST data_length
        #  178 BUILD_TUPLE
        #  180 YIELD_VALUE
        #  182 RESUME
        #  184 POP_TOP
        #  186 LOAD_GLOBAL NULL + bytes
        #  198 LOAD_FAST data
        #  200 PRECALL
        #  204 CALL
        #  214 RETURN_VALUE
        pass

    def read_user_tag_string(self, offset, length):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST length
        #   20 LOAD_CONST 1
        #   22 BINARY_OP +
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST buffer
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR device
        #   54 LOAD_FAST offset
        #   56 LOAD_FAST length
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 BUILD_TUPLE
        #  126 YIELD_VALUE
        #  128 RESUME
        #  130 POP_TOP
        #  132 LOAD_FAST buffer
        #  134 LOAD_ATTR value
        #  144 LOAD_METHOD decode
        #  166 LOAD_CONST 'UTF-8'
        #  168 PRECALL
        #  172 CALL
        #  182 RETURN_VALUE
        pass

    def write_user_tag_string(self, offset, length, string):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 PUSH_NULL
        #   20 LOAD_FAST string
        #   22 LOAD_ATTR encode
        #   32 LOAD_CONST 'UTF-8'
        #   34 PRECALL
        #   38 CALL
        #   48 PRECALL
        #   52 CALL
        #   62 STORE_FAST buffer
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR device
        #   76 LOAD_FAST offset
        #   78 LOAD_FAST length
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 BUILD_TUPLE
        #  148 YIELD_VALUE
        #  150 RESUME
        #  152 POP_TOP
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        pass

    def get_nvm_modified(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST modified
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST modified
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_GLOBAL NULL + bool
        #   94 LOAD_FAST modified
        #   96 LOAD_ATTR value
        #  106 PRECALL
        #  110 CALL
        #  120 RETURN_VALUE
        pass

    def get_nvm_hash(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def get_setting_hash(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def flush(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def reset(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_bootloader_info(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR MAX_STRING_LENGTH
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST buffer
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR device
        #   58 LOAD_GLOBAL NULL + cast
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST buffer
        #   84 PRECALL
        #   88 CALL
        #   98 LOAD_GLOBAL c_char_p
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR MAX_STRING_LENGTH
        #  136 BUILD_TUPLE
        #  138 YIELD_VALUE
        #  140 RESUME
        #  142 POP_TOP
        #  144 LOAD_FAST buffer
        #  146 LOAD_ATTR value
        #  156 LOAD_METHOD decode
        #  178 LOAD_CONST 'UTF-8'
        #  180 PRECALL
        #  184 CALL
        #  194 RETURN_VALUE
        pass

    def bootloader_jump(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_reset_flag(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST flag
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST flag
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST flag
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def clear_reset_flag(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_rgb_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_rgb_values(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 3
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST values
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR device
        #   52 LOAD_FAST index
        #   54 LOAD_FAST values
        #   56 BUILD_TUPLE
        #   58 YIELD_VALUE
        #   60 RESUME
        #   62 POP_TOP
        #   64 LOAD_GLOBAL NULL + tuple
        #   76 LOAD_FAST values
        #   78 PRECALL
        #   82 CALL
        #   92 RETURN_VALUE
        pass

    def set_rgb_values(self, index, values, instant):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL c_uint8
        #   18 LOAD_CONST 3
        #   20 BINARY_OP *
        #   24 LOAD_METHOD from_buffer_copy
        #   46 LOAD_GLOBAL NULL + bytes
        #   58 LOAD_FAST values
        #   60 PRECALL
        #   64 CALL
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST array
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR device
        #  102 LOAD_FAST index
        #  104 LOAD_FAST array
        #  106 LOAD_FAST instant
        #  108 BUILD_TUPLE
        #  110 YIELD_VALUE
        #  112 RESUME
        #  114 POP_TOP
        #  116 LOAD_CONST None
        #  118 RETURN_VALUE
        pass

    def set_rgb_values_hex(self, index, hex_color, instant):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST hex_color
        #   22 LOAD_FAST instant
        #   24 BUILD_TUPLE
        #   26 YIELD_VALUE
        #   28 RESUME
        #   30 POP_TOP
        #   32 LOAD_CONST None
        #   34 RETURN_VALUE
        pass

    def get_led_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_led_value(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST value
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST value
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_FAST value
        #   86 LOAD_ATTR value
        #   96 RETURN_VALUE
        pass

    def set_led_value(self, index, value, instant):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST value
        #   22 LOAD_FAST instant
        #   24 BUILD_TUPLE
        #   26 YIELD_VALUE
        #   28 RESUME
        #   30 POP_TOP
        #   32 LOAD_CONST None
        #   34 RETURN_VALUE
        pass

    def set_device_mode(self, mode):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST mode
        #   20 BUILD_TUPLE
        #   22 YIELD_VALUE
        #   24 RESUME
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        pass

    def get_device_mode(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST mode
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST mode
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST mode
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_stream_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_GLOBAL NULL + c_uint8
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST filler_bits
        #   62 LOAD_GLOBAL NULL + c_uint8
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST id_bits
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR device
        #  102 LOAD_GLOBAL NULL + byref
        #  114 LOAD_FAST count
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_GLOBAL NULL + byref
        #  142 LOAD_FAST filler_bits
        #  144 PRECALL
        #  148 CALL
        #  158 LOAD_GLOBAL NULL + byref
        #  170 LOAD_FAST id_bits
        #  172 PRECALL
        #  176 CALL
        #  186 BUILD_TUPLE
        #  188 YIELD_VALUE
        #  190 RESUME
        #  192 POP_TOP
        #  194 LOAD_FAST count
        #  196 LOAD_ATTR value
        #  206 LOAD_FAST filler_bits
        #  208 LOAD_ATTR value
        #  218 LOAD_FAST id_bits
        #  220 LOAD_ATTR value
        #  230 BUILD_TUPLE
        #  232 RETURN_VALUE
        pass

    def get_stream(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 PUSH_NULL
        #    8 LOAD_GLOBAL NULL + POINTER
        #   20 LOAD_GLOBAL AsphodelStreamInfo
        #   32 PRECALL
        #   36 CALL
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST ptr
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR device
        #   74 LOAD_FAST index
        #   76 LOAD_GLOBAL NULL + byref
        #   88 LOAD_FAST ptr
        #   90 PRECALL
        #   94 CALL
        #  104 BUILD_TUPLE
        #  106 YIELD_VALUE
        #  108 RESUME
        #  110 POP_TOP
        #  112 LOAD_FAST ptr
        #  114 LOAD_ATTR contents
        #  124 STORE_FAST stream
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR lib
        #  138 LOAD_ATTR lib
        #  148 LOAD_ATTR asphodel_free_stream
        #  158 LOAD_FAST stream
        #  160 STORE_ATTR _free_func
        #  170 LOAD_FAST stream
        #  172 RETURN_VALUE
        pass

    def get_stream_channels(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST channels
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST channels_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST channels
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_uint8
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + byref
        #  188 LOAD_FAST channels_length
        #  190 PRECALL
        #  194 CALL
        #  204 BUILD_TUPLE
        #  206 YIELD_VALUE
        #  208 RESUME
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + tuple
        #  224 LOAD_FAST channels
        #  226 LOAD_CONST 0
        #  228 LOAD_FAST channels_length
        #  230 LOAD_ATTR value
        #  240 BUILD_SLICE
        #  242 BINARY_SUBSCR
        #  252 PRECALL
        #  256 CALL
        #  266 RETURN_VALUE
        pass

    def get_stream_format(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + AsphodelStreamInfo
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST info
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST info
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_GLOBAL NULL + StreamFormat
        #   96 LOAD_FAST info
        #   98 LOAD_ATTR filler_bits
        #  108 LOAD_FAST info
        #  110 LOAD_ATTR counter_bits
        #  120 LOAD_FAST info
        #  122 LOAD_ATTR rate
        #  132 LOAD_FAST info
        #  134 LOAD_ATTR rate_error
        #  144 LOAD_FAST info
        #  146 LOAD_ATTR warm_up_delay
        #  156 PRECALL
        #  160 CALL
        #  170 RETURN_VALUE
        pass

    def enable_stream(self, index, enable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST enable
        #   22 BUILD_TUPLE
        #   24 YIELD_VALUE
        #   26 RESUME
        #   28 POP_TOP
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        pass

    def warm_up_stream(self, index, enable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST enable
        #   22 BUILD_TUPLE
        #   24 YIELD_VALUE
        #   26 RESUME
        #   28 POP_TOP
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        pass

    def get_stream_status(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST enable
        #   34 LOAD_GLOBAL NULL + c_int
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST warm_up
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR device
        #   74 LOAD_FAST index
        #   76 LOAD_GLOBAL NULL + byref
        #   88 LOAD_FAST enable
        #   90 PRECALL
        #   94 CALL
        #  104 LOAD_GLOBAL NULL + byref
        #  116 LOAD_FAST warm_up
        #  118 PRECALL
        #  122 CALL
        #  132 BUILD_TUPLE
        #  134 YIELD_VALUE
        #  136 RESUME
        #  138 POP_TOP
        #  140 LOAD_GLOBAL NULL + bool
        #  152 LOAD_FAST enable
        #  154 LOAD_ATTR value
        #  164 PRECALL
        #  168 CALL
        #  178 LOAD_GLOBAL NULL + bool
        #  190 LOAD_FAST warm_up
        #  192 LOAD_ATTR value
        #  202 PRECALL
        #  206 CALL
        #  216 BUILD_TUPLE
        #  218 RETURN_VALUE
        pass

    def get_stream_rate_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST available
        #   34 LOAD_GLOBAL NULL + c_int
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST channel_index
        #   62 LOAD_GLOBAL NULL + c_int
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST invert
        #   90 LOAD_GLOBAL NULL + c_float
        #  102 PRECALL
        #  106 CALL
        #  116 STORE_FAST scale
        #  118 LOAD_GLOBAL NULL + c_float
        #  130 PRECALL
        #  134 CALL
        #  144 STORE_FAST offset
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR device
        #  158 LOAD_FAST index
        #  160 LOAD_GLOBAL NULL + byref
        #  172 LOAD_FAST available
        #  174 PRECALL
        #  178 CALL
        #  188 LOAD_GLOBAL NULL + byref
        #  200 LOAD_FAST channel_index
        #  202 PRECALL
        #  206 CALL
        #  216 LOAD_GLOBAL NULL + byref
        #  228 LOAD_FAST invert
        #  230 PRECALL
        #  234 CALL
        #  244 LOAD_GLOBAL NULL + byref
        #  256 LOAD_FAST scale
        #  258 PRECALL
        #  262 CALL
        #  272 LOAD_GLOBAL NULL + byref
        #  284 LOAD_FAST offset
        #  286 PRECALL
        #  290 CALL
        #  300 BUILD_TUPLE
        #  302 YIELD_VALUE
        #  304 RESUME
        #  306 POP_TOP
        #  308 LOAD_GLOBAL NULL + StreamRateInfo
        #  320 LOAD_GLOBAL NULL + bool
        #  332 LOAD_FAST available
        #  334 LOAD_ATTR value
        #  344 PRECALL
        #  348 CALL
        #  358 LOAD_FAST channel_index
        #  360 LOAD_ATTR value
        #  370 LOAD_FAST invert
        #  372 LOAD_ATTR value
        #  382 LOAD_FAST scale
        #  384 LOAD_ATTR value
        #  394 LOAD_FAST offset
        #  396 LOAD_ATTR value
        #  406 PRECALL
        #  410 CALL
        #  420 RETURN_VALUE
        pass

    def get_channel_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_channel(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 PUSH_NULL
        #    8 LOAD_GLOBAL NULL + POINTER
        #   20 LOAD_GLOBAL AsphodelChannelInfo
        #   32 PRECALL
        #   36 CALL
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST ptr
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR device
        #   74 LOAD_FAST index
        #   76 LOAD_GLOBAL NULL + byref
        #   88 LOAD_FAST ptr
        #   90 PRECALL
        #   94 CALL
        #  104 BUILD_TUPLE
        #  106 YIELD_VALUE
        #  108 RESUME
        #  110 POP_TOP
        #  112 LOAD_FAST ptr
        #  114 LOAD_ATTR contents
        #  124 STORE_FAST channel
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR lib
        #  138 LOAD_ATTR lib
        #  148 LOAD_ATTR asphodel_free_channel
        #  158 LOAD_FAST channel
        #  160 STORE_ATTR _free_func
        #  170 LOAD_FAST channel
        #  172 RETURN_VALUE
        pass

    def get_channel_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_channel_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + AsphodelChannelInfo
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST info
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST info
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_GLOBAL NULL + ChannelInfo
        #   96 LOAD_FAST info
        #   98 LOAD_ATTR channel_type
        #  108 LOAD_FAST info
        #  110 LOAD_ATTR unit_type
        #  120 LOAD_FAST info
        #  122 LOAD_ATTR filler_bits
        #  132 LOAD_FAST info
        #  134 LOAD_ATTR data_bits
        #  144 LOAD_FAST info
        #  146 LOAD_ATTR samples
        #  156 LOAD_FAST info
        #  158 LOAD_ATTR bits_per_sample
        #  168 LOAD_FAST info
        #  170 LOAD_ATTR minimum
        #  180 LOAD_FAST info
        #  182 LOAD_ATTR maximum
        #  192 LOAD_FAST info
        #  194 LOAD_ATTR resolution
        #  204 LOAD_FAST info
        #  206 LOAD_ATTR chunk_count
        #  216 PRECALL
        #  220 CALL
        #  230 RETURN_VALUE
        pass

    def get_channel_coefficients(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_float
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST coefficients
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST coefficients_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST coefficients
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_float
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + byref
        #  188 LOAD_FAST coefficients_length
        #  190 PRECALL
        #  194 CALL
        #  204 BUILD_TUPLE
        #  206 YIELD_VALUE
        #  208 RESUME
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + tuple
        #  224 LOAD_FAST coefficients
        #  226 LOAD_CONST 0
        #  228 LOAD_FAST coefficients_length
        #  230 LOAD_ATTR value
        #  240 BUILD_SLICE
        #  242 BINARY_SUBSCR
        #  252 PRECALL
        #  256 CALL
        #  266 RETURN_VALUE
        pass

    def get_channel_chunk(self, index, chunk_number):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST chunk
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST chunk_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_FAST chunk_number
        #   86 LOAD_GLOBAL NULL + cast
        #   98 LOAD_GLOBAL NULL + byref
        #  110 LOAD_FAST chunk
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_GLOBAL NULL + POINTER
        #  138 LOAD_GLOBAL c_uint8
        #  150 PRECALL
        #  154 CALL
        #  164 PRECALL
        #  168 CALL
        #  178 LOAD_GLOBAL NULL + byref
        #  190 LOAD_FAST chunk_length
        #  192 PRECALL
        #  196 CALL
        #  206 BUILD_TUPLE
        #  208 YIELD_VALUE
        #  210 RESUME
        #  212 POP_TOP
        #  214 LOAD_GLOBAL NULL + bytes
        #  226 LOAD_FAST chunk
        #  228 LOAD_CONST 0
        #  230 LOAD_FAST chunk_length
        #  232 LOAD_ATTR value
        #  242 BUILD_SLICE
        #  244 BINARY_SUBSCR
        #  254 PRECALL
        #  258 CALL
        #  268 RETURN_VALUE
        pass

    def channel_specific(self, index, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST reply
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST reply_length
        #   70 LOAD_GLOBAL NULL + c_uint8
        #   82 LOAD_GLOBAL NULL + len
        #   94 LOAD_FAST values
        #   96 PRECALL
        #  100 CALL
        #  110 BINARY_OP *
        #  114 PRECALL
        #  118 CALL
        #  128 STORE_FAST data
        #  130 LOAD_GLOBAL NULL + range
        #  142 LOAD_GLOBAL NULL + len
        #  154 LOAD_FAST values
        #  156 PRECALL
        #  160 CALL
        #  170 PRECALL
        #  174 CALL
        #  184 GET_ITER
        #  186 FOR_ITER to 214
        #  188 STORE_FAST i
        #  190 LOAD_FAST values
        #  192 LOAD_FAST i
        #  194 BINARY_SUBSCR
        #  204 LOAD_FAST data
        #  206 LOAD_FAST i
        #  208 STORE_SUBSCR
        #  212 JUMP_BACKWARD to 186
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR device
        #  226 LOAD_FAST index
        #  228 LOAD_GLOBAL NULL + cast
        #  240 LOAD_GLOBAL NULL + byref
        #  252 LOAD_FAST data
        #  254 PRECALL
        #  258 CALL
        #  268 LOAD_GLOBAL NULL + POINTER
        #  280 LOAD_GLOBAL c_uint8
        #  292 PRECALL
        #  296 CALL
        #  306 PRECALL
        #  310 CALL
        #  320 LOAD_GLOBAL NULL + len
        #  332 LOAD_FAST values
        #  334 PRECALL
        #  338 CALL
        #  348 LOAD_GLOBAL NULL + cast
        #  360 LOAD_GLOBAL NULL + byref
        #  372 LOAD_FAST reply
        #  374 PRECALL
        #  378 CALL
        #  388 LOAD_GLOBAL NULL + POINTER
        #  400 LOAD_GLOBAL c_uint8
        #  412 PRECALL
        #  416 CALL
        #  426 PRECALL
        #  430 CALL
        #  440 LOAD_GLOBAL NULL + byref
        #  452 LOAD_FAST reply_length
        #  454 PRECALL
        #  458 CALL
        #  468 BUILD_TUPLE
        #  470 YIELD_VALUE
        #  472 RESUME
        #  474 POP_TOP
        #  476 LOAD_GLOBAL NULL + bytes
        #  488 LOAD_FAST reply
        #  490 LOAD_CONST 0
        # ... bytecode truncated ...
        pass

    def get_channel_calibration(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST available
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR lib
        #   46 LOAD_METHOD AsphodelChannelCalibration
        #   68 PRECALL
        #   72 CALL
        #   82 STORE_FAST cal
        #   84 LOAD_FAST self
        #   86 LOAD_ATTR device
        #   96 LOAD_FAST index
        #   98 LOAD_GLOBAL NULL + byref
        #  110 LOAD_FAST available
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_GLOBAL NULL + byref
        #  138 LOAD_FAST cal
        #  140 PRECALL
        #  144 CALL
        #  154 BUILD_TUPLE
        #  156 YIELD_VALUE
        #  158 RESUME
        #  160 POP_TOP
        #  162 LOAD_GLOBAL NULL + bool
        #  174 LOAD_FAST available
        #  176 LOAD_ATTR value
        #  186 PRECALL
        #  190 CALL
        #  200 POP_JUMP_FORWARD_IF_TRUE to 206
        #  202 LOAD_CONST None
        #  204 RETURN_VALUE
        #  206 LOAD_GLOBAL NULL + ChannelCalibration
        #  218 LOAD_FAST cal
        #  220 LOAD_ATTR base_setting_index
        #  230 LOAD_FAST cal
        #  232 LOAD_ATTR resolution_setting_index
        #  242 LOAD_FAST cal
        #  244 LOAD_ATTR scale
        #  254 LOAD_FAST cal
        #  256 LOAD_ATTR offset
        #  266 LOAD_FAST cal
        #  268 LOAD_ATTR minimum
        #  278 LOAD_FAST cal
        #  280 LOAD_ATTR maximum
        #  290 PRECALL
        #  294 CALL
        #  304 RETURN_VALUE
        pass

    def get_supply_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_supply_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_supply_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR lib
        #   18 LOAD_METHOD AsphodelSupplyInfo
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST info
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR device
        #   68 LOAD_FAST index
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST info
        #   84 PRECALL
        #   88 CALL
        #   98 BUILD_TUPLE
        #  100 YIELD_VALUE
        #  102 RESUME
        #  104 POP_TOP
        #  106 LOAD_GLOBAL NULL + SupplyInfo
        #  118 LOAD_FAST info
        #  120 LOAD_ATTR unit_type
        #  130 LOAD_FAST info
        #  132 LOAD_ATTR is_battery
        #  142 LOAD_FAST info
        #  144 LOAD_ATTR nominal
        #  154 LOAD_FAST info
        #  156 LOAD_ATTR scale
        #  166 LOAD_FAST info
        #  168 LOAD_ATTR offset
        #  178 PRECALL
        #  182 CALL
        #  192 RETURN_VALUE
        pass

    def check_supply(self, index, tries):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int32
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST measurement
        #   34 LOAD_GLOBAL NULL + c_uint8
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST result
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR device
        #   74 LOAD_FAST index
        #   76 LOAD_GLOBAL NULL + byref
        #   88 LOAD_FAST measurement
        #   90 PRECALL
        #   94 CALL
        #  104 LOAD_GLOBAL NULL + byref
        #  116 LOAD_FAST result
        #  118 PRECALL
        #  122 CALL
        #  132 LOAD_FAST tries
        #  134 BUILD_TUPLE
        #  136 YIELD_VALUE
        #  138 RESUME
        #  140 POP_TOP
        #  142 LOAD_FAST measurement
        #  144 LOAD_ATTR value
        #  154 LOAD_FAST result
        #  156 LOAD_ATTR value
        #  166 BUILD_TUPLE
        #  168 RETURN_VALUE
        pass

    def get_ctrl_var_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_ctrl_var_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_ctrl_var_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR lib
        #   18 LOAD_METHOD AsphodelCtrlVarInfo
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST info
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR device
        #   68 LOAD_FAST index
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST info
        #   84 PRECALL
        #   88 CALL
        #   98 BUILD_TUPLE
        #  100 YIELD_VALUE
        #  102 RESUME
        #  104 POP_TOP
        #  106 LOAD_GLOBAL NULL + CtrlVarInfo
        #  118 LOAD_FAST info
        #  120 LOAD_ATTR unit_type
        #  130 LOAD_FAST info
        #  132 LOAD_ATTR minimum
        #  142 LOAD_FAST info
        #  144 LOAD_ATTR maximum
        #  154 LOAD_FAST info
        #  156 LOAD_ATTR scale
        #  166 LOAD_FAST info
        #  168 LOAD_ATTR offset
        #  178 PRECALL
        #  182 CALL
        #  192 RETURN_VALUE
        pass

    def get_ctrl_var(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int32
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST value
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST value
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_FAST value
        #   86 LOAD_ATTR value
        #   96 RETURN_VALUE
        pass

    def set_ctrl_var(self, index, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST value
        #   22 BUILD_TUPLE
        #   24 YIELD_VALUE
        #   26 RESUME
        #   28 POP_TOP
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        pass

    def get_setting_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_setting_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_setting_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + AsphodelSettingInfo
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST info
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST info
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_FAST info
        #   86 RETURN_VALUE
        pass

    def get_setting_default(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST default
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST default_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST default
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_uint8
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + byref
        #  188 LOAD_FAST default_length
        #  190 PRECALL
        #  194 CALL
        #  204 BUILD_TUPLE
        #  206 YIELD_VALUE
        #  208 RESUME
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + bytes
        #  224 LOAD_FAST default
        #  226 LOAD_CONST 0
        #  228 LOAD_FAST default_length
        #  230 LOAD_ATTR value
        #  240 BUILD_SLICE
        #  242 BINARY_SUBSCR
        #  252 PRECALL
        #  256 CALL
        #  266 RETURN_VALUE
        pass

    def get_custom_enum_counts(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST counts
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST counts_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST counts
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint8
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST counts_length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_GLOBAL NULL + tuple
        #  222 LOAD_FAST counts
        #  224 LOAD_CONST 0
        #  226 LOAD_FAST counts_length
        #  228 LOAD_ATTR value
        #  238 BUILD_SLICE
        #  240 BINARY_SUBSCR
        #  250 PRECALL
        #  254 CALL
        #  264 RETURN_VALUE
        pass

    def get_custom_enum_value_name(self, index, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_FAST value
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST buffer
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL c_char_p
        #  134 PRECALL
        #  138 CALL
        #  148 LOAD_GLOBAL NULL + byref
        #  160 LOAD_FAST buffer_length
        #  162 PRECALL
        #  166 CALL
        #  176 BUILD_TUPLE
        #  178 YIELD_VALUE
        #  180 RESUME
        #  182 POP_TOP
        #  184 LOAD_FAST buffer
        #  186 LOAD_CONST 0
        #  188 LOAD_FAST buffer_length
        #  190 LOAD_ATTR value
        #  200 BUILD_SLICE
        #  202 BINARY_SUBSCR
        #  212 LOAD_METHOD decode
        #  234 LOAD_CONST 'UTF-8'
        #  236 PRECALL
        #  240 CALL
        #  250 RETURN_VALUE
        pass

    def get_setting_category_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_setting_category_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_setting_category_settings(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST settings
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST settings_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST settings
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_uint8
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + byref
        #  188 LOAD_FAST settings_length
        #  190 PRECALL
        #  194 CALL
        #  204 BUILD_TUPLE
        #  206 YIELD_VALUE
        #  208 RESUME
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + tuple
        #  224 LOAD_FAST settings
        #  226 LOAD_CONST 0
        #  228 LOAD_FAST settings_length
        #  230 LOAD_ATTR value
        #  240 BUILD_SLICE
        #  242 BINARY_SUBSCR
        #  252 PRECALL
        #  256 CALL
        #  266 RETURN_VALUE
        pass

    def get_gpio_port_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_gpio_port_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_gpio_port_info(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR lib
        #   18 LOAD_METHOD AsphodelGPIOPortInfo
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST info
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR device
        #   68 LOAD_FAST index
        #   70 LOAD_GLOBAL NULL + byref
        #   82 LOAD_FAST info
        #   84 PRECALL
        #   88 CALL
        #   98 BUILD_TUPLE
        #  100 YIELD_VALUE
        #  102 RESUME
        #  104 POP_TOP
        #  106 LOAD_GLOBAL NULL + GPIOPortInfo
        #  118 LOAD_FAST info
        #  120 LOAD_ATTR input_pins
        #  130 LOAD_FAST info
        #  132 LOAD_ATTR output_pins
        #  142 LOAD_FAST info
        #  144 LOAD_ATTR floating_pins
        #  154 LOAD_FAST info
        #  156 LOAD_ATTR loaded_pins
        #  166 LOAD_FAST info
        #  168 LOAD_ATTR overridden_pins
        #  178 PRECALL
        #  182 CALL
        #  192 RETURN_VALUE
        pass

    def get_gpio_port_values(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST pin_values
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_FAST index
        #   48 LOAD_GLOBAL NULL + byref
        #   60 LOAD_FAST pin_values
        #   62 PRECALL
        #   66 CALL
        #   76 BUILD_TUPLE
        #   78 YIELD_VALUE
        #   80 RESUME
        #   82 POP_TOP
        #   84 LOAD_FAST pin_values
        #   86 LOAD_ATTR value
        #   96 RETURN_VALUE
        pass

    def set_gpio_port_modes(self, index, mode, pins):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST mode
        #   22 LOAD_FAST pins
        #   24 BUILD_TUPLE
        #   26 YIELD_VALUE
        #   28 RESUME
        #   30 POP_TOP
        #   32 LOAD_CONST None
        #   34 RETURN_VALUE
        pass

    def disable_gpio_overrides(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_bus_counts(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST spi_count
        #   34 LOAD_GLOBAL NULL + c_int
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST i2c_count
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR device
        #   74 LOAD_GLOBAL NULL + byref
        #   86 LOAD_FAST spi_count
        #   88 PRECALL
        #   92 CALL
        #  102 LOAD_GLOBAL NULL + byref
        #  114 LOAD_FAST i2c_count
        #  116 PRECALL
        #  120 CALL
        #  130 BUILD_TUPLE
        #  132 YIELD_VALUE
        #  134 RESUME
        #  136 POP_TOP
        #  138 LOAD_FAST spi_count
        #  140 LOAD_ATTR value
        #  150 LOAD_FAST i2c_count
        #  152 LOAD_ATTR value
        #  162 BUILD_TUPLE
        #  164 RETURN_VALUE
        pass

    def set_spi_cs_mode(self, index, mode):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST index
        #   20 LOAD_FAST mode
        #   22 BUILD_TUPLE
        #   24 YIELD_VALUE
        #   26 RESUME
        #   28 POP_TOP
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        pass

    def do_spi_transfer(self, index, write_bytes):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST write_bytes
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST data_length
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST data_length
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_GLOBAL NULL + bytes
        #   88 LOAD_FAST write_bytes
        #   90 PRECALL
        #   94 CALL
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST tx_data
        #  120 LOAD_GLOBAL NULL + c_uint8
        #  132 LOAD_FAST data_length
        #  134 BINARY_OP *
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST rx_data
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR device
        #  166 LOAD_FAST index
        #  168 LOAD_GLOBAL NULL + cast
        #  180 LOAD_GLOBAL NULL + byref
        #  192 LOAD_FAST tx_data
        #  194 PRECALL
        #  198 CALL
        #  208 LOAD_GLOBAL NULL + POINTER
        #  220 LOAD_GLOBAL c_uint8
        #  232 PRECALL
        #  236 CALL
        #  246 PRECALL
        #  250 CALL
        #  260 LOAD_GLOBAL NULL + cast
        #  272 LOAD_GLOBAL NULL + byref
        #  284 LOAD_FAST rx_data
        #  286 PRECALL
        #  290 CALL
        #  300 LOAD_GLOBAL NULL + POINTER
        #  312 LOAD_GLOBAL c_uint8
        #  324 PRECALL
        #  328 CALL
        #  338 PRECALL
        #  342 CALL
        #  352 LOAD_FAST data_length
        #  354 BUILD_TUPLE
        #  356 YIELD_VALUE
        #  358 RESUME
        #  360 POP_TOP
        #  362 LOAD_GLOBAL NULL + bytes
        #  374 LOAD_FAST rx_data
        #  376 LOAD_CONST 0
        #  378 LOAD_FAST data_length
        #  380 BUILD_SLICE
        #  382 BINARY_SUBSCR
        #  392 PRECALL
        #  396 CALL
        #  406 RETURN_VALUE
        pass

    def do_i2c_write(self, index, addr, write_bytes):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST write_bytes
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST data_length
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST data_length
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_GLOBAL NULL + bytes
        #   88 LOAD_FAST write_bytes
        #   90 PRECALL
        #   94 CALL
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST tx_data
        #  120 LOAD_FAST self
        #  122 LOAD_ATTR device
        #  132 LOAD_FAST index
        #  134 LOAD_FAST addr
        #  136 LOAD_GLOBAL NULL + cast
        #  148 LOAD_GLOBAL NULL + byref
        #  160 LOAD_FAST tx_data
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + POINTER
        #  188 LOAD_GLOBAL c_uint8
        #  200 PRECALL
        #  204 CALL
        #  214 PRECALL
        #  218 CALL
        #  228 LOAD_FAST data_length
        #  230 BUILD_TUPLE
        #  232 YIELD_VALUE
        #  234 RESUME
        #  236 POP_TOP
        #  238 LOAD_CONST None
        #  240 RETURN_VALUE
        pass

    def do_i2c_read(self, index, addr, read_length):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_FAST read_length
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST rx_data
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR device
        #   52 LOAD_FAST index
        #   54 LOAD_FAST addr
        #   56 LOAD_GLOBAL NULL + cast
        #   68 LOAD_GLOBAL NULL + byref
        #   80 LOAD_FAST rx_data
        #   82 PRECALL
        #   86 CALL
        #   96 LOAD_GLOBAL NULL + POINTER
        #  108 LOAD_GLOBAL c_uint8
        #  120 PRECALL
        #  124 CALL
        #  134 PRECALL
        #  138 CALL
        #  148 LOAD_FAST read_length
        #  150 BUILD_TUPLE
        #  152 YIELD_VALUE
        #  154 RESUME
        #  156 POP_TOP
        #  158 LOAD_GLOBAL NULL + bytes
        #  170 LOAD_FAST rx_data
        #  172 LOAD_CONST 0
        #  174 LOAD_FAST read_length
        #  176 BUILD_SLICE
        #  178 BINARY_SUBSCR
        #  188 PRECALL
        #  192 CALL
        #  202 RETURN_VALUE
        pass

    def do_i2c_write_read(self, index, addr, write_bytes, read_length):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST write_bytes
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST tx_len
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST tx_len
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_GLOBAL NULL + bytes
        #   88 LOAD_FAST write_bytes
        #   90 PRECALL
        #   94 CALL
        #  104 PRECALL
        #  108 CALL
        #  118 STORE_FAST tx_data
        #  120 LOAD_GLOBAL NULL + c_uint8
        #  132 LOAD_FAST read_length
        #  134 BINARY_OP *
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST rx_data
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR device
        #  166 LOAD_FAST index
        #  168 LOAD_FAST addr
        #  170 LOAD_GLOBAL NULL + cast
        #  182 LOAD_GLOBAL NULL + byref
        #  194 LOAD_FAST tx_data
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_GLOBAL NULL + POINTER
        #  222 LOAD_GLOBAL c_uint8
        #  234 PRECALL
        #  238 CALL
        #  248 PRECALL
        #  252 CALL
        #  262 LOAD_FAST tx_len
        #  264 LOAD_GLOBAL NULL + cast
        #  276 LOAD_GLOBAL NULL + byref
        #  288 LOAD_FAST rx_data
        #  290 PRECALL
        #  294 CALL
        #  304 LOAD_GLOBAL NULL + POINTER
        #  316 LOAD_GLOBAL c_uint8
        #  328 PRECALL
        #  332 CALL
        #  342 PRECALL
        #  346 CALL
        #  356 LOAD_FAST read_length
        #  358 BUILD_TUPLE
        #  360 YIELD_VALUE
        #  362 RESUME
        #  364 POP_TOP
        #  366 LOAD_GLOBAL NULL + bytes
        #  378 LOAD_FAST rx_data
        #  380 LOAD_CONST 0
        #  382 LOAD_FAST read_length
        #  384 BUILD_SLICE
        #  386 BINARY_SUBSCR
        #  396 PRECALL
        #  400 CALL
        #  410 RETURN_VALUE
        pass

    def do_radio_fixed_test(self, channel, duration, mode):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST channel
        #   20 LOAD_FAST duration
        #   22 LOAD_FAST mode
        #   24 BUILD_TUPLE
        #   26 YIELD_VALUE
        #   28 RESUME
        #   30 POP_TOP
        #   32 LOAD_CONST None
        #   34 RETURN_VALUE
        pass

    def do_radio_sweep_test(self, start, stop, hop_interval, hop_count, mode):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST start
        #   20 LOAD_FAST stop
        #   22 LOAD_FAST hop_interval
        #   24 LOAD_FAST hop_count
        #   26 LOAD_FAST mode
        #   28 BUILD_TUPLE
        #   30 YIELD_VALUE
        #   32 RESUME
        #   34 POP_TOP
        #   36 LOAD_CONST None
        #   38 RETURN_VALUE
        pass

    def get_info_region_count(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST count
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST count
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST count
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def get_info_region_name(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + create_string_buffer
        #   18 LOAD_CONST 255
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST buffer
        #   36 LOAD_GLOBAL NULL + c_uint8
        #   48 LOAD_CONST 255
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST buffer_length
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR device
        #   78 LOAD_FAST index
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL NULL + byref
        #  104 LOAD_FAST buffer
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_GLOBAL c_char_p
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + byref
        #  158 LOAD_FAST buffer_length
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 YIELD_VALUE
        #  178 RESUME
        #  180 POP_TOP
        #  182 LOAD_FAST buffer
        #  184 LOAD_CONST 0
        #  186 LOAD_FAST buffer_length
        #  188 LOAD_ATTR value
        #  198 BUILD_SLICE
        #  200 BINARY_SUBSCR
        #  210 LOAD_METHOD decode
        #  232 LOAD_CONST 'UTF-8'
        #  234 PRECALL
        #  238 CALL
        #  248 RETURN_VALUE
        pass

    def get_info_region(self, index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST data
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST data_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_FAST index
        #   84 LOAD_GLOBAL NULL + cast
        #   96 LOAD_GLOBAL NULL + byref
        #  108 LOAD_FAST data
        #  110 PRECALL
        #  114 CALL
        #  124 LOAD_GLOBAL NULL + POINTER
        #  136 LOAD_GLOBAL c_uint8
        #  148 PRECALL
        #  152 CALL
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_GLOBAL NULL + byref
        #  188 LOAD_FAST data_length
        #  190 PRECALL
        #  194 CALL
        #  204 BUILD_TUPLE
        #  206 YIELD_VALUE
        #  208 RESUME
        #  210 POP_TOP
        #  212 LOAD_GLOBAL NULL + tuple
        #  224 LOAD_FAST data
        #  226 LOAD_CONST 0
        #  228 LOAD_FAST data_length
        #  230 LOAD_ATTR value
        #  240 BUILD_SLICE
        #  242 BINARY_SUBSCR
        #  252 PRECALL
        #  256 CALL
        #  266 RETURN_VALUE
        pass

    def get_stack_info(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 LOAD_CONST 2
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST array
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR device
        #   52 LOAD_FAST array
        #   54 BUILD_TUPLE
        #   56 YIELD_VALUE
        #   58 RESUME
        #   60 POP_TOP
        #   62 LOAD_GLOBAL NULL + tuple
        #   74 LOAD_FAST array
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST values
        #   92 LOAD_FAST values
        #   94 RETURN_VALUE
        pass

    def echo_raw(self, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_METHOD get_max_incoming_param_length
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST max_length
        #   46 LOAD_GLOBAL NULL + c_uint8
        #   58 LOAD_FAST max_length
        #   60 BINARY_OP *
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST reply
        #   80 LOAD_GLOBAL NULL + c_size_t
        #   92 LOAD_FAST max_length
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST reply_length
        #  110 LOAD_GLOBAL c_uint8
        #  122 LOAD_GLOBAL NULL + len
        #  134 LOAD_FAST values
        #  136 PRECALL
        #  140 CALL
        #  150 BINARY_OP *
        #  154 LOAD_METHOD from_buffer_copy
        #  176 LOAD_GLOBAL NULL + bytes
        #  188 LOAD_FAST values
        #  190 PRECALL
        #  194 CALL
        #  204 PRECALL
        #  208 CALL
        #  218 STORE_FAST data
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR device
        #  232 LOAD_GLOBAL NULL + cast
        #  244 LOAD_GLOBAL NULL + byref
        #  256 LOAD_FAST data
        #  258 PRECALL
        #  262 CALL
        #  272 LOAD_GLOBAL NULL + POINTER
        #  284 LOAD_GLOBAL c_uint8
        #  296 PRECALL
        #  300 CALL
        #  310 PRECALL
        #  314 CALL
        #  324 LOAD_GLOBAL NULL + len
        #  336 LOAD_FAST values
        #  338 PRECALL
        #  342 CALL
        #  352 LOAD_GLOBAL NULL + cast
        #  364 LOAD_GLOBAL NULL + byref
        #  376 LOAD_FAST reply
        #  378 PRECALL
        #  382 CALL
        #  392 LOAD_GLOBAL NULL + POINTER
        #  404 LOAD_GLOBAL c_uint8
        #  416 PRECALL
        #  420 CALL
        #  430 PRECALL
        #  434 CALL
        #  444 LOAD_GLOBAL NULL + byref
        #  456 LOAD_FAST reply_length
        #  458 PRECALL
        #  462 CALL
        #  472 BUILD_TUPLE
        #  474 YIELD_VALUE
        #  476 RESUME
        #  478 POP_TOP
        #  480 LOAD_GLOBAL NULL + min
        #  492 LOAD_FAST max_length
        #  494 LOAD_FAST reply_length
        #  496 LOAD_ATTR value
        #  506 PRECALL
        #  510 CALL
        #  520 STORE_FAST actual_length
        #  522 LOAD_GLOBAL NULL + bytes
        #  534 LOAD_FAST reply
        #  536 LOAD_CONST 0
        #  538 LOAD_FAST actual_length
        # ... bytecode truncated ...
        pass

    def echo_transaction(self, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_METHOD get_max_incoming_param_length
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST max_length
        #   46 LOAD_GLOBAL NULL + c_uint8
        #   58 LOAD_FAST max_length
        #   60 BINARY_OP *
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST reply
        #   80 LOAD_GLOBAL NULL + c_size_t
        #   92 LOAD_FAST max_length
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST reply_length
        #  110 LOAD_GLOBAL c_uint8
        #  122 LOAD_GLOBAL NULL + len
        #  134 LOAD_FAST values
        #  136 PRECALL
        #  140 CALL
        #  150 BINARY_OP *
        #  154 LOAD_METHOD from_buffer_copy
        #  176 LOAD_GLOBAL NULL + bytes
        #  188 LOAD_FAST values
        #  190 PRECALL
        #  194 CALL
        #  204 PRECALL
        #  208 CALL
        #  218 STORE_FAST data
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR device
        #  232 LOAD_GLOBAL NULL + cast
        #  244 LOAD_GLOBAL NULL + byref
        #  256 LOAD_FAST data
        #  258 PRECALL
        #  262 CALL
        #  272 LOAD_GLOBAL NULL + POINTER
        #  284 LOAD_GLOBAL c_uint8
        #  296 PRECALL
        #  300 CALL
        #  310 PRECALL
        #  314 CALL
        #  324 LOAD_GLOBAL NULL + len
        #  336 LOAD_FAST values
        #  338 PRECALL
        #  342 CALL
        #  352 LOAD_GLOBAL NULL + cast
        #  364 LOAD_GLOBAL NULL + byref
        #  376 LOAD_FAST reply
        #  378 PRECALL
        #  382 CALL
        #  392 LOAD_GLOBAL NULL + POINTER
        #  404 LOAD_GLOBAL c_uint8
        #  416 PRECALL
        #  420 CALL
        #  430 PRECALL
        #  434 CALL
        #  444 LOAD_GLOBAL NULL + byref
        #  456 LOAD_FAST reply_length
        #  458 PRECALL
        #  462 CALL
        #  472 BUILD_TUPLE
        #  474 YIELD_VALUE
        #  476 RESUME
        #  478 POP_TOP
        #  480 LOAD_GLOBAL NULL + min
        #  492 LOAD_FAST max_length
        #  494 LOAD_FAST reply_length
        #  496 LOAD_ATTR value
        #  506 PRECALL
        #  510 CALL
        #  520 STORE_FAST actual_length
        #  522 LOAD_GLOBAL NULL + bytes
        #  534 LOAD_FAST reply
        #  536 LOAD_CONST 0
        #  538 LOAD_FAST actual_length
        # ... bytecode truncated ...
        pass

    def echo_params(self, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_METHOD get_max_incoming_param_length
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST max_length
        #   46 LOAD_GLOBAL NULL + c_uint8
        #   58 LOAD_FAST max_length
        #   60 BINARY_OP *
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST reply
        #   80 LOAD_GLOBAL NULL + c_size_t
        #   92 LOAD_FAST max_length
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST reply_length
        #  110 LOAD_GLOBAL c_uint8
        #  122 LOAD_GLOBAL NULL + len
        #  134 LOAD_FAST values
        #  136 PRECALL
        #  140 CALL
        #  150 BINARY_OP *
        #  154 LOAD_METHOD from_buffer_copy
        #  176 LOAD_GLOBAL NULL + bytes
        #  188 LOAD_FAST values
        #  190 PRECALL
        #  194 CALL
        #  204 PRECALL
        #  208 CALL
        #  218 STORE_FAST data
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR device
        #  232 LOAD_GLOBAL NULL + cast
        #  244 LOAD_GLOBAL NULL + byref
        #  256 LOAD_FAST data
        #  258 PRECALL
        #  262 CALL
        #  272 LOAD_GLOBAL NULL + POINTER
        #  284 LOAD_GLOBAL c_uint8
        #  296 PRECALL
        #  300 CALL
        #  310 PRECALL
        #  314 CALL
        #  324 LOAD_GLOBAL NULL + len
        #  336 LOAD_FAST values
        #  338 PRECALL
        #  342 CALL
        #  352 LOAD_GLOBAL NULL + cast
        #  364 LOAD_GLOBAL NULL + byref
        #  376 LOAD_FAST reply
        #  378 PRECALL
        #  382 CALL
        #  392 LOAD_GLOBAL NULL + POINTER
        #  404 LOAD_GLOBAL c_uint8
        #  416 PRECALL
        #  420 CALL
        #  430 PRECALL
        #  434 CALL
        #  444 LOAD_GLOBAL NULL + byref
        #  456 LOAD_FAST reply_length
        #  458 PRECALL
        #  462 CALL
        #  472 BUILD_TUPLE
        #  474 YIELD_VALUE
        #  476 RESUME
        #  478 POP_TOP
        #  480 LOAD_GLOBAL NULL + min
        #  492 LOAD_FAST max_length
        #  494 LOAD_FAST reply_length
        #  496 LOAD_ATTR value
        #  506 PRECALL
        #  510 CALL
        #  520 STORE_FAST actual_length
        #  522 LOAD_GLOBAL NULL + bytes
        #  534 LOAD_FAST reply
        #  536 LOAD_CONST 0
        #  538 LOAD_FAST actual_length
        # ... bytecode truncated ...
        pass

    def enable_rf_power(self, enable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST enable
        #   20 BUILD_TUPLE
        #   22 YIELD_VALUE
        #   24 RESUME
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        pass

    def get_rf_power_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST enabled
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST enabled
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_GLOBAL NULL + bool
        #   94 LOAD_FAST enabled
        #   96 LOAD_ATTR value
        #  106 PRECALL
        #  110 CALL
        #  120 RETURN_VALUE
        pass

    def get_rf_power_ctrl_vars(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST ctrl_var_indexes
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST ctrl_var_indexes
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint8
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_GLOBAL NULL + tuple
        #  222 LOAD_FAST ctrl_var_indexes
        #  224 LOAD_CONST 0
        #  226 LOAD_FAST length
        #  228 LOAD_ATTR value
        #  238 BUILD_SLICE
        #  240 BINARY_SUBSCR
        #  250 PRECALL
        #  254 CALL
        #  264 RETURN_VALUE
        pass

    def reset_rf_power_timeout(self, timeout):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST timeout
        #   20 BUILD_TUPLE
        #   22 YIELD_VALUE
        #   24 RESUME
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        pass

    def stop_radio(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def start_radio_scan(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_raw_radio_scan_results(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST serials
        #   40 LOAD_GLOBAL NULL + c_size_t
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST serials_length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST serials
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint32
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST serials_length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_GLOBAL NULL + tuple
        #  222 LOAD_FAST serials
        #  224 LOAD_CONST 0
        #  226 LOAD_FAST serials_length
        #  228 LOAD_ATTR value
        #  238 BUILD_SLICE
        #  240 BINARY_SUBSCR
        #  250 PRECALL
        #  254 CALL
        #  264 RETURN_VALUE
        pass

    def get_radio_scan_results(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 PUSH_NULL
        #    8 LOAD_GLOBAL NULL + POINTER
        #   20 LOAD_GLOBAL c_uint32
        #   32 PRECALL
        #   36 CALL
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST serials_ptr
        #   62 LOAD_GLOBAL NULL + c_size_t
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST serials_length
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR device
        #  102 LOAD_GLOBAL NULL + byref
        #  114 LOAD_FAST serials_ptr
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_GLOBAL NULL + byref
        #  142 LOAD_FAST serials_length
        #  144 PRECALL
        #  148 CALL
        #  158 BUILD_TUPLE
        #  160 YIELD_VALUE
        #  162 RESUME
        #  164 POP_TOP
        #  166 LOAD_GLOBAL NULL + set
        #  178 LOAD_FAST serials_ptr
        #  180 LOAD_CONST 0
        #  182 LOAD_FAST serials_length
        #  184 LOAD_ATTR value
        #  194 BUILD_SLICE
        #  196 BINARY_SUBSCR
        #  206 PRECALL
        #  210 CALL
        #  220 STORE_FAST serials
        #  222 LOAD_FAST self
        #  224 LOAD_ATTR lib
        #  234 LOAD_ATTR lib
        #  244 LOAD_METHOD asphodel_free_radio_scan_results
        #  266 LOAD_FAST serials_ptr
        #  268 PRECALL
        #  272 CALL
        #  282 POP_TOP
        #  284 LOAD_FAST serials
        #  286 RETURN_VALUE
        pass

    def get_raw_radio_extra_scan_results(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 PUSH_NULL
        #    8 LOAD_FAST self
        #   10 LOAD_ATTR lib
        #   20 LOAD_ATTR AsphodelExtraScanResult
        #   30 LOAD_CONST 255
        #   32 BINARY_OP *
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST results
        #   52 LOAD_GLOBAL NULL + c_size_t
        #   64 LOAD_CONST 255
        #   66 PRECALL
        #   70 CALL
        #   80 STORE_FAST results_length
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR device
        #   94 LOAD_GLOBAL NULL + cast
        #  106 LOAD_GLOBAL NULL + byref
        #  118 LOAD_FAST results
        #  120 PRECALL
        #  124 CALL
        #  134 LOAD_GLOBAL NULL + POINTER
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR lib
        #  158 LOAD_ATTR AsphodelExtraScanResult
        #  168 PRECALL
        #  172 CALL
        #  182 PRECALL
        #  186 CALL
        #  196 LOAD_GLOBAL NULL + byref
        #  208 LOAD_FAST results_length
        #  210 PRECALL
        #  214 CALL
        #  224 BUILD_TUPLE
        #  226 YIELD_VALUE
        #  228 RESUME
        #  230 POP_TOP
        #  232 BUILD_LIST
        #  234 STORE_FAST result_list
        #  236 LOAD_FAST results
        #  238 LOAD_CONST 0
        #  240 LOAD_FAST results_length
        #  242 LOAD_ATTR value
        #  252 BUILD_SLICE
        #  254 BINARY_SUBSCR
        #  264 GET_ITER
        #  266 FOR_ITER to 374
        #  268 STORE_FAST result_struct
        #  270 LOAD_FAST result_list
        #  272 LOAD_METHOD append
        #  294 LOAD_GLOBAL NULL + ExtraScanResult
        #  306 LOAD_FAST result_struct
        #  308 LOAD_ATTR serial_number
        #  318 LOAD_FAST result_struct
        #  320 LOAD_ATTR asphodel_type
        #  330 LOAD_FAST result_struct
        #  332 LOAD_ATTR device_mode
        #  342 PRECALL
        #  346 CALL
        #  356 PRECALL
        #  360 CALL
        #  370 POP_TOP
        #  372 JUMP_BACKWARD to 266
        #  374 LOAD_FAST result_list
        #  376 RETURN_VALUE
        pass

    def get_radio_extra_scan_results(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 PUSH_NULL
        #    8 LOAD_GLOBAL NULL + POINTER
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR lib
        #   32 LOAD_ATTR AsphodelExtraScanResult
        #   42 PRECALL
        #   46 CALL
        #   56 PRECALL
        #   60 CALL
        #   70 STORE_FAST results_ptr
        #   72 LOAD_GLOBAL NULL + c_size_t
        #   84 PRECALL
        #   88 CALL
        #   98 STORE_FAST results_length
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR device
        #  112 LOAD_GLOBAL NULL + byref
        #  124 LOAD_FAST results_ptr
        #  126 PRECALL
        #  130 CALL
        #  140 LOAD_GLOBAL NULL + byref
        #  152 LOAD_FAST results_length
        #  154 PRECALL
        #  158 CALL
        #  168 BUILD_TUPLE
        #  170 YIELD_VALUE
        #  172 RESUME
        #  174 POP_TOP
        #  176 BUILD_LIST
        #  178 STORE_FAST result_list
        #  180 LOAD_FAST results_ptr
        #  182 LOAD_CONST 0
        #  184 LOAD_FAST results_length
        #  186 LOAD_ATTR value
        #  196 BUILD_SLICE
        #  198 BINARY_SUBSCR
        #  208 GET_ITER
        #  210 FOR_ITER to 318
        #  212 STORE_FAST result_struct
        #  214 LOAD_FAST result_list
        #  216 LOAD_METHOD append
        #  238 LOAD_GLOBAL NULL + ExtraScanResult
        #  250 LOAD_FAST result_struct
        #  252 LOAD_ATTR serial_number
        #  262 LOAD_FAST result_struct
        #  264 LOAD_ATTR asphodel_type
        #  274 LOAD_FAST result_struct
        #  276 LOAD_ATTR device_mode
        #  286 PRECALL
        #  290 CALL
        #  300 PRECALL
        #  304 CALL
        #  314 POP_TOP
        #  316 JUMP_BACKWARD to 210
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR lib
        #  330 LOAD_ATTR lib
        #  340 LOAD_METHOD asphodel_free_radio_extra_scan_results
        #  362 LOAD_FAST results_ptr
        #  364 PRECALL
        #  368 CALL
        #  378 POP_TOP
        #  380 LOAD_FAST result_list
        #  382 RETURN_VALUE
        pass

    def get_radio_scan_power(self, serial_numbers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 LOAD_GLOBAL NULL + len
        #   30 LOAD_FAST serial_numbers
        #   32 PRECALL
        #   36 CALL
        #   46 BINARY_OP *
        #   50 LOAD_FAST serial_numbers
        #   52 CALL_FUNCTION_EX
        #   54 STORE_FAST sn_array
        #   56 LOAD_GLOBAL NULL + c_int8
        #   68 LOAD_GLOBAL NULL + len
        #   80 LOAD_FAST serial_numbers
        #   82 PRECALL
        #   86 CALL
        #   96 BINARY_OP *
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST powers
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR device
        #  128 LOAD_GLOBAL NULL + cast
        #  140 LOAD_GLOBAL NULL + byref
        #  152 LOAD_FAST sn_array
        #  154 PRECALL
        #  158 CALL
        #  168 LOAD_GLOBAL NULL + POINTER
        #  180 LOAD_GLOBAL c_uint32
        #  192 PRECALL
        #  196 CALL
        #  206 PRECALL
        #  210 CALL
        #  220 LOAD_GLOBAL NULL + cast
        #  232 LOAD_GLOBAL NULL + byref
        #  244 LOAD_FAST powers
        #  246 PRECALL
        #  250 CALL
        #  260 LOAD_GLOBAL NULL + POINTER
        #  272 LOAD_GLOBAL c_int8
        #  284 PRECALL
        #  288 CALL
        #  298 PRECALL
        #  302 CALL
        #  312 LOAD_GLOBAL NULL + len
        #  324 LOAD_FAST serial_numbers
        #  326 PRECALL
        #  330 CALL
        #  340 BUILD_TUPLE
        #  342 YIELD_VALUE
        #  344 RESUME
        #  346 POP_TOP
        #  348 LOAD_GLOBAL NULL + list
        #  360 LOAD_FAST powers
        #  362 LOAD_CONST 0
        #  364 LOAD_GLOBAL NULL + len
        #  376 LOAD_FAST serial_numbers
        #  378 PRECALL
        #  382 CALL
        #  392 BUILD_SLICE
        #  394 BINARY_SUBSCR
        #  404 PRECALL
        #  408 CALL
        #  418 RETURN_VALUE
        pass

    def connect_radio(self, serial_number):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST serial_number
        #   20 BUILD_TUPLE
        #   22 YIELD_VALUE
        #   24 RESUME
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        pass

    def get_radio_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST connected
        #   34 LOAD_GLOBAL NULL + c_uint32
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST serial_number
        #   62 LOAD_GLOBAL NULL + c_uint8
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST protocol_type
        #   90 LOAD_GLOBAL NULL + c_int
        #  102 PRECALL
        #  106 CALL
        #  116 STORE_FAST scanning
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR device
        #  130 LOAD_GLOBAL NULL + byref
        #  142 LOAD_FAST connected
        #  144 PRECALL
        #  148 CALL
        #  158 LOAD_GLOBAL NULL + byref
        #  170 LOAD_FAST serial_number
        #  172 PRECALL
        #  176 CALL
        #  186 LOAD_GLOBAL NULL + byref
        #  198 LOAD_FAST protocol_type
        #  200 PRECALL
        #  204 CALL
        #  214 LOAD_GLOBAL NULL + byref
        #  226 LOAD_FAST scanning
        #  228 PRECALL
        #  232 CALL
        #  242 BUILD_TUPLE
        #  244 YIELD_VALUE
        #  246 RESUME
        #  248 POP_TOP
        #  250 LOAD_GLOBAL NULL + bool
        #  262 LOAD_FAST connected
        #  264 LOAD_ATTR value
        #  274 PRECALL
        #  278 CALL
        #  288 LOAD_FAST serial_number
        #  290 LOAD_ATTR value
        #  300 LOAD_FAST protocol_type
        #  302 LOAD_ATTR value
        #  312 LOAD_GLOBAL NULL + bool
        #  324 LOAD_FAST scanning
        #  326 LOAD_ATTR value
        #  336 PRECALL
        #  340 CALL
        #  350 BUILD_TUPLE
        #  352 RETURN_VALUE
        pass

    def get_radio_ctrl_vars(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint8
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST ctrl_var_indexes
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST ctrl_var_indexes
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint8
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_GLOBAL NULL + tuple
        #  222 LOAD_FAST ctrl_var_indexes
        #  224 LOAD_CONST 0
        #  226 LOAD_FAST length
        #  228 LOAD_ATTR value
        #  238 BUILD_SLICE
        #  240 BINARY_SUBSCR
        #  250 PRECALL
        #  254 CALL
        #  264 RETURN_VALUE
        pass

    def get_radio_default_serial(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST serial_number
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR device
        #   46 LOAD_GLOBAL NULL + byref
        #   58 LOAD_FAST serial_number
        #   60 PRECALL
        #   64 CALL
        #   74 BUILD_TUPLE
        #   76 YIELD_VALUE
        #   78 RESUME
        #   80 POP_TOP
        #   82 LOAD_FAST serial_number
        #   84 LOAD_ATTR value
        #   94 RETURN_VALUE
        pass

    def start_radio_scan_boot(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def connect_radio_boot(self, serial_number):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST serial_number
        #   20 BUILD_TUPLE
        #   22 YIELD_VALUE
        #   24 RESUME
        #   26 POP_TOP
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        pass

    def stop_remote(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def restart_remote(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_remote_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_int
        #   18 PRECALL
        #   22 CALL
        #   32 STORE_FAST connected
        #   34 LOAD_GLOBAL NULL + c_uint32
        #   46 PRECALL
        #   50 CALL
        #   60 STORE_FAST serial_number
        #   62 LOAD_GLOBAL NULL + c_uint8
        #   74 PRECALL
        #   78 CALL
        #   88 STORE_FAST protocol_type
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR device
        #  102 LOAD_GLOBAL NULL + byref
        #  114 LOAD_FAST connected
        #  116 PRECALL
        #  120 CALL
        #  130 LOAD_GLOBAL NULL + byref
        #  142 LOAD_FAST serial_number
        #  144 PRECALL
        #  148 CALL
        #  158 LOAD_GLOBAL NULL + byref
        #  170 LOAD_FAST protocol_type
        #  172 PRECALL
        #  176 CALL
        #  186 BUILD_TUPLE
        #  188 YIELD_VALUE
        #  190 RESUME
        #  192 POP_TOP
        #  194 LOAD_GLOBAL NULL + bool
        #  206 LOAD_FAST connected
        #  208 LOAD_ATTR value
        #  218 PRECALL
        #  222 CALL
        #  232 LOAD_FAST serial_number
        #  234 LOAD_ATTR value
        #  244 LOAD_FAST protocol_type
        #  246 LOAD_ATTR value
        #  256 BUILD_TUPLE
        #  258 RETURN_VALUE
        pass

    def restart_remote_app(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def restart_remote_boot(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def bootloader_start_program(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 BUILD_TUPLE
        #   20 YIELD_VALUE
        #   22 RESUME
        #   24 POP_TOP
        #   26 LOAD_CONST None
        #   28 RETURN_VALUE
        pass

    def get_bootloader_page_info(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint32
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST page_info
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST page_info
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint32
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_FAST page_info
        #  212 LOAD_CONST 0
        #  214 LOAD_FAST length
        #  216 LOAD_ATTR value
        #  226 BUILD_SLICE
        #  228 BINARY_SUBSCR
        #  238 STORE_FAST values
        #  240 LOAD_GLOBAL NULL + tuple
        #  252 LOAD_GLOBAL NULL + zip
        #  264 LOAD_FAST values
        #  266 LOAD_CONST 0
        #  268 LOAD_CONST None
        #  270 LOAD_CONST 2
        #  272 BUILD_SLICE
        #  274 BINARY_SUBSCR
        #  284 LOAD_FAST values
        #  286 LOAD_CONST 1
        #  288 LOAD_CONST None
        #  290 LOAD_CONST 2
        #  292 BUILD_SLICE
        #  294 BINARY_SUBSCR
        #  304 PRECALL
        #  308 CALL
        #  318 PRECALL
        #  322 CALL
        #  332 RETURN_VALUE
        pass

    def get_bootloader_block_sizes(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + c_uint16
        #   18 LOAD_CONST 255
        #   20 BINARY_OP *
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST block_sizes
        #   40 LOAD_GLOBAL NULL + c_uint8
        #   52 LOAD_CONST 255
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST length
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR device
        #   82 LOAD_GLOBAL NULL + cast
        #   94 LOAD_GLOBAL NULL + byref
        #  106 LOAD_FAST block_sizes
        #  108 PRECALL
        #  112 CALL
        #  122 LOAD_GLOBAL NULL + POINTER
        #  134 LOAD_GLOBAL c_uint16
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 LOAD_GLOBAL NULL + byref
        #  186 LOAD_FAST length
        #  188 PRECALL
        #  192 CALL
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_GLOBAL NULL + tuple
        #  222 LOAD_FAST block_sizes
        #  224 LOAD_CONST 0
        #  226 LOAD_FAST length
        #  228 LOAD_ATTR value
        #  238 BUILD_SLICE
        #  240 BINARY_SUBSCR
        #  250 PRECALL
        #  254 CALL
        #  264 RETURN_VALUE
        pass

    def start_bootloader_page(self, page_number, nonce):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST nonce
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST nonce_length
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST nonce_length
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_FAST nonce
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST nonce_array
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR device
        #  106 LOAD_FAST page_number
        #  108 LOAD_GLOBAL NULL + cast
        #  120 LOAD_GLOBAL NULL + byref
        #  132 LOAD_FAST nonce_array
        #  134 PRECALL
        #  138 CALL
        #  148 LOAD_GLOBAL NULL + POINTER
        #  160 LOAD_GLOBAL c_uint8
        #  172 PRECALL
        #  176 CALL
        #  186 PRECALL
        #  190 CALL
        #  200 LOAD_FAST nonce_length
        #  202 BUILD_TUPLE
        #  204 YIELD_VALUE
        #  206 RESUME
        #  208 POP_TOP
        #  210 LOAD_CONST None
        #  212 RETURN_VALUE
        pass

    def write_bootloader_code_block(self, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST data
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST data_length
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST data_length
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_FAST data
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST data_array
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR device
        #  106 LOAD_GLOBAL NULL + cast
        #  118 LOAD_GLOBAL NULL + byref
        #  130 LOAD_FAST data_array
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_GLOBAL NULL + POINTER
        #  158 LOAD_GLOBAL c_uint8
        #  170 PRECALL
        #  174 CALL
        #  184 PRECALL
        #  188 CALL
        #  198 LOAD_FAST data_length
        #  200 BUILD_TUPLE
        #  202 YIELD_VALUE
        #  204 RESUME
        #  206 POP_TOP
        #  208 LOAD_CONST None
        #  210 RETURN_VALUE
        pass

    def write_bootloader_page(self, data, block_sizes):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_GLOBAL NULL + len
        #   18 LOAD_FAST data
        #   20 PRECALL
        #   24 CALL
        #   34 STORE_FAST data_length
        #   36 LOAD_GLOBAL c_uint8
        #   48 LOAD_FAST data_length
        #   50 BINARY_OP *
        #   54 LOAD_METHOD from_buffer_copy
        #   76 LOAD_FAST data
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST data_array
        #   94 LOAD_GLOBAL NULL + len
        #  106 LOAD_FAST block_sizes
        #  108 PRECALL
        #  112 CALL
        #  122 STORE_FAST block_sizes_length
        #  124 LOAD_GLOBAL NULL + c_uint16
        #  136 LOAD_FAST block_sizes_length
        #  138 BINARY_OP *
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST block_sizes_array
        #  158 LOAD_GLOBAL NULL + range
        #  170 LOAD_FAST block_sizes_length
        #  172 PRECALL
        #  176 CALL
        #  186 GET_ITER
        #  188 FOR_ITER to 216
        #  190 STORE_FAST i
        #  192 LOAD_FAST block_sizes
        #  194 LOAD_FAST i
        #  196 BINARY_SUBSCR
        #  206 LOAD_FAST block_sizes_array
        #  208 LOAD_FAST i
        #  210 STORE_SUBSCR
        #  214 JUMP_BACKWARD to 188
        #  216 LOAD_FAST self
        #  218 LOAD_ATTR device
        #  228 LOAD_GLOBAL NULL + cast
        #  240 LOAD_GLOBAL NULL + byref
        #  252 LOAD_FAST data_array
        #  254 PRECALL
        #  258 CALL
        #  268 LOAD_GLOBAL NULL + POINTER
        #  280 LOAD_GLOBAL c_uint8
        #  292 PRECALL
        #  296 CALL
        #  306 PRECALL
        #  310 CALL
        #  320 LOAD_FAST data_length
        #  322 LOAD_GLOBAL NULL + cast
        #  334 LOAD_GLOBAL NULL + byref
        #  346 LOAD_FAST block_sizes_array
        #  348 PRECALL
        #  352 CALL
        #  362 LOAD_GLOBAL NULL + POINTER
        #  374 LOAD_GLOBAL c_uint16
        #  386 PRECALL
        #  390 CALL
        #  400 PRECALL
        #  404 CALL
        #  414 LOAD_FAST block_sizes_length
        #  416 BUILD_TUPLE
        #  418 YIELD_VALUE
        #  420 RESUME
        #  422 POP_TOP
        #  424 LOAD_CONST None
        #  426 RETURN_VALUE
        pass

    def finish_bootloader_page(self, mac_tag):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST mac_tag
        #    8 POP_JUMP_FORWARD_IF_NOT_NONE to 14
        #   10 LOAD_CONST b''
        #   12 STORE_FAST mac_tag
        #   14 LOAD_GLOBAL NULL + len
        #   26 LOAD_FAST mac_tag
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST mac_tag_length
        #   44 LOAD_GLOBAL c_uint8
        #   56 LOAD_FAST mac_tag_length
        #   58 BINARY_OP *
        #   62 LOAD_METHOD from_buffer_copy
        #   84 LOAD_FAST mac_tag
        #   86 PRECALL
        #   90 CALL
        #  100 STORE_FAST mac_tag_array
        #  102 LOAD_FAST self
        #  104 LOAD_ATTR device
        #  114 LOAD_GLOBAL NULL + cast
        #  126 LOAD_GLOBAL NULL + byref
        #  138 LOAD_FAST mac_tag_array
        #  140 PRECALL
        #  144 CALL
        #  154 LOAD_GLOBAL NULL + POINTER
        #  166 LOAD_GLOBAL c_uint8
        #  178 PRECALL
        #  182 CALL
        #  192 PRECALL
        #  196 CALL
        #  206 LOAD_FAST mac_tag_length
        #  208 BUILD_TUPLE
        #  210 YIELD_VALUE
        #  212 RESUME
        #  214 POP_TOP
        #  216 LOAD_CONST None
        #  218 RETURN_VALUE
        pass

    def verify_bootloader_page(self, mac_tag):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST mac_tag
        #    8 POP_JUMP_FORWARD_IF_NOT_NONE to 14
        #   10 LOAD_CONST b''
        #   12 STORE_FAST mac_tag
        #   14 LOAD_GLOBAL NULL + len
        #   26 LOAD_FAST mac_tag
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST mac_tag_length
        #   44 LOAD_GLOBAL c_uint8
        #   56 LOAD_FAST mac_tag_length
        #   58 BINARY_OP *
        #   62 LOAD_METHOD from_buffer_copy
        #   84 LOAD_FAST mac_tag
        #   86 PRECALL
        #   90 CALL
        #  100 STORE_FAST mac_tag_array
        #  102 LOAD_FAST self
        #  104 LOAD_ATTR device
        #  114 LOAD_GLOBAL NULL + cast
        #  126 LOAD_GLOBAL NULL + byref
        #  138 LOAD_FAST mac_tag_array
        #  140 PRECALL
        #  144 CALL
        #  154 LOAD_GLOBAL NULL + POINTER
        #  166 LOAD_GLOBAL c_uint8
        #  178 PRECALL
        #  182 CALL
        #  192 PRECALL
        #  196 CALL
        #  206 LOAD_FAST mac_tag_length
        #  208 BUILD_TUPLE
        #  210 YIELD_VALUE
        #  212 RESUME
        #  214 POP_TOP
        #  216 LOAD_CONST None
        #  218 RETURN_VALUE
        pass

    def get_strain_bridge_count(self, channel_info):
        count = c_int()
        self.lib.lib.asphodel_get_strain_bridge_count(channel_info, byref(count))
        return count.value

    def get_strain_bridge_subchannel(self, channel_info, bridge_index):
        subchannel = c_size_t()
        self.lib.lib.asphodel_get_strain_bridge_subchannel(channel_info, bridge_index, byref(subchannel))
        return subchannel.value

    def get_strain_bridge_values(self, channel_info, bridge_index):
        array = (c_float * 5)()
        self.lib.lib.asphodel_get_strain_bridge_values(channel_info, bridge_index, array)
        return BridgeValues(*array)

    def set_strain_outputs(self, channel_index, bridge_index, pos, neg):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST channel_index
        #   20 LOAD_FAST bridge_index
        #   22 LOAD_FAST pos
        #   24 LOAD_FAST neg
        #   26 BUILD_TUPLE
        #   28 YIELD_VALUE
        #   30 RESUME
        #   32 POP_TOP
        #   34 LOAD_CONST None
        #   36 RETURN_VALUE
        pass

    def check_strain_resistances(self, channel_info, bridge_index, baseline, pos_high, neg_high):
        passed = c_int(0)
        pos_res = c_double()
        neg_res = c_double()
        self.lib.lib.asphodel_check_strain_resistances(channel_info, bridge_index, baseline, pos_high, neg_high, byref(pos_res), byref(neg_res), byref(passed))
        return (bool(passed.value), pos_res.value, neg_res.value)

    def get_accel_self_test_limits(self, channel_info):
        array = (c_float * 6)()
        self.lib.lib.asphodel_get_accel_self_test_limits(channel_info, array)
        return SelfTestLimits(*array)

    def enable_accel_self_test(self, channel_index, enable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RETURN_GENERATOR
        #    2 POP_TOP
        #    4 RESUME
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR device
        #   18 LOAD_FAST channel_index
        #   20 LOAD_FAST enable
        #   22 BUILD_TUPLE
        #   24 YIELD_VALUE
        #   26 RESUME
        #   28 POP_TOP
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        pass

    def check_accel_self_test(self, channel_info, disabled, enabled):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + c_double
        #   14 LOAD_CONST 3
        #   16 BINARY_OP *
        #   20 LOAD_FAST disabled
        #   22 CALL_FUNCTION_EX
        #   24 STORE_FAST dis_array
        #   26 LOAD_GLOBAL NULL + c_double
        #   38 LOAD_CONST 3
        #   40 BINARY_OP *
        #   44 LOAD_FAST enabled
        #   46 CALL_FUNCTION_EX
        #   48 STORE_FAST en_array
        #   50 LOAD_GLOBAL NULL + c_int
        #   62 LOAD_CONST 0
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST passed
        #   80 LOAD_FAST self
        #   82 LOAD_ATTR lib
        #   92 LOAD_ATTR lib
        #  102 LOAD_METHOD asphodel_check_accel_self_test
        #  124 LOAD_FAST channel_info
        #  126 LOAD_FAST dis_array
        #  128 LOAD_FAST en_array
        #  130 LOAD_GLOBAL NULL + byref
        #  142 LOAD_FAST passed
        #  144 PRECALL
        #  148 CALL
        #  158 PRECALL
        #  162 CALL
        #  172 POP_TOP
        #  174 LOAD_GLOBAL NULL + bool
        #  186 LOAD_FAST passed
        #  188 LOAD_ATTR value
        #  198 PRECALL
        #  202 CALL
        #  212 RETURN_VALUE
        pass

    def get_channel_decoder(self, index, bit_offset):
        channel_info = self.get_channel(index)
        return self.lib.create_channel_decoder(channel_info, bit_offset)

    def get_stream_decoder(self, index, bit_offset):
        stream_info = self.get_stream(index)
        channel_info_list = []
        indexes = stream_info.channel_index_list[0:stream_info.channel_count]
        for ch_index in indexes:
            channel_info_list.append(self.get_channel(ch_index))
            return self.lib.create_stream_decoder(stream_info, channel_info_list, bit_offset)

    def get_device_decoder(self):
        (stream_count, filler_bits, id_bits) = self.get_stream_count()
        info_list = []
        for i in range(stream_count):
            stream_struct = self.get_stream(i)
            channel_info_list = []
            channels = stream_struct.channel_count
            indexes = stream_struct.channel_index_list[0:channels]
            for ch_index in indexes:
                channel_info_list.append(self.get_channel(ch_index))
                info_list.append((i, stream_struct, channel_info_list))
                return self.lib.create_device_decoder(info_list, filler_bits, id_bits)

    def get_streaming_counts(self, response_time, buffer_time, timeout):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_DEREF self
        #    6 LOAD_METHOD get_stream_count
        #   28 PRECALL
        #   32 CALL
        #   42 UNPACK_SEQUENCE
        #   46 STORE_FAST stream_count
        #   48 STORE_FAST _filler_bits
        #   50 STORE_FAST _id_bits
        #   52 LOAD_CLOSURE self
        #   54 BUILD_TUPLE
        #   56 LOAD_CONST <code object <listcomp> at 0x105bb2230, file "asphodel\__init__.py", line 3681>
        #   58 MAKE_FUNCTION closure
        #   60 LOAD_GLOBAL NULL + range
        #   72 LOAD_FAST stream_count
        #   74 PRECALL
        #   78 CALL
        #   88 GET_ITER
        #   90 PRECALL
        #   94 CALL
        #  104 STORE_FAST streams
        #  106 LOAD_DEREF self
        #  108 LOAD_ATTR lib
        #  118 LOAD_METHOD get_streaming_counts
        #  140 LOAD_FAST streams
        #  142 LOAD_FAST response_time
        #  144 LOAD_FAST buffer_time
        #  146 LOAD_FAST timeout
        #  148 PRECALL
        #  152 CALL
        #  162 RETURN_VALUE
        pass

    def get_channel_unit_formatter(self, index, use_metric):
        info = self.get_channel_info(index)
        return self.lib.create_unit_formatter(info.unit_type, info.minimum, info.maximum, info.resolution, use_metric)

    def get_ctrl_var_unit_formatter(self, index, use_metric):
        info = self.get_ctrl_var_info(index)
        (unit_type, minimum, maximum, scale, offset) = info
        return self.lib.create_unit_formatter(unit_type, minimum * scale + offset, maximum * scale + offset, scale, use_metric)

    def get_setting(self, index):
        info = self.get_setting_info(index)
        name = self.get_setting_name(index)
        default = self.get_setting_default(index)
        name_bytes = name.encode('UTF-8')
        info.name = name_bytes
        info.name_length = len(name_bytes)

def recreate_channel_decoder(*args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + nativelib
    #   14 LOAD_ATTR create_channel_decoder
    #   24 LOAD_FAST args
    #   26 BUILD_MAP
    #   28 LOAD_FAST kwargs
    #   30 DICT_MERGE
    #   32 CALL_FUNCTION_EX
    #   34 RETURN_VALUE
    pass

class AsphodelNativeChannelDecoder:

    def __init__(self, lib, decoder, channel_info, stream_decoder):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST lib
        #    4 LOAD_FAST self
        #    6 STORE_ATTR lib
        #   16 LOAD_FAST decoder
        #   18 LOAD_FAST self
        #   20 STORE_ATTR _decoder
        #   30 LOAD_FAST channel_info
        #   32 LOAD_FAST self
        #   34 STORE_ATTR channel_info
        #   44 LOAD_FAST stream_decoder
        #   46 LOAD_FAST self
        #   48 STORE_ATTR stream_decoder
        #   58 LOAD_FAST stream_decoder
        #   60 POP_JUMP_FORWARD_IF_FALSE to 66
        #   62 LOAD_CONST False
        #   64 JUMP_FORWARD to 68
        #   66 LOAD_CONST True
        #   68 LOAD_FAST self
        #   70 STORE_ATTR auto_free
        #   80 LOAD_FAST self
        #   82 LOAD_ATTR _decoder
        #   92 LOAD_ATTR channel_bit_offset
        #  102 LOAD_FAST self
        #  104 STORE_ATTR channel_bit_offset
        #  114 LOAD_FAST self
        #  116 LOAD_ATTR _decoder
        #  126 LOAD_ATTR samples
        #  136 LOAD_FAST self
        #  138 STORE_ATTR samples
        #  148 NOP
        #  150 LOAD_FAST self
        #  152 LOAD_ATTR _decoder
        #  162 LOAD_ATTR channel_name
        #  172 LOAD_METHOD decode
        #  194 LOAD_CONST 'UTF-8'
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_FAST self
        #  212 STORE_ATTR channel_name
        #  222 JUMP_FORWARD to 270
        #  224 PUSH_EXC_INFO
        #  226 LOAD_GLOBAL UnicodeDecodeError
        #  238 CHECK_EXC_MATCH
        #  240 POP_JUMP_FORWARD_IF_FALSE to 262
        #  242 POP_TOP
        #  244 LOAD_CONST '<ERROR>'
        #  246 LOAD_FAST self
        #  248 STORE_ATTR channel_name
        #  258 POP_EXCEPT
        #  260 JUMP_FORWARD to 270
        #  262 RERAISE
        #  264 COPY
        #  266 POP_EXCEPT
        #  268 RERAISE
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR _decoder
        #  282 LOAD_ATTR subchannels
        #  292 LOAD_FAST self
        #  294 STORE_ATTR subchannels
        #  304 BUILD_LIST
        #  306 LOAD_FAST self
        #  308 STORE_ATTR subchannel_names
        #  318 LOAD_GLOBAL NULL + range
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR subchannels
        #  342 PRECALL
        #  346 CALL
        #  356 GET_ITER
        #  358 FOR_ITER to 576
        #  360 STORE_FAST i
        #  362 NOP
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR _decoder
        #  376 LOAD_ATTR subchannel_names
        #  386 LOAD_FAST i
        #  388 BINARY_SUBSCR
        #  398 LOAD_METHOD decode
        #  420 LOAD_CONST 'UTF-8'
        #  422 PRECALL
        # ... bytecode truncated ...
        pass

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
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL cb
        #    2 RESUME
        #    4 LOAD_CLOSURE cb
        #    6 BUILD_TUPLE
        #    8 LOAD_CONST <code object callback at 0x105b7a550, file "asphodel\__init__.py", line 3769>
        #   10 MAKE_FUNCTION closure
        #   12 STORE_FAST callback
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR lib
        #   26 LOAD_METHOD AsphodelDecodeCallback
        #   48 LOAD_FAST callback
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST c_cb
        #   66 LOAD_FAST c_cb
        #   68 LOAD_FAST self
        #   70 STORE_ATTR _callback
        #   80 LOAD_FAST c_cb
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR _decoder
        #   94 STORE_ATTR callback
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        pass

def recreate_stream_decoder(*args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + nativelib
    #   14 LOAD_ATTR create_stream_decoder
    #   24 LOAD_FAST args
    #   26 BUILD_MAP
    #   28 LOAD_FAST kwargs
    #   30 DICT_MERGE
    #   32 CALL_FUNCTION_EX
    #   34 RETURN_VALUE
    pass

class AsphodelNativeStreamDecoder:

    def __init__(self, lib, decoder, stream_info, channel_info_list, bit_offset, device_decoder):
        self.lib = lib
        self._decoder = decoder
        self.stream_info = stream_info
        self._channel_info_list = channel_info_list[:]
        self.bit_offset = bit_offset
        self.device_decoder = device_decoder
        self.auto_free = False if device_decoder else True
        self.counter_byte_offset = self._decoder.counter_byte_offset
        self.used_bits = self._decoder.used_bits
        self.channels = self._decoder.channels
        self.decoders = []
        for i in range(self.channels):
            d = AsphodelNativeChannelDecoder(self.lib, self._decoder.decoders[i].contents, channel_info_list[i], self)
            self.decoders.append(d)
            return None

    def __del__(self):
        if self.auto_free:
            self.free()
            return None

    def __reduce__(self):
        if self._decoder.lost_packet_callback:
            raise Exception('Cannot reduce stream decoder with callback')
        for d in self.decoders:
            if d._decoder.callback:
                raise Exception('Cannot reduce channel decoder with callback')
            args = (self.stream_info, self._channel_info_list, self.bit_offset)
            return (recreate_stream_decoder, args)

    def free(self):
        if self._decoder:
            self._decoder.free_decoder(self._decoder)
            self._decoder = None
            return None

    def reset(self):
        self._decoder.reset(self._decoder)

    def last_count(self):
        return self._decoder.last_count

    def decode(self, buffer):
        b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
        self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))

    def set_lost_packet_callback(self, cb):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL cb
        #    2 RESUME
        #    4 LOAD_CLOSURE cb
        #    6 BUILD_TUPLE
        #    8 LOAD_CONST <code object callback at 0x105bb2b30, file "asphodel\__init__.py", line 3837>
        #   10 MAKE_FUNCTION closure
        #   12 STORE_FAST callback
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR lib
        #   26 LOAD_METHOD AsphodelLostPacketCallback
        #   48 LOAD_FAST callback
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST c_cb
        #   66 LOAD_FAST c_cb
        #   68 LOAD_FAST self
        #   70 STORE_ATTR _callback
        #   80 LOAD_FAST c_cb
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR _decoder
        #   94 STORE_ATTR lost_packet_callback
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        pass

def recreate_device_decoder(*args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + nativelib
    #   14 LOAD_ATTR create_device_decoder
    #   24 LOAD_FAST args
    #   26 BUILD_MAP
    #   28 LOAD_FAST kwargs
    #   30 DICT_MERGE
    #   32 CALL_FUNCTION_EX
    #   34 RETURN_VALUE
    pass

class AsphodelNativeDeviceDecoder:

    def __init__(self, lib, decoder, info_list, filler_bits, id_bits):
        self.lib = lib
        self._decoder = decoder
        self._info_list = info_list
        self._filler_bits = filler_bits
        self._id_bits = id_bits
        bit_offset = self._filler_bits + self._id_bits
        self.id_byte_offset = self._decoder.id_byte_offset
        self.used_bits = self._decoder.used_bits
        self.streams = self._decoder.streams
        self.stream_ids = self._decoder.stream_ids[0:self.streams]
        self.decoders = []
        for i in range(self.streams):
            d = AsphodelNativeStreamDecoder(self.lib, self._decoder.decoders[i].contents, info_list[i][1], info_list[i][2], bit_offset, self)
            self.decoders.append(d)
            return None

    def __del__(self):
        self.free()

    def __reduce__(self):
        if self._decoder.unknown_id_callback:
            raise Exception('Cannot reduce device decoder with callback')
        for d in self.decoders:
            if d._decoder.lost_packet_callback:
                raise Exception('Cannot reduce stream decoder with callback')
            for cd in d.decoders:
                if cd._decoder.callback:
                    raise Exception('Cannot reduce channel decoder with callback')
                args = (self._info_list, self._filler_bits, self._id_bits)
                return (recreate_device_decoder, args)

    def free(self):
        if self._decoder:
            self._decoder.free_decoder(self._decoder)
            self._decoder = None
            return None

    def reset(self):
        self._decoder.reset(self._decoder)

    def decode(self, buffer):
        b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
        self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))

    def set_unknown_id_callback(self, cb):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL cb
        #    2 RESUME
        #    4 LOAD_CLOSURE cb
        #    6 BUILD_TUPLE
        #    8 LOAD_CONST <code object callback at 0x105bb2e30, file "asphodel\__init__.py", line 3903>
        #   10 MAKE_FUNCTION closure
        #   12 STORE_FAST callback
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR lib
        #   26 LOAD_METHOD AsphodelUnknownIDCallback
        #   48 LOAD_FAST callback
        #   50 PRECALL
        #   54 CALL
        #   64 STORE_FAST c_cb
        #   66 LOAD_FAST c_cb
        #   68 LOAD_FAST self
        #   70 STORE_ATTR _callback
        #   80 LOAD_FAST c_cb
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR _decoder
        #   94 STORE_ATTR unknown_id_callback
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        pass

def recreate_unit_formatter(*args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + nativelib
    #   14 LOAD_ATTR create_unit_formatter
    #   24 LOAD_FAST args
    #   26 BUILD_MAP
    #   28 LOAD_FAST kwargs
    #   30 DICT_MERGE
    #   32 CALL_FUNCTION_EX
    #   34 RETURN_VALUE
    pass

def recreate_custom_unit_formatter(*args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + nativelib
    #   14 LOAD_ATTR create_custom_unit_formatter
    #   24 LOAD_FAST args
    #   26 BUILD_MAP
    #   28 LOAD_FAST kwargs
    #   30 DICT_MERGE
    #   32 CALL_FUNCTION_EX
    #   34 RETURN_VALUE
    pass

class AsphodelNativeUnitFormatter:

    def __init__(self, lib, formatter, recreate):
        self.lib = lib
        self.formatter = formatter
        self._recreate = recreate
        self.unit_ascii = self.formatter.unit_ascii.decode('ascii')
        self.unit_utf8 = self.formatter.unit_utf8.decode('UTF-8')
        self.unit_html = self.formatter.unit_html.decode('ascii')
        self.conversion_scale = self.formatter.conversion_scale
        self.conversion_offset = self.formatter.conversion_offset

    def __del__(self):
        self.free()

    def __reduce__(self):
        return self._recreate

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            self_tuple = (self.unit_ascii, self.unit_utf8, self.unit_html, self.conversion_scale, self.conversion_offset)
            other_tuple = (other.unit_ascii, other.unit_utf8, other.unit_html, other.conversion_scale, other.conversion_offset)
            return self_tuple == other_tuple

    def free(self):
        if self.formatter:
            self.formatter.free(self.formatter)
            self.formatter = None
            return None

    def format_bare(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_bare(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')

    def format_ascii(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_ascii(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')

    def format_utf8(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_utf8(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('UTF-8')

    def format_html(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_html(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')

def format_nvm_data(data, size):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_CONST <code object to_ascii at 0x105b7aaf0, file "asphodel\__init__.py", line 3977>
    #    4 MAKE_FUNCTION
    #    6 STORE_FAST to_ascii
    #    8 BUILD_LIST
    #   10 STORE_FAST output
    #   12 LOAD_GLOBAL NULL + range
    #   24 LOAD_CONST 0
    #   26 LOAD_GLOBAL NULL + len
    #   38 LOAD_FAST data
    #   40 PRECALL
    #   44 CALL
    #   54 LOAD_FAST size
    #   56 PRECALL
    #   60 CALL
    #   70 GET_ITER
    #   72 FOR_ITER to 410
    #   74 STORE_FAST i
    #   76 LOAD_FAST data
    #   78 LOAD_FAST i
    #   80 LOAD_GLOBAL NULL + min
    #   92 LOAD_GLOBAL NULL + len
    #  104 LOAD_FAST data
    #  106 PRECALL
    #  110 CALL
    #  120 LOAD_FAST i
    #  122 LOAD_FAST size
    #  124 BINARY_OP +
    #  128 PRECALL
    #  132 CALL
    #  142 BUILD_SLICE
    #  144 BINARY_SUBSCR
    #  154 STORE_FAST data_chunk
    #  156 LOAD_CONST ' '
    #  158 LOAD_METHOD join
    #  180 LOAD_GLOBAL NULL + map
    #  192 LOAD_CONST '{:02x}'
    #  194 LOAD_ATTR format
    #  204 LOAD_FAST data_chunk
    #  206 PRECALL
    #  210 CALL
    #  220 PRECALL
    #  224 CALL
    #  234 STORE_FAST hex_values
    #  236 LOAD_CONST '   '
    #  238 LOAD_FAST size
    #  240 LOAD_GLOBAL NULL + len
    #  252 LOAD_FAST data_chunk
    #  254 PRECALL
    #  258 CALL
    #  268 BINARY_OP -
    #  272 BINARY_OP *
    #  276 STORE_FAST filler
    #  278 LOAD_CONST ''
    #  280 LOAD_METHOD join
    #  302 LOAD_GLOBAL NULL + map
    #  314 LOAD_FAST to_ascii
    #  316 LOAD_FAST data_chunk
    #  318 PRECALL
    #  322 CALL
    #  332 PRECALL
    #  336 CALL
    #  346 STORE_FAST ascii_values
    #  348 LOAD_FAST output
    #  350 LOAD_METHOD append
    #  372 LOAD_FAST hex_values
    #  374 LOAD_FAST filler
    #  376 BINARY_OP +
    #  380 LOAD_CONST ' '
    #  382 BINARY_OP +
    #  386 LOAD_FAST ascii_values
    #  388 BINARY_OP +
    #  392 PRECALL
    #  396 CALL
    #  406 POP_TOP
    #  408 JUMP_BACKWARD to 72
    #  410 LOAD_FAST output
    #  412 RETURN_VALUE
    pass

def find_devices():
    usb_devices = find_usb_devices()
    tcp_devices = find_tcp_devices()
    return usb_devices + tcp_devices

def find_device_by_serial(serial):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL nativelib
    #   14 LOAD_METHOD find_tcp_devices
    #   36 PRECALL
    #   40 CALL
    #   50 GET_ITER
    #   52 FOR_ITER to 128
    #   54 STORE_FAST device
    #   56 LOAD_FAST device
    #   58 LOAD_METHOD tcp_get_advertisement
    #   80 PRECALL
    #   84 CALL
    #   94 STORE_FAST adv
    #   96 LOAD_FAST adv
    #   98 LOAD_ATTR serial_number
    #  108 LOAD_FAST serial
    #  110 COMPARE_OP ==
    #  116 POP_JUMP_FORWARD_IF_FALSE to 126
    #  118 LOAD_FAST device
    #  120 SWAP
    #  122 POP_TOP
    #  124 RETURN_VALUE
    #  126 JUMP_BACKWARD to 52
    #  128 LOAD_GLOBAL nativelib
    #  140 LOAD_METHOD find_usb_devices
    #  162 PRECALL
    #  166 CALL
    #  176 GET_ITER
    #  178 FOR_ITER to 488
    #  180 STORE_FAST device
    #  182 NOP
    #  184 LOAD_FAST device
    #  186 LOAD_METHOD open
    #  208 PRECALL
    #  212 CALL
    #  222 POP_TOP
    #  224 LOAD_FAST device
    #  226 LOAD_METHOD get_serial_number
    #  248 PRECALL
    #  252 CALL
    #  262 LOAD_FAST serial
    #  264 COMPARE_OP ==
    #  270 POP_JUMP_FORWARD_IF_FALSE to 320
    #  272 LOAD_FAST device
    #  274 LOAD_FAST device
    #  276 LOAD_METHOD close
    #  298 PRECALL
    #  302 CALL
    #  312 POP_TOP
    #  314 SWAP
    #  316 POP_TOP
    #  318 RETURN_VALUE
    #  320 JUMP_FORWARD to 394
    #  322 PUSH_EXC_INFO
    #  324 LOAD_GLOBAL AsphodelError
    #  336 CHECK_EXC_MATCH
    #  338 POP_JUMP_FORWARD_IF_FALSE to 386
    #  340 POP_TOP
    #  342 POP_EXCEPT
    #  344 LOAD_FAST device
    #  346 LOAD_METHOD close
    #  368 PRECALL
    #  372 CALL
    #  382 POP_TOP
    #  384 JUMP_BACKWARD to 178
    #  386 RERAISE
    #  388 COPY
    #  390 POP_EXCEPT
    #  392 RERAISE
    #  394 NOP
    #  396 LOAD_FAST device
    #  398 LOAD_METHOD close
    #  420 PRECALL
    #  424 CALL
    #  434 POP_TOP
    #  436 JUMP_BACKWARD to 178
    #  438 PUSH_EXC_INFO
    #  440 LOAD_FAST device
    #  442 LOAD_METHOD close
    #  464 PRECALL
    # ... bytecode truncated ...
    pass
