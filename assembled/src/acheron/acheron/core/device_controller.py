# Source Generated with Decompyle++
# File: device_controller.pyc (Python 3.11)

from __future__ import annotations
import datetime
import enum
import functools
import logging
import struct
import threading
from typing import Any, cast, Collection, Optional, Protocol, TYPE_CHECKING, Union
import weakref
from weakref import ReferenceType
from diskcache import Cache
from PySide6 import QtCore
from asphodel.device_info import DeviceInfo
from ..device_logging import DeviceLoggerAdapter
from ..device_process.proxy import DeviceOperation, DeviceProxy, Proxy, SimpleDeviceOperation
from .main_schedule import DeviceSchedule
from .preferences import get_device_preferences, Preferences
from ..calc_process.types import CalcSettings, ChannelInformation, Trigger
from ..calc_process.runnner import CalcProcess
from ..device_process.bootloader import already_programmed
from ..device_process.remote_funcs import explode
from ..device_process.schedule import OutputConfig, ScheduleItem
from ..device_process.stream_controller import create_remote, HardwareTestFunction, RFTestParams, start_stream_controller, stop_stream_controller, StreamControl, StreamSettings, StreamStatus
if TYPE_CHECKING:
    from .dispatcher import Dispatcher
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: DeviceControllerState = <NODE:12>()
# INVALID FROM DECOMPILER: RFPowerStatus = <NODE:12>()
MANUAL_CONTROL = 'manual'
REMOTE_CONTROL = 'remote'

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DeviceControllerState(enum.Enum):

    DISCONNECTED = enum.auto()

    CONNECTING = enum.auto()

    STREAMING_STARTING = enum.auto()

    RUNNING = enum.auto()

    RUNNING_FUNCTION = enum.auto()

class RFPowerStatus(enum.Enum):

    NOT_SUPPORTED = enum.auto()

    DISABLED = enum.auto()

    ENABLED = enum.auto()

class HardwareTestCallback(Protocol):

    def hardware_test_function_finished(self, test_id, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def hardware_test_run_finished(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

class DeviceController(QtCore.QObject):

    state_changed_signal = QtCore.Signal(object, str)

    disconnected_signal = QtCore.Signal(object)

    progress_signal = QtCore.Signal(int, int, str)

    rgb_updated = QtCore.Signal(int, object)

    led_updated = QtCore.Signal(int, int)

    ctrl_var_updated = QtCore.Signal(int, int)

    rf_power_changed = QtCore.Signal(object, object)

    rf_power_needed = QtCore.Signal(object, bool)

    active_triggers_changed = QtCore.Signal(object, object, object)

    alerts_changed = QtCore.Signal(object)

    scan_data = QtCore.Signal(object, object)

    active_scan_data = QtCore.Signal(object, int, object)

    remote_connecting = QtCore.Signal(object, int, bool)

    scan_first_pass = QtCore.Signal()

    manual_control_changed = QtCore.Signal(bool)

    ongoing_items = QtCore.Signal(object)

    trigger_count_changed = QtCore.Signal(int)

    schedule_count_changed = QtCore.Signal(int)

    rf_test_finished = QtCore.Signal()

    remote_target_changed = QtCore.Signal(object, bool, bool)

    remote_connected = QtCore.Signal(bool)

    remote_target_connected = QtCore.Signal(bool)

    channel_update = QtCore.Signal(object, object, object)

    plot_update = QtCore.Signal(object, object, object)

    fft_update = QtCore.Signal(object, object, object, object)

    lost_packet_update = QtCore.Signal(object, object, object)

    def __init__(self, dispatcher, serial_number, preferences, diskcache, schedule, calc_process_name, disable_streaming, disable_archiving, parent_controller, parties):
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
        #   68 LOAD_FAST dispatcher
        #   70 LOAD_FAST self
        #   72 STORE_ATTR dispatcher
        #   82 LOAD_FAST serial_number
        #   84 LOAD_FAST self
        #   86 STORE_ATTR serial_number
        #   96 LOAD_FAST preferences
        #   98 LOAD_FAST self
        #  100 STORE_ATTR preferences
        #  110 LOAD_FAST diskcache
        #  112 LOAD_FAST self
        #  114 STORE_ATTR diskcache
        #  124 LOAD_FAST schedule
        #  126 LOAD_FAST self
        #  128 STORE_ATTR schedule
        #  138 LOAD_FAST calc_process_name
        #  140 LOAD_FAST self
        #  142 STORE_ATTR calc_process_name
        #  152 LOAD_FAST disable_streaming
        #  154 LOAD_FAST self
        #  156 STORE_ATTR disable_streaming
        #  166 LOAD_FAST disable_archiving
        #  168 LOAD_FAST self
        #  170 STORE_ATTR disable_archiving
        #  180 LOAD_FAST parent_controller
        #  182 LOAD_FAST self
        #  184 STORE_ATTR parent_controller
        #  194 LOAD_FAST parties
        #  196 LOAD_METHOD copy
        #  218 PRECALL
        #  222 CALL
        #  232 LOAD_FAST self
        #  234 STORE_ATTR parties
        #  244 LOAD_FAST self
        #  246 LOAD_ATTR parties
        #  256 POP_JUMP_FORWARD_IF_TRUE to 320
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR parties
        #  270 LOAD_METHOD add
        #  292 LOAD_GLOBAL MANUAL_CONTROL
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 LOAD_FAST serial_number
        #  322 LOAD_FAST self
        #  324 STORE_ATTR display_name
        #  334 LOAD_GLOBAL NULL + get_device_preferences
        #  346 LOAD_FAST serial_number
        #  348 PRECALL
        #  352 CALL
        #  362 LOAD_FAST self
        #  364 STORE_ATTR device_prefs
        #  374 LOAD_GLOBAL DeviceControllerState
        #  386 LOAD_ATTR DISCONNECTED
        #  396 LOAD_FAST self
        #  398 STORE_ATTR state
        #  408 LOAD_CONST None
        #  410 LOAD_FAST self
        #  412 STORE_ATTR proxy
        #  422 LOAD_GLOBAL NULL + threading
        #  434 LOAD_ATTR Event
        #  444 PRECALL
        #  448 CALL
        #  458 LOAD_FAST self
        #  460 STORE_ATTR proxy_finished
        #  470 LOAD_FAST self
        #  472 LOAD_ATTR proxy_finished
        #  482 LOAD_METHOD set
        #  504 PRECALL
        #  508 CALL
        #  518 POP_TOP
        # ... bytecode truncated ...
        pass

    def _setup_proxy_operations(self):
        self.start_stream_controller_op = DeviceOperation(start_stream_controller)
        self.stop_stream_controller_op = DeviceOperation(stop_stream_controller)
        self.stop_stream_controller_op.completed.connect(self._stop_stream_controller_cb)
        self.close_device_op = SimpleDeviceOperation('close')

    def update_preferences(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR calc_settings
        #   32 POP_JUMP_FORWARD_IF_NONE to 48
        #   34 LOAD_FAST self
        #   36 LOAD_ATTR stream_settings
        #   46 POP_JUMP_FORWARD_IF_NOT_NONE to 52
        #   48 LOAD_CONST None
        #   50 RETURN_VALUE
        #   52 LOAD_FAST self
        #   54 LOAD_METHOD _get_settings
        #   76 PRECALL
        #   80 CALL
        #   90 UNPACK_SEQUENCE
        #   94 STORE_FAST stream_settings
        #   96 STORE_FAST calc_settings
        #   98 LOAD_FAST self
        #  100 LOAD_ATTR calc_settings
        #  110 LOAD_FAST calc_settings
        #  112 COMPARE_OP !=
        #  118 POP_JUMP_FORWARD_IF_FALSE to 186
        #  120 LOAD_FAST calc_settings
        #  122 LOAD_FAST self
        #  124 STORE_ATTR calc_settings
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR calc_process
        #  146 LOAD_METHOD change_settings
        #  168 LOAD_FAST calc_settings
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR stream_settings
        #  198 LOAD_FAST stream_settings
        #  200 COMPARE_OP !=
        #  206 POP_JUMP_FORWARD_IF_FALSE to 298
        #  208 LOAD_FAST stream_settings
        #  210 LOAD_FAST self
        #  212 STORE_ATTR stream_settings
        #  222 LOAD_FAST self
        #  224 LOAD_ATTR calc_process
        #  234 LOAD_METHOD send_stream_ctrl_message
        #  256 LOAD_GLOBAL StreamControl
        #  268 LOAD_ATTR CHANGE_SETTINGS
        #  278 LOAD_FAST stream_settings
        #  280 BUILD_TUPLE
        #  282 PRECALL
        #  286 CALL
        #  296 POP_TOP
        #  298 LOAD_FAST self
        #  300 LOAD_METHOD _update_alert_triggers
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 LOAD_CONST None
        #  340 RETURN_VALUE
        pass

    def update_disable_streaming(self, disable):
        self.disable_streaming = disable
        self._update_main_schedule_item()

    def update_disable_archiving(self, disable):
        if disable:
            self.logger.info('Disabling archiving')
        else:
            self.logger.info('Enabling archiving')
        self.disable_archiving = disable
        self._update_main_schedule_item()

    def set_active_streams(self, streams):
        self.disable_streaming = False

    def _set_state(self, state, message):
        if self.state == state:
            return None
        self.state = None
        self.state_changed_signal.emit(state, message)
        if state == DeviceControllerState.DISCONNECTED:
            self.logger.info('Disconnected')
            self.disconnected_signal.emit(self)
            return None

    def set_proxy(self, proxy):
        if self.proxy:
            self._error(self.tr('Reconnecting'))
        self.proxy = proxy
        self.proxy_finished.clear()
        self.proxy.disconnected.connect(functools.partial(self._proxy_disconnect_cb, weakref.ref(proxy)))
        self._start_stream_controller()

    def _proxy_disconnect_cb(self, proxy_ref):
        proxy = proxy_ref()

    def _streaming_disconnected(self, message):
        self.dispatcher.connectivity_manager.stop_device(self.serial_number)
        self.active_triggers_changed.emit(self, frozenset(), self.trigger_names)
        self.last_emitted_active_triggers = frozenset()
        self._set_state(DeviceControllerState.DISCONNECTED, message)
        self._stop_rf_power_handling()
        self.rf_power_needed.emit(self, False)
        self._set_schedule_count(0)

    def _error(self, message):
        if self.streaming:
            self.streaming = False
            if self.calc_process:
                self.calc_process.stop()
                if not self.proxy:
                    self.calc_process.close()
                    self.dispatcher.register_old_calc_process(self.calc_process)
                    self.calc_process = None
            if self.proxy:
                self.proxy.send_job(self.stop_stream_controller_op)
        self._disconnect_proxy()
        self._streaming_disconnected(message)
        self._remote_disconnected_cb()

    def _disconnect_proxy(self):
        if self.proxy:
            self.proxy.send_job(self.close_device_op)
            self.proxy.close_connection()
            self.dispatcher.register_old_proxy(self.proxy)
            self.proxy = None
            self.proxy_finished.set()
            return None

    def _stop_stream_controller_cb(self):
        if self.calc_process:
            self.calc_process.close()
            self.dispatcher.register_old_calc_process(self.calc_process)
            self.calc_process = None
            return None

    def stop(self):
        self._error(self.tr('Closed'))

    def join(self):
        self.proxy_finished.wait()

    def _get_settings(self):
        interval = datetime.timedelta(minutes = self.preferences.archive_interval)
        output_config = OutputConfig(compression_level = self.preferences.compression_level, base_name = None, base_directory = self.preferences.base_dir, device_directory = True, date_dir_structure = True, datetime_filename = True, roll_over_interval = interval, upload_marker = self.preferences.upload_enabled)
        stream_settings = StreamSettings(auto_rgb = self.preferences.auto_rgb, response_time = self.device_prefs.response_time, buffer_time = self.device_prefs.buffer_time, timeout = self.device_prefs.stream_timeout, default_output_config = output_config)
        calc_settings = CalcSettings(channel_interval = self.preferences.update_timer_interval / 1000, plot_interval = self.preferences.graph_timer_interval / 1000, fft_interval = self.preferences.graph_timer_interval / 1000, downsample = self.preferences.downsample)
        return (stream_settings, calc_settings)

    def _update_main_schedule_item(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL MANUAL_CONTROL
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR parties
        #   26 CONTAINS_OP
        #   28 POP_JUMP_FORWARD_IF_FALSE to 96
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR schedule
        #   42 LOAD_METHOD clear_partition
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR main_schedule_id
        #   76 PRECALL
        #   80 CALL
        #   90 POP_TOP
        #   92 LOAD_CONST None
        #   94 RETURN_VALUE
        #   96 LOAD_FAST self
        #   98 LOAD_ATTR disable_streaming
        #  108 POP_JUMP_FORWARD_IF_FALSE to 140
        #  110 LOAD_GLOBAL NULL + frozenset
        #  122 PRECALL
        #  126 CALL
        #  136 STORE_FAST active_streams
        #  138 JUMP_FORWARD to 154
        #  140 LOAD_FAST self
        #  142 LOAD_ATTR desired_streams
        #  152 STORE_FAST active_streams
        #  154 LOAD_GLOBAL NULL + ScheduleItem
        #  166 LOAD_FAST self
        #  168 LOAD_ATTR main_schedule_id
        #  178 LOAD_FAST active_streams
        #  180 LOAD_CONST None
        #  182 LOAD_CONST None
        #  184 LOAD_CONST None
        #  186 LOAD_CONST None
        #  188 LOAD_CONST None
        #  190 LOAD_FAST self
        #  192 LOAD_ATTR disable_archiving
        #  202 POP_JUMP_FORWARD_IF_FALSE to 208
        #  204 LOAD_CONST None
        #  206 JUMP_FORWARD to 210
        #  208 LOAD_CONST True
        #  210 KW_NAMES
        #  212 PRECALL
        #  216 CALL
        #  226 STORE_FAST schedule_item
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR schedule
        #  240 LOAD_METHOD add_item
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR main_schedule_id
        #  274 LOAD_FAST schedule_item
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        pass

    def _update_remote_schedule_item(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR remote_target_serial
        #   14 POP_JUMP_FORWARD_IF_FALSE to 170
        #   16 LOAD_GLOBAL MANUAL_CONTROL
        #   28 LOAD_FAST self
        #   30 LOAD_ATTR parties
        #   40 CONTAINS_OP
        #   42 POP_JUMP_FORWARD_IF_FALSE to 170
        #   44 LOAD_GLOBAL NULL + ScheduleItem
        #   56 LOAD_CONST '_remote'
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR remote_target_serial
        #   70 LOAD_FAST self
        #   72 LOAD_ATTR remote_target_bootloader
        #   82 LOAD_CONST None
        #   84 LOAD_CONST None
        #   86 LOAD_CONST None
        #   88 LOAD_CONST None
        #   90 LOAD_CONST None
        #   92 LOAD_CONST None
        #   94 KW_NAMES
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST schedule_item
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR schedule
        #  124 LOAD_METHOD add_item
        #  146 LOAD_CONST '_remote'
        #  148 LOAD_FAST schedule_item
        #  150 PRECALL
        #  154 CALL
        #  164 POP_TOP
        #  166 LOAD_CONST None
        #  168 RETURN_VALUE
        #  170 LOAD_FAST self
        #  172 LOAD_ATTR schedule
        #  182 LOAD_METHOD clear_partition
        #  204 LOAD_CONST '_remote'
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        pass

    def _update_schedule_items(self):
        self._update_main_schedule_item()
        self._update_remote_schedule_item()

    def _start_stream_controller(self):
        self.device_info = None
        if not self.proxy:
            return None
        self.streaming = None
        self._set_state(DeviceControllerState.CONNECTING, self.tr('Loading device information...'))
        (self.stream_settings, self.calc_settings) = self._get_settings()
        if self.calc_process:
            self.calc_process.stop()
            self.dispatcher.register_old_calc_process(self.calc_process)
            self.calc_process = None
        self._update_schedule_items()
        schedule_items = self.schedule.get_items()
        self._update_alert_triggers()
        self.triggers = self._get_triggers()
        self.calc_process = CalcProcess(self.calc_process_name, self.serial_number, self.is_shown, self.calc_settings, self.triggers)
        self.proxy.disconnected.connect(self.calc_process.close)
        self.calc_process.processing_start.connect(self._processing_start_cb)
        self.calc_process.processing_stop.connect(self._processing_stop_cb)
        self.calc_process.status_received.connect(self._status_cb)
        self.calc_process.channel_update.connect(self.channel_update)
        self.calc_process.plot_update.connect(self.plot_update)
        self.calc_process.fft_update.connect(self.fft_update)
        self.calc_process.lost_packet_update.connect(self.lost_packet_update)
        self.calc_process.unknown_id.connect(self._unknown_id_cb)
        self.calc_process.active_triggers_changed.connect(self._active_triggers_changed_cb)
        (ctrl_pipe, packet_pipe, status_pipe) = self.calc_process.get_pipes()
        self.proxy.send_job(self.start_stream_controller_op, self.stream_settings, schedule_items, self.main_schedule_id, self.dispatcher.active_triggers, self.diskcache, ctrl_pipe, packet_pipe, status_pipe)

    def do_explode(self):
        if self.proxy:
            self.proxy.send_job(DeviceOperation(explode))
            return None

    def force_run_bootloader(self):
        if self.calc_process:
            message = self.tr('Connecting to bootloader...')
            self.logger.info(message)
            self._set_state(DeviceControllerState.CONNECTING, message)
            self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RUN_BOOTLOADER,))
            return None

    def force_run_application(self):
        if self.calc_process:
            message = self.tr('Connecting to application...')
            self.logger.info(message)
            self._set_state(DeviceControllerState.CONNECTING, message)
            self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RUN_APPLICATION,))
            return None

    def force_reset(self):
        if self.calc_process:
            message = self.tr('Resetting device...')
            self.logger.info(message)
            self._set_state(DeviceControllerState.CONNECTING, message)
            self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RESET,))
            return None

    def write_nvm(self, nvm):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 30
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_NOT_NONE to 86
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR logger
        #   42 LOAD_METHOD warning
        #   64 LOAD_CONST 'Connot write NVM while disconnected!'
        #   66 PRECALL
        #   70 CALL
        #   80 POP_TOP
        #   82 LOAD_CONST None
        #   84 RETURN_VALUE
        #   86 LOAD_GLOBAL NULL + bytes
        #   98 LOAD_FAST nvm
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST nvm
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR device_info
        #  128 LOAD_ATTR nvm
        #  138 LOAD_FAST nvm
        #  140 COMPARE_OP !=
        #  146 POP_JUMP_FORWARD_IF_FALSE to 410
        #  148 LOAD_FAST nvm
        #  150 LOAD_FAST self
        #  152 LOAD_ATTR device_info
        #  162 STORE_ATTR nvm
        #  172 LOAD_FAST self
        #  174 LOAD_METHOD tr
        #  196 LOAD_CONST 'Writing NVM...'
        #  198 PRECALL
        #  202 CALL
        #  212 STORE_FAST message
        #  214 LOAD_FAST self
        #  216 LOAD_METHOD _set_state
        #  238 LOAD_GLOBAL DeviceControllerState
        #  250 LOAD_ATTR CONNECTING
        #  260 LOAD_FAST message
        #  262 PRECALL
        #  266 CALL
        #  276 POP_TOP
        #  278 LOAD_FAST self
        #  280 LOAD_ATTR logger
        #  290 LOAD_METHOD info
        #  312 LOAD_FAST message
        #  314 PRECALL
        #  318 CALL
        #  328 POP_TOP
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR calc_process
        #  342 LOAD_METHOD send_stream_ctrl_message
        #  364 LOAD_GLOBAL StreamControl
        #  376 LOAD_ATTR WRITE_NVM
        #  386 LOAD_FAST nvm
        #  388 BUILD_TUPLE
        #  390 PRECALL
        #  394 CALL
        #  404 POP_TOP
        #  406 LOAD_CONST None
        #  408 RETURN_VALUE
        #  410 LOAD_FAST self
        #  412 LOAD_ATTR device_info
        #  422 LOAD_ATTR nvm_modified
        #  432 LOAD_CONST True
        #  434 IS_OP
        #  436 POP_JUMP_FORWARD_IF_FALSE to 482
        #  438 LOAD_FAST self
        #  440 LOAD_METHOD force_reset
        #  462 PRECALL
        #  466 CALL
        #  476 POP_TOP
        #  478 LOAD_CONST None
        #  480 RETURN_VALUE
        #  482 LOAD_FAST self
        #  484 LOAD_ATTR logger
        #  494 LOAD_METHOD info
        # ... bytecode truncated ...
        pass

    def _unknown_id_cb(self, unknown_id):
        msg = 'Unknown ID {} while decoding packet'.format(unknown_id)
        self.logger.error(msg)

    def set_global_active_triggers(self, active_triggers):
        if self.calc_process:
            self.calc_process.send_stream_ctrl_message((StreamControl.ACTIVE_TRIGGERS_CHANGED, active_triggers))
            return None

    def _get_triggers(self):
        old_triggers_count = self.trigger_count
        all_triggers = set()

    def _update_trigger_names(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + set
        #   14 PRECALL
        #   18 CALL
        #   28 STORE_FAST trigger_names
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR registered_triggers
        #   42 LOAD_METHOD items
        #   64 PRECALL
        #   68 CALL
        #   78 GET_ITER
        #   80 FOR_ITER to 166
        #   82 UNPACK_SEQUENCE
        #   86 STORE_FAST key
        #   88 STORE_FAST triggers
        #   90 LOAD_FAST key
        #   92 LOAD_CONST 'alerts'
        #   94 COMPARE_OP !=
        #  100 POP_JUMP_FORWARD_IF_FALSE to 164
        #  102 LOAD_FAST trigger_names
        #  104 LOAD_METHOD update
        #  126 LOAD_CONST <code object <genexpr> at 0x105af8650, file "acheron\core\device_controller.py", line 545>
        #  128 MAKE_FUNCTION
        #  130 LOAD_FAST triggers
        #  132 GET_ITER
        #  134 PRECALL
        #  138 CALL
        #  148 PRECALL
        #  152 CALL
        #  162 POP_TOP
        #  164 JUMP_BACKWARD to 80
        #  166 LOAD_GLOBAL NULL + frozenset
        #  178 LOAD_FAST trigger_names
        #  180 PRECALL
        #  184 CALL
        #  194 STORE_FAST new_trigger_names
        #  196 LOAD_FAST new_trigger_names
        #  198 LOAD_FAST self
        #  200 LOAD_ATTR trigger_names
        #  210 COMPARE_OP !=
        #  216 POP_JUMP_FORWARD_IF_FALSE to 354
        #  218 LOAD_FAST new_trigger_names
        #  220 LOAD_METHOD difference
        #  242 LOAD_FAST self
        #  244 LOAD_ATTR last_emitted_active_triggers
        #  254 PRECALL
        #  258 CALL
        #  268 STORE_FAST inactive
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR active_triggers_changed
        #  282 LOAD_METHOD emit
        #  304 LOAD_FAST self
        #  306 LOAD_FAST self
        #  308 LOAD_ATTR last_emitted_active_triggers
        #  318 LOAD_FAST inactive
        #  320 PRECALL
        #  324 CALL
        #  334 POP_TOP
        #  336 LOAD_FAST new_trigger_names
        #  338 LOAD_FAST self
        #  340 STORE_ATTR trigger_names
        #  350 LOAD_CONST None
        #  352 RETURN_VALUE
        #  354 LOAD_CONST None
        #  356 RETURN_VALUE
        pass

    def register_triggers(self, key, triggers):
        old_triggers = self.registered_triggers.get(key)
        if old_triggers == triggers:
            return None
        self.registered_triggers[key] = None
        self._update_trigger_names()
        if self.calc_process:
            triggers = self._get_triggers()
            if self.triggers != triggers:
                self.triggers = triggers
                self.calc_process.change_triggers(triggers)
                return None
            return None

    def _update_alert_triggers(self):
        triggers = set()
        alert_triggers = { }
        alert_limits = self.device_prefs.get_all_alert_limits()
        for limit_type, channel_id, subchannel_index, value in alert_limits:
            id = f'''_alert_{channel_id}_{subchannel_index}_{limit_type}'''
            trigger = Trigger(id = id, channel_id = channel_id, subchannel_index = subchannel_index, limit_type = limit_type, activate_limit = value, deactivate_limit = value)
            triggers.add(trigger)
            alert_triggers[id] = trigger
            self.alert_triggers = alert_triggers
            self.register_triggers('alerts', triggers)
            return None

    def _email_callback(self, exception):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST exception
        #    4 POP_JUMP_FORWARD_IF_NOT_NONE to 62
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR logger
        #   18 LOAD_METHOD info
        #   40 LOAD_CONST 'Sent alert email'
        #   42 PRECALL
        #   46 CALL
        #   56 POP_TOP
        #   58 LOAD_CONST None
        #   60 RETURN_VALUE
        #   62 LOAD_FAST self
        #   64 LOAD_ATTR logger
        #   74 LOAD_METHOD error
        #   96 LOAD_CONST 'Error sending alert email'
        #   98 LOAD_FAST exception
        #  100 KW_NAMES
        #  102 PRECALL
        #  106 CALL
        #  116 POP_TOP
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass

    def _active_triggers_changed_cb(self, active_triggers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + frozenset
        #   14 LOAD_CONST <code object <genexpr> at 0x105b60130, file "acheron\core\device_controller.py", line 601>
        #   16 MAKE_FUNCTION
        #   18 LOAD_FAST active_triggers
        #   20 GET_ITER
        #   22 PRECALL
        #   26 CALL
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST alerts
        #   52 LOAD_GLOBAL NULL + frozenset
        #   64 LOAD_CONST <code object <genexpr> at 0x105b60230, file "acheron\core\device_controller.py", line 603>
        #   66 MAKE_FUNCTION
        #   68 LOAD_FAST active_triggers
        #   70 GET_ITER
        #   72 PRECALL
        #   76 CALL
        #   86 PRECALL
        #   90 CALL
        #  100 STORE_FAST without_alerts
        #  102 LOAD_FAST without_alerts
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR last_emitted_active_triggers
        #  116 COMPARE_OP !=
        #  122 POP_JUMP_FORWARD_IF_FALSE to 530
        #  124 LOAD_FAST without_alerts
        #  126 LOAD_METHOD difference
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR last_emitted_active_triggers
        #  160 PRECALL
        #  164 CALL
        #  174 STORE_FAST triggers_on
        #  176 LOAD_FAST self
        #  178 LOAD_ATTR last_emitted_active_triggers
        #  188 LOAD_METHOD difference
        #  210 LOAD_FAST without_alerts
        #  212 PRECALL
        #  216 CALL
        #  226 STORE_FAST triggers_off
        #  228 LOAD_GLOBAL NULL + sorted
        #  240 LOAD_FAST triggers_on
        #  242 PRECALL
        #  246 CALL
        #  256 GET_ITER
        #  258 FOR_ITER to 318
        #  260 STORE_FAST trigger_name
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR logger
        #  274 LOAD_METHOD info
        #  296 LOAD_CONST 'Trigger enabled: %s'
        #  298 LOAD_FAST trigger_name
        #  300 PRECALL
        #  304 CALL
        #  314 POP_TOP
        #  316 JUMP_BACKWARD to 258
        #  318 LOAD_GLOBAL NULL + sorted
        #  330 LOAD_FAST triggers_off
        #  332 PRECALL
        #  336 CALL
        #  346 GET_ITER
        #  348 FOR_ITER to 408
        #  350 STORE_FAST trigger_name
        #  352 LOAD_FAST self
        #  354 LOAD_ATTR logger
        #  364 LOAD_METHOD info
        #  386 LOAD_CONST 'Trigger disabled: %s'
        #  388 LOAD_FAST trigger_name
        #  390 PRECALL
        #  394 CALL
        #  404 POP_TOP
        #  406 JUMP_BACKWARD to 348
        #  408 LOAD_FAST self
        #  410 LOAD_ATTR trigger_names
        #  420 LOAD_METHOD difference
        #  442 LOAD_FAST without_alerts
        #  444 PRECALL
        #  448 CALL
        #  458 STORE_FAST inactive
        #  460 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def _processing_start_cb(self, device_info, active_streams, channel_info):
        self.device_info = device_info
        self.channel_info = channel_info
        self.active_streams = active_streams
        if device_info.user_tag_1:
            self.display_name = device_info.user_tag_1
        else:
            self.display_name = self.serial_number
        self._set_state(DeviceControllerState.STREAMING_STARTING, self.tr('Starting streaming...'))
        connected_message = self.tr('Connected')
        self._set_state(DeviceControllerState.RUNNING, connected_message)
        self.logger.info(connected_message)
        self.start_connectivity()
        rf_power_status = self._start_rf_power_handling()
        if rf_power_status == RFPowerStatus.ENABLED:
            self.logger.info('RF power already running')

    def _processing_stop_cb(self):
        self.device_info = None
        self.channel_info.clear()
        self.active_streams = frozenset()
        message = self.tr('Device Stopped')
        self.logger.debug(message)
        self._streaming_disconnected(message)

    def _status_cb(self, status):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST status
        #    4 LOAD_CONST 0
        #    6 BINARY_SUBSCR
        #   16 STORE_FAST status_type
        #   18 LOAD_FAST status_type
        #   20 LOAD_GLOBAL StreamStatus
        #   32 LOAD_ATTR RECONNECTING
        #   42 COMPARE_OP ==
        #   48 POP_JUMP_FORWARD_IF_FALSE to 156
        #   50 LOAD_FAST self
        #   52 LOAD_METHOD _set_state
        #   74 LOAD_GLOBAL DeviceControllerState
        #   86 LOAD_ATTR CONNECTING
        #   96 LOAD_FAST self
        #   98 LOAD_METHOD tr
        #  120 LOAD_CONST 'Reconnecting...'
        #  122 PRECALL
        #  126 CALL
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 LOAD_CONST None
        #  154 RETURN_VALUE
        #  156 LOAD_FAST status_type
        #  158 LOAD_GLOBAL StreamStatus
        #  170 LOAD_ATTR DEVICE_INFO_START
        #  180 COMPARE_OP ==
        #  186 POP_JUMP_FORWARD_IF_FALSE to 294
        #  188 LOAD_FAST self
        #  190 LOAD_METHOD _set_state
        #  212 LOAD_GLOBAL DeviceControllerState
        #  224 LOAD_ATTR CONNECTING
        #  234 LOAD_FAST self
        #  236 LOAD_METHOD tr
        #  258 LOAD_CONST 'Loading device information...'
        #  260 PRECALL
        #  264 CALL
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 LOAD_CONST None
        #  292 RETURN_VALUE
        #  294 LOAD_FAST status_type
        #  296 LOAD_GLOBAL StreamStatus
        #  308 LOAD_ATTR DEVICE_INFO_PROGRESS
        #  318 COMPARE_OP ==
        #  324 POP_JUMP_FORWARD_IF_FALSE to 456
        #  326 LOAD_FAST status
        #  328 LOAD_CONST 1
        #  330 LOAD_CONST None
        #  332 BUILD_SLICE
        #  334 BINARY_SUBSCR
        #  344 UNPACK_SEQUENCE
        #  348 STORE_FAST finished
        #  350 STORE_FAST total
        #  352 STORE_FAST _section_name
        #  354 LOAD_FAST self
        #  356 LOAD_METHOD tr
        #  378 LOAD_CONST 'Loading device information...'
        #  380 PRECALL
        #  384 CALL
        #  394 STORE_FAST message
        #  396 LOAD_FAST self
        #  398 LOAD_ATTR progress_signal
        #  408 LOAD_METHOD emit
        #  430 LOAD_FAST finished
        #  432 LOAD_FAST total
        #  434 LOAD_FAST message
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_CONST None
        #  454 RETURN_VALUE
        #  456 LOAD_FAST status_type
        #  458 LOAD_GLOBAL StreamStatus
        #  470 LOAD_ATTR WRITE_NVM_PROGRESS
        #  480 COMPARE_OP ==
        #  486 POP_JUMP_FORWARD_IF_FALSE to 492
        #  488 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def set_user_tag(self, index, s):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR device_info
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 46
        #   16 LOAD_GLOBAL NULL + AssertionError
        #   28 LOAD_CONST 'No device information'
        #   30 PRECALL
        #   34 CALL
        #   44 RAISE_VARARGS
        #   46 LOAD_CONST 'user_tag_'
        #   48 LOAD_GLOBAL NULL + str
        #   60 LOAD_FAST index
        #   62 LOAD_CONST 1
        #   64 BINARY_OP +
        #   68 PRECALL
        #   72 CALL
        #   82 BINARY_OP +
        #   86 STORE_FAST tag_key
        #   88 LOAD_FAST self
        #   90 LOAD_ATTR device_info
        #  100 LOAD_ATTR tag_locations
        #  110 LOAD_FAST index
        #  112 BINARY_SUBSCR
        #  122 UNPACK_SEQUENCE
        #  126 STORE_FAST offset
        #  128 STORE_FAST length
        #  130 LOAD_GLOBAL NULL + setattr
        #  142 LOAD_FAST self
        #  144 LOAD_ATTR device_info
        #  154 LOAD_FAST tag_key
        #  156 LOAD_FAST s
        #  158 PRECALL
        #  162 CALL
        #  172 POP_TOP
        #  174 LOAD_FAST s
        #  176 LOAD_METHOD encode
        #  198 LOAD_CONST 'UTF-8'
        #  200 PRECALL
        #  204 CALL
        #  214 STORE_FAST b
        #  216 LOAD_GLOBAL NULL + bytearray
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR device_info
        #  240 LOAD_ATTR nvm
        #  250 PRECALL
        #  254 CALL
        #  264 STORE_FAST new_nvm
        #  266 LOAD_GLOBAL NULL + struct
        #  278 LOAD_ATTR pack_into
        #  288 LOAD_CONST '{}s'
        #  290 LOAD_METHOD format
        #  312 LOAD_FAST length
        #  314 PRECALL
        #  318 CALL
        #  328 LOAD_FAST new_nvm
        #  330 LOAD_FAST offset
        #  332 LOAD_FAST b
        #  334 PRECALL
        #  338 CALL
        #  348 POP_TOP
        #  350 LOAD_FAST self
        #  352 LOAD_METHOD write_nvm
        #  374 LOAD_FAST new_nvm
        #  376 PRECALL
        #  380 CALL
        #  390 POP_TOP
        #  392 LOAD_CONST None
        #  394 RETURN_VALUE
        pass

    def set_is_shown(self, is_shown):
        self.is_shown = is_shown
        if self.calc_process:
            self.calc_process.set_is_shown(is_shown)
            return None

    def plot_change(self, channel_id, subchannel_index):
        if self.calc_process:
            self.calc_process.plot_change(channel_id, subchannel_index)
            return None

    def reset_lost_packets(self):
        if self.calc_process:
            self.calc_process.reset_lost_packets()
            return None

    def set_device_mode(self, new_mode):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 110
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 114
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR calc_process
        #   42 LOAD_METHOD send_stream_ctrl_message
        #   64 LOAD_GLOBAL StreamControl
        #   76 LOAD_ATTR SET_DEVICE_MODE
        #   86 LOAD_FAST new_mode
        #   88 BUILD_TUPLE
        #   90 PRECALL
        #   94 CALL
        #  104 POP_TOP
        #  106 LOAD_CONST None
        #  108 RETURN_VALUE
        #  110 LOAD_CONST None
        #  112 RETURN_VALUE
        #  114 LOAD_CONST None
        #  116 RETURN_VALUE
        pass

    def set_rgb(self, index, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 282
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 286
        #   30 NOP
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR device_info
        #   44 LOAD_ATTR rgb_settings
        #   54 LOAD_FAST index
        #   56 BINARY_SUBSCR
        #   66 LOAD_FAST values
        #   68 COMPARE_OP ==
        #   74 POP_JUMP_FORWARD_IF_FALSE to 80
        #   76 LOAD_CONST None
        #   78 RETURN_VALUE
        #   80 LOAD_FAST values
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR device_info
        #   94 LOAD_ATTR rgb_settings
        #  104 LOAD_FAST index
        #  106 STORE_SUBSCR
        #  110 JUMP_FORWARD to 146
        #  112 PUSH_EXC_INFO
        #  114 LOAD_GLOBAL IndexError
        #  126 CHECK_EXC_MATCH
        #  128 POP_JUMP_FORWARD_IF_FALSE to 138
        #  130 POP_TOP
        #  132 POP_EXCEPT
        #  134 LOAD_CONST None
        #  136 RETURN_VALUE
        #  138 RERAISE
        #  140 COPY
        #  142 POP_EXCEPT
        #  144 RERAISE
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR calc_process
        #  158 LOAD_METHOD send_stream_ctrl_message
        #  180 LOAD_GLOBAL StreamControl
        #  192 LOAD_ATTR SET_RGB
        #  202 LOAD_FAST index
        #  204 LOAD_FAST values
        #  206 BUILD_TUPLE
        #  208 PRECALL
        #  212 CALL
        #  222 POP_TOP
        #  224 LOAD_FAST self
        #  226 LOAD_ATTR rgb_updated
        #  236 LOAD_METHOD emit
        #  258 LOAD_FAST index
        #  260 LOAD_FAST values
        #  262 PRECALL
        #  266 CALL
        #  276 POP_TOP
        #  278 LOAD_CONST None
        #  280 RETURN_VALUE
        #  282 LOAD_CONST None
        #  284 RETURN_VALUE
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        pass

    def set_led(self, index, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 282
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 286
        #   30 NOP
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR device_info
        #   44 LOAD_ATTR led_settings
        #   54 LOAD_FAST index
        #   56 BINARY_SUBSCR
        #   66 LOAD_FAST value
        #   68 COMPARE_OP ==
        #   74 POP_JUMP_FORWARD_IF_FALSE to 80
        #   76 LOAD_CONST None
        #   78 RETURN_VALUE
        #   80 LOAD_FAST value
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR device_info
        #   94 LOAD_ATTR led_settings
        #  104 LOAD_FAST index
        #  106 STORE_SUBSCR
        #  110 JUMP_FORWARD to 146
        #  112 PUSH_EXC_INFO
        #  114 LOAD_GLOBAL IndexError
        #  126 CHECK_EXC_MATCH
        #  128 POP_JUMP_FORWARD_IF_FALSE to 138
        #  130 POP_TOP
        #  132 POP_EXCEPT
        #  134 LOAD_CONST None
        #  136 RETURN_VALUE
        #  138 RERAISE
        #  140 COPY
        #  142 POP_EXCEPT
        #  144 RERAISE
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR calc_process
        #  158 LOAD_METHOD send_stream_ctrl_message
        #  180 LOAD_GLOBAL StreamControl
        #  192 LOAD_ATTR SET_LED
        #  202 LOAD_FAST index
        #  204 LOAD_FAST value
        #  206 BUILD_TUPLE
        #  208 PRECALL
        #  212 CALL
        #  222 POP_TOP
        #  224 LOAD_FAST self
        #  226 LOAD_ATTR led_updated
        #  236 LOAD_METHOD emit
        #  258 LOAD_FAST index
        #  260 LOAD_FAST value
        #  262 PRECALL
        #  266 CALL
        #  276 POP_TOP
        #  278 LOAD_CONST None
        #  280 RETURN_VALUE
        #  282 LOAD_CONST None
        #  284 RETURN_VALUE
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        pass

    def set_ctrl_var(self, index, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 328
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 332
        #   30 NOP
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR device_info
        #   44 LOAD_ATTR ctrl_vars
        #   54 LOAD_FAST index
        #   56 BINARY_SUBSCR
        #   66 STORE_FAST old
        #   68 JUMP_FORWARD to 104
        #   70 PUSH_EXC_INFO
        #   72 LOAD_GLOBAL IndexError
        #   84 CHECK_EXC_MATCH
        #   86 POP_JUMP_FORWARD_IF_FALSE to 96
        #   88 POP_TOP
        #   90 POP_EXCEPT
        #   92 LOAD_CONST None
        #   94 RETURN_VALUE
        #   96 RERAISE
        #   98 COPY
        #  100 POP_EXCEPT
        #  102 RERAISE
        #  104 LOAD_FAST old
        #  106 LOAD_CONST 2
        #  108 BINARY_SUBSCR
        #  118 LOAD_FAST value
        #  120 COMPARE_OP ==
        #  126 POP_JUMP_FORWARD_IF_FALSE to 132
        #  128 LOAD_CONST None
        #  130 RETURN_VALUE
        #  132 LOAD_FAST old
        #  134 LOAD_CONST 0
        #  136 BINARY_SUBSCR
        #  146 LOAD_FAST old
        #  148 LOAD_CONST 1
        #  150 BINARY_SUBSCR
        #  160 LOAD_FAST value
        #  162 BUILD_TUPLE
        #  164 LOAD_FAST self
        #  166 LOAD_ATTR device_info
        #  176 LOAD_ATTR ctrl_vars
        #  186 LOAD_FAST index
        #  188 STORE_SUBSCR
        #  192 LOAD_FAST self
        #  194 LOAD_ATTR calc_process
        #  204 LOAD_METHOD send_stream_ctrl_message
        #  226 LOAD_GLOBAL StreamControl
        #  238 LOAD_ATTR SET_CTRL_VAR
        #  248 LOAD_FAST index
        #  250 LOAD_FAST value
        #  252 BUILD_TUPLE
        #  254 PRECALL
        #  258 CALL
        #  268 POP_TOP
        #  270 LOAD_FAST self
        #  272 LOAD_ATTR ctrl_var_updated
        #  282 LOAD_METHOD emit
        #  304 LOAD_FAST index
        #  306 LOAD_FAST value
        #  308 PRECALL
        #  312 CALL
        #  322 POP_TOP
        #  324 LOAD_CONST None
        #  326 RETURN_VALUE
        #  328 LOAD_CONST None
        #  330 RETURN_VALUE
        #  332 LOAD_CONST None
        #  334 RETURN_VALUE
        pass

    def _start_rf_power_handling(self):
        status = self.get_rf_power_status()
        self.rf_power_changed.emit(self, status)
        return status

    def _stop_rf_power_handling(self):
        self.rf_power_changed.emit(self, RFPowerStatus.NOT_SUPPORTED)

    def get_rf_power_status(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR device_info
        #   14 POP_JUMP_FORWARD_IF_FALSE to 40
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 LOAD_ATTR rf_power_status
        #   38 POP_JUMP_FORWARD_IF_NOT_NONE to 64
        #   40 LOAD_GLOBAL RFPowerStatus
        #   52 LOAD_ATTR NOT_SUPPORTED
        #   62 RETURN_VALUE
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR device_info
        #   76 LOAD_ATTR rf_power_status
        #   86 POP_JUMP_FORWARD_IF_FALSE to 112
        #   88 LOAD_GLOBAL RFPowerStatus
        #  100 LOAD_ATTR ENABLED
        #  110 RETURN_VALUE
        #  112 LOAD_GLOBAL RFPowerStatus
        #  124 LOAD_ATTR DISABLED
        #  134 RETURN_VALUE
        pass

    def enable_rf_power(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 284
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 288
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR device_info
        #   42 LOAD_ATTR supports_rf_power
        #   52 POP_JUMP_FORWARD_IF_FALSE to 292
        #   54 LOAD_CONST True
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR device_info
        #   68 STORE_ATTR rf_power_status
        #   78 LOAD_FAST self
        #   80 LOAD_ATTR logger
        #   90 LOAD_METHOD info
        #  112 LOAD_CONST 'Enabling RF power'
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 LOAD_FAST self
        #  132 LOAD_ATTR calc_process
        #  142 LOAD_METHOD send_stream_ctrl_message
        #  164 LOAD_GLOBAL StreamControl
        #  176 LOAD_ATTR SET_RF_POWER
        #  186 LOAD_CONST True
        #  188 BUILD_TUPLE
        #  190 PRECALL
        #  194 CALL
        #  204 POP_TOP
        #  206 LOAD_FAST self
        #  208 LOAD_ATTR rf_power_changed
        #  218 LOAD_METHOD emit
        #  240 LOAD_FAST self
        #  242 LOAD_GLOBAL RFPowerStatus
        #  254 LOAD_ATTR ENABLED
        #  264 PRECALL
        #  268 CALL
        #  278 POP_TOP
        #  280 LOAD_CONST None
        #  282 RETURN_VALUE
        #  284 LOAD_CONST None
        #  286 RETURN_VALUE
        #  288 LOAD_CONST None
        #  290 RETURN_VALUE
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        pass

    def disable_rf_power(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 284
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 288
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR device_info
        #   42 LOAD_ATTR supports_rf_power
        #   52 POP_JUMP_FORWARD_IF_FALSE to 292
        #   54 LOAD_CONST False
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR device_info
        #   68 STORE_ATTR rf_power_status
        #   78 LOAD_FAST self
        #   80 LOAD_ATTR logger
        #   90 LOAD_METHOD info
        #  112 LOAD_CONST 'Disabling RF power'
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 LOAD_FAST self
        #  132 LOAD_ATTR calc_process
        #  142 LOAD_METHOD send_stream_ctrl_message
        #  164 LOAD_GLOBAL StreamControl
        #  176 LOAD_ATTR SET_RF_POWER
        #  186 LOAD_CONST False
        #  188 BUILD_TUPLE
        #  190 PRECALL
        #  194 CALL
        #  204 POP_TOP
        #  206 LOAD_FAST self
        #  208 LOAD_ATTR rf_power_changed
        #  218 LOAD_METHOD emit
        #  240 LOAD_FAST self
        #  242 LOAD_GLOBAL RFPowerStatus
        #  254 LOAD_ATTR DISABLED
        #  264 PRECALL
        #  268 CALL
        #  278 POP_TOP
        #  280 LOAD_CONST None
        #  282 RETURN_VALUE
        #  284 LOAD_CONST None
        #  286 RETURN_VALUE
        #  288 LOAD_CONST None
        #  290 RETURN_VALUE
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        pass

    def load_firmware(self, firmware_data, url):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 30
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR device_info
        #   28 POP_JUMP_FORWARD_IF_TRUE to 34
        #   30 LOAD_CONST None
        #   32 RETURN_VALUE
        #   34 LOAD_GLOBAL NULL + already_programmed
        #   46 LOAD_FAST firmware_data
        #   48 LOAD_FAST self
        #   50 LOAD_ATTR device_info
        #   60 PRECALL
        #   64 CALL
        #   74 POP_JUMP_FORWARD_IF_FALSE to 132
        #   76 LOAD_FAST self
        #   78 LOAD_ATTR logger
        #   88 LOAD_METHOD info
        #  110 LOAD_CONST 'Firmware already present!'
        #  112 PRECALL
        #  116 CALL
        #  126 POP_TOP
        #  128 LOAD_CONST None
        #  130 RETURN_VALUE
        #  132 LOAD_FAST self
        #  134 LOAD_ATTR device_info
        #  144 LOAD_ATTR board_info
        #  154 UNPACK_SEQUENCE
        #  158 STORE_FAST device_name
        #  160 STORE_FAST device_rev
        #  162 LOAD_CONST False
        #  164 STORE_FAST found
        #  166 BUILD_LIST
        #  168 STORE_FAST board_strs
        #  170 LOAD_FAST firmware_data
        #  172 LOAD_CONST 'board'
        #  174 BINARY_SUBSCR
        #  184 GET_ITER
        #  186 FOR_ITER to 282
        #  188 UNPACK_SEQUENCE
        #  192 STORE_FAST rev
        #  194 STORE_FAST name
        #  196 LOAD_FAST rev
        #  198 LOAD_FAST device_rev
        #  200 COMPARE_OP ==
        #  206 POP_JUMP_FORWARD_IF_FALSE to 228
        #  208 LOAD_FAST name
        #  210 LOAD_FAST device_name
        #  212 COMPARE_OP ==
        #  218 POP_JUMP_FORWARD_IF_FALSE to 228
        #  220 LOAD_CONST True
        #  222 STORE_FAST found
        #  224 POP_TOP
        #  226 JUMP_FORWARD to 282
        #  228 LOAD_FAST board_strs
        #  230 LOAD_METHOD append
        #  252 LOAD_FAST name
        #  254 FORMAT_VALUE
        #  256 LOAD_CONST ' rev '
        #  258 LOAD_FAST rev
        #  260 FORMAT_VALUE
        #  262 BUILD_STRING
        #  264 PRECALL
        #  268 CALL
        #  278 POP_TOP
        #  280 JUMP_BACKWARD to 186
        #  282 LOAD_FAST found
        #  284 POP_JUMP_FORWARD_IF_TRUE to 382
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR logger
        #  298 LOAD_METHOD error
        #  320 LOAD_CONST 'Firmware only supports %s!'
        #  322 LOAD_CONST ', '
        #  324 LOAD_METHOD join
        #  346 LOAD_FAST board_strs
        #  348 PRECALL
        #  352 CALL
        #  362 PRECALL
        #  366 CALL
        # ... bytecode truncated ...
        pass

    def start_active_scan(self, serial_number, bootloader):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 76
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR active_scan_data
        #   28 LOAD_METHOD emit
        #   50 LOAD_FAST self
        #   52 LOAD_FAST serial_number
        #   54 LOAD_CONST None
        #   56 PRECALL
        #   60 CALL
        #   70 POP_TOP
        #   72 LOAD_CONST None
        #   74 RETURN_VALUE
        #   76 LOAD_FAST self
        #   78 LOAD_ATTR calc_process
        #   88 LOAD_METHOD send_stream_ctrl_message
        #  110 LOAD_GLOBAL StreamControl
        #  122 LOAD_ATTR DO_ACTIVE_SCAN
        #  132 LOAD_FAST serial_number
        #  134 LOAD_FAST bootloader
        #  136 BUILD_TUPLE
        #  138 PRECALL
        #  142 CALL
        #  152 POP_TOP
        #  154 LOAD_CONST None
        #  156 RETURN_VALUE
        pass

    def set_remote_target(self, serial_number, bootloader, streaming):
        self.remote_target_serial = serial_number
        self.remote_target_bootloader = bootloader
        self.remote_target_streaming = streaming
        if self.remote_target_controller:
            self.remote_target_controller.manual_control_changed.disconnect(self._remote_target_manual_control_changed_cb)
            self.remote_target_controller.release_party(MANUAL_CONTROL)
            self.remote_target_connected.emit(False)
            self.remote_target_controller = None
        self._update_remote_schedule_item()
        self.remote_target_changed.emit(serial_number, bootloader, streaming)

    def clear_remote_target(self):
        self.remote_target_serial = None
        if self.remote_target_controller:
            self.remote_target_controller.manual_control_changed.disconnect(self._remote_target_manual_control_changed_cb)
            self.remote_target_controller.release_party(MANUAL_CONTROL)
            self.remote_target_connected.emit(False)
            self.remote_target_controller = None
        self._update_remote_schedule_item()
        self.remote_target_changed.emit(None, False, False)

    def _remote_connected_cb(self, serial_number_int, serial_number_str, bootloader):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR proxy
        #   14 POP_JUMP_FORWARD_IF_TRUE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_GLOBAL NULL + cast
        #   32 LOAD_GLOBAL DeviceProxy
        #   44 LOAD_FAST self
        #   46 LOAD_ATTR proxy
        #   56 PRECALL
        #   60 CALL
        #   70 LOAD_METHOD create_subproxy
        #   92 LOAD_GLOBAL create_remote
        #  104 LOAD_FAST serial_number_int
        #  106 LOAD_FAST bootloader
        #  108 PRECALL
        #  112 CALL
        #  122 STORE_FAST subproxy
        #  124 LOAD_GLOBAL REMOTE_CONTROL
        #  136 BUILD_SET
        #  138 STORE_FAST parties
        #  140 LOAD_FAST self
        #  142 LOAD_ATTR remote_target_serial
        #  152 LOAD_FAST serial_number_int
        #  154 COMPARE_OP ==
        #  160 POP_JUMP_FORWARD_IF_FALSE to 214
        #  162 LOAD_FAST parties
        #  164 LOAD_METHOD add
        #  186 LOAD_GLOBAL MANUAL_CONTROL
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR dispatcher
        #  226 LOAD_METHOD create_remote
        #  248 LOAD_FAST self
        #  250 LOAD_FAST serial_number_str
        #  252 LOAD_FAST subproxy
        #  254 LOAD_FAST parties
        #  256 PRECALL
        #  260 CALL
        #  270 LOAD_FAST self
        #  272 STORE_ATTR remote_controller
        #  282 LOAD_FAST self
        #  284 LOAD_ATTR remote_connected
        #  294 LOAD_METHOD emit
        #  316 LOAD_CONST True
        #  318 PRECALL
        #  322 CALL
        #  332 POP_TOP
        #  334 LOAD_FAST self
        #  336 LOAD_ATTR remote_target_serial
        #  346 LOAD_FAST serial_number_int
        #  348 COMPARE_OP ==
        #  354 POP_JUMP_FORWARD_IF_FALSE to 602
        #  356 LOAD_FAST self
        #  358 LOAD_ATTR remote_controller
        #  368 LOAD_FAST self
        #  370 STORE_ATTR remote_target_controller
        #  380 LOAD_FAST self
        #  382 LOAD_ATTR remote_target_controller
        #  392 LOAD_ATTR manual_control_changed
        #  402 LOAD_METHOD connect
        #  424 LOAD_FAST self
        #  426 LOAD_ATTR _remote_target_manual_control_changed_cb
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_FAST self
        #  454 LOAD_ATTR remote_target_connected
        #  464 LOAD_METHOD emit
        #  486 LOAD_CONST True
        #  488 PRECALL
        #  492 CALL
        #  502 POP_TOP
        #  504 LOAD_FAST self
        #  506 LOAD_ATTR remote_target_streaming
        #  516 POP_JUMP_FORWARD_IF_TRUE to 598
        #  518 LOAD_FAST self
        # ... bytecode truncated ...
        pass

    def _remote_disconnected_cb(self):
        if self.remote_controller:
            self.remote_controller.release_party(REMOTE_CONTROL)
            self.remote_connected.emit(False)
            self.remote_controller = None
        self.remote_target_connected.emit(False)

    def _remote_target_manual_control_changed_cb(self, manual_control):
        if not manual_control:
            self.clear_remote_target()
            return None

    def run_hardware_tests(self, functions, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + str
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR hardware_run_id
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST run_id
        #   42 LOAD_FAST self
        #   44 COPY
        #   46 LOAD_ATTR hardware_run_id
        #   56 LOAD_CONST 1
        #   58 BINARY_OP +=
        #   62 SWAP
        #   64 STORE_ATTR hardware_run_id
        #   74 LOAD_FAST callback
        #   76 LOAD_FAST self
        #   78 LOAD_ATTR hardware_test_callbacks
        #   88 LOAD_FAST run_id
        #   90 STORE_SUBSCR
        #   94 LOAD_FAST self
        #   96 LOAD_ATTR calc_process
        #  106 POP_JUMP_FORWARD_IF_NONE to 190
        #  108 LOAD_FAST self
        #  110 LOAD_ATTR calc_process
        #  120 LOAD_METHOD send_stream_ctrl_message
        #  142 LOAD_GLOBAL StreamControl
        #  154 LOAD_ATTR DO_HARDWARE_TESTS
        #  164 LOAD_FAST functions
        #  166 LOAD_FAST run_id
        #  168 BUILD_TUPLE
        #  170 PRECALL
        #  174 CALL
        #  184 POP_TOP
        #  186 LOAD_CONST None
        #  188 RETURN_VALUE
        #  190 LOAD_CONST None
        #  192 RETURN_VALUE
        pass

    def register_parties(self, parties):
        was_manually_controlled = MANUAL_CONTROL in self.parties
        self.parties.update(parties)
        if not MANUAL_CONTROL in parties or was_manually_controlled:
            self._update_schedule_items()
            self.manual_control_changed.emit(True)
            return None
        return None

    def release_party(self, party):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST party
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR parties
        #   16 CONTAINS_OP
        #   18 POP_JUMP_FORWARD_IF_FALSE to 24
        #   20 LOAD_CONST None
        #   22 RETURN_VALUE
        #   24 LOAD_GLOBAL MANUAL_CONTROL
        #   36 LOAD_FAST self
        #   38 LOAD_ATTR parties
        #   48 CONTAINS_OP
        #   50 STORE_FAST was_manually_controlled
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR parties
        #   64 LOAD_METHOD discard
        #   86 LOAD_FAST party
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR parties
        #  116 POP_JUMP_FORWARD_IF_FALSE to 248
        #  118 LOAD_FAST party
        #  120 LOAD_GLOBAL MANUAL_CONTROL
        #  132 COMPARE_OP ==
        #  138 POP_JUMP_FORWARD_IF_FALSE to 240
        #  140 LOAD_FAST was_manually_controlled
        #  142 POP_JUMP_FORWARD_IF_FALSE to 244
        #  144 LOAD_FAST self
        #  146 LOAD_METHOD _update_schedule_items
        #  168 PRECALL
        #  172 CALL
        #  182 POP_TOP
        #  184 LOAD_FAST self
        #  186 LOAD_ATTR manual_control_changed
        #  196 LOAD_METHOD emit
        #  218 LOAD_CONST False
        #  220 PRECALL
        #  224 CALL
        #  234 POP_TOP
        #  236 LOAD_CONST None
        #  238 RETURN_VALUE
        #  240 LOAD_CONST None
        #  242 RETURN_VALUE
        #  244 LOAD_CONST None
        #  246 RETURN_VALUE
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR dispatcher
        #  260 LOAD_METHOD stop_controller
        #  282 LOAD_FAST self
        #  284 PRECALL
        #  288 CALL
        #  298 POP_TOP
        #  300 LOAD_CONST None
        #  302 RETURN_VALUE
        pass

    def clear_manual_control(self):
        self.release_party(MANUAL_CONTROL)

    def get_manual_control(self):
        return MANUAL_CONTROL in self.parties

    def _set_schedule_count(self, schedule_count):
        if schedule_count != self.schedule_count:
            self.schedule_count = schedule_count
            self.schedule_count_changed.emit(schedule_count)
            return None

    def start_connectivity(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 174
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR channel_info
        #   28 POP_JUMP_FORWARD_IF_FALSE to 178
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR dispatcher
        #   42 LOAD_ATTR connectivity_manager
        #   52 LOAD_METHOD create_device_pipe
        #   74 LOAD_FAST self
        #   76 LOAD_ATTR serial_number
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR channel_info
        #   98 PRECALL
        #  102 CALL
        #  112 STORE_FAST pipe
        #  114 LOAD_FAST pipe
        #  116 POP_JUMP_FORWARD_IF_NONE to 182
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR calc_process
        #  130 LOAD_METHOD set_connectivity_pipe
        #  152 LOAD_FAST pipe
        #  154 PRECALL
        #  158 CALL
        #  168 POP_TOP
        #  170 LOAD_CONST None
        #  172 RETURN_VALUE
        #  174 LOAD_CONST None
        #  176 RETURN_VALUE
        #  178 LOAD_CONST None
        #  180 RETURN_VALUE
        #  182 LOAD_CONST None
        #  184 RETURN_VALUE
        pass

    def start_rf_test(self, params):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR calc_process
        #   14 POP_JUMP_FORWARD_IF_NONE to 96
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR calc_process
        #   28 LOAD_METHOD send_stream_ctrl_message
        #   50 LOAD_GLOBAL StreamControl
        #   62 LOAD_ATTR DO_RF_TEST
        #   72 LOAD_FAST params
        #   74 BUILD_TUPLE
        #   76 PRECALL
        #   80 CALL
        #   90 POP_TOP
        #   92 LOAD_CONST None
        #   94 RETURN_VALUE
        #   96 LOAD_GLOBAL NULL + RuntimeError
        #  108 LOAD_CONST 'Not connected'
        #  110 PRECALL
        #  114 CALL
        #  124 RAISE_VARARGS
        pass

    def schedule_items_deleted(self, ids):
        if self.calc_process:
            self.calc_process.send_stream_ctrl_message((StreamControl.DELETE_SCHEDULE_IDS, ids))
            return None

    def schedule_item_updated(self, schedule_item):
        if self.calc_process:
            self.calc_process.send_stream_ctrl_message((StreamControl.UPDATE_SCHEDULE_ITEM, schedule_item))
            return None
