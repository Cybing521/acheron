# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

import functools
import logging
import os
import re
from typing import cast, Optional, Union
from PySide6 import QtCore
from hyperborea.preferences import read_bool_setting, read_int_setting, write_bool_setting
from ..calc_process.types import LimitType
logger = logging.getLogger(__name__)
SomePreferences = Union[('Preferences', 'DevicePreferences')]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

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

    def __init__(self, setting_name, default):
        self.setting_name = setting_name
        self.default = default

    def __get__(self, obj, objtype):
        return read_bool_setting(obj.settings, self.setting_name, self.default)

    def __set__(self, obj, value):
        write_bool_setting(obj.settings, self.setting_name, value)

class IntProperty(property):

    def __init__(self, setting_name, default):
        self.setting_name = setting_name
        self.default = default

    def __get__(self, obj, objtype):
        return read_int_setting(obj.settings, self.setting_name, self.default)

    def __set__(self, obj, val):
        obj.settings.setValue(self.setting_name, val)

class StringProperty(property):

    def __init__(self, setting_name):
        self.setting_name = setting_name

    def __get__(self, obj, objtype):
        s = obj.settings.value(self.setting_name)
        if s is None:
            return ''
        return str(s).strip()

    def __set__(self, obj, val):
        obj.settings.setValue(self.setting_name, val.strip())

class Preferences:

    def __init__(self):
        self.settings = QtCore.QSettings()

    def get_base_dir(self):
        base_dir = self._base_dir
        if not base_dir:
            documents_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            base_dir = os.path.join(documents_path, app_name + ' Data')
        return os.path.normpath(base_dir)

    def set_base_dir(self, value):
        self._base_dir = value

    def get_diskcache_dir(self):
        diskcache_dir = self._diskcache_dir
        if not diskcache_dir:
            cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            diskcache_dir = os.path.join(cache_path, app_name + ' Cache')
        return os.path.normpath(diskcache_dir)

    def set_diskcache_dir(self, value):
        self._diskcache_dir = value

    def get_firmware_dir(self):
        firmware_dir = self._firmware_dir
        if not firmware_dir:
            cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
            app_name = QtCore.QCoreApplication.applicationName()
            firmware_dir = os.path.join(cache_path, app_name + ' Firmware')
        return os.path.normpath(firmware_dir)

    def set_firmware_dir(self, value):
        self._firmware_dir = value

    def initial_serials(self):
        value = self.settings.value('InitialSerials')
        if not value:
            return []
        if isinstance(value, str):
            return [item.strip() for item in value.split(',') if item.strip()]
        if isinstance(value, (list, tuple)):
            return [str(item).strip() for item in value if str(item).strip()]
        return [str(value).strip()]

    dark_mode = BoolProperty('DarkMode', True)
    show_supplies = BoolProperty('ShowSupplies', False)
    _base_dir = StringProperty('BasePath')
    base_dir = property(get_base_dir, set_base_dir)
    _diskcache_dir = StringProperty('DiskCachePath')
    diskcache_dir = property(get_diskcache_dir, set_diskcache_dir)
    _firmware_dir = StringProperty('FirmwareCachePath')
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

class DevicePreferences:

    response_time = IntProperty('ResponseTime', 50)

    buffer_time = IntProperty('BufferTime', 500)

    stream_timeout = IntProperty('StreamTimeout', 1000)

    modbus_enable = BoolProperty('ModbusEnable', False)

    modbus_register_offset = IntProperty('ModbusRegisterOffset', 0)

    def __init__(self, serial_number):
        self.settings = QtCore.QSettings()
        self.settings.beginGroup(serial_number)

    def _get_prefix(cls, limit_type, channel_id, subchannel_index):
        key = cls._alert_key_types[limit_type]
        return f'''AlertCh{channel_id}_{subchannel_index}/{key}'''

    def _key_to_limit_type(cls, key):
        for k, v in cls._alert_key_types.items():
            if key == v:
                
                return None, k
            raise ValueError(f'''No corresponding LimitType for {key}''')

    def _get_alert_value(self, key):
        s = self.settings.value(key)

    def get_alert_limits(self, channel_id, subchannel_index):
        limits = { }

    def set_alert_limits(self, channel_id, subchannel_index, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR _alert_key_types
        #   14 LOAD_METHOD keys
        #   36 PRECALL
        #   40 CALL
        #   50 GET_ITER
        #   52 FOR_ITER to 312
        #   54 STORE_FAST limit_type
        #   56 LOAD_FAST self
        #   58 LOAD_METHOD _get_prefix
        #   80 LOAD_FAST limit_type
        #   82 LOAD_FAST channel_id
        #   84 LOAD_FAST subchannel_index
        #   86 PRECALL
        #   90 CALL
        #  100 STORE_FAST prefix
        #  102 LOAD_FAST values
        #  104 LOAD_METHOD get
        #  126 LOAD_FAST limit_type
        #  128 PRECALL
        #  132 CALL
        #  142 STORE_FAST value
        #  144 LOAD_FAST value
        #  146 POP_JUMP_FORWARD_IF_NONE to 260
        #  148 LOAD_GLOBAL NULL + write_bool_setting
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR settings
        #  172 LOAD_FAST prefix
        #  174 LOAD_CONST 'Enabled'
        #  176 BINARY_OP +
        #  180 LOAD_CONST True
        #  182 PRECALL
        #  186 CALL
        #  196 POP_TOP
        #  198 LOAD_FAST self
        #  200 LOAD_ATTR settings
        #  210 LOAD_METHOD setValue
        #  232 LOAD_FAST prefix
        #  234 LOAD_CONST 'Value'
        #  236 BINARY_OP +
        #  240 LOAD_FAST value
        #  242 PRECALL
        #  246 CALL
        #  256 POP_TOP
        #  258 JUMP_BACKWARD to 52
        #  260 LOAD_GLOBAL NULL + write_bool_setting
        #  272 LOAD_FAST self
        #  274 LOAD_ATTR settings
        #  284 LOAD_FAST prefix
        #  286 LOAD_CONST 'Enabled'
        #  288 BINARY_OP +
        #  292 LOAD_CONST False
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 JUMP_BACKWARD to 52
        #  312 LOAD_CONST None
        #  314 RETURN_VALUE
        pass

    def get_all_alert_limits(self):
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

    def _validate_port(port):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST port
        #    4 POP_JUMP_FORWARD_IF_NONE to 42
        #    6 LOAD_CONST 0
        #    8 LOAD_FAST port
        #   10 SWAP
        #   12 COPY
        #   14 COMPARE_OP <=
        #   20 POP_JUMP_FORWARD_IF_FALSE to 34
        #   22 LOAD_CONST 65535
        #   24 COMPARE_OP <=
        #   30 POP_JUMP_FORWARD_IF_FALSE to 42
        #   32 JUMP_FORWARD to 38
        #   34 POP_TOP
        #   36 JUMP_FORWARD to 42
        #   38 LOAD_FAST port
        #   40 RETURN_VALUE
        #   42 LOAD_CONST None
        #   44 RETURN_VALUE
        pass

    def get_channel_port(self, channel_id, subchannel_index):
        setting_name = f'''Channel{channel_id}_{subchannel_index}_Port'''
        port = read_int_setting(self.settings, setting_name, None)
        return self._validate_port(port)

    def get_all_channel_ports(self):
        pattern = re.compile('Channel([0-9]+)_([0-9]+)_Port')
        channel_ports = { }

def get_device_preferences(serial_number):
    return DevicePreferences(serial_number)
