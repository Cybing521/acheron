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
from device_logging import DeviceLoggerAdapter, RemoteToLocalLogHandler
from proxy_remote import _simple_access, create_subproxy_util, do_device_cleanup, FromProcessType, JobTuple, proxy_process, TIMEOUT
logger = logging.getLogger(__name__)
P = ParamSpec('P')

class DeviceOperation(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class SimpleDeviceOperation(DeviceOperation):
    pass
# WARNING: Decompyle incomplete


class DeviceProxy(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class DeviceSubProxy(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

Proxy = Union[(DeviceProxy, DeviceSubProxy)]

class DeviceProxyManager:
    
    def __init__(self = None, process_name = None):
        self.process_name = process_name
        self.setup_logging()
        self.proxies = []
        self.next_proxy_number = 0

    
    def setup_logging(self = None):
        local_handler = RemoteToLocalLogHandler(__name__ + '.remote')
        self.log_queue = multiprocessing.Queue()
        self.log_listener = QueueListener(self.log_queue, local_handler)
        self.log_listener.start()

    
    def stop(self = None):
        for proxy in self.proxies:
            proxy.close_connection()
            for proxy in self.proxies:
                proxy.wait_for_close()
                self.log_listener.stop()
                return None

    
    def clear_finished_proxies(self = None):
        for proxy in self.proxies.copy():
            if proxy.is_finished():
                self.proxies.remove(proxy)
            return None

    
    def new_proxy(self = None, serial_number = None, find_func = None, *args, **kwargs):
        proxy_number = self.next_proxy_number
        '{}:{}'.format(proxy_number, serial_number) = self, self.next_proxy_number += 1, .next_proxy_number
    # WARNING: Decompyle incomplete


