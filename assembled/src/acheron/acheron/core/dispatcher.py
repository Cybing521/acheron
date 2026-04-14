# Source Generated with Decompyle++
# File: dispatcher.pyc (Python 3.11)

from collections import deque
import datetime
import functools
import logging
import os
import queue
import threading
from typing import Any, Callable, Optional, ParamSpec
import urllib.parse as urllib
import urllib.request as urllib
import weakref
from weakref import ReferenceType
import diskcache
from PySide6 import QtCore
import asphodel
from ..device_process.proxy import DeviceProxyManager, DeviceSubProxy, Proxy
from .device_controller import DeviceController, RFPowerStatus
from .main_schedule import MainSchedule
from .preferences import Preferences
from .radio_scan import ActiveScanDatabase
from ..calc_process.runnner import CalcProcess
from ..device_process.remote_funcs import connect_and_open_tcp_device, find_and_open_tcp_device, find_and_open_usb_device
logger = logging.getLogger(__name__)
P = ParamSpec('P')

try:
    from ..connectivity.alert_emailer import AlertEmailManager
except Exception:
    AlertEmailManager = None

try:
    from ..connectivity.connectivity_manager import ConnectivityManager
except Exception:
    ConnectivityManager = None

try:
    from ..connectivity.event_upload import EventUploader
except Exception:
    EventUploader = None

try:
    from ..connectivity.modbus import ModbusHandler
except Exception:
    ModbusHandler = None

try:
    from ..connectivity.s3upload import mark_file_for_upload, S3UploadManager
except Exception:
    mark_file_for_upload = None
    S3UploadManager = None

try:
    from ..connectivity.socket_handler import SocketHandler
except Exception:
    SocketHandler = None

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class Dispatcher(QtCore.QObject):

    controller_created = QtCore.Signal(object)

    controller_stopped = QtCore.Signal(object)

    rf_power_changed = QtCore.Signal(int, int)

    active_triggers_changed = QtCore.Signal(object)

    initial_devices_connected = QtCore.Signal(bool, object)

    upload_manager_changed = QtCore.Signal(object)

    _create_signal = QtCore.Signal(object)

    _cleanup = QtCore.Signal(object)

    class _NullConnectivityManager:

        def add_handler(self, _handler):
            return None

        def stop(self):
            return None

        def join(self):
            return None

    def __init__(self, proxy_manager, preferences, calc_process_name):
        super().__init__()
        self.proxy_manager = proxy_manager
        self.preferences = preferences
        self.calc_process_name = calc_process_name
        self.disable_streaming = self.preferences.disable_streaming
        self.disable_archiving = self.preferences.disable_archiving
        self.alert_manager = AlertEmailManager(self.preferences) if AlertEmailManager is not None else None
        self.upload_manager = None
        self.upload_options = None
        self.event_uploader = EventUploader(self.preferences) if EventUploader is not None else self._NullConnectivityManager()
        self.main_schedule = MainSchedule()
        self.diskcache = diskcache.Cache(self.preferences.diskcache_dir, size_limit = 100000000.0)
        self.active_scan_database = ActiveScanDatabase(self.preferences)
        self.lock = threading.Lock()
        self.proxies = {}
        self.opening_proxies = set()
        self.controllers = {}
        self.controller_info = {}
        self.disconnected_controllers = set()
        self.manually_disconnected = set()
        self.rf_power_statuses = {}
        self.rf_power_needed = set()
        self.controller_active_triggers = {}
        self.active_triggers = frozenset()
        self.updating_rf = False
        self.finished = threading.Event()
        self.controller_connect_queue = queue.Queue()
        self.background_connect_thread = threading.Thread(target = self.background_connect_loop, daemon = True)
        self.final_join = threading.Event()
        self.background_join_deque = deque()
        self.background_join_thread = threading.Thread(target = self._background_join_run, daemon = True)
        self.background_join_thread.start()
        self.create_upload_manager()
        self.create_connectivity_manager()
        self.setup_callbacks()
        QtCore.QTimer.singleShot(0, self.initial_device_connect)

    def setup_callbacks(self):
        self._create_signal.connect(self._create_cb)
        self._cleanup.connect(self._cleanup_cb)

    def stop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + list
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR controllers
        #   42 LOAD_METHOD values
        #   64 PRECALL
        #   68 CALL
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST controllers
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR opening_proxies
        #  106 LOAD_METHOD clear
        #  128 PRECALL
        #  132 CALL
        #  142 POP_TOP
        #  144 LOAD_CONST None
        #  146 LOAD_CONST None
        #  148 LOAD_CONST None
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 JUMP_FORWARD to 190
        #  168 PUSH_EXC_INFO
        #  170 WITH_EXCEPT_START
        #  172 POP_JUMP_FORWARD_IF_TRUE to 182
        #  174 RERAISE
        #  176 COPY
        #  178 POP_EXCEPT
        #  180 RERAISE
        #  182 POP_TOP
        #  184 POP_EXCEPT
        #  186 POP_TOP
        #  188 POP_TOP
        #  190 LOAD_GLOBAL NULL + set
        #  202 PRECALL
        #  206 CALL
        #  216 STORE_FAST stopped
        #  218 LOAD_FAST controllers
        #  220 GET_ITER
        #  222 FOR_ITER to 612
        #  224 STORE_FAST controller
        #  226 LOAD_FAST controller
        #  228 LOAD_FAST stopped
        #  230 CONTAINS_OP
        #  232 POP_JUMP_FORWARD_IF_FALSE to 236
        #  234 JUMP_BACKWARD to 222
        #  236 LOAD_FAST controller
        #  238 LOAD_ATTR parent_controller
        #  248 STORE_FAST parent
        #  250 LOAD_FAST parent
        #  252 POP_JUMP_FORWARD_IF_NONE to 436
        #  254 LOAD_FAST parent
        #  256 LOAD_FAST stopped
        #  258 CONTAINS_OP
        #  260 POP_JUMP_FORWARD_IF_FALSE to 436
        #  262 LOAD_FAST parent
        #  264 LOAD_METHOD stop
        #  286 PRECALL
        #  290 CALL
        #  300 POP_TOP
        #  302 LOAD_FAST parent
        #  304 LOAD_METHOD join
        #  326 PRECALL
        #  330 CALL
        #  340 POP_TOP
        #  342 LOAD_FAST self
        #  344 LOAD_ATTR controller_stopped
        #  354 LOAD_METHOD emit
        #  376 LOAD_FAST parent
        #  378 PRECALL
        #  382 CALL
        #  392 POP_TOP
        #  394 LOAD_FAST stopped
        #  396 LOAD_METHOD add
        #  418 LOAD_FAST parent
        # ... bytecode truncated ...
        pass

    def join(self):
        self.final_join.set()
        if self.background_connect_thread.ident is not None:
            self.background_connect_thread.join()
        if self.background_join_thread.ident is not None:
            self.background_join_thread.join()
        self.connectivity_manager.join()
        self.event_uploader.join()

    def _cleanup_cb(self, joined):
        joined.clear()
        self.proxy_manager.clear_finished_proxies()

    def _do_join_pass(self):
        joined = []

    def _background_join_run(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR final_join
        #   14 LOAD_METHOD wait
        #   36 LOAD_CONST 0.1
        #   38 KW_NAMES
        #   40 PRECALL
        #   44 CALL
        #   54 POP_JUMP_FORWARD_IF_TRUE to 208
        #   56 LOAD_FAST self
        #   58 LOAD_METHOD _do_join_pass
        #   80 PRECALL
        #   84 CALL
        #   94 STORE_FAST joined
        #   96 LOAD_FAST joined
        #   98 POP_JUMP_FORWARD_IF_FALSE to 154
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR _cleanup
        #  112 LOAD_METHOD emit
        #  134 LOAD_FAST joined
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 DELETE_FAST joined
        #  154 LOAD_FAST self
        #  156 LOAD_ATTR final_join
        #  166 LOAD_METHOD wait
        #  188 LOAD_CONST 0.1
        #  190 KW_NAMES
        #  192 PRECALL
        #  196 CALL
        #  206 POP_JUMP_BACKWARD_IF_FALSE to 56
        #  208 LOAD_FAST self
        #  210 LOAD_METHOD _do_join_pass
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_GLOBAL logger
        #  260 LOAD_METHOD debug
        #  282 LOAD_CONST 'Background join thread exiting'
        #  284 PRECALL
        #  288 CALL
        #  298 POP_TOP
        #  300 LOAD_CONST None
        #  302 RETURN_VALUE
        pass

    def create_upload_manager(self):
        if self.preferences.upload_enabled:
            upload_options = {
                'base_dir': self.preferences.base_dir,
                's3_bucket': self.preferences.s3_bucket,
                'key_prefix': self.preferences.upload_directory,
                'access_key_id': self.preferences.access_key_id,
                'secret_access_key': self.preferences.secret_access_key,
                'aws_region': self.preferences.aws_region,
                'delete_after_upload': self.preferences.delete_original,
                'archive_interval': datetime.timedelta(minutes = self.preferences.archive_interval) }
        else:
            upload_options = None
        if upload_options == self.upload_options:
            return None
        self.upload_options = None
        if self.upload_manager:
            self.upload_manager.stop()
            self.background_join_deque.append(self.upload_manager.join)
            self.upload_manager = None

    def create_connectivity_manager(self):
        if ConnectivityManager is None:
            self.connectivity_manager = self._NullConnectivityManager()
            return None
        self.connectivity_manager = ConnectivityManager(self.preferences)
        if SocketHandler is not None:
            self.connectivity_manager.add_handler(SocketHandler(self.preferences))
        if ModbusHandler is not None:
            self.connectivity_manager.add_handler(ModbusHandler(self.preferences))

    def _create_cb(self, f):
        f()

    def _start_proxy(self, proxy, controller):
        connected = functools.partial(self._proxy_connected, weakref.ref(proxy), weakref.ref(controller))
        proxy.connected.connect(connected)
        disconnected = functools.partial(self._proxy_disconnected, weakref.ref(proxy), weakref.ref(controller))
        proxy.disconnected.connect(disconnected)
        self.opening_proxies.add(proxy)

    def _create_proxy(self, serial_number, location, reconnect_info, find_func, *args, **kwargs):
        controller = self._update_or_create_controller((serial_number,), None, reconnect_info, None, set())

    def _proxy_connected(self, proxy_ref, controller_ref):
        proxy = proxy_ref()
        controller = controller_ref()

    def _proxy_disconnected(self, proxy_ref, controller_ref):
        proxy = proxy_ref()
        controller = controller_ref()
        self.lock

    def get_proxy_locations(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + set
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR proxies
        #   42 LOAD_METHOD values
        #   64 PRECALL
        #   68 CALL
        #   78 PRECALL
        #   82 CALL
        #   92 SWAP
        #   94 LOAD_CONST None
        #   96 LOAD_CONST None
        #   98 LOAD_CONST None
        #  100 PRECALL
        #  104 CALL
        #  114 POP_TOP
        #  116 RETURN_VALUE
        #  118 PUSH_EXC_INFO
        #  120 WITH_EXCEPT_START
        #  122 POP_JUMP_FORWARD_IF_TRUE to 132
        #  124 RERAISE
        #  126 COPY
        #  128 POP_EXCEPT
        #  130 RERAISE
        #  132 POP_TOP
        #  134 POP_EXCEPT
        #  136 POP_TOP
        #  138 POP_TOP
        #  140 LOAD_CONST None
        #  142 RETURN_VALUE
        pass

    def create_usb_proxy(self, serial_number, location):
        reconnect_info = {
            'type': 'usb',
            'location': location,
            'serial_number': serial_number }
        self._create_proxy(serial_number, location, reconnect_info, find_and_open_usb_device, location)

    def create_tcp_proxy(self, serial_number, location):
        reconnect_info = {
            'type': 'tcp',
            'location': location,
            'serial_number': serial_number }
        self._create_proxy(serial_number, location, reconnect_info, find_and_open_tcp_device, serial_number, location)

    def create_tcp_proxy_from_device(self, tcp_device):
        adv = tcp_device.tcp_get_advertisement()
        serial_number = adv.serial_number
        location = tcp_device.get_location_string()
        self.create_tcp_proxy(serial_number, location)

    def create_manual_tcp_proxy(self, hostname, port, timeout, serial_number, err_cb):
        manual_tcp_info = {
            'hostname': hostname,
            'port': port,
            'timeout': timeout,
            'serial_number': serial_number,
            'err_cb': err_cb }
        self.controller_connect_queue.put(manual_tcp_info)

    def _collect_new_usb_device_keys(self, locations):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + set
        #   14 PRECALL
        #   18 CALL
        #   28 STORE_FAST keys
        #   30 LOAD_GLOBAL NULL + asphodel
        #   42 LOAD_ATTR find_usb_devices
        #   52 PRECALL
        #   56 CALL
        #   66 GET_ITER
        #   68 FOR_ITER to 428
        #   70 STORE_FAST device
        #   72 LOAD_FAST device
        #   74 LOAD_METHOD get_location_string
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST location
        #  112 LOAD_FAST location
        #  114 LOAD_FAST locations
        #  116 CONTAINS_OP
        #  118 POP_JUMP_FORWARD_IF_FALSE to 426
        #  120 NOP
        #  122 LOAD_FAST device
        #  124 LOAD_METHOD open
        #  146 PRECALL
        #  150 CALL
        #  160 POP_TOP
        #  162 LOAD_FAST device
        #  164 LOAD_METHOD get_serial_number
        #  186 PRECALL
        #  190 CALL
        #  200 STORE_FAST serial_number
        #  202 JUMP_FORWARD to 286
        #  204 PUSH_EXC_INFO
        #  206 LOAD_GLOBAL asphodel
        #  218 LOAD_ATTR AsphodelError
        #  228 CHECK_EXC_MATCH
        #  230 POP_JUMP_FORWARD_IF_FALSE to 278
        #  232 POP_TOP
        #  234 POP_EXCEPT
        #  236 LOAD_FAST device
        #  238 LOAD_METHOD close
        #  260 PRECALL
        #  264 CALL
        #  274 POP_TOP
        #  276 JUMP_BACKWARD to 68
        #  278 RERAISE
        #  280 COPY
        #  282 POP_EXCEPT
        #  284 RERAISE
        #  286 NOP
        #  288 LOAD_FAST device
        #  290 LOAD_METHOD close
        #  312 PRECALL
        #  316 CALL
        #  326 POP_TOP
        #  328 JUMP_FORWARD to 380
        #  330 PUSH_EXC_INFO
        #  332 LOAD_FAST device
        #  334 LOAD_METHOD close
        #  356 PRECALL
        #  360 CALL
        #  370 POP_TOP
        #  372 RERAISE
        #  374 COPY
        #  376 POP_EXCEPT
        #  378 RERAISE
        #  380 LOAD_FAST keys
        #  382 LOAD_METHOD add
        #  404 LOAD_FAST serial_number
        #  406 LOAD_FAST location
        #  408 BUILD_TUPLE
        #  410 PRECALL
        #  414 CALL
        #  424 POP_TOP
        #  426 JUMP_BACKWARD to 68
        #  428 LOAD_FAST keys
        #  430 RETURN_VALUE
        pass

    def _collect_new_tcp_device_keys(self, locations):
        keys = set()
        for device in asphodel.find_tcp_devices():
            adv = device.tcp_get_advertisement()
            if adv.connected:
                continue
            location = device.get_location_string()
            serial_number = adv.serial_number
            if location not in locations:
                keys.add((serial_number, location))
            return keys

    def rescan_usb(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL asphodel
        #   14 LOAD_ATTR nativelib
        #   24 LOAD_ATTR usb_devices_supported
        #   34 POP_JUMP_FORWARD_IF_TRUE to 40
        #   36 LOAD_CONST None
        #   38 RETURN_VALUE
        #   40 LOAD_FAST self
        #   42 LOAD_METHOD get_proxy_locations
        #   64 PRECALL
        #   68 CALL
        #   78 STORE_FAST locations
        #   80 LOAD_FAST self
        #   82 LOAD_METHOD _collect_new_usb_device_keys
        #  104 LOAD_FAST locations
        #  106 PRECALL
        #  110 CALL
        #  120 STORE_FAST usb_keys
        #  122 LOAD_FAST usb_keys
        #  124 GET_ITER
        #  126 FOR_ITER to 182
        #  128 UNPACK_SEQUENCE
        #  132 STORE_FAST serial_number
        #  134 STORE_FAST location
        #  136 LOAD_FAST self
        #  138 LOAD_METHOD create_usb_proxy
        #  160 LOAD_FAST serial_number
        #  162 LOAD_FAST location
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 JUMP_BACKWARD to 126
        #  182 LOAD_CONST None
        #  184 RETURN_VALUE
        pass

    def initial_device_connect(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL QtCore
        #   14 LOAD_ATTR QCoreApplication
        #   24 LOAD_METHOD processEvents
        #   46 PRECALL
        #   50 CALL
        #   60 POP_TOP
        #   62 LOAD_CONST False
        #   64 STORE_FAST tcp_scanned
        #   66 BUILD_LIST
        #   68 STORE_FAST tcp_devices
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR preferences
        #   82 LOAD_ATTR initial_connect_usb
        #   92 POP_JUMP_FORWARD_IF_TRUE to 118
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR preferences
        #  106 LOAD_ATTR rescan_connect_usb
        #  116 POP_JUMP_FORWARD_IF_FALSE to 158
        #  118 LOAD_FAST self
        #  120 LOAD_METHOD rescan_usb
        #  142 PRECALL
        #  146 CALL
        #  156 POP_TOP
        #  158 LOAD_FAST self
        #  160 LOAD_ATTR preferences
        #  170 LOAD_ATTR initial_connect_tcp
        #  180 POP_JUMP_FORWARD_IF_TRUE to 206
        #  182 LOAD_FAST self
        #  184 LOAD_ATTR preferences
        #  194 LOAD_ATTR rescan_connect_tcp
        #  204 POP_JUMP_FORWARD_IF_FALSE to 548
        #  206 LOAD_GLOBAL asphodel
        #  218 LOAD_ATTR nativelib
        #  228 LOAD_ATTR tcp_devices_supported
        #  238 POP_JUMP_FORWARD_IF_FALSE to 548
        #  240 LOAD_GLOBAL NULL + asphodel
        #  252 LOAD_ATTR find_tcp_devices
        #  262 PRECALL
        #  266 CALL
        #  276 STORE_FAST tcp_devices
        #  278 LOAD_CONST True
        #  280 STORE_FAST tcp_scanned
        #  282 LOAD_FAST self
        #  284 LOAD_METHOD get_proxy_locations
        #  306 PRECALL
        #  310 CALL
        #  320 STORE_FAST locations
        #  322 LOAD_FAST tcp_devices
        #  324 GET_ITER
        #  326 FOR_ITER to 548
        #  328 STORE_FAST device
        #  330 LOAD_FAST device
        #  332 LOAD_METHOD tcp_get_advertisement
        #  354 PRECALL
        #  358 CALL
        #  368 STORE_FAST adv
        #  370 LOAD_FAST adv
        #  372 LOAD_ATTR connected
        #  382 POP_JUMP_FORWARD_IF_FALSE to 386
        #  384 JUMP_BACKWARD to 326
        #  386 LOAD_FAST adv
        #  388 LOAD_ATTR serial_number
        #  398 STORE_FAST serial_number
        #  400 LOAD_FAST device
        #  402 LOAD_METHOD get_location_string
        #  424 PRECALL
        #  428 CALL
        #  438 STORE_FAST location
        #  440 LOAD_FAST location
        #  442 LOAD_FAST locations
        #  444 CONTAINS_OP
        #  446 POP_JUMP_FORWARD_IF_FALSE to 546
        #  448 LOAD_GLOBAL logger
        #  460 LOAD_METHOD debug
        #  482 LOAD_CONST 'Connecting TCP device %s'
        #  484 LOAD_FAST serial_number
        #  486 PRECALL
        #  490 CALL
        #  500 POP_TOP
        # ... bytecode truncated ...
        pass

    def _update_or_create_controller(self, serial_numbers, proxy, reconnect_info, parent_controller, parties):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR controllers
        #   30 LOAD_METHOD get
        #   52 LOAD_FAST serial_numbers
        #   54 PRECALL
        #   58 CALL
        #   68 STORE_FAST controller
        #   70 LOAD_FAST controller
        #   72 EXTENDED_ARG
        #   74 POP_JUMP_FORWARD_IF_TRUE to 844
        #   76 LOAD_GLOBAL logger
        #   88 LOAD_METHOD debug
        #  110 LOAD_CONST 'Creating device controller for %s'
        #  112 LOAD_FAST serial_numbers
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 LOAD_FAST self
        #  132 LOAD_ATTR main_schedule
        #  142 LOAD_METHOD get_schedule
        #  164 LOAD_FAST serial_numbers
        #  166 PRECALL
        #  170 CALL
        #  180 STORE_FAST schedule
        #  182 LOAD_GLOBAL NULL + DeviceController
        #  194 LOAD_FAST self
        #  196 LOAD_FAST serial_numbers
        #  198 LOAD_CONST -1
        #  200 BINARY_SUBSCR
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR preferences
        #  222 LOAD_FAST self
        #  224 LOAD_ATTR diskcache
        #  234 LOAD_FAST schedule
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR calc_process_name
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR disable_streaming
        #  260 LOAD_FAST self
        #  262 LOAD_ATTR disable_archiving
        #  272 LOAD_FAST parent_controller
        #  274 LOAD_FAST parties
        #  276 PRECALL
        #  280 CALL
        #  290 STORE_FAST controller
        #  292 LOAD_FAST controller
        #  294 LOAD_ATTR rf_power_changed
        #  304 LOAD_METHOD connect
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR rf_power_changed_cb
        #  338 PRECALL
        #  342 CALL
        #  352 POP_TOP
        #  354 LOAD_FAST controller
        #  356 LOAD_ATTR rf_power_needed
        #  366 LOAD_METHOD connect
        #  388 LOAD_FAST self
        #  390 LOAD_ATTR rf_power_needed_cb
        #  400 PRECALL
        #  404 CALL
        #  414 POP_TOP
        #  416 LOAD_FAST controller
        #  418 LOAD_ATTR active_triggers_changed
        #  428 LOAD_METHOD connect
        #  450 LOAD_FAST self
        #  452 LOAD_ATTR active_triggers_changed_cb
        #  462 PRECALL
        #  466 CALL
        #  476 POP_TOP
        #  478 LOAD_FAST controller
        #  480 LOAD_ATTR disconnected_signal
        #  490 LOAD_METHOD connect
        #  512 LOAD_FAST self
        #  514 LOAD_ATTR active_scan_database
        #  524 LOAD_ATTR controller_disconnected
        # ... bytecode truncated ...
        pass

    def stop_controller(self, controller):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 BUILD_LIST
        #    4 STORE_FAST children
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR lock
        #   18 BEFORE_WITH
        #   20 POP_TOP
        #   22 LOAD_FAST self
        #   24 LOAD_ATTR controllers
        #   34 LOAD_METHOD values
        #   56 PRECALL
        #   60 CALL
        #   70 GET_ITER
        #   72 FOR_ITER to 142
        #   74 STORE_FAST c
        #   76 LOAD_FAST c
        #   78 LOAD_ATTR parent_controller
        #   88 LOAD_FAST controller
        #   90 COMPARE_OP ==
        #   96 POP_JUMP_FORWARD_IF_FALSE to 140
        #   98 LOAD_FAST children
        #  100 LOAD_METHOD append
        #  122 LOAD_FAST c
        #  124 PRECALL
        #  128 CALL
        #  138 POP_TOP
        #  140 JUMP_BACKWARD to 72
        #  142 NOP
        #  144 LOAD_CONST None
        #  146 LOAD_CONST None
        #  148 LOAD_CONST None
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 JUMP_FORWARD to 190
        #  168 PUSH_EXC_INFO
        #  170 WITH_EXCEPT_START
        #  172 POP_JUMP_FORWARD_IF_TRUE to 182
        #  174 RERAISE
        #  176 COPY
        #  178 POP_EXCEPT
        #  180 RERAISE
        #  182 POP_TOP
        #  184 POP_EXCEPT
        #  186 POP_TOP
        #  188 POP_TOP
        #  190 LOAD_FAST children
        #  192 GET_ITER
        #  194 FOR_ITER to 242
        #  196 STORE_FAST child
        #  198 LOAD_FAST self
        #  200 LOAD_METHOD stop_controller
        #  222 LOAD_FAST child
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 JUMP_BACKWARD to 194
        #  242 LOAD_FAST controller
        #  244 LOAD_METHOD stop
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_CONST False
        #  284 STORE_FAST last_power_needed
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR lock
        #  298 BEFORE_WITH
        #  300 POP_TOP
        #  302 LOAD_GLOBAL NULL + set
        #  314 PRECALL
        #  318 CALL
        #  328 STORE_FAST serial_number_tuples
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR controllers
        #  342 LOAD_METHOD items
        #  364 PRECALL
        #  368 CALL
        #  378 GET_ITER
        #  380 FOR_ITER to 446
        #  382 UNPACK_SEQUENCE
        # ... bytecode truncated ...
        pass

    def _check_reconnect_devices(self):
        rescan_connect_usb = self.preferences.rescan_connect_usb
        rescan_connect_tcp = self.preferences.rescan_connect_tcp
        scan_usb = rescan_connect_usb
        scan_tcp = rescan_connect_tcp
        self.lock
        locations = set(self.proxies.values())

    def _connect_manual_tcp_proxy(self, hostname, port, timeout, serial_number, err_cb):
        try:
            device = asphodel.create_tcp_device(hostname, port, timeout, serial_number)
        except asphodel.AsphodelError:
            logger.exception('Could not connect to TCP device.')
            if err_cb:
                err_cb()
            return None

        adv = device.tcp_get_advertisement()
        found_serial_number = adv.serial_number
        location = device.get_location_string()
        reconnect_info = {
            'type': 'manual_tcp',
            'location': location,
            'serial_number': found_serial_number,
            'hostname': hostname,
            'port': port,
            'timeout': timeout }
        f = functools.partial(self._create_proxy, found_serial_number, location, reconnect_info, connect_and_open_tcp_device, hostname, port, timeout, found_serial_number)
        self._create_signal.emit(f)

    def background_connect_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 NOP
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR finished
        #   18 LOAD_METHOD is_set
        #   40 PRECALL
        #   44 CALL
        #   54 POP_JUMP_FORWARD_IF_FALSE to 60
        #   56 LOAD_CONST None
        #   58 RETURN_VALUE
        #   60 LOAD_FAST self
        #   62 LOAD_METHOD _check_reconnect_devices
        #   84 PRECALL
        #   88 CALL
        #   98 POP_TOP
        #  100 NOP
        #  102 NOP
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR controller_connect_queue
        #  116 LOAD_METHOD get
        #  138 LOAD_CONST True
        #  140 LOAD_CONST 1.5
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST manual_tcp_info
        #  158 PUSH_NULL
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR _connect_manual_tcp_proxy
        #  172 LOAD_CONST ()
        #  174 BUILD_MAP
        #  176 LOAD_FAST manual_tcp_info
        #  178 DICT_MERGE
        #  180 CALL_FUNCTION_EX
        #  182 POP_TOP
        #  184 JUMP_FORWARD to 228
        #  186 PUSH_EXC_INFO
        #  188 LOAD_GLOBAL queue
        #  200 LOAD_ATTR Empty
        #  210 CHECK_EXC_MATCH
        #  212 POP_JUMP_FORWARD_IF_FALSE to 220
        #  214 POP_TOP
        #  216 POP_EXCEPT
        #  218 JUMP_FORWARD to 230
        #  220 RERAISE
        #  222 COPY
        #  224 POP_EXCEPT
        #  226 RERAISE
        #  228 JUMP_BACKWARD to 102
        #  230 JUMP_BACKWARD to 6
        #  232 PUSH_EXC_INFO
        #  234 LOAD_GLOBAL Exception
        #  246 CHECK_EXC_MATCH
        #  248 POP_JUMP_FORWARD_IF_FALSE to 310
        #  250 POP_TOP
        #  252 LOAD_GLOBAL logger
        #  264 LOAD_METHOD exception
        #  286 LOAD_CONST 'Uncaught exception in background_connect_loop'
        #  288 PRECALL
        #  292 CALL
        #  302 POP_TOP
        #  304 POP_EXCEPT
        #  306 LOAD_CONST None
        #  308 RETURN_VALUE
        #  310 RERAISE
        #  312 COPY
        #  314 POP_EXCEPT
        #  316 RERAISE
        pass

    def set_disable_streaming(self, disable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST disable
        #   20 LOAD_FAST self
        #   22 STORE_ATTR disable_streaming
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR controllers
        #   44 LOAD_METHOD values
        #   66 PRECALL
        #   70 CALL
        #   80 GET_ITER
        #   82 FOR_ITER to 130
        #   84 STORE_FAST controller
        #   86 LOAD_FAST controller
        #   88 LOAD_METHOD update_disable_streaming
        #  110 LOAD_FAST disable
        #  112 PRECALL
        #  116 CALL
        #  126 POP_TOP
        #  128 JUMP_BACKWARD to 82
        #  130 NOP
        #  132 LOAD_CONST None
        #  134 LOAD_CONST None
        #  136 LOAD_CONST None
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        #  158 PUSH_EXC_INFO
        #  160 WITH_EXCEPT_START
        #  162 POP_JUMP_FORWARD_IF_TRUE to 172
        #  164 RERAISE
        #  166 COPY
        #  168 POP_EXCEPT
        #  170 RERAISE
        #  172 POP_TOP
        #  174 POP_EXCEPT
        #  176 POP_TOP
        #  178 POP_TOP
        #  180 LOAD_CONST None
        #  182 RETURN_VALUE
        pass

    def set_disable_archiving(self, disable):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST disable
        #   20 LOAD_FAST self
        #   22 STORE_ATTR disable_archiving
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR controllers
        #   44 LOAD_METHOD values
        #   66 PRECALL
        #   70 CALL
        #   80 GET_ITER
        #   82 FOR_ITER to 130
        #   84 STORE_FAST controller
        #   86 LOAD_FAST controller
        #   88 LOAD_METHOD update_disable_archiving
        #  110 LOAD_FAST disable
        #  112 PRECALL
        #  116 CALL
        #  126 POP_TOP
        #  128 JUMP_BACKWARD to 82
        #  130 NOP
        #  132 LOAD_CONST None
        #  134 LOAD_CONST None
        #  136 LOAD_CONST None
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        #  158 PUSH_EXC_INFO
        #  160 WITH_EXCEPT_START
        #  162 POP_JUMP_FORWARD_IF_TRUE to 172
        #  164 RERAISE
        #  166 COPY
        #  168 POP_EXCEPT
        #  170 RERAISE
        #  172 POP_TOP
        #  174 POP_EXCEPT
        #  176 POP_TOP
        #  178 POP_TOP
        #  180 LOAD_CONST None
        #  182 RETURN_VALUE
        pass

    def mark_for_upload(self, files):
        if len(files) == 0:
            return None
        for filename in None:
            logger.info('Marking file {}'.format(filename))
            mark_file_for_upload(filename)
            if self.upload_manager:
                self.upload_manager.rescan()
                return None
            return None

    def update_preferences(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR controllers
        #   30 LOAD_METHOD copy
        #   52 PRECALL
        #   56 CALL
        #   66 STORE_FAST controller_copy
        #   68 LOAD_CONST None
        #   70 LOAD_CONST None
        #   72 LOAD_CONST None
        #   74 PRECALL
        #   78 CALL
        #   88 POP_TOP
        #   90 JUMP_FORWARD to 114
        #   92 PUSH_EXC_INFO
        #   94 WITH_EXCEPT_START
        #   96 POP_JUMP_FORWARD_IF_TRUE to 106
        #   98 RERAISE
        #  100 COPY
        #  102 POP_EXCEPT
        #  104 RERAISE
        #  106 POP_TOP
        #  108 POP_EXCEPT
        #  110 POP_TOP
        #  112 POP_TOP
        #  114 LOAD_FAST controller_copy
        #  116 LOAD_METHOD values
        #  138 PRECALL
        #  142 CALL
        #  152 GET_ITER
        #  154 FOR_ITER to 200
        #  156 STORE_FAST controller
        #  158 LOAD_FAST controller
        #  160 LOAD_METHOD update_preferences
        #  182 PRECALL
        #  186 CALL
        #  196 POP_TOP
        #  198 JUMP_BACKWARD to 154
        #  200 LOAD_FAST self
        #  202 LOAD_METHOD create_upload_manager
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR alert_manager
        #  252 LOAD_METHOD update_preferences
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 LOAD_FAST self
        #  292 LOAD_ATTR connectivity_manager
        #  302 LOAD_METHOD update_preferences
        #  324 PRECALL
        #  328 CALL
        #  338 POP_TOP
        #  340 LOAD_CONST None
        #  342 RETURN_VALUE
        pass

    def _emit_rf_power_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 PUSH_NULL
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR rf_power_changed
        #   16 LOAD_ATTR emit
        #   26 LOAD_FAST self
        #   28 LOAD_METHOD get_rf_power_status
        #   50 PRECALL
        #   54 CALL
        #   64 CALL_FUNCTION_EX
        #   66 POP_TOP
        #   68 LOAD_CONST None
        #   70 RETURN_VALUE
        pass

    def get_rf_power_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST 0
        #    4 STORE_FAST enabled
        #    6 LOAD_CONST 0
        #    8 STORE_FAST total
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR lock
        #   22 BEFORE_WITH
        #   24 POP_TOP
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR rf_power_statuses
        #   38 LOAD_METHOD values
        #   60 PRECALL
        #   64 CALL
        #   74 GET_ITER
        #   76 FOR_ITER to 134
        #   78 STORE_FAST status
        #   80 LOAD_FAST status
        #   82 LOAD_GLOBAL RFPowerStatus
        #   94 LOAD_ATTR ENABLED
        #  104 COMPARE_OP ==
        #  110 POP_JUMP_FORWARD_IF_FALSE to 122
        #  112 LOAD_FAST enabled
        #  114 LOAD_CONST 1
        #  116 BINARY_OP +=
        #  120 STORE_FAST enabled
        #  122 LOAD_FAST total
        #  124 LOAD_CONST 1
        #  126 BINARY_OP +=
        #  130 STORE_FAST total
        #  132 JUMP_BACKWARD to 76
        #  134 NOP
        #  136 LOAD_CONST None
        #  138 LOAD_CONST None
        #  140 LOAD_CONST None
        #  142 PRECALL
        #  146 CALL
        #  156 POP_TOP
        #  158 JUMP_FORWARD to 182
        #  160 PUSH_EXC_INFO
        #  162 WITH_EXCEPT_START
        #  164 POP_JUMP_FORWARD_IF_TRUE to 174
        #  166 RERAISE
        #  168 COPY
        #  170 POP_EXCEPT
        #  172 RERAISE
        #  174 POP_TOP
        #  176 POP_EXCEPT
        #  178 POP_TOP
        #  180 POP_TOP
        #  182 LOAD_FAST enabled
        #  184 LOAD_FAST total
        #  186 BUILD_TUPLE
        #  188 RETURN_VALUE
        pass

    def rf_power_changed_cb(self, controller, status):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST status
        #   20 LOAD_GLOBAL RFPowerStatus
        #   32 LOAD_ATTR NOT_SUPPORTED
        #   42 COMPARE_OP ==
        #   48 POP_JUMP_FORWARD_IF_FALSE to 102
        #   50 NOP
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR rf_power_statuses
        #   64 LOAD_FAST controller
        #   66 DELETE_SUBSCR
        #   68 JUMP_FORWARD to 122
        #   70 PUSH_EXC_INFO
        #   72 LOAD_GLOBAL KeyError
        #   84 CHECK_EXC_MATCH
        #   86 POP_JUMP_FORWARD_IF_FALSE to 94
        #   88 POP_TOP
        #   90 POP_EXCEPT
        #   92 JUMP_FORWARD to 122
        #   94 RERAISE
        #   96 COPY
        #   98 POP_EXCEPT
        #  100 RERAISE
        #  102 LOAD_FAST status
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR rf_power_statuses
        #  116 LOAD_FAST controller
        #  118 STORE_SUBSCR
        #  122 LOAD_CONST None
        #  124 LOAD_CONST None
        #  126 LOAD_CONST None
        #  128 PRECALL
        #  132 CALL
        #  142 POP_TOP
        #  144 JUMP_FORWARD to 168
        #  146 PUSH_EXC_INFO
        #  148 WITH_EXCEPT_START
        #  150 POP_JUMP_FORWARD_IF_TRUE to 160
        #  152 RERAISE
        #  154 COPY
        #  156 POP_EXCEPT
        #  158 RERAISE
        #  160 POP_TOP
        #  162 POP_EXCEPT
        #  164 POP_TOP
        #  166 POP_TOP
        #  168 LOAD_FAST self
        #  170 LOAD_ATTR updating_rf
        #  180 POP_JUMP_FORWARD_IF_TRUE to 226
        #  182 LOAD_FAST self
        #  184 LOAD_METHOD _emit_rf_power_status
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        #  226 LOAD_CONST None
        #  228 RETURN_VALUE
        pass

    def enable_all_rf_power(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST True
        #    4 LOAD_FAST self
        #    6 STORE_ATTR updating_rf
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR lock
        #   28 BEFORE_WITH
        #   30 POP_TOP
        #   32 LOAD_GLOBAL NULL + set
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR controllers
        #   56 LOAD_METHOD values
        #   78 PRECALL
        #   82 CALL
        #   92 PRECALL
        #   96 CALL
        #  106 STORE_FAST all_controllers
        #  108 LOAD_CONST None
        #  110 LOAD_CONST None
        #  112 LOAD_CONST None
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 JUMP_FORWARD to 154
        #  132 PUSH_EXC_INFO
        #  134 WITH_EXCEPT_START
        #  136 POP_JUMP_FORWARD_IF_TRUE to 146
        #  138 RERAISE
        #  140 COPY
        #  142 POP_EXCEPT
        #  144 RERAISE
        #  146 POP_TOP
        #  148 POP_EXCEPT
        #  150 POP_TOP
        #  152 POP_TOP
        #  154 LOAD_FAST all_controllers
        #  156 GET_ITER
        #  158 FOR_ITER to 204
        #  160 STORE_FAST controller
        #  162 LOAD_FAST controller
        #  164 LOAD_METHOD enable_rf_power
        #  186 PRECALL
        #  190 CALL
        #  200 POP_TOP
        #  202 JUMP_BACKWARD to 158
        #  204 LOAD_CONST False
        #  206 LOAD_FAST self
        #  208 STORE_ATTR updating_rf
        #  218 LOAD_FAST self
        #  220 LOAD_METHOD _emit_rf_power_status
        #  242 PRECALL
        #  246 CALL
        #  256 POP_TOP
        #  258 LOAD_CONST None
        #  260 RETURN_VALUE
        pass

    def disable_all_rf_power(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST True
        #    4 LOAD_FAST self
        #    6 STORE_ATTR updating_rf
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR lock
        #   28 BEFORE_WITH
        #   30 POP_TOP
        #   32 LOAD_GLOBAL NULL + set
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR controllers
        #   56 LOAD_METHOD values
        #   78 PRECALL
        #   82 CALL
        #   92 PRECALL
        #   96 CALL
        #  106 STORE_FAST all_controllers
        #  108 LOAD_CONST None
        #  110 LOAD_CONST None
        #  112 LOAD_CONST None
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 JUMP_FORWARD to 154
        #  132 PUSH_EXC_INFO
        #  134 WITH_EXCEPT_START
        #  136 POP_JUMP_FORWARD_IF_TRUE to 146
        #  138 RERAISE
        #  140 COPY
        #  142 POP_EXCEPT
        #  144 RERAISE
        #  146 POP_TOP
        #  148 POP_EXCEPT
        #  150 POP_TOP
        #  152 POP_TOP
        #  154 LOAD_FAST all_controllers
        #  156 GET_ITER
        #  158 FOR_ITER to 204
        #  160 STORE_FAST controller
        #  162 LOAD_FAST controller
        #  164 LOAD_METHOD disable_rf_power
        #  186 PRECALL
        #  190 CALL
        #  200 POP_TOP
        #  202 JUMP_BACKWARD to 158
        #  204 LOAD_CONST False
        #  206 LOAD_FAST self
        #  208 STORE_ATTR updating_rf
        #  218 LOAD_FAST self
        #  220 LOAD_METHOD _emit_rf_power_status
        #  242 PRECALL
        #  246 CALL
        #  256 POP_TOP
        #  258 LOAD_CONST None
        #  260 RETURN_VALUE
        pass

    def rf_power_needed_cb(self, controller, needed):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST False
        #    4 STORE_FAST turn_on
        #    6 LOAD_CONST False
        #    8 STORE_FAST turn_off
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR lock
        #   22 BEFORE_WITH
        #   24 POP_TOP
        #   26 LOAD_FAST needed
        #   28 POP_JUMP_FORWARD_IF_FALSE to 178
        #   30 LOAD_FAST controller
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR rf_power_needed
        #   44 CONTAINS_OP
        #   46 POP_JUMP_FORWARD_IF_FALSE to 76
        #   48 NOP
        #   50 LOAD_CONST None
        #   52 LOAD_CONST None
        #   54 LOAD_CONST None
        #   56 PRECALL
        #   60 CALL
        #   70 POP_TOP
        #   72 LOAD_CONST None
        #   74 RETURN_VALUE
        #   76 LOAD_GLOBAL NULL + bool
        #   88 LOAD_FAST self
        #   90 LOAD_ATTR rf_power_needed
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST was_needed
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR rf_power_needed
        #  128 LOAD_METHOD add
        #  150 LOAD_FAST controller
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_FAST was_needed
        #  170 POP_JUMP_FORWARD_IF_TRUE to 176
        #  172 LOAD_CONST True
        #  174 STORE_FAST turn_on
        #  176 JUMP_FORWARD to 296
        #  178 LOAD_FAST controller
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR rf_power_needed
        #  192 CONTAINS_OP
        #  194 POP_JUMP_FORWARD_IF_FALSE to 268
        #  196 LOAD_FAST self
        #  198 LOAD_ATTR rf_power_needed
        #  208 LOAD_METHOD discard
        #  230 LOAD_FAST controller
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR rf_power_needed
        #  260 POP_JUMP_FORWARD_IF_TRUE to 266
        #  262 LOAD_CONST True
        #  264 STORE_FAST turn_off
        #  266 JUMP_FORWARD to 296
        #  268 NOP
        #  270 LOAD_CONST None
        #  272 LOAD_CONST None
        #  274 LOAD_CONST None
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        #  296 LOAD_CONST None
        #  298 LOAD_CONST None
        #  300 LOAD_CONST None
        #  302 PRECALL
        #  306 CALL
        #  316 POP_TOP
        #  318 JUMP_FORWARD to 342
        #  320 PUSH_EXC_INFO
        #  322 WITH_EXCEPT_START
        #  324 POP_JUMP_FORWARD_IF_TRUE to 334
        # ... bytecode truncated ...
        pass

    def create_remote(self, controller, serial_number_str, subproxy, parties):
        reconnect_info = {
            'type': 'remote',
            'serial_number': serial_number_str }
        parent_sn = controller.serial_number
        serial_numbers = (parent_sn, serial_number_str)
        new_controller = self._update_or_create_controller(serial_numbers, None, reconnect_info, controller, parties)
        self._start_proxy(subproxy, new_controller)
        return new_controller

    def active_triggers_changed_cb(self, controller, active_triggers):
        self.lock
        last = self.controller_active_triggers[controller]

    def register_old_calc_process(self, calc_process):
        self.background_join_deque.append(calc_process.join)

    def register_old_proxy(self, proxy):
        self.background_join_deque.append(proxy.wait_for_close)

    def upload_file(self, filename):
        if self.upload_manager:
            self.upload_manager.upload(filename)
            return None

    def get_controller(self, serial_numbers, registration_str):
        if len(serial_numbers) > 1:
            party = f'''parent-{serial_numbers[-1]}'''
            parent_controller = self.get_controller(serial_numbers[:-1], party)
        else:
            parent_controller = None
        controller = self._update_or_create_controller(serial_numbers, None, None, parent_controller, {
            registration_str})
        return controller

    def mark_manually_disconnected(self, controller):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + set
        #   30 PRECALL
        #   34 CALL
        #   44 STORE_FAST serial_number_tuples
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR controllers
        #   58 LOAD_METHOD items
        #   80 PRECALL
        #   84 CALL
        #   94 GET_ITER
        #   96 FOR_ITER to 162
        #   98 UNPACK_SEQUENCE
        #  102 STORE_FAST serial_numbers
        #  104 STORE_FAST c
        #  106 LOAD_FAST c
        #  108 LOAD_FAST controller
        #  110 COMPARE_OP ==
        #  116 POP_JUMP_FORWARD_IF_FALSE to 160
        #  118 LOAD_FAST serial_number_tuples
        #  120 LOAD_METHOD add
        #  142 LOAD_FAST serial_numbers
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 JUMP_BACKWARD to 96
        #  162 LOAD_FAST self
        #  164 LOAD_ATTR manually_disconnected
        #  174 LOAD_METHOD update
        #  196 LOAD_FAST serial_number_tuples
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_CONST None
        #  216 LOAD_CONST None
        #  218 LOAD_CONST None
        #  220 PRECALL
        #  224 CALL
        #  234 POP_TOP
        #  236 LOAD_CONST None
        #  238 RETURN_VALUE
        #  240 PUSH_EXC_INFO
        #  242 WITH_EXCEPT_START
        #  244 POP_JUMP_FORWARD_IF_TRUE to 254
        #  246 RERAISE
        #  248 COPY
        #  250 POP_EXCEPT
        #  252 RERAISE
        #  254 POP_TOP
        #  256 POP_EXCEPT
        #  258 POP_TOP
        #  260 POP_TOP
        #  262 LOAD_CONST None
        #  264 RETURN_VALUE
        pass
