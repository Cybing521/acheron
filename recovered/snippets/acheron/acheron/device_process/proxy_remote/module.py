# Source Generated with Decompyle++
# File: tmpfqc5ggps.marshal (Python 3.11)

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
from device_logging import DeviceLoggerAdapter
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

def _simple_access(device = None, function_name = None, *args, **kwargs):
    func = getattr(device, function_name)
# WARNING: Decompyle incomplete


def get_device_logger(logger = None, device = None):
    (serial_number, proxy_string) = device_identifiers.get(device, ('unknown', 'unknown'))
    return DeviceLoggerAdapter(logger, serial_number, proxy_string)


def setup_remote_logging(log_queue = None):
    handler = QueueHandler(log_queue)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)
    pyusb_logger = logging.getLogger('usb')
    pyusb_logger.propagate = False


def register_device_cleanup(device = None, cleanup_func = None, *args, **kwargs):
    cleanup_list = device_cleanup.setdefault(device, [])
    cleanup_list.append((cleanup_func, args, kwargs))


def unregister_device_cleanup(device = None, cleanup_func = None, *args, **kwargs):
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


def do_device_cleanup(device = None):
    cleanup_list = device_cleanup.pop(device, [])
# WARNING: Decompyle incomplete


def do_final_cleanup(device = None):
    subproxy_devices = set(device_cleanup.keys())
    subproxy_devices.discard(device)
    subproxy_devices.discard(None)
    for subproxy_device in subproxy_devices:
        do_device_cleanup(subproxy_device)
        do_device_cleanup(device)
        do_device_cleanup(None)
        return None


def proxy_process(log_queue, incoming, outgoing, serial_number, proxy_string = None, find_func = None, ffargs = None, ffkwargs = ('log_queue', 'multiprocessing.Queue[Any]', 'incoming', 'multiprocessing.Queue[Optional[JobTuple]]', 'outgoing', 'multiprocessing.Queue[Optional[FromProcessType]]', 'serial_number', str, 'proxy_string', str, 'find_func', Callable, 'ffargs', tuple, 'ffkwargs', dict, 'return', None)):
    sys.stdout = open(os.devnull)
    sys.stderr = open(os.devnull)
    setup_remote_logging(log_queue)
    device = None
    device_logger = DeviceLoggerAdapter(logger, serial_number, proxy_string)
    if sys.platform == 'win32':
        signal.signal(signal.SIGINT, signal.SIG_IGN)
    else:
        os.setpgrp()
    arg_strs = ffargs()
    (lambda .0: pass# WARNING: Decompyle incomplete
)(ffkwargs.items()())
    find_func_str = '{}({})'.format(find_func.__name__, ', '.join(arg_strs))
    device_logger.debug('Proxy process starting with %s', find_func_str)
    me = psutil.Process(os.getpid())
# WARNING: Decompyle incomplete


def create_subproxy_util(device = None, func = None, subproxy_id = None, proxy_string = ('device', AsphodelNativeDevice, 'func', Callable, 'subproxy_id', int, 'proxy_string', str, 'args', Any, 'kwargs', Any, 'return', Optional[tuple[(str, str)]]), *args, **kwargs):
    ''' called from create_subproxy() to handle registration '''
    pass
# WARNING: Decompyle incomplete

