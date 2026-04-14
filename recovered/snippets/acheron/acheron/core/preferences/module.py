# Source Generated with Decompyle++
# File: tmpzx1pgis2.marshal (Python 3.11)

import functools
import logging
import os
import re
from typing import cast, Optional, Union
from PySide6 import QtCore
from hyperborea.preferences import read_bool_setting, read_int_setting, write_bool_setting
from calc_process.types import LimitType
logger = logging.getLogger(__name__)
SomePreferences = Union[('Preferences', 'DevicePreferences')]

def create_empty_settings():
    settings = QtCore.QSettings()
    setting_keys = [
        'ArchiveIntervalMinutes',
        'DiskCachePath',
        'FirmwareCachePath',
        'FirmwareRootDir',
        'GraphTimerInterval',
        'InitialConnectTCP',
        'InitialConnectUSB',
        'InitialSerials',
        'RescanConnectTCP',
        'RescanConnectUSB',
        'RFTest',
        'UpdateTimerInterval']
    for setting_key in setting_keys:
        value = settings.value(setting_key)
        if not value:
            settings.setValue(setting_key, '')
        return None


class BoolProperty(property):
    
    def __init__(self = None, setting_name = None, default = None):
        self.setting_name = setting_name
        self.default = default

    
    def __get__(self = None, obj = None, objtype = None):
        return read_bool_setting(obj.settings, self.setting_name, self.default)

    
    def __set__(self = None, obj = None, value = None):
        write_bool_setting(obj.settings, self.setting_name, value)



class IntProperty(property):
    
    def __init__(self = None, setting_name = None, default = None):
        self.setting_name = setting_name
        self.default = default

    
    def __get__(self = None, obj = None, objtype = None):
        return read_int_setting(obj.settings, self.setting_name, self.default)

    
    def __set__(self = None, obj = None, val = None):
        obj.settings.setValue(self.setting_name, val)



class StringProperty(property):
    
    def __init__(self = None, setting_name = None):
        self.setting_name = setting_name

    
    def __get__(self = None, obj = None, objtype = None):
        s = obj.settings.value(self.setting_name)
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, obj = None, val = None):
        obj.settings.setValue(self.setting_name, val.strip())



class Preferences:
    
    def __init__(self = None):
        self.settings = QtCore.QSettings()

    dark_mode = BoolProperty('DarkMode', True)
    show_supplies = BoolProperty('ShowSupplies', False)
    _base_dir = StringProperty('BasePath')
    
    def get_base_dir(self = None):
        base_dir = self._base_dir
        if not base_dir:
            documents_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            base_dir = os.path.join(documents_path, app_name + ' Data')
        return os.path.normpath(base_dir)

    
    def set_base_dir(self = None, value = None):
        self._base_dir = value

    base_dir = property(get_base_dir, set_base_dir)
    _diskcache_dir = StringProperty('DiskCachePath')
    
    def get_diskcache_dir(self = None):
        diskcache_dir = self._diskcache_dir
        if not diskcache_dir:
            cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            diskcache_dir = os.path.join(cache_path, app_name + ' Cache')
        return os.path.normpath(diskcache_dir)

    
    def set_diskcache_dir(self = None, value = None):
        self._diskcache_dir = value

    diskcache_dir = property(get_diskcache_dir, set_diskcache_dir)
    _firmware_dir = StringProperty('FirmwareCachePath')
    
    def get_firmware_dir(self = None):
        firmware_dir = self._firmware_dir
        if not firmware_dir:
            cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            firmware_dir = os.path.join(cache_path, app_name + ' Firmware')
        return os.path.normpath(firmware_dir)

    
    def set_firmware_dir(self = None, value = None):
        self._firmware_dir = value

    firmware_dir = property(get_firmware_dir, set_firmware_dir)
    firmware_root_dir = StringProperty('FirmwareRootDir')
    auto_rgb = BoolProperty('AutoRGB', True)
    downsample = BoolProperty('Downsample', True)
    plot_mean = BoolProperty('PlotMean', False)
    compression_level = IntProperty('CompressionLevel', 6)
    archive_interval = IntProperty('ArchiveIntervalMinutes', 10)
    modbus_enable = BoolProperty('ModbusEnable', False)
    modbus_port = IntProperty('ModbusPort', 502)
    upload_enabled = BoolProperty('Upload/Enabled', False)
    s3_bucket = StringProperty('Upload/S3Bucket')
    aws_region = StringProperty('Upload/AWSRegion')
    upload_directory = StringProperty('Upload/Directory')
    access_key_id = StringProperty('Upload/AccessKeyID')
    secret_access_key = StringProperty('Upload/SecretAccessKey')
    delete_original = BoolProperty('Upload/DeleteOriginal', False)
    alert_email_enabled = BoolProperty('AlertEmail/Enabled', False)
    alert_from_address = StringProperty('AlertEmail/FromAddress')
    alert_to_address = StringProperty('AlertEmail/ToAddress')
    alert_smtp_host = StringProperty('AlertEmail/SMTPHost')
    alert_smtp_port = IntProperty('AlertEmail/SMTPPort', 587)
    alert_security = StringProperty('AlertEmail/Security')
    alert_use_auth = BoolProperty('AlertEmail/UseAuth', True)
    alert_smtp_user = StringProperty('AlertEmail/SMTPUser')
    alert_smtp_password = StringProperty('AlertEmail/SMTPPassword')
    update_timer_interval = IntProperty('UpdateTimerInterval', 100)
    graph_timer_interval = IntProperty('GraphTimerInterval', 100)
    show_rf_test = BoolProperty('RFTest', False)
    show_supplies = BoolProperty('ShowSupplies', False)
    collapsed = BoolProperty('Collapsed', False)
    closeable_tabs = BoolProperty('ClosableTabs', False)
    automatic_rescan = BoolProperty('DialogAutomaticRescan', True)
    background_active_scan = BoolProperty('BackgroundActiveScan', False)
    initial_connect_usb = BoolProperty('InitialConnectUSB', True)
    initial_connect_tcp = BoolProperty('InitialConnectTCP', False)
    rescan_connect_usb = BoolProperty('RescanConnectUSB', False)
    rescan_connect_tcp = BoolProperty('RescanConnectTCP', False)
    disable_streaming = BoolProperty('DisableStreaming', False)
    disable_archiving = BoolProperty('DisableArchiving', False)
    socket_buffer_size = IntProperty('SocketBufferSize', 0)
    event_upload_enabled = BoolProperty('EventUploadEnabled', True)
    initial_serials = (lambda self = None: v = self.settings.value('InitialSerials')# WARNING: Decompyle incomplete
)()


class DevicePreferences:
    
    def __init__(self = None, serial_number = None):
        self.settings = QtCore.QSettings()
        self.settings.beginGroup(serial_number)

    response_time = IntProperty('ResponseTime', 50)
    buffer_time = IntProperty('BufferTime', 500)
    stream_timeout = IntProperty('StreamTimeout', 1000)
    modbus_enable = BoolProperty('ModbusEnable', False)
    modbus_register_offset = IntProperty('ModbusRegisterOffset', 0)
    _alert_key_types = {
        LimitType.STD_LOW_LIMIT: 'StdLow',
        LimitType.STD_HIGH_LIMIT: 'StdHigh',
        LimitType.MEAN_LOW_LIMIT: 'MeanLow',
        LimitType.MEAN_HIGH_LIMIT: 'MeanHigh' }
    _get_prefix = (lambda cls = None, limit_type = None, channel_id = classmethod, subchannel_index = ('limit_type', LimitType, 'channel_id', int, 'subchannel_index', int, 'return', str): key = cls._alert_key_types[limit_type]f'''AlertCh{channel_id}_{subchannel_index}/{key}''')()
    _key_to_limit_type = (lambda cls = None, key = None: for k, v in cls._alert_key_types.items():
if key == v:
None, kraise ValueError(f'''No corresponding LimitType for {key}'''))()
    
    def _get_alert_value(self = None, key = None):
        s = self.settings.value(key)
    # WARNING: Decompyle incomplete

    
    def get_alert_limits(self = None, channel_id = None, subchannel_index = None):
        limits = { }
    # WARNING: Decompyle incomplete

    
    def set_alert_limits(self = None, channel_id = None, subchannel_index = None, values = ('channel_id', int, 'subchannel_index', int, 'values', dict[(LimitType, float)], 'return', None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_all_alert_limits(self = None):
        keys = '|'.join(self._alert_key_types.values())
        pattern = re.compile('AlertCh(\\d+)_(\\d+)/(' + keys + ')Enabled')
        parsed_values = []
        for setting_name in self.settings.allKeys():
            match = pattern.match(setting_name)
            if not match:
                continue
            enabled = read_bool_setting(self.settings, setting_name, False)
            if not enabled:
                continue
            (channel_id, subchannel_index, key) = match.groups()
            v_key = f'''AlertCh{channel_id}_{subchannel_index}/{key}Value'''
            value = self._get_alert_value(v_key)
            if not value:
                continue
            parsed_values.append((self._key_to_limit_type(key), int(channel_id), int(subchannel_index), value))
            return parsed_values

    _validate_port = (lambda port = None: pass# WARNING: Decompyle incomplete
)()
    
    def get_channel_port(self = None, channel_id = None, subchannel_index = None):
        setting_name = f'''Channel{channel_id}_{subchannel_index}_Port'''
        port = read_int_setting(self.settings, setting_name, None)
        return self._validate_port(port)

    
    def get_all_channel_ports(self = None):
        pattern = re.compile('Channel([0-9]+)_([0-9]+)_Port')
        channel_ports = { }
    # WARNING: Decompyle incomplete


get_device_preferences = (lambda serial_number = None: DevicePreferences(serial_number))()
