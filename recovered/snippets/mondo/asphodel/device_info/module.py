# Source Generated with Decompyle++
# File: tmpukq2cynu.marshal (Python 3.11)

from collections.abc import Generator
from dataclasses import dataclass, fields
import inspect
import logging
import math
from typing import Any, Callable, cast, Optional, ParamSpec, TypeVar, TYPE_CHECKING, Union
import asphodel
if TYPE_CHECKING:
    from diskcache import Cache
logger = logging.getLogger(__name__)
ProgressCallback = Callable[([
    int,
    int,
    str], None)]
LoggerType = Union[(logging.Logger, logging.LoggerAdapter[logging.Logger])]
P = ParamSpec('P')
T = TypeVar('T')
GetterFirst = tuple[(int, int, dict[(str, Any)])]
GetterFirstGenerator = Generator[(GetterFirst, None, None)]
GetterSecond = dict[(str, Any)]
GetterSecondGenerator = Generator[(GetterSecond, None, None)]
GetterGenerator = Generator[(Union[(GetterFirst, GetterSecond)], None, None)]
Getter = Callable[([
    asphodel.AsphodelNativeDevice,
    dict[(str, Any)],
    'Incrementer'], GetterGenerator)]
ActiveScanInfo = <NODE:12>()
DeviceInfo = <NODE:12>()

def try_optional(func = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


class Incrementer:
    
    def __init__(self = None, progress_callback = None, logger = None):
        self.progress_callback = progress_callback
        self.logger = logger
        self.finished = None
        self.total = None

    
    def increment(self = None, difference = None, section_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_values(self = None, finished = None, total = None):
        pass
    # WARNING: Decompyle incomplete



def single_call(key_name = None, func_name = None, optional = None):
    pass
# WARNING: Decompyle incomplete


def array_call(key, device_info, incrementer, count_fn = None, element_fn = None, count_key = None, element_cost = (None, 1, True), skippable = ('key', str, 'device_info', dict[(str, Any)], 'incrementer', Incrementer, 'count_fn', Optional[Callable[([], int)]], 'element_fn', Callable[([
    int], Any)], 'count_key', Optional[str], 'element_cost', int, 'skippable', bool, 'return', GetterGenerator)):
    pass
# WARNING: Decompyle incomplete


def get_custom_enums(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_setting_categories(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_streams(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_channels(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_channel_calibrations(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_supplies(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_supply_results(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_ctrl_vars(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_ctrl_var_settings(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_settings(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_nvm(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_nvm_active_scan(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_led_settings(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_rgb_settings(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_rf_power_status(device = None, _device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_rf_power_ctrl_vars(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_radio_ctrl_vars(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_radio_scan_power(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_radio_default_serial(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def get_device_mode(device = None, device_info = None, incrementer = None):
    pass
# WARNING: Decompyle incomplete


def hash_is_valid(h = None):
    if not h:
        return False
    lowercase_string = None.lower()
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(lowercase_string()):
        return False
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(lowercase_string()):
        return False
    return all


def get_device_info_dict(device, device_logger, allow_reconnect, diskcache = None, progress_callback = None, setting_getters = None, nvm_getters = ('device', asphodel.AsphodelNativeDevice, 'device_logger', LoggerType, 'allow_reconnect', bool, 'diskcache', 'Optional[Cache]', 'progress_callback', Optional[ProgressCallback], 'setting_getters', list[Getter], 'nvm_getters', list[Getter], 'return', dict[(str, Any)])):
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
# WARNING: Decompyle incomplete

default_setting_getters: list[Getter] = [
    single_call('protocol_version', 'get_protocol_version_string'),
    single_call('board_info', 'get_board_info'),
    single_call('chip_family', 'get_chip_family'),
    single_call('chip_model', 'get_chip_model'),
    single_call('chip_id', 'get_chip_id'),
    single_call('bootloader_info', 'get_bootloader_info'),
    single_call('commit_id', 'get_commit_id', optional = True),
    single_call('repo_branch', 'get_repo_branch', optional = True),
    single_call('repo_name', 'get_repo_name', optional = True),
    get_custom_enums,
    get_setting_categories,
    get_streams,
    get_channels,
    get_channel_calibrations,
    get_supplies,
    get_ctrl_vars,
    get_settings,
    get_rf_power_ctrl_vars,
    get_radio_ctrl_vars,
    get_radio_scan_power,
    get_radio_default_serial,
    get_led_settings,
    get_rgb_settings,
    get_supply_results,
    get_ctrl_var_settings,
    get_rf_power_status,
    get_device_mode]
active_scan_setting_getters: list[Getter] = [
    single_call('board_info', 'get_board_info'),
    single_call('bootloader_info', 'get_bootloader_info')]

def get_active_scan_info(remote = None, device_logger = None, diskcache = None):
    device_info_dict = get_device_info_dict(remote, device_logger, False, diskcache, None, active_scan_setting_getters, [
        get_nvm_active_scan])
    if 'nvm' not in device_info_dict:
        device_info_dict['nvm'] = None
    return ActiveScanInfo.from_dict(device_info_dict)


def get_device_info(device = None, allow_reconnect = None, device_logger = None, diskcache = (None, None), progress_callback = ('device', asphodel.AsphodelNativeDevice, 'allow_reconnect', bool, 'device_logger', LoggerType, 'diskcache', 'Optional[Cache]', 'progress_callback', Optional[ProgressCallback], 'return', DeviceInfo)):
    device_info_dict = get_device_info_dict(device, device_logger, allow_reconnect, diskcache, progress_callback, default_setting_getters, [
        get_nvm])
# WARNING: Decompyle incomplete


def get_remote_board_info(serial_number = None, diskcache = None):
    return diskcache.get(serial_number, default = None)

