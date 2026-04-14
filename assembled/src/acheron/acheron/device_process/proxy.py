# Source Generated with Decompyle++
# File: proxy.pyc (Python 3.11)

import itertools
import logging
from logging.handlers import QueueListener
import multiprocessing
import queue
import threading
import traceback
from typing import Any, Callable, Optional, ParamSpec, Union
from PySide6 import QtCore
import asphodel
from hyperborea.namedprocess import NamedProcess
from ..device_logging import DeviceLoggerAdapter, RemoteToLocalLogHandler
from .proxy_remote import _simple_access, create_subproxy_util, do_device_cleanup, FromProcessType, JobTuple, proxy_process, TIMEOUT
logger = logging.getLogger(__name__)
P = ParamSpec('P')

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DeviceOperation(QtCore.QObject):

    __doc__ = '\n    This class represents an operation on the hardware (e.g. set_leds).\n    '

    completed = QtCore.Signal(object)

    error = QtCore.Signal()

    def __init__(self, func, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_FAST func
        #   70 LOAD_FAST self
        #   72 STORE_ATTR func
        #   82 LOAD_FAST args
        #   84 LOAD_FAST self
        #   86 STORE_ATTR args
        #   96 LOAD_FAST kwargs
        #   98 LOAD_FAST self
        #  100 STORE_ATTR kwargs
        #  110 LOAD_CONST None
        #  112 RETURN_VALUE
        pass

class SimpleDeviceOperation(DeviceOperation):

    def __init__(self, function_name, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 PUSH_NULL
        #    6 LOAD_GLOBAL NULL + super
        #   18 PRECALL
        #   22 CALL
        #   32 LOAD_ATTR __init__
        #   42 LOAD_GLOBAL _simple_access
        #   54 LOAD_FAST function_name
        #   56 BUILD_LIST
        #   58 LOAD_FAST args
        #   60 LIST_EXTEND
        #   62 LIST_TO_TUPLE
        #   64 BUILD_MAP
        #   66 LOAD_FAST kwargs
        #   68 DICT_MERGE
        #   70 CALL_FUNCTION_EX
        #   72 POP_TOP
        #   74 LOAD_CONST None
        #   76 RETURN_VALUE
        pass

class DeviceProxy(QtCore.QObject):

    __doc__ = '\n    This class represents a Device being handled in a different process.\n    '

    connected = QtCore.Signal()

    disconnected = QtCore.Signal()

    error = QtCore.Signal(str)

    def __init__(self, proxy_manager, process_name, log_queue, serial_number, proxy_string, find_func, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_FAST proxy_manager
        #   70 LOAD_FAST self
        #   72 STORE_ATTR proxy_manager
        #   82 LOAD_FAST serial_number
        #   84 LOAD_FAST self
        #   86 STORE_ATTR serial_number
        #   96 LOAD_FAST proxy_string
        #   98 LOAD_FAST self
        #  100 STORE_ATTR proxy_string
        #  110 LOAD_FAST log_queue
        #  112 LOAD_FAST self
        #  114 STORE_ATTR log_queue
        #  124 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #  136 LOAD_GLOBAL logger
        #  148 LOAD_FAST serial_number
        #  150 LOAD_FAST proxy_string
        #  152 PRECALL
        #  156 CALL
        #  166 LOAD_FAST self
        #  168 STORE_ATTR logger
        #  178 LOAD_GLOBAL NULL + multiprocessing
        #  190 LOAD_ATTR Queue
        #  200 PRECALL
        #  204 CALL
        #  214 LOAD_FAST self
        #  216 STORE_ATTR to_process_queue
        #  226 LOAD_GLOBAL NULL + multiprocessing
        #  238 LOAD_ATTR Queue
        #  248 PRECALL
        #  252 CALL
        #  262 LOAD_FAST self
        #  264 STORE_ATTR from_process_queue
        #  274 LOAD_GLOBAL NULL + NamedProcess
        #  286 LOAD_FAST process_name
        #  288 LOAD_FAST serial_number
        #  290 LOAD_GLOBAL proxy_process
        #  302 LOAD_FAST self
        #  304 LOAD_ATTR log_queue
        #  314 LOAD_FAST self
        #  316 LOAD_ATTR to_process_queue
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR from_process_queue
        #  338 LOAD_FAST serial_number
        #  340 LOAD_FAST proxy_string
        #  342 LOAD_FAST find_func
        #  344 LOAD_FAST args
        #  346 LOAD_FAST kwargs
        #  348 BUILD_TUPLE
        #  350 KW_NAMES
        #  352 PRECALL
        #  356 CALL
        #  366 LOAD_FAST self
        #  368 STORE_ATTR process
        #  378 LOAD_CONST True
        #  380 LOAD_FAST self
        #  382 LOAD_ATTR process
        #  392 STORE_ATTR daemon
        #  402 LOAD_GLOBAL NULL + threading
        #  414 LOAD_ATTR Thread
        #  424 LOAD_FAST self
        #  426 LOAD_ATTR monitor
        #  436 KW_NAMES
        #  438 PRECALL
        #  442 CALL
        #  452 LOAD_FAST self
        #  454 STORE_ATTR monitor_thread
        #  464 LOAD_GLOBAL NULL + threading
        #  476 LOAD_ATTR Lock
        #  486 PRECALL
        #  490 CALL
        #  500 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def handle_exception(self, proxy, exc):
        m = traceback.format_exception_only(type(exc), exc)
        message = ''.join(m)
        message = message.rstrip('\n')
        proxy.error.emit(message)
        proxy.close_connection()

    def handle_reply(self, reply):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST reply
        #    6 LOAD_CONST True
        #    8 IS_OP
        #   10 POP_JUMP_FORWARD_IF_FALSE to 66
        #   12 LOAD_FAST self
        #   14 LOAD_ATTR connected
        #   24 LOAD_METHOD emit
        #   46 PRECALL
        #   50 CALL
        #   60 POP_TOP
        #   62 LOAD_CONST None
        #   64 RETURN_VALUE
        #   66 LOAD_GLOBAL NULL + isinstance
        #   78 LOAD_FAST reply
        #   80 LOAD_GLOBAL Exception
        #   92 PRECALL
        #   96 CALL
        #  106 POP_JUMP_FORWARD_IF_FALSE to 156
        #  108 LOAD_FAST self
        #  110 LOAD_METHOD handle_exception
        #  132 LOAD_FAST self
        #  134 LOAD_FAST reply
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 LOAD_CONST None
        #  154 RETURN_VALUE
        #  156 LOAD_FAST reply
        #  158 UNPACK_SEQUENCE
        #  162 STORE_FAST job_id
        #  164 STORE_FAST result
        #  166 STORE_FAST exc
        #  168 LOAD_FAST self
        #  170 LOAD_ATTR job_lock
        #  180 BEFORE_WITH
        #  182 POP_TOP
        #  184 LOAD_FAST self
        #  186 LOAD_ATTR jobs
        #  196 LOAD_METHOD pop
        #  218 LOAD_FAST job_id
        #  220 PRECALL
        #  224 CALL
        #  234 UNPACK_SEQUENCE
        #  238 STORE_FAST operation
        #  240 STORE_FAST proxy
        #  242 LOAD_CONST None
        #  244 LOAD_CONST None
        #  246 LOAD_CONST None
        #  248 PRECALL
        #  252 CALL
        #  262 POP_TOP
        #  264 JUMP_FORWARD to 288
        #  266 PUSH_EXC_INFO
        #  268 WITH_EXCEPT_START
        #  270 POP_JUMP_FORWARD_IF_TRUE to 280
        #  272 RERAISE
        #  274 COPY
        #  276 POP_EXCEPT
        #  278 RERAISE
        #  280 POP_TOP
        #  282 POP_EXCEPT
        #  284 POP_TOP
        #  286 POP_TOP
        #  288 LOAD_FAST exc
        #  290 POP_JUMP_FORWARD_IF_NOT_NONE to 384
        #  292 LOAD_FAST result
        #  294 POP_JUMP_FORWARD_IF_NOT_NONE to 326
        #  296 LOAD_GLOBAL NULL + type
        #  308 LOAD_CONST None
        #  310 PRECALL
        #  314 CALL
        #  324 STORE_FAST result
        #  326 DELETE_FAST proxy
        #  328 LOAD_FAST operation
        #  330 LOAD_ATTR completed
        #  340 LOAD_METHOD emit
        #  362 LOAD_FAST result
        #  364 PRECALL
        # ... bytecode truncated ...
        pass

    def monitor(self):
        self.logger.debug('Monitor thread starting')
        normal_exit = False

    def close_connection(self):
        try:
            self.to_process_queue.put(None)
            return None
        except ValueError:
            return None

    def send_job(self, operation, *subproxy, args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST subproxy
        #    4 POP_JUMP_FORWARD_IF_NOT_NONE to 16
        #    6 LOAD_FAST self
        #    8 STORE_FAST proxy
        #   10 LOAD_CONST None
        #   12 STORE_FAST subproxy_id
        #   14 JUMP_FORWARD to 34
        #   16 LOAD_FAST subproxy
        #   18 STORE_FAST proxy
        #   20 LOAD_FAST subproxy
        #   22 LOAD_ATTR subproxy_id
        #   32 STORE_FAST subproxy_id
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR job_lock
        #   46 BEFORE_WITH
        #   48 POP_TOP
        #   50 LOAD_FAST self
        #   52 LOAD_ATTR next_job_index
        #   62 STORE_FAST job_index
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR next_job_index
        #   76 LOAD_CONST 1
        #   78 BINARY_OP +
        #   82 LOAD_CONST 4294967295
        #   84 BINARY_OP &
        #   88 LOAD_FAST self
        #   90 STORE_ATTR next_job_index
        #  100 LOAD_FAST operation
        #  102 LOAD_FAST proxy
        #  104 BUILD_TUPLE
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR jobs
        #  118 LOAD_FAST job_index
        #  120 STORE_SUBSCR
        #  124 LOAD_CONST None
        #  126 LOAD_CONST None
        #  128 LOAD_CONST None
        #  130 PRECALL
        #  134 CALL
        #  144 POP_TOP
        #  146 JUMP_FORWARD to 170
        #  148 PUSH_EXC_INFO
        #  150 WITH_EXCEPT_START
        #  152 POP_JUMP_FORWARD_IF_TRUE to 162
        #  154 RERAISE
        #  156 COPY
        #  158 POP_EXCEPT
        #  160 RERAISE
        #  162 POP_TOP
        #  164 POP_EXCEPT
        #  166 POP_TOP
        #  168 POP_TOP
        #  170 LOAD_GLOBAL NULL + dict
        #  182 LOAD_GLOBAL NULL + list
        #  194 LOAD_FAST operation
        #  196 LOAD_ATTR kwargs
        #  206 LOAD_METHOD items
        #  228 PRECALL
        #  232 CALL
        #  242 PRECALL
        #  246 CALL
        #  256 LOAD_GLOBAL NULL + list
        #  268 LOAD_FAST kwargs
        #  270 LOAD_METHOD items
        #  292 PRECALL
        #  296 CALL
        #  306 PRECALL
        #  310 CALL
        #  320 BINARY_OP +
        #  324 PRECALL
        #  328 CALL
        #  338 STORE_FAST new_kwargs
        #  340 LOAD_FAST operation
        #  342 LOAD_ATTR args
        #  352 LOAD_FAST args
        #  354 BINARY_OP +
        #  358 STORE_FAST new_args
        #  360 LOAD_FAST job_index
        #  362 LOAD_FAST subproxy_id
        # ... bytecode truncated ...
        pass

    def wait_for_close(self):
        if self.monitor_thread.is_alive():
            self.close_connection()
            self.monitor_thread.join()
            return None

    def is_finished(self):
        return not self.monitor_thread.is_alive()

    def create_subproxy(self, func, *args, **kwargs):
        subproxy_id = next(self.subproxy_id_counter)

class DeviceSubProxy(QtCore.QObject):

    connected = QtCore.Signal()

    disconnected = QtCore.Signal()

    error = QtCore.Signal(str)

    def __init__(self, proxy, subproxy_id, start_op):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_FAST proxy
        #   70 LOAD_FAST self
        #   72 STORE_ATTR proxy
        #   82 LOAD_FAST proxy
        #   84 LOAD_ATTR logger
        #   94 LOAD_FAST self
        #   96 STORE_ATTR logger
        #  106 LOAD_FAST subproxy_id
        #  108 LOAD_FAST self
        #  110 STORE_ATTR subproxy_id
        #  120 LOAD_FAST start_op
        #  122 LOAD_ATTR completed
        #  132 LOAD_METHOD connect
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR _connected_cb
        #  166 PRECALL
        #  170 CALL
        #  180 POP_TOP
        #  182 LOAD_CONST False
        #  184 LOAD_FAST self
        #  186 STORE_ATTR closed
        #  196 LOAD_CONST False
        #  198 LOAD_FAST self
        #  200 STORE_ATTR closed_finished
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR proxy
        #  222 LOAD_ATTR disconnected
        #  232 LOAD_METHOD connect
        #  254 LOAD_FAST self
        #  256 LOAD_ATTR disconnected
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_FAST self
        #  284 LOAD_ATTR proxy
        #  294 LOAD_ATTR error
        #  304 LOAD_METHOD connect
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR error
        #  338 PRECALL
        #  342 CALL
        #  352 POP_TOP
        #  354 LOAD_GLOBAL NULL + DeviceOperation
        #  366 LOAD_GLOBAL do_device_cleanup
        #  378 PRECALL
        #  382 CALL
        #  392 LOAD_FAST self
        #  394 STORE_ATTR close_job
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR close_job
        #  416 LOAD_ATTR completed
        #  426 LOAD_METHOD connect
        #  448 LOAD_FAST self
        #  450 LOAD_ATTR close_completed
        #  460 PRECALL
        #  464 CALL
        #  474 POP_TOP
        #  476 LOAD_FAST self
        #  478 LOAD_ATTR close_job
        #  488 LOAD_ATTR error
        #  498 LOAD_METHOD connect
        #  520 LOAD_FAST self
        #  522 LOAD_ATTR close_completed
        #  532 PRECALL
        #  536 CALL
        #  546 POP_TOP
        #  548 LOAD_FAST self
        #  550 LOAD_ATTR logger
        #  560 LOAD_METHOD debug
        #  582 LOAD_CONST 'Starting subproxy'
        #  584 PRECALL
        # ... bytecode truncated ...
        pass

    def close_connection(self):
        if not self.closed:
            self.closed = True
            self.proxy.send_job(self.close_job, subproxy = self)
            return None

    def close_completed(self):
        self.proxy.disconnected.disconnect(self.disconnected)
        self.proxy.error.disconnect(self.error)
        self.disconnected.emit()
        self.closed_finished = True

    def _connected_cb(self, result):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST result
        #    4 POP_JUMP_FORWARD_IF_NONE to 124
        #    6 LOAD_FAST result
        #    8 UNPACK_SEQUENCE
        #   12 STORE_FAST serial_number
        #   14 STORE_FAST subproxy_string
        #   16 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #   28 LOAD_GLOBAL logger
        #   40 LOAD_FAST serial_number
        #   42 LOAD_FAST subproxy_string
        #   44 PRECALL
        #   48 CALL
        #   58 LOAD_FAST self
        #   60 STORE_ATTR logger
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR connected
        #   82 LOAD_METHOD emit
        #  104 PRECALL
        #  108 CALL
        #  118 POP_TOP
        #  120 LOAD_CONST None
        #  122 RETURN_VALUE
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR error
        #  136 LOAD_METHOD emit
        #  158 LOAD_CONST 'Subproxy Creation Failed'
        #  160 PRECALL
        #  164 CALL
        #  174 POP_TOP
        #  176 LOAD_FAST self
        #  178 LOAD_ATTR proxy
        #  188 LOAD_ATTR disconnected
        #  198 LOAD_METHOD disconnect
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR disconnected
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR proxy
        #  260 LOAD_ATTR error
        #  270 LOAD_METHOD disconnect
        #  292 LOAD_FAST self
        #  294 LOAD_ATTR error
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 LOAD_FAST self
        #  322 LOAD_ATTR disconnected
        #  332 LOAD_METHOD emit
        #  354 PRECALL
        #  358 CALL
        #  368 POP_TOP
        #  370 LOAD_CONST None
        #  372 RETURN_VALUE
        pass

    def wait_for_close(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def is_finished(self):
        return self.closed_finished

    def send_job(self, operation, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 PUSH_NULL
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR proxy
        #   16 LOAD_ATTR send_job
        #   26 LOAD_FAST operation
        #   28 BUILD_LIST
        #   30 LOAD_FAST args
        #   32 LIST_EXTEND
        #   34 LIST_TO_TUPLE
        #   36 LOAD_CONST 'subproxy'
        #   38 LOAD_FAST self
        #   40 BUILD_MAP
        #   42 LOAD_FAST kwargs
        #   44 DICT_MERGE
        #   46 CALL_FUNCTION_EX
        #   48 POP_TOP
        #   50 LOAD_CONST None
        #   52 RETURN_VALUE
        pass

class DeviceProxyManager:

    def __init__(self, process_name):
        self.process_name = process_name
        self.setup_logging()
        self.proxies = []
        self.next_proxy_number = 0

    def setup_logging(self):
        local_handler = RemoteToLocalLogHandler(__name__ + '.remote')
        self.log_queue = multiprocessing.Queue()
        self.log_listener = QueueListener(self.log_queue, local_handler)
        self.log_listener.start()

    def stop(self):
        for proxy in self.proxies:
            proxy.close_connection()
            for proxy in self.proxies:
                proxy.wait_for_close()
                self.log_listener.stop()
                return None

    def clear_finished_proxies(self):
        for proxy in self.proxies.copy():
            if proxy.is_finished():
                self.proxies.remove(proxy)
            return None

    def new_proxy(self, serial_number, find_func, *args, **kwargs):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR next_proxy_number
        #   14 STORE_FAST proxy_number
        #   16 LOAD_FAST self
        #   18 COPY
        #   20 LOAD_ATTR next_proxy_number
        #   30 LOAD_CONST 1
        #   32 BINARY_OP +=
        #   36 SWAP
        #   38 STORE_ATTR next_proxy_number
        #   48 LOAD_CONST '{}:{}'
        #   50 LOAD_METHOD format
        #   72 LOAD_FAST proxy_number
        #   74 LOAD_FAST serial_number
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST proxy_string
        #   92 LOAD_GLOBAL NULL + DeviceProxy
        #  104 LOAD_FAST self
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR process_name
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR log_queue
        #  130 LOAD_FAST serial_number
        #  132 LOAD_FAST proxy_string
        #  134 LOAD_FAST find_func
        #  136 BUILD_LIST
        #  138 LOAD_FAST args
        #  140 LIST_EXTEND
        #  142 LIST_TO_TUPLE
        #  144 BUILD_MAP
        #  146 LOAD_FAST kwargs
        #  148 DICT_MERGE
        #  150 CALL_FUNCTION_EX
        #  152 STORE_FAST proxy
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR proxies
        #  166 LOAD_METHOD append
        #  188 LOAD_FAST proxy
        #  190 PRECALL
        #  194 CALL
        #  204 POP_TOP
        #  206 LOAD_FAST proxy
        #  208 RETURN_VALUE
        pass

Proxy = Union[DeviceProxy, DeviceSubProxy]
