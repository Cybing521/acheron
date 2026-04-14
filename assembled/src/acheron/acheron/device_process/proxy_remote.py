# Source Generated with Decompyle++
# File: proxy_remote.pyc (Python 3.11)

import logging
from logging.handlers import QueueHandler
import multiprocessing
import os
import queue
import signal
import sys
import threading
from typing import Any, Callable, cast, Literal, Optional, Union
import psutil
from asphodel import AsphodelNativeDevice
from ..device_logging import DeviceLoggerAdapter
logger = logging.getLogger(__name__)
TIMEOUT = 0.1
CleanupTuple = tuple[(Callable, tuple, dict)]
JobTuple = tuple[(int, Optional[int], Callable, tuple, dict)]
JobReplyTuple = tuple[(int, Any, Optional[Exception])]
FromProcessType = Union[(Literal[True], JobReplyTuple, Exception)]
device_cleanup: dict[(Optional[AsphodelNativeDevice], list[CleanupTuple])] = { }
device_lock = threading.Lock()
subproxy_devices: dict[(Optional[int], AsphodelNativeDevice)] = { }
device_identifiers: dict[(AsphodelNativeDevice, tuple[(str, str)])] = { }

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def _simple_access(device, function_name, *args, **kwargs):
    func = getattr(device, function_name)

def get_device_logger(logger, device):
    (serial_number, proxy_string) = device_identifiers.get(device, ('unknown', 'unknown'))
    return DeviceLoggerAdapter(logger, serial_number, proxy_string)

def setup_remote_logging(log_queue):
    handler = QueueHandler(log_queue)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)
    pyusb_logger = logging.getLogger('usb')
    pyusb_logger.propagate = False

def register_device_cleanup(device, cleanup_func, *args, **kwargs):
    cleanup_list = device_cleanup.setdefault(device, [])
    cleanup_list.append((cleanup_func, args, kwargs))

def unregister_device_cleanup(device, cleanup_func, *args, **kwargs):
    cleanup_list = device_cleanup.get(device, None)
    if cleanup_list:
        
        try:
            cleanup_list.remove((cleanup_func, args, kwargs))
        except ValueError:
            pass

        if not cleanup_list:
            del device_cleanup[device]
            return None
        return None
        return None

def do_device_cleanup(device):
    cleanup_list = device_cleanup.pop(device, [])

def do_final_cleanup(device):
    subproxy_devices = set(device_cleanup.keys())
    subproxy_devices.discard(device)
    subproxy_devices.discard(None)
    for subproxy_device in subproxy_devices:
        do_device_cleanup(subproxy_device)
        do_device_cleanup(device)
        do_device_cleanup(None)
        return None

def proxy_process(log_queue, incoming, outgoing, serial_number, proxy_string, find_func, ffargs, ffkwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + open
    #   14 LOAD_GLOBAL os
    #   26 LOAD_ATTR devnull
    #   36 PRECALL
    #   40 CALL
    #   50 LOAD_GLOBAL sys
    #   62 STORE_ATTR stdout
    #   72 LOAD_GLOBAL NULL + open
    #   84 LOAD_GLOBAL os
    #   96 LOAD_ATTR devnull
    #  106 PRECALL
    #  110 CALL
    #  120 LOAD_GLOBAL sys
    #  132 STORE_ATTR stderr
    #  142 LOAD_GLOBAL NULL + setup_remote_logging
    #  154 LOAD_FAST log_queue
    #  156 PRECALL
    #  160 CALL
    #  170 POP_TOP
    #  172 LOAD_CONST None
    #  174 STORE_FAST device
    #  176 LOAD_GLOBAL NULL + DeviceLoggerAdapter
    #  188 LOAD_GLOBAL logger
    #  200 LOAD_FAST serial_number
    #  202 LOAD_FAST proxy_string
    #  204 PRECALL
    #  208 CALL
    #  218 STORE_FAST device_logger
    #  220 LOAD_GLOBAL sys
    #  232 LOAD_ATTR platform
    #  242 LOAD_CONST 'win32'
    #  244 COMPARE_OP ==
    #  250 POP_JUMP_FORWARD_IF_FALSE to 336
    #  252 LOAD_GLOBAL NULL + signal
    #  264 LOAD_ATTR signal
    #  274 LOAD_GLOBAL signal
    #  286 LOAD_ATTR SIGINT
    #  296 LOAD_GLOBAL signal
    #  308 LOAD_ATTR SIG_IGN
    #  318 PRECALL
    #  322 CALL
    #  332 POP_TOP
    #  334 JUMP_FORWARD to 374
    #  336 LOAD_GLOBAL NULL + os
    #  348 LOAD_ATTR setpgrp
    #  358 PRECALL
    #  362 CALL
    #  372 POP_TOP
    #  374 LOAD_CONST <code object <listcomp> at 0x105abff00, file "acheron\device_process\proxy_remote.py", line 136>
    #  376 MAKE_FUNCTION
    #  378 LOAD_FAST ffargs
    #  380 GET_ITER
    #  382 PRECALL
    #  386 CALL
    #  396 STORE_FAST arg_strs
    #  398 LOAD_FAST arg_strs
    #  400 LOAD_METHOD extend
    #  422 LOAD_CONST <code object <genexpr> at 0x105a733f0, file "acheron\device_process\proxy_remote.py", line 137>
    #  424 MAKE_FUNCTION
    #  426 LOAD_FAST ffkwargs
    #  428 LOAD_METHOD items
    #  450 PRECALL
    #  454 CALL
    #  464 GET_ITER
    #  466 PRECALL
    #  470 CALL
    #  480 PRECALL
    #  484 CALL
    #  494 POP_TOP
    #  496 LOAD_CONST '{}({})'
    #  498 LOAD_METHOD format
    #  520 LOAD_FAST find_func
    #  522 LOAD_ATTR __name__
    #  532 LOAD_CONST ', '
    #  534 LOAD_METHOD join
    #  556 LOAD_FAST arg_strs
    #  558 PRECALL
    #  562 CALL
    #  572 PRECALL
    # ... bytecode truncated ...
    pass

def create_subproxy_util(device, func, subproxy_id, proxy_string, *args, **kwargs):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 NOP
    #    4 PUSH_NULL
    #    6 LOAD_FAST func
    #    8 LOAD_FAST device
    #   10 BUILD_LIST
    #   12 LOAD_FAST args
    #   14 LIST_EXTEND
    #   16 LIST_TO_TUPLE
    #   18 BUILD_MAP
    #   20 LOAD_FAST kwargs
    #   22 DICT_MERGE
    #   24 CALL_FUNCTION_EX
    #   26 STORE_FAST subproxy_device
    #   28 LOAD_FAST subproxy_device
    #   30 LOAD_GLOBAL subproxy_devices
    #   42 LOAD_FAST subproxy_id
    #   44 STORE_SUBSCR
    #   48 LOAD_FAST subproxy_device
    #   50 LOAD_METHOD get_serial_number
    #   72 PRECALL
    #   76 CALL
    #   86 STORE_FAST subproxy_sn
    #   88 LOAD_CONST '{}->{}'
    #   90 LOAD_METHOD format
    #  112 LOAD_FAST proxy_string
    #  114 LOAD_FAST subproxy_sn
    #  116 PRECALL
    #  120 CALL
    #  130 STORE_FAST subproxy_string
    #  132 LOAD_FAST subproxy_sn
    #  134 LOAD_FAST subproxy_string
    #  136 BUILD_TUPLE
    #  138 LOAD_GLOBAL device_identifiers
    #  150 LOAD_FAST subproxy_device
    #  152 STORE_SUBSCR
    #  156 LOAD_FAST subproxy_sn
    #  158 LOAD_FAST subproxy_string
    #  160 BUILD_TUPLE
    #  162 RETURN_VALUE
    #  164 PUSH_EXC_INFO
    #  166 LOAD_GLOBAL Exception
    #  178 CHECK_EXC_MATCH
    #  180 POP_JUMP_FORWARD_IF_FALSE to 270
    #  182 POP_TOP
    #  184 LOAD_GLOBAL NULL + get_device_logger
    #  196 LOAD_GLOBAL logger
    #  208 LOAD_FAST device
    #  210 PRECALL
    #  214 CALL
    #  224 LOAD_METHOD exception
    #  246 LOAD_CONST 'Unhandled exception in create_subproxy_util()'
    #  248 PRECALL
    #  252 CALL
    #  262 POP_TOP
    #  264 POP_EXCEPT
    #  266 LOAD_CONST None
    #  268 RETURN_VALUE
    #  270 RERAISE
    #  272 COPY
    #  274 POP_EXCEPT
    #  276 RERAISE
    pass
