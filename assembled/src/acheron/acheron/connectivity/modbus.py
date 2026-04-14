# Source Generated with Decompyle++
# File: modbus.pyc (Python 3.11)

import logging
import re
import struct
import threading
from typing import Any, cast, Iterable, Optional
from intervaltree import Interval, IntervalTree
import numpy
from numpy.typing import NDArray
from pymodbus.server.sync import ModbusTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusServerContext
from pymodbus.interfaces import IModbusSlaveContext
from pymodbus.transaction import ModbusSocketFramer
from PySide6 import QtCore
from asphodel import AsphodelChannelInfo
from hyperborea.ringbuffer import RingBuffer
from .connectivity_manager import DeviceCallback
from ..calc_process.types import ChannelInformation
from ..core.preferences import get_device_preferences, Preferences
from ..device_logging import DeviceLoggerAdapter
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def get_numeric_serial(serial_number):
    matches = re.findall('\\d+', serial_number)
    return int(matches[-1]) if matches else 0

class ModbusDeviceMapping:

    def __init__(self, serial_number, channel_info):
        self.serial_number = serial_number
        self.channel_info = channel_info
        self.logger = DeviceLoggerAdapter(logger, serial_number)
        self.mean_ringbuffers = { }
        self.instant_ringbuffers = []
        self.last_instant_value = []
        self.channel_modbus_index = { }
        self.modbus_index_channel = { }
        for channel_id, info in sorted(channel_info.items()):
            subchannel_count = len(info.subchannel_names)
            self.mean_ringbuffers[channel_id] = RingBuffer(info.mean_len, subchannel_count)
            modbus_index = len(self.instant_ringbuffers)
            self.channel_modbus_index[channel_id] = modbus_index
            for i in range(subchannel_count):
                self.instant_ringbuffers.append(RingBuffer(info.mean_len, 1))
                self.last_instant_value.append(0)
                self.modbus_index_channel[modbus_index + i] = (channel_id, i)
                self.channel_count = len(self.instant_ringbuffers)
                self.numeric_serial = get_numeric_serial(serial_number)
                return None

    def callback(self, channel_id, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR mean_ringbuffers
        #   14 LOAD_FAST channel_id
        #   16 BINARY_SUBSCR
        #   26 LOAD_METHOD extend
        #   48 LOAD_FAST data
        #   50 PRECALL
        #   54 CALL
        #   64 POP_TOP
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR channel_modbus_index
        #   78 LOAD_FAST channel_id
        #   80 BINARY_SUBSCR
        #   90 STORE_FAST modbus_index
        #   92 LOAD_GLOBAL NULL + enumerate
        #  104 LOAD_FAST data
        #  106 LOAD_ATTR T
        #  116 PRECALL
        #  120 CALL
        #  130 GET_ITER
        #  132 FOR_ITER to 234
        #  134 UNPACK_SEQUENCE
        #  138 STORE_FAST i
        #  140 STORE_FAST subchannel_data
        #  142 LOAD_FAST self
        #  144 LOAD_ATTR instant_ringbuffers
        #  154 LOAD_FAST modbus_index
        #  156 LOAD_FAST i
        #  158 BINARY_OP +
        #  162 BINARY_SUBSCR
        #  172 LOAD_METHOD extend
        #  194 LOAD_FAST subchannel_data
        #  196 LOAD_CONST None
        #  198 LOAD_CONST None
        #  200 BUILD_SLICE
        #  202 LOAD_CONST None
        #  204 BUILD_TUPLE
        #  206 BINARY_SUBSCR
        #  216 PRECALL
        #  220 CALL
        #  230 POP_TOP
        #  232 JUMP_BACKWARD to 132
        #  234 LOAD_CONST None
        #  236 RETURN_VALUE
        pass

    def _mean_to_16bit(self, value, channel):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST value
        #    6 LOAD_FAST channel
        #    8 LOAD_ATTR maximum
        #   18 COMPARE_OP >=
        #   24 POP_JUMP_FORWARD_IF_FALSE to 30
        #   26 LOAD_CONST 65535
        #   28 RETURN_VALUE
        #   30 LOAD_FAST value
        #   32 LOAD_FAST channel
        #   34 LOAD_ATTR minimum
        #   44 COMPARE_OP <=
        #   50 POP_JUMP_FORWARD_IF_FALSE to 56
        #   52 LOAD_CONST 0
        #   54 RETURN_VALUE
        #   56 LOAD_FAST value
        #   58 LOAD_FAST channel
        #   60 LOAD_ATTR minimum
        #   70 BINARY_OP -
        #   74 LOAD_FAST channel
        #   76 LOAD_ATTR maximum
        #   86 LOAD_FAST channel
        #   88 LOAD_ATTR minimum
        #   98 BINARY_OP -
        #  102 BINARY_OP /
        #  106 STORE_FAST ratio
        #  108 LOAD_GLOBAL NULL + round
        #  120 LOAD_CONST 65535
        #  122 LOAD_FAST ratio
        #  124 BINARY_OP *
        #  128 PRECALL
        #  132 CALL
        #  142 RETURN_VALUE
        #  144 PUSH_EXC_INFO
        #  146 LOAD_GLOBAL ValueError
        #  158 CHECK_EXC_MATCH
        #  160 POP_JUMP_FORWARD_IF_FALSE to 170
        #  162 POP_TOP
        #  164 POP_EXCEPT
        #  166 LOAD_CONST 0
        #  168 RETURN_VALUE
        #  170 RERAISE
        #  172 COPY
        #  174 POP_EXCEPT
        #  176 RERAISE
        pass

    def _std_to_16bit(self, value, channel):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST value
        #    6 LOAD_CONST 0
        #    8 COMPARE_OP <=
        #   14 POP_JUMP_FORWARD_IF_FALSE to 20
        #   16 LOAD_CONST 0
        #   18 RETURN_VALUE
        #   20 LOAD_FAST channel
        #   22 LOAD_ATTR maximum
        #   32 LOAD_FAST channel
        #   34 LOAD_ATTR minimum
        #   44 BINARY_OP -
        #   48 LOAD_CONST 2.0
        #   50 BINARY_OP /
        #   54 STORE_FAST std_max
        #   56 LOAD_FAST value
        #   58 LOAD_FAST std_max
        #   60 COMPARE_OP >=
        #   66 POP_JUMP_FORWARD_IF_FALSE to 72
        #   68 LOAD_CONST 65535
        #   70 RETURN_VALUE
        #   72 LOAD_GLOBAL NULL + round
        #   84 LOAD_FAST value
        #   86 LOAD_FAST std_max
        #   88 BINARY_OP /
        #   92 LOAD_CONST 65535
        #   94 BINARY_OP *
        #   98 PRECALL
        #  102 CALL
        #  112 RETURN_VALUE
        #  114 PUSH_EXC_INFO
        #  116 LOAD_GLOBAL ValueError
        #  128 CHECK_EXC_MATCH
        #  130 POP_JUMP_FORWARD_IF_FALSE to 140
        #  132 POP_TOP
        #  134 POP_EXCEPT
        #  136 LOAD_CONST 0
        #  138 RETURN_VALUE
        #  140 RERAISE
        #  142 COPY
        #  144 POP_EXCEPT
        #  146 RERAISE
        pass

    def _get_mean(self, modbus_index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR modbus_index_channel
        #   16 LOAD_FAST modbus_index
        #   18 BINARY_SUBSCR
        #   28 UNPACK_SEQUENCE
        #   32 STORE_FAST channel_id
        #   34 STORE_FAST subchannel
        #   36 JUMP_FORWARD to 72
        #   38 PUSH_EXC_INFO
        #   40 LOAD_GLOBAL KeyError
        #   52 CHECK_EXC_MATCH
        #   54 POP_JUMP_FORWARD_IF_FALSE to 64
        #   56 POP_TOP
        #   58 POP_EXCEPT
        #   60 LOAD_CONST None
        #   62 RETURN_VALUE
        #   64 RERAISE
        #   66 COPY
        #   68 POP_EXCEPT
        #   70 RERAISE
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR mean_ringbuffers
        #   84 LOAD_FAST channel_id
        #   86 BINARY_SUBSCR
        #   96 STORE_FAST ringbuffer
        #   98 LOAD_FAST ringbuffer
        #  100 LOAD_METHOD get_contents
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_CONST None
        #  138 LOAD_CONST None
        #  140 BUILD_SLICE
        #  142 LOAD_FAST subchannel
        #  144 BUILD_TUPLE
        #  146 BINARY_SUBSCR
        #  156 STORE_FAST data
        #  158 LOAD_GLOBAL NULL + numpy
        #  170 LOAD_ATTR mean
        #  180 LOAD_FAST data
        #  182 PRECALL
        #  186 CALL
        #  196 LOAD_METHOD item
        #  218 PRECALL
        #  222 CALL
        #  232 STORE_FAST value
        #  234 LOAD_FAST value
        #  236 LOAD_FAST channel_id
        #  238 BUILD_TUPLE
        #  240 RETURN_VALUE
        pass

    def get_mean_float(self, modbus_index):
        result = self._get_mean(modbus_index)

    def get_mean_16bit(self, modbus_index):
        result = self._get_mean(modbus_index)

    def _get_std(self, modbus_index):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR modbus_index_channel
        #   16 LOAD_FAST modbus_index
        #   18 BINARY_SUBSCR
        #   28 UNPACK_SEQUENCE
        #   32 STORE_FAST channel_id
        #   34 STORE_FAST subchannel
        #   36 JUMP_FORWARD to 72
        #   38 PUSH_EXC_INFO
        #   40 LOAD_GLOBAL KeyError
        #   52 CHECK_EXC_MATCH
        #   54 POP_JUMP_FORWARD_IF_FALSE to 64
        #   56 POP_TOP
        #   58 POP_EXCEPT
        #   60 LOAD_CONST None
        #   62 RETURN_VALUE
        #   64 RERAISE
        #   66 COPY
        #   68 POP_EXCEPT
        #   70 RERAISE
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR mean_ringbuffers
        #   84 LOAD_FAST channel_id
        #   86 BINARY_SUBSCR
        #   96 STORE_FAST ringbuffer
        #   98 LOAD_FAST ringbuffer
        #  100 LOAD_METHOD get_contents
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_CONST None
        #  138 LOAD_CONST None
        #  140 BUILD_SLICE
        #  142 LOAD_FAST subchannel
        #  144 BUILD_TUPLE
        #  146 BINARY_SUBSCR
        #  156 STORE_FAST data
        #  158 LOAD_GLOBAL NULL + numpy
        #  170 LOAD_ATTR std
        #  180 LOAD_FAST data
        #  182 PRECALL
        #  186 CALL
        #  196 LOAD_METHOD item
        #  218 PRECALL
        #  222 CALL
        #  232 STORE_FAST value
        #  234 LOAD_FAST value
        #  236 LOAD_FAST channel_id
        #  238 BUILD_TUPLE
        #  240 RETURN_VALUE
        pass

    def get_std_float(self, modbus_index):
        result = self._get_std(modbus_index)

    def get_std_16bit(self, modbus_index):
        result = self._get_std(modbus_index)

    def get_instant_float(self, modbus_index):
        try:
            ringbuffer = self.instant_ringbuffers[modbus_index]
        except IndexError:
            return None

        data = ringbuffer.get_contents()
        if data.size != 0:
            value = numpy.mean(data).item()
            self.last_instant_value[modbus_index] = value
            ringbuffer.clear()
        else:
            value = self.last_instant_value[modbus_index]
        return value

    def get_instant_16bit(self, modbus_index):
        value = self.get_instant_float(modbus_index)

class ModbusSlave(IModbusSlaveContext):

    def __init__(self):
        super().__init__()
        self.float_encoder = struct.Struct('<f')
        self.int_encoder = struct.Struct('<i')
        self.decoder = struct.Struct('<HH')
        self.device_mappings = {}
        self.device_intervals = {}
        self.interval_tree = IntervalTree()

    def add_device_mapping(self, serial_number, register_offset, device_mapping):
        self.remove_device_mapping(serial_number)
        t = (register_offset, device_mapping)
        self.device_mappings[serial_number] = t
        overlap_serials = set()
        intervals = set()
        for block in range(7):
            if block < 6:
                block_length = device_mapping.channel_count
            else:
                block_length = 2
            start_address = 1000 * block + register_offset
            end_address = start_address + block_length * 2 - 1
            interval = Interval(start_address, end_address, t)
            intervals.add(interval)
            overlap_intervals = self.interval_tree[start_address:end_address]
            for overlap_interval in overlap_intervals:
                overlapping_device_mapping = cast(ModbusDeviceMapping, overlap_interval.data[1])
                overlap_serials.add(overlapping_device_mapping.serial_number)
                self.interval_tree.add(interval)
                self.device_intervals[serial_number] = intervals
                device_logger = DeviceLoggerAdapter(logger, serial_number)
                if overlap_serials:
                    other_devices = ', '.join(sorted(overlap_serials))
                    device_logger.warning('Modbus addresses overlap with: %s', other_devices)
        device_logger.info('Modbus starting (offset %s)', register_offset)

    def remove_device_mapping(self, serial_number):
        result = self.device_mappings.pop(serial_number, None)

    def read_register_words(self, address):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + sorted
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR interval_tree
        #   28 LOAD_FAST address
        #   30 BINARY_SUBSCR
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST intervals
        #   56 LOAD_FAST intervals
        #   58 POP_JUMP_FORWARD_IF_TRUE to 64
        #   60 LOAD_CONST (0, 0)
        #   62 RETURN_VALUE
        #   64 LOAD_FAST intervals
        #   66 LOAD_CONST 0
        #   68 BINARY_SUBSCR
        #   78 STORE_FAST interval
        #   80 LOAD_GLOBAL NULL + cast
        #   92 LOAD_GLOBAL tuple
        #  104 LOAD_GLOBAL int
        #  116 LOAD_GLOBAL ModbusDeviceMapping
        #  128 BUILD_TUPLE
        #  130 BINARY_SUBSCR
        #  140 LOAD_FAST interval
        #  142 LOAD_ATTR data
        #  152 PRECALL
        #  156 CALL
        #  166 UNPACK_SEQUENCE
        #  170 STORE_FAST register_offset
        #  172 STORE_FAST device_mapping
        #  174 LOAD_FAST interval
        #  176 LOAD_ATTR begin
        #  186 LOAD_FAST register_offset
        #  188 BINARY_OP -
        #  192 STORE_FAST block_address
        #  194 LOAD_FAST block_address
        #  196 LOAD_CONST 1000
        #  198 BINARY_OP //
        #  202 STORE_FAST block
        #  204 LOAD_FAST address
        #  206 LOAD_FAST interval
        #  208 LOAD_ATTR begin
        #  218 BINARY_OP -
        #  222 LOAD_CONST 2
        #  224 BINARY_OP //
        #  228 STORE_FAST index
        #  230 LOAD_FAST block
        #  232 LOAD_CONST 0
        #  234 COMPARE_OP ==
        #  240 POP_JUMP_FORWARD_IF_FALSE to 494
        #  242 LOAD_FAST device_mapping
        #  244 LOAD_METHOD get_mean_float
        #  266 LOAD_FAST index
        #  268 PRECALL
        #  272 CALL
        #  282 STORE_FAST value_float
        #  284 LOAD_FAST value_float
        #  286 POP_JUMP_FORWARD_IF_NOT_NONE to 320
        #  288 LOAD_GLOBAL NULL + IndexError
        #  300 LOAD_CONST 'Unknown index %s'
        #  302 LOAD_FAST index
        #  304 PRECALL
        #  308 CALL
        #  318 RAISE_VARARGS
        #  320 LOAD_GLOBAL NULL + cast
        #  332 LOAD_GLOBAL tuple
        #  344 LOAD_GLOBAL int
        #  356 LOAD_GLOBAL int
        #  368 BUILD_TUPLE
        #  370 BINARY_SUBSCR
        #  380 LOAD_FAST self
        #  382 LOAD_ATTR decoder
        #  392 LOAD_METHOD unpack
        #  414 LOAD_FAST self
        #  416 LOAD_ATTR float_encoder
        #  426 LOAD_METHOD pack
        #  448 LOAD_FAST value_float
        #  450 PRECALL
        #  454 CALL
        # ... bytecode truncated ...
        pass

    def reset(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def validate(self, fx, address, count):
        if self.decode(fx) in ('i', 'h'):
            return True

    def getValues(self, fx, address, count):
        read_address = address & -2
        if read_address != address:
            word_count = (count + 2) // 2
        else:
            word_count = (count + 1) // 2
        results = []
        for i in range(word_count):
            words = self.read_register_words(read_address + i * 2)
            results.extend(words)
            if address != read_address:
                results = results[1:]
        results = results[:count]
        return results[:count]

    def setValues(self, fx, address, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

class ModbusHandler:

    def __init__(self, preferences):
        self.preferences = preferences
        self.stopped = False
        self.identity = ModbusDeviceIdentification()
        app = QtCore.QCoreApplication.instance()
        if app is not None:
            self.identity.VendorName = app.organizationName()
            self.identity.ProductCode = app.applicationName()
            self.identity.VendorUrl = app.organizationDomain()
            self.identity.ProductName = app.applicationName()
            self.identity.ModelName = app.applicationName()
            self.identity.MajorMinorRevision = app.applicationVersion()
        self.slave = ModbusSlave()
        self.context = ModbusServerContext(slaves=self.slave, single=True)
        self.modbus_server = None
        self.modbus_started = threading.Event()
        self.thread = None
        self.update_preferences()

    def stop(self):
        self.stopped = True
        self._stop_modbus()

    def join(self):
        if getattr(self, 'stopped', True):
            return None
        if hasattr(self, '_stop_modbus'):
            self.stop()
        return None

    def stop_device(self, serial_number):
        self.slave.remove_device_mapping(serial_number)

    def get_device_callback(self, serial_number, channel_info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + get_device_preferences
        #   14 LOAD_FAST serial_number
        #   16 PRECALL
        #   20 CALL
        #   30 STORE_FAST device_prefs
        #   32 LOAD_FAST device_prefs
        #   34 LOAD_ATTR modbus_enable
        #   44 POP_JUMP_FORWARD_IF_TRUE to 50
        #   46 LOAD_CONST None
        #   48 RETURN_VALUE
        #   50 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #   62 LOAD_GLOBAL logger
        #   74 LOAD_FAST serial_number
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST device_logger
        #   92 LOAD_FAST device_prefs
        #   94 LOAD_ATTR modbus_register_offset
        #  104 STORE_FAST register_offset
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR modbus_server
        #  118 POP_JUMP_FORWARD_IF_NOT_NONE to 166
        #  120 LOAD_FAST device_logger
        #  122 LOAD_METHOD warning
        #  144 LOAD_CONST 'Modbus server not running'
        #  146 PRECALL
        #  150 CALL
        #  160 POP_TOP
        #  162 LOAD_CONST None
        #  164 RETURN_VALUE
        #  166 LOAD_GLOBAL NULL + ModbusDeviceMapping
        #  178 LOAD_FAST serial_number
        #  180 LOAD_FAST channel_info
        #  182 PRECALL
        #  186 CALL
        #  196 STORE_FAST device_mapping
        #  198 LOAD_FAST self
        #  200 LOAD_ATTR slave
        #  210 LOAD_METHOD add_device_mapping
        #  232 LOAD_FAST serial_number
        #  234 LOAD_FAST register_offset
        #  236 LOAD_FAST device_mapping
        #  238 PRECALL
        #  242 CALL
        #  252 POP_TOP
        #  254 LOAD_FAST device_mapping
        #  256 LOAD_ATTR callback
        #  266 RETURN_VALUE
        pass

    def update_preferences(self):
        if self.stopped:
            return None
        address = (None, self.preferences.modbus_port)
        if not self.preferences.modbus_enable:
            self._stop_modbus()
            return None
        self._start_modbus(address)
        return None

    def _start_modbus(self, address):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR thread
        #   14 POP_JUMP_FORWARD_IF_NONE to 80
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR thread
        #   28 LOAD_METHOD join
        #   50 PRECALL
        #   54 CALL
        #   64 POP_TOP
        #   66 LOAD_CONST None
        #   68 LOAD_FAST self
        #   70 STORE_ATTR thread
        #   80 NOP
        #   82 LOAD_GLOBAL NULL + ModbusTcpServer
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR context
        #  106 LOAD_GLOBAL ModbusSocketFramer
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR identity
        #  130 LOAD_FAST address
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_FAST self
        #  148 STORE_ATTR modbus_server
        #  158 JUMP_FORWARD to 260
        #  160 PUSH_EXC_INFO
        #  162 LOAD_GLOBAL Exception
        #  174 CHECK_EXC_MATCH
        #  176 POP_JUMP_FORWARD_IF_FALSE to 252
        #  178 POP_TOP
        #  180 LOAD_GLOBAL logger
        #  192 LOAD_METHOD exception
        #  214 LOAD_CONST 'Error starting modbus server'
        #  216 PRECALL
        #  220 CALL
        #  230 POP_TOP
        #  232 LOAD_CONST None
        #  234 LOAD_FAST self
        #  236 STORE_ATTR modbus_server
        #  246 POP_EXCEPT
        #  248 LOAD_CONST None
        #  250 RETURN_VALUE
        #  252 RERAISE
        #  254 COPY
        #  256 POP_EXCEPT
        #  258 RERAISE
        #  260 LOAD_FAST self
        #  262 LOAD_ATTR modbus_started
        #  272 LOAD_METHOD clear
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 LOAD_GLOBAL NULL + threading
        #  322 LOAD_ATTR Thread
        #  332 LOAD_FAST self
        #  334 LOAD_ATTR _thread_run
        #  344 KW_NAMES
        #  346 PRECALL
        #  350 CALL
        #  360 LOAD_FAST self
        #  362 STORE_ATTR thread
        #  372 LOAD_FAST self
        #  374 LOAD_ATTR thread
        #  384 LOAD_METHOD start
        #  406 PRECALL
        #  410 CALL
        #  420 POP_TOP
        #  422 LOAD_FAST self
        #  424 LOAD_ATTR modbus_started
        #  434 LOAD_METHOD wait
        #  456 PRECALL
        #  460 CALL
        #  470 POP_TOP
        #  472 LOAD_GLOBAL logger
        #  484 LOAD_METHOD debug
        #  506 LOAD_CONST 'Started modbus server on port %s'
        #  508 LOAD_FAST address
        #  510 LOAD_CONST 1
        #  512 BINARY_SUBSCR
        # ... bytecode truncated ...
        pass

    def _stop_modbus(self):
        if self.modbus_server:
            logger.debug('Stopping modbus server')
            self.modbus_server.shutdown()
            self.modbus_server = None
            return None

    def _thread_run(self):
        try:
            modbus_server = cast(ModbusTcpServer, self.modbus_server)
            self.modbus_started.set()
            modbus_server.serve_forever()
            return None
        except Exception:
            logger.exception('Uncaught exception in _thread_run')
            self._stop_modbus()
            return None
