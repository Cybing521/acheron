# Source Generated with Decompyle++
# File: tmp2ca81sop.marshal (Python 3.11)

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
from device_logging import DeviceLoggerAdapter
from device_process.proxy import DeviceOperation, DeviceProxy, Proxy, SimpleDeviceOperation
from main_schedule import DeviceSchedule
from preferences import get_device_preferences, Preferences
from calc_process.types import CalcSettings, ChannelInformation, Trigger
from calc_process.runnner import CalcProcess
from device_process.bootloader import already_programmed
from device_process.remote_funcs import explode
from device_process.schedule import OutputConfig, ScheduleItem
from device_process.stream_controller import create_remote, HardwareTestFunction, RFTestParams, start_stream_controller, stop_stream_controller, StreamControl, StreamSettings, StreamStatus
if TYPE_CHECKING:
    from dispatcher import Dispatcher
logger = logging.getLogger(__name__)
DeviceControllerState = <NODE:12>()
RFPowerStatus = <NODE:12>()
MANUAL_CONTROL = 'manual'
REMOTE_CONTROL = 'remote'

class HardwareTestCallback(Protocol):
    
    def hardware_test_function_finished(self = None, test_id = None, data = None):
        pass

    
    def hardware_test_run_finished(self = None):
        pass



class DeviceController(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

