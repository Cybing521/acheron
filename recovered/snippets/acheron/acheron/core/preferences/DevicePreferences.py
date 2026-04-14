# Source Generated with Decompyle++
# File: tmp3zctdg76.marshal (Python 3.11)


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

