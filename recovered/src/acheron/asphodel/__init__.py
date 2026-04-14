# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import ast
import binascii
from collections import namedtuple
from ctypes import addressof, byref, c_char_p, c_double, c_float, c_int, c_int8, c_int16, c_int32, c_uint, c_uint8, c_uint16, c_uint32, c_uint64, c_size_t, c_void_p, cast, cdll, CFUNCTYPE, create_string_buffer, POINTER, pointer, Structure, Union
from ctypes.util import find_library
import functools
import os
import string
import sys
import time
import threading
from typing import Optional
import weakref

try:
    from version import version as __version__
except ImportError:
    __version__ = 'UNKNOWN'

ASPHODEL_PROTOCOL_TYPE_BASIC = 0
ASPHODEL_PROTOCOL_TYPE_RF_POWER = 1
ASPHODEL_PROTOCOL_TYPE_RADIO = 2
ASPHODEL_PROTOCOL_TYPE_REMOTE = 4
ASPHODEL_PROTOCOL_TYPE_BOOTLOADER = 8
GPIO_PIN_MODE_HI_Z = 0
GPIO_PIN_MODE_PULL_DOWN = 1
GPIO_PIN_MODE_PULL_UP = 2
GPIO_PIN_MODE_LOW = 3
GPIO_PIN_MODE_HIGH = 4
SPI_CS_MODE_LOW = 0
SPI_CS_MODE_HIGH = 1
SPI_CS_MODE_AUTO_TRANSFER = 2
SPI_CS_MODE_AUTO_BYTE = 3
ASPHODEL_SUPPLY_LOW_BATTERY = 1
ASPHODEL_SUPPLY_TOO_LOW = 2
ASPHODEL_SUPPLY_TOO_HIGH = 4
ASPHODEL_TCP_FILTER_DEFAULT = 0
ASPHODEL_TCP_FILTER_PREFER_IPV6 = 0
ASPHODEL_TCP_FILTER_PREFER_IPV4 = 1
ASPHODEL_TCP_FILTER_ONLY_IPV6 = 2
ASPHODEL_TCP_FILTER_ONLY_IPV4 = 3
ASPHODEL_TCP_FILTER_RETURN_ALL = 4

class AsphodelError(IOError):
    pass

StreamFormat = namedtuple('StreamFormat', [
    'filler_bits',
    'counter_bits',
    'rate',
    'rate_error',
    'warm_up_delay'])
ChannelInfo = namedtuple('ChannelInfo', [
    'channel_type',
    'unit_type',
    'filler_bits',
    'data_bits',
    'samples',
    'bits_per_sample',
    'minimum',
    'maximum',
    'resolution',
    'chunk_count'])
ChannelCalibration = namedtuple('ChannelCalibration', [
    'base_setting_index',
    'resolution_setting_index',
    'scale',
    'offset',
    'minimum',
    'maximum'])
SupplyInfo = namedtuple('SupplyInfo', [
    'unit_type',
    'is_battery',
    'nominal',
    'scale',
    'offset'])
CtrlVarInfo = namedtuple('CtrlVarInfo', [
    'unit_type',
    'minimum',
    'maximum',
    'scale',
    'offset'])
ExtraScanResult = namedtuple('ExtraScanResult', [
    'serial_number',
    'asphodel_type',
    'device_mode'])
GPIOPortInfo = namedtuple('GPIOPortInfo', [
    'input_pins',
    'output_pins',
    'floating_pins',
    'loaded_pins',
    'overridden_pins'])
BridgeValues = namedtuple('BridgeValues', [
    'pos_sense',
    'neg_sense',
    'nominal',
    'minimum',
    'maximum'])
SelfTestLimits = namedtuple('SelfTestLimits', [
    'x_min',
    'x_max',
    'y_min',
    'y_max',
    'z_min',
    'z_max'])
StreamRateInfo = namedtuple('StreamRateInfo', [
    'available',
    'channel_index',
    'invert',
    'scale',
    'offset'])
TCPAdvInfo = namedtuple('TCPAdvInfo', [
    'tcp_version',
    'connected',
    'max_incoming_param_length',
    'max_outgoing_param_length',
    'stream_packet_length',
    'protocol_type',
    'serial_number',
    'board_rev',
    'board_type',
    'build_info',
    'build_date',
    'user_tag1',
    'user_tag2',
    'remote_max_incoming_param_length',
    'remote_max_outgoing_param_length',
    'remote_stream_packet_length'])

class AsphodelStreamInfo(Structure):
    _fields_ = [
        ('channel_index_list', POINTER(c_uint8)),
        ('channel_count', c_uint8),
        ('filler_bits', c_uint8),
        ('counter_bits', c_uint8),
        ('rate', c_float),
        ('rate_error', c_float),
        ('warm_up_delay', c_float)]
    __reduce__ = object.__reduce__
    
    def __del__(self):
        
        try:
            self._free_func(self)
            return None
        except AttributeError:
            return None


    
    def __repr__(self):
        channel_index_list = self.channel_index_list[:self.channel_count]
        items = [
            ('channel_index_list', channel_index_list),
            ('channel_count', self.channel_count),
            ('filler_bits', self.filler_bits),
            ('counter_bits', self.counter_bits),
            ('rate', self.rate),
            ('rate_error', self.rate_error),
            ('warm_up_delay', self.warm_up_delay)]
        contents = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        return '<AsphodelStreamInfo {' + contents + '}>'

    
    def __getstate__(self):
        return {
            '_channel_array': self.channel_index_list[:self.channel_count],
            'channel_count': self.channel_count,
            'filler_bits': self.filler_bits,
            'counter_bits': self.counter_bits,
            'rate': self.rate,
            'rate_error': self.rate_error,
            'warm_up_delay': self.warm_up_delay }

    
    def __setstate__(self, state):
        pass
    # WARNING: Decompyle incomplete

    
    def to_json_obj(self):
        return self.__getstate__()

    from_json_obj = (lambda cls, obj: instance = cls.__new__(cls)instance.__setstate__(obj)instance)()


class AsphodelChannelInfo(Structure):
    pass
# WARNING: Decompyle incomplete


class SettingStructure(Structure):
    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete



class AsphodelByteSetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('nvm_word_byte', c_uint8)]


class AsphodelByteArraySetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('maximum_length', c_uint8),
        ('length_nvm_word', c_uint16),
        ('length_nvm_word_byte', c_uint8)]


class AsphodelStringSetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('maximum_length', c_uint8)]


class AsphodelInt32Setting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('minimum', c_int32),
        ('maximum', c_int32)]


class AsphodelInt32ScaledSetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('minimum', c_int32),
        ('maximum', c_int32),
        ('unit_type', c_uint8),
        ('scale', c_float),
        ('offset', c_float)]


class AsphodelFloatSetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('minimum', c_float),
        ('maximum', c_float),
        ('unit_type', c_uint8),
        ('scale', c_float),
        ('offset', c_float)]


class AsphodelFloatArraySetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('minimum', c_float),
        ('maximum', c_float),
        ('unit_type', c_uint8),
        ('scale', c_float),
        ('offset', c_float),
        ('maximum_length', c_uint8),
        ('length_nvm_word', c_uint16),
        ('length_nvm_word_byte', c_uint8)]


class AsphodelCustomEnumSetting(SettingStructure):
    _fields_ = [
        ('nvm_word', c_uint16),
        ('nvm_word_byte', c_uint8),
        ('custom_enum_index', c_uint8)]


class AsphodelSettingUnion(Union):
    _fields_ = [
        ('byte_setting', AsphodelByteSetting),
        ('byte_array_setting', AsphodelByteArraySetting),
        ('string_setting', AsphodelStringSetting),
        ('int32_setting', AsphodelInt32Setting),
        ('int32_scaled_setting', AsphodelInt32ScaledSetting),
        ('float_setting', AsphodelFloatSetting),
        ('float_array_setting', AsphodelFloatArraySetting),
        ('custom_enum_setting', AsphodelCustomEnumSetting)]


class AsphodelSettingInfo(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('name_length', c_uint8),
        ('default_bytes', POINTER(c_uint8)),
        ('default_bytes_length', c_uint8),
        ('setting_type', c_uint8),
        ('u', AsphodelSettingUnion)]
    __reduce__ = object.__reduce__
    
    def __repr__(self):
        if self.setting_type < len(setting_type_names):
            s = setting_type_names[self.setting_type]
            setting_type_str = '{} ({})'.format(self.setting_type, s)
            if s == 'SETTING_TYPE_BYTE' and s == 'SETTING_TYPE_BOOLEAN' and s == 'SETTING_TYPE_UNIT_TYPE' or s == 'SETTING_TYPE_CHANNEL_TYPE':
                u_str = repr(self.u.byte_setting)
            elif s == 'SETTING_TYPE_BYTE_ARRAY':
                u_str = repr(self.u.byte_array_setting)
            elif s == 'SETTING_TYPE_STRING':
                u_str = repr(self.u.string_setting)
            elif s == 'SETTING_TYPE_INT32':
                u_str = repr(self.u.int32_setting)
            elif s == 'SETTING_TYPE_INT32_SCALED':
                u_str = repr(self.u.int32_scaled_setting)
            elif s == 'SETTING_TYPE_FLOAT':
                u_str = repr(self.u.float_setting)
            elif s == 'SETTING_TYPE_FLOAT_ARRAY':
                u_str = repr(self.u.float_array_setting)
            elif s == 'SETTING_TYPE_CUSTOM_ENUM':
                u_str = repr(self.u.custom_enum_setting)
            else:
                u_str = 'UNKNOWN TYPE'
        else:
            setting_type_str = '{}'.format(self.setting_type)
            u_str = 'UNKNOWN TYPE'
        default_bytes = self.default_bytes[:self.default_bytes_length]
        default_bytes_str = ','.join(map('0x{:02x}'.format, default_bytes))
        items = [
            ('name', self.name),
            ('name_length', self.name_length),
            ('default_bytes', default_bytes_str),
            ('default_bytes_length', self.default_bytes_length),
            ('setting_type', setting_type_str),
            ('u', u_str)]
        contents = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        return '<AsphodelSettingInfo {' + contents + '}>'

    
    def __getstate__(self):
        default_bytes = self.default_bytes[:self.default_bytes_length]
        return {
            '_name_array': self.name,
            'name_length': self.name_length,
            '_default_bytes': default_bytes,
            'default_bytes_length': self.default_bytes_length,
            'setting_type': self.setting_type,
            'u': self.u }

    
    def __setstate__(self, state):
        pass
    # WARNING: Decompyle incomplete

    from_str = (lambda cls, s: 
def trim_prefix(s, prefix):
if not s.startswith(prefix):
raise AsphodelError('Invalid string prefix "{}"'.format(prefix))s[len(prefix):]
def trim_suffix(s, suffix):
if not s.endswith(suffix):
raise AsphodelError('Invalid string suffix "{}"'.format(suffix))s[:-len(suffix)]s = trim_prefix(s, '<AsphodelSettingInfo {')s = trim_suffix(s, '}>')u = AsphodelSettingUnion()if not s.endswith('UNKNOWN TYPE'):
s = trim_suffix(s, '}>')(s, u_vals) = s.rsplit(' {', 1)(s, u_type) = s.rsplit(', u=<')u_dict = dict(map((lambda s: s.split('=', 1)), u_vals.split(', ')))
            if 'unit_type' in u_dict:
                u_dict['unit_type'] = u_dict['unit_type'].split(' ', 1)[0]
            for k, v in u_dict.items():
                u_dict[k] = int(v)
                except ValueError:
                    u_dict[k] = float(v)
                    continue
                for field_name, field_type in AsphodelSettingUnion._fields_:
                    if field_type.__name__ == u_type:
                        u_struct = getattr(u, field_name)
                        for name, value in u_dict.items():
                            setattr(u_struct, name, value)
                    (s, setting_type_str) = s.rsplit(', setting_type=', 1)
                    setting_type = int(setting_type_str.split(' (', 1)[0])
                    (s, default_bytes_length_str) = s.rsplit(', default_bytes_length=', 1)
                    default_bytes_length = int(default_bytes_length_str)
                    (s, default_bytes_str) = s.rsplit(', default_bytes=', 1)
                    b = ''.join(map((lambda x: x[2:]), default_bytes_str.split(',')))
                    default_bytes = binascii.a2b_hex(b)
                    if len(default_bytes) != default_bytes_length:
                        raise AsphodelError('Bad default_bytes_length')
                    (s, name_length_str) = s.rsplit(', name_length=', 1)
                    name_length = int(name_length_str)
                    name_str = trim_prefix(s, 'name=')
                    name = ast.literal_eval(name_str)
                    if not isinstance(name, bytes):
                        raise AsphodelError('Bad name')
                    if len(name) != name_length:
                        raise AsphodelError('Bad name_length')
                    instance = cls.__new__(cls)
                    instance.__setstate__({
                        '_name_array': name,
                        'name_length': name_length,
                        '_default_bytes': default_bytes,
                        'default_bytes_length': default_bytes_length,
                        'setting_type': setting_type,
                        'u': u })
                    return instance
)()


class AsphodelNative:
    AsphodelTransferCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_void_p)
    AsphodelStreamingCallback = CFUNCTYPE(None, c_int, POINTER(c_uint8), c_size_t, c_size_t, c_void_p)
    AsphodelConnectCallback = CFUNCTYPE(None, c_int, c_int, c_void_p)
    AsphodelCommandCallback = CFUNCTYPE(None, c_int, c_void_p)
    AsphodelDecodeCallback = CFUNCTYPE(None, c_uint64, POINTER(c_double), c_size_t, c_size_t, c_void_p)
    AsphodelCounterDecoderFunc = CFUNCTYPE(c_uint64, POINTER(c_uint8), c_uint64)
    AsphodelLostPacketCallback = CFUNCTYPE(None, c_uint64, c_uint64, c_void_p)
    AsphodelIDDecoderFunc = CFUNCTYPE(c_uint8, POINTER(c_uint8))
    AsphodelUnknownIDCallback = CFUNCTYPE(None, c_uint8, c_void_p)
    
    class AsphodelDeviceStruct(Structure):
        pass

    AsphodelDeviceStruct._fields_ = [
        ('protocol_type', c_int),
        ('location_string', c_char_p),
        ('open_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct))),
        ('close_device', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
        ('free_device', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
        ('get_serial_number', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_char_p, c_size_t)),
        ('do_transfer', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint8, POINTER(c_uint8), c_size_t, AsphodelTransferCallback, c_void_p)),
        ('do_transfer_reset', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint8, POINTER(c_uint8), c_size_t, AsphodelTransferCallback, c_void_p)),
        ('start_streaming_packets', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_int, c_int, c_uint, AsphodelStreamingCallback, c_void_p)),
        ('stop_streaming_packets', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct))),
        ('get_stream_packets_blocking', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(c_uint8), POINTER(c_int), c_uint)),
        ('get_max_incoming_param_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
        ('get_max_outgoing_param_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
        ('get_stream_packet_length', CFUNCTYPE(c_size_t, POINTER(AsphodelDeviceStruct))),
        ('poll_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_int, POINTER(c_int))),
        ('set_connect_callback', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), AsphodelConnectCallback, c_void_p)),
        ('wait_for_connect', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), c_uint)),
        ('get_remote_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
        ('reconnect_device', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
        ('error_callback', CFUNCTYPE(None, POINTER(AsphodelDeviceStruct), c_int, c_void_p)),
        ('error_closure', c_void_p),
        ('reconnect_device_bootloader', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
        ('reconnect_device_application', CFUNCTYPE(c_int, POINTER(AsphodelDeviceStruct), POINTER(POINTER(AsphodelDeviceStruct)))),
        ('implementation_info', c_void_p),
        ('transport_type', c_char_p),
        ('_reserved', c_void_p * 9)]
    
    class AsphodelChannelCalibration(Structure):
        _fields_ = [
            ('base_setting_index', c_int),
            ('resolution_setting_index', c_int),
            ('scale', c_float),
            ('offset', c_float),
            ('minimum', c_float),
            ('maximum', c_float)]

    
    class AsphodelSupplyInfo(Structure):
        _fields_ = [
            ('name', c_char_p),
            ('name_length', c_uint8),
            ('unit_type', c_uint8),
            ('is_battery', c_uint8),
            ('nominal', c_int32),
            ('scale', c_float),
            ('offset', c_float)]

    
    class AsphodelCtrlVarInfo(Structure):
        _fields_ = [
            ('name', c_char_p),
            ('name_length', c_uint8),
            ('unit_type', c_uint8),
            ('minimum', c_int32),
            ('maximum', c_int32),
            ('scale', c_float),
            ('offset', c_float)]

    
    class AsphodelExtraScanResult(Structure):
        _fields_ = [
            ('serial_number', c_uint32),
            ('asphodel_type', c_uint8),
            ('device_mode', c_uint8),
            ('_reserved', c_uint16)]

    
    class AsphodelGPIOPortInfo(Structure):
        _fields_ = [
            ('name', c_char_p),
            ('name_length', c_uint8),
            ('input_pins', c_uint32),
            ('output_pins', c_uint32),
            ('floating_pins', c_uint32),
            ('loaded_pins', c_uint32),
            ('overridden_pins', c_uint32)]

    
    class AsphodelStreamAndChannels(Structure):
        _fields_ = [
            ('stream_id', c_uint8),
            ('stream_info', POINTER(AsphodelStreamInfo)),
            ('channel_info', POINTER(POINTER(AsphodelChannelInfo)))]

    
    class AsphodelChannelDecoder(Structure):
        pass

    AsphodelChannelDecoder._fields_ = [
        ('decode', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder), c_uint64, POINTER(c_uint8))),
        ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder))),
        ('reset', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder))),
        ('set_conversion_factor', CFUNCTYPE(None, POINTER(AsphodelChannelDecoder), c_double, c_double)),
        ('channel_bit_offset', c_uint16),
        ('samples', c_size_t),
        ('channel_name', c_char_p),
        ('subchannels', c_size_t),
        ('subchannel_names', POINTER(c_char_p)),
        ('callback', AsphodelDecodeCallback),
        ('closure', c_void_p)]
    
    class AsphodelStreamDecoder(Structure):
        pass

    AsphodelStreamDecoder._fields_ = [
        ('decode', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder), POINTER(c_uint8))),
        ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder))),
        ('reset', CFUNCTYPE(None, POINTER(AsphodelStreamDecoder))),
        ('last_count', c_uint64),
        ('counter_byte_offset', c_size_t),
        ('counter_decoder', AsphodelCounterDecoderFunc),
        ('channels', c_size_t),
        ('decoders', POINTER(POINTER(AsphodelChannelDecoder))),
        ('lost_packet_callback', AsphodelLostPacketCallback),
        ('lost_packet_closure', c_void_p),
        ('used_bits', c_uint16)]
    
    class AsphodelDeviceDecoder(Structure):
        pass

    AsphodelDeviceDecoder._fields_ = [
        ('decode', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder), POINTER(c_uint8))),
        ('free_decoder', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder))),
        ('reset', CFUNCTYPE(None, POINTER(AsphodelDeviceDecoder))),
        ('id_byte_offset', c_size_t),
        ('id_decoder', AsphodelIDDecoderFunc),
        ('streams', c_size_t),
        ('stream_ids', POINTER(c_uint8)),
        ('decoders', POINTER(POINTER(AsphodelStreamDecoder))),
        ('unknown_id_callback', AsphodelUnknownIDCallback),
        ('unknown_id_closure', c_void_p),
        ('used_bits', c_uint16)]
    
    class AsphodelTCPAdvInfo(Structure):
        _fields_ = [
            ('tcp_version', c_uint8),
            ('connected', c_uint8),
            ('max_incoming_param_length', c_size_t),
            ('max_outgoing_param_length', c_size_t),
            ('stream_packet_length', c_size_t),
            ('protocol_type', c_int),
            ('serial_number', c_char_p),
            ('board_rev', c_uint8),
            ('board_type', c_char_p),
            ('build_info', c_char_p),
            ('build_date', c_char_p),
            ('user_tag1', c_char_p),
            ('user_tag2', c_char_p),
            ('remote_max_incoming_param_length', c_size_t),
            ('remote_max_outgoing_param_length', c_size_t),
            ('remote_stream_packet_length', c_size_t)]

    
    class AsphodelUnitFormatter(Structure):
        pass

    AsphodelUnitFormatter._fields_ = [
        ('format_bare', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
        ('format_ascii', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
        ('format_utf8', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
        ('format_html', CFUNCTYPE(c_int, POINTER(AsphodelUnitFormatter), c_char_p, c_size_t, c_double)),
        ('free', CFUNCTYPE(None, POINTER(AsphodelUnitFormatter))),
        ('unit_ascii', c_char_p),
        ('unit_utf8', c_char_p),
        ('unit_html', c_char_p),
        ('conversion_scale', c_double),
        ('conversion_offset', c_double)]
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def free(self):
        if self.device_list:
            for device in self.device_list:
                device.free()
                self.device_list = None
                if self.lib:
                    if self.usb_devices_supported:
                        self.lib.asphodel_usb_deinit()
                    if self.tcp_devices_supported:
                        self.lib.asphodel_tcp_deinit()
                    self.lib = None
                    return None
                return None

    
    def __del__(self):
        self.free()

    
    def asphodel_error_check(self, result, func, arguments = (None, None)):
        if result != 0:
            error_name = self.lib.asphodel_error_name(result)
            raise AsphodelError(result, error_name)

    
    def asphodel_string_decode_check(self, result, func, arguments):
        return result.decode('UTF-8')

    
    def load_library_function(self, name, restype, argtypes, errcheck, ignore_missing = (True,)):
        pass
    # WARNING: Decompyle incomplete

    
    def load_device_function(self, base_name, argtypes):
        non_blocking_name = base_name
        blocking_name = base_name + '_blocking'
        blocking_argtypes = [
            POINTER(self.AsphodelDeviceStruct)]
        blocking_argtypes.extend(argtypes)
        non_blocking_argtypes = list(blocking_argtypes)
        non_blocking_argtypes.append(self.AsphodelCommandCallback)
        non_blocking_argtypes.append(c_void_p)
        self.load_library_function(non_blocking_name, c_int, non_blocking_argtypes, self.asphodel_error_check)
        self.load_library_function(blocking_name, c_int, blocking_argtypes, self.asphodel_error_check)

    
    def setup_api_h_prototypes(self):
        string_decode = self.asphodel_string_decode_check
        self.load_library_function('asphodel_error_name', c_char_p, [
            c_int], string_decode)
        self.load_library_function('asphodel_unit_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_unit_type_count', c_uint8, [], None)
        self.load_library_function('asphodel_channel_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_channel_type_count', c_uint8, [], None)
        self.load_library_function('asphodel_setting_type_name', c_char_p, [
            c_uint8], string_decode)
        self.load_library_function('asphodel_get_setting_type_count', c_uint8, [], None)

    
    def setup_bootloader_h_prototypes(self):
        self.load_device_function('asphodel_bootloader_start_program', [])
        self.load_device_function('asphodel_get_bootloader_page_info', [
            POINTER(c_uint32),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_bootloader_block_sizes', [
            POINTER(c_uint16),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_start_bootloader_page', [
            c_uint32,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_bootloader_code_block', [
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_bootloader_page', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint16),
            c_uint8])
        self.load_device_function('asphodel_finish_bootloader_page', [
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_verify_bootloader_page', [
            POINTER(c_uint8),
            c_size_t])

    
    def setup_channel_specific_h_prototypes(self):
        self.load_library_function('asphodel_get_strain_bridge_count', c_int, [
            POINTER(AsphodelChannelInfo),
            POINTER(c_int)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_strain_bridge_subchannel', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_strain_bridge_values', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            c_float * 5], self.asphodel_error_check)
        self.load_device_function('asphodel_set_strain_outputs', [
            c_int,
            c_int,
            c_int,
            c_int])
        self.load_library_function('asphodel_check_strain_resistances', c_int, [
            POINTER(AsphodelChannelInfo),
            c_int,
            c_double,
            c_double,
            c_double,
            POINTER(c_double),
            POINTER(c_double),
            POINTER(c_int)], self.asphodel_error_check)
        self.load_library_function('asphodel_get_accel_self_test_limits', c_int, [
            POINTER(AsphodelChannelInfo),
            c_float * 6], self.asphodel_error_check)
        self.load_device_function('asphodel_enable_accel_self_test', [
            c_int,
            c_int])
        self.load_library_function('asphodel_check_accel_self_test', c_int, [
            POINTER(AsphodelChannelInfo),
            c_double * 3,
            c_double * 3,
            POINTER(c_int)], self.asphodel_error_check)

    
    def setup_ctrl_var_h_prototypes(self):
        self.load_device_function('asphodel_get_ctrl_var_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_ctrl_var_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_ctrl_var_info', [
            c_int,
            POINTER(self.AsphodelCtrlVarInfo)])
        self.load_device_function('asphodel_get_ctrl_var', [
            c_int,
            POINTER(c_int32)])
        self.load_device_function('asphodel_set_ctrl_var', [
            c_int,
            c_int32])

    
    def setup_decode_h_prototypes(self):
        self.load_library_function('asphodel_create_channel_decoder', c_int, [
            POINTER(AsphodelChannelInfo),
            c_uint16,
            POINTER(POINTER(self.AsphodelChannelDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_create_stream_decoder', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint16,
            POINTER(POINTER(self.AsphodelStreamDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_create_device_decoder', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint8,
            c_uint8,
            c_uint8,
            POINTER(POINTER(self.AsphodelDeviceDecoder))], self.asphodel_error_check)
        self.load_library_function('asphodel_get_streaming_counts', c_int, [
            POINTER(self.AsphodelStreamAndChannels),
            c_uint8,
            c_double,
            c_double,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_uint)], self.asphodel_error_check)

    
    def setup_device_h_prototypes(self):
        self.load_device_function('asphodel_get_protocol_version', [
            POINTER(c_uint16)])
        self.load_device_function('asphodel_get_protocol_version_string', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_board_info', [
            POINTER(c_uint8),
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_user_tag_locations', [
            c_size_t * 6])
        self.load_device_function('asphodel_get_build_info', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_build_date', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_commit_id', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_repo_branch', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_repo_name', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_family', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_model', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_chip_id', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_nvm_size', [
            POINTER(c_size_t)])
        self.load_device_function('asphodel_erase_nvm', [])
        self.load_device_function('asphodel_write_nvm_raw', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_write_nvm_section', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_read_nvm_raw', [
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_read_nvm_section', [
            c_size_t,
            POINTER(c_uint8),
            c_size_t])
        self.load_device_function('asphodel_read_user_tag_string', [
            c_size_t,
            c_size_t,
            c_char_p])
        self.load_device_function('asphodel_write_user_tag_string', [
            c_size_t,
            c_size_t,
            c_char_p])
        self.load_device_function('asphodel_get_nvm_modified', [
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_nvm_hash', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_get_setting_hash', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_flush', [])
        self.load_device_function('asphodel_reset', [])
        self.load_device_function('asphodel_get_bootloader_info', [
            c_char_p,
            c_size_t])
        self.load_device_function('asphodel_bootloader_jump', [])
        self.load_device_function('asphodel_get_reset_flag', [
            POINTER(c_uint8)])
        self.load_device_function('asphodel_clear_reset_flag', [])
        self.load_device_function('asphodel_get_rgb_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_rgb_values', [
            c_int,
            c_uint8 * 3])
        self.load_device_function('asphodel_set_rgb_values', [
            c_int,
            c_uint8 * 3,
            c_int])
        self.load_device_function('asphodel_set_rgb_values_hex', [
            c_int,
            c_uint32,
            c_int])
        self.load_device_function('asphodel_get_led_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_led_value', [
            c_int,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_set_led_value', [
            c_int,
            c_uint8,
            c_int])
        self.load_device_function('asphodel_set_device_mode', [
            c_uint8])
        self.load_device_function('asphodel_get_device_mode', [
            POINTER(c_uint8)])

    
    def setup_device_type_h_prototypes(self):
        self.load_library_function('asphodel_supports_rf_power_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_radio_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_remote_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_supports_bootloader_commands', c_int, [
            POINTER(self.AsphodelDeviceStruct)], None)

    
    def setup_low_level_h_prototypes(self):
        self.load_device_function('asphodel_get_gpio_port_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_gpio_port_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_gpio_port_info', [
            c_int,
            POINTER(self.AsphodelGPIOPortInfo)])
        self.load_device_function('asphodel_get_gpio_port_values', [
            c_int,
            POINTER(c_uint32)])
        self.load_device_function('asphodel_set_gpio_port_modes', [
            c_int,
            c_uint8,
            c_uint32])
        self.load_device_function('asphodel_disable_gpio_overrides', [])
        self.load_device_function('asphodel_get_bus_counts', [
            POINTER(c_int),
            POINTER(c_int)])
        self.load_device_function('asphodel_set_spi_cs_mode', [
            c_int,
            c_uint8])
        self.load_device_function('asphodel_do_spi_transfer', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_i2c_write', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_i2c_read', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_radio_fixed_test', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            c_uint8,
            POINTER(c_uint8),
            c_uint8])
        self.load_device_function('asphodel_do_radio_fixed_test', [
            c_uint16,
            c_uint16,
            c_uint8])
        self.load_device_function('asphodel_do_radio_sweep_test', [
            c_uint16,
            c_uint16,
            c_uint16,
            c_uint16,
            c_uint8])
        self.load_device_function('asphodel_get_info_region_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_info_region_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_info_region', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stack_info', [
            c_uint32 * 2])
        self.load_device_function('asphodel_echo_raw', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_echo_transaction', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_echo_params', [
            POINTER(c_uint8),
            c_size_t,
            POINTER(c_uint8),
            POINTER(c_size_t)])

    
    def setup_mem_test_h_prototypes(self):
        
        try:
            self.load_library_function('asphodel_mem_test_supported', c_int, [], None, ignore_missing = False)
            self.mem_test_supported = self.lib.asphodel_mem_test_supported()
        except AttributeError:
            self.mem_test_supported = False

        self.load_library_function('asphodel_mem_test_set_limit', None, [
            c_int], None)
        self.load_library_function('asphodel_mem_test_get_limit', c_int, [], None)

    
    def setup_radio_h_prototypes(self):
        self.load_device_function('asphodel_stop_radio', [])
        self.load_device_function('asphodel_start_radio_scan', [])
        self.load_device_function('asphodel_get_raw_radio_scan_results', [
            POINTER(c_uint32),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_get_radio_scan_results', [
            POINTER(POINTER(c_uint32)),
            POINTER(c_size_t)])
        self.load_library_function('asphodel_free_radio_scan_results', None, [
            POINTER(c_uint32)], None)
        self.load_device_function('asphodel_get_raw_radio_extra_scan_results', [
            POINTER(self.AsphodelExtraScanResult),
            POINTER(c_size_t)])
        self.load_device_function('asphodel_get_radio_extra_scan_results', [
            POINTER(POINTER(self.AsphodelExtraScanResult)),
            POINTER(c_size_t)])
        self.load_library_function('asphodel_free_radio_extra_scan_results', None, [
            POINTER(self.AsphodelExtraScanResult)], None)
        self.load_device_function('asphodel_get_radio_scan_power', [
            POINTER(c_uint32),
            POINTER(c_int8),
            c_size_t])
        self.load_device_function('asphodel_connect_radio', [
            c_uint32])
        self.load_device_function('asphodel_get_radio_status', [
            POINTER(c_int),
            POINTER(c_uint32),
            POINTER(c_uint8),
            POINTER(c_int)])
        self.load_device_function('asphodel_get_radio_ctrl_vars', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_radio_default_serial', [
            POINTER(c_uint32)])
        self.load_device_function('asphodel_start_radio_scan_boot', [])
        self.load_device_function('asphodel_connect_radio_boot', [
            c_uint32])
        self.load_device_function('asphodel_stop_remote', [])
        self.load_device_function('asphodel_restart_remote', [])
        self.load_device_function('asphodel_get_remote_status', [
            POINTER(c_int),
            POINTER(c_uint32),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_restart_remote_app', [])
        self.load_device_function('asphodel_restart_remote_boot', [])

    
    def setup_rf_power_h_prototypes(self):
        self.load_device_function('asphodel_enable_rf_power', [
            c_int])
        self.load_device_function('asphodel_get_rf_power_status', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_rf_power_ctrl_vars', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_reset_rf_power_timeout', [
            c_uint32])

    
    def setup_setting_h_prototypes(self):
        self.load_device_function('asphodel_get_setting_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_setting_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_info', [
            c_int,
            POINTER(AsphodelSettingInfo)])
        self.load_device_function('asphodel_get_setting_default', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_custom_enum_counts', [
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_custom_enum_value_name', [
            c_int,
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_category_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_setting_category_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_setting_category_settings', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])

    
    def setup_stream_h_prototypes(self):
        self.load_device_function('asphodel_get_stream_count', [
            POINTER(c_int),
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stream', [
            c_int,
            POINTER(POINTER(AsphodelStreamInfo))])
        self.load_library_function('asphodel_free_stream', None, [
            POINTER(AsphodelStreamInfo)], None)
        self.load_device_function('asphodel_get_stream_channels', [
            c_int,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_stream_format', [
            c_int,
            POINTER(AsphodelStreamInfo)])
        self.load_device_function('asphodel_enable_stream', [
            c_int,
            c_int])
        self.load_device_function('asphodel_warm_up_stream', [
            c_int,
            c_int])
        self.load_device_function('asphodel_get_stream_status', [
            c_int,
            POINTER(c_int),
            POINTER(c_int)])
        self.load_device_function('asphodel_get_stream_rate_info', [
            c_int,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_float),
            POINTER(c_float)])
        self.load_device_function('asphodel_get_channel_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_channel', [
            c_int,
            POINTER(POINTER(AsphodelChannelInfo))])
        self.load_library_function('asphodel_free_channel', None, [
            POINTER(AsphodelChannelInfo)], None)
        self.load_device_function('asphodel_get_channel_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_info', [
            c_int,
            POINTER(AsphodelChannelInfo)])
        self.load_device_function('asphodel_get_channel_coefficients', [
            c_int,
            POINTER(c_float),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_chunk', [
            c_int,
            c_uint8,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_channel_specific', [
            c_int,
            POINTER(c_uint8),
            c_uint8,
            POINTER(c_uint8),
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_channel_calibration', [
            c_int,
            POINTER(c_int),
            POINTER(self.AsphodelChannelCalibration)])

    
    def setup_supply_h_prototypes(self):
        self.load_device_function('asphodel_get_supply_count', [
            POINTER(c_int)])
        self.load_device_function('asphodel_get_supply_name', [
            c_int,
            c_char_p,
            POINTER(c_uint8)])
        self.load_device_function('asphodel_get_supply_info', [
            c_int,
            POINTER(self.AsphodelSupplyInfo)])
        self.load_device_function('asphodel_check_supply', [
            c_int,
            POINTER(c_int32),
            POINTER(c_uint8),
            c_uint])

    
    def setup_tcp_h_prototypes(self):
        
        try:
            self.load_library_function('asphodel_tcp_devices_supported', c_int, [], None, ignore_missing = False)
            s = self.lib.asphodel_tcp_devices_supported()
            self.tcp_devices_supported = s
        except AttributeError:
            self.tcp_devices_supported = False

        self.load_library_function('asphodel_tcp_init', c_int, [], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_deinit', None, [], None)
        self.load_library_function('asphodel_tcp_find_devices', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_find_devices_filter', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t),
            c_uint32], self.asphodel_error_check)
        self.load_library_function('asphodel_tcp_get_advertisement', POINTER(self.AsphodelTCPAdvInfo), [
            POINTER(self.AsphodelDeviceStruct)], None)
        self.load_library_function('asphodel_tcp_create_device', c_int, [
            c_char_p,
            c_uint16,
            c_int,
            c_char_p,
            POINTER(POINTER(self.AsphodelDeviceStruct))], self.asphodel_error_check)

    
    def setup_unit_format_h_prototypes(self):
        self.load_library_function('asphodel_create_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
            c_uint8,
            c_double,
            c_double,
            c_double,
            c_int], None)
        self.load_library_function('asphodel_create_custom_unit_formatter', POINTER(self.AsphodelUnitFormatter), [
            c_double,
            c_double,
            c_double,
            c_char_p,
            c_char_p,
            c_char_p], None)
        self.load_library_function('asphodel_format_value_ascii', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)
        self.load_library_function('asphodel_format_value_utf8', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)
        self.load_library_function('asphodel_format_value_html', c_int, [
            c_char_p,
            c_size_t,
            c_uint8,
            c_double,
            c_int,
            c_double], None)

    
    def setup_usb_h_prototypes(self):
        
        try:
            self.load_library_function('asphodel_usb_devices_supported', c_int, [], None, ignore_missing = False)
            s = self.lib.asphodel_usb_devices_supported()
            self.usb_devices_supported = s
        except AttributeError:
            self.usb_devices_supported = True

        self.load_library_function('asphodel_usb_init', c_int, [], self.asphodel_error_check)
        self.load_library_function('asphodel_usb_deinit', None, [], None)
        self.load_library_function('asphodel_usb_find_devices', c_int, [
            POINTER(POINTER(self.AsphodelDeviceStruct)),
            POINTER(c_size_t)], self.asphodel_error_check)
        self.load_library_function('asphodel_usb_get_backend_version', c_char_p, [], None)

    
    def setup_version_h_prototypes(self):
        self.load_library_function('asphodel_get_library_protocol_version', c_uint16, [], None)
        self.load_library_function('asphodel_get_library_protocol_version_string', c_char_p, [], None)
        self.load_library_function('asphodel_get_library_build_info', c_char_p, [], None)
        self.load_library_function('asphodel_get_library_build_date', c_char_p, [], None)

    
    def find_usb_devices(self):
        count = c_size_t(0)
        self.lib.asphodel_usb_find_devices(None, byref(count))
        array_size = count.value
        if array_size == 0:
            return []
        array = POINTER(self.AsphodelDeviceStruct) * array_size()
        array_ptr = cast(byref(array), POINTER(POINTER(self.AsphodelDeviceStruct)))
        self.lib.asphodel_usb_find_devices(array_ptr, byref(count))
        array_entries = min(array_size, count.value)
        device_list = []
        for i in range(array_entries):
            device_list.append(AsphodelNativeDevice(self, array[i].contents))
            return device_list

    
    def find_tcp_devices(self, flags = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def create_tcp_device(self, host, port, timeout, serial = (None,)):
        device_ptr = POINTER(self.AsphodelDeviceStruct)()
        if serial:
            serial_bytes = serial.encode('UTF-8')
        else:
            serial_bytes = None
        self.lib.asphodel_tcp_create_device(host.encode('UTF-8'), port, timeout, serial_bytes, byref(device_ptr))
        return AsphodelNativeDevice(self, device_ptr.contents)

    
    def tcp_get_advertisement(self, device):
        adv_ptr = self.lib.asphodel_tcp_get_advertisement(device)
        adv = adv_ptr.contents
        
        def decode_safe(b):
            
            try:
                return b.decode('UTF-8')
            except UnicodeDecodeError:
                return 'ERROR'


        return TCPAdvInfo(adv.tcp_version, bool(adv.connected), adv.max_incoming_param_length, adv.max_outgoing_param_length, adv.stream_packet_length, adv.protocol_type, decode_safe(adv.serial_number), adv.board_rev, decode_safe(adv.board_type), decode_safe(adv.build_info), decode_safe(adv.build_date), decode_safe(adv.user_tag1), decode_safe(adv.user_tag2), adv.remote_max_incoming_param_length, adv.remote_max_outgoing_param_length, adv.remote_stream_packet_length)

    
    def create_channel_decoder(self, channel_info, bit_offset):
        decoder_ptr = POINTER(self.AsphodelChannelDecoder)()
        self.lib.asphodel_create_channel_decoder(channel_info, bit_offset, byref(decoder_ptr))
        return AsphodelNativeChannelDecoder(self, decoder_ptr.contents, channel_info)

    
    def create_stream_decoder(self, stream_info, channel_info_list, bit_offset):
        decoder_ptr = POINTER(self.AsphodelStreamDecoder)()
        array_type = POINTER(AsphodelChannelInfo) * len(channel_info_list)
    # WARNING: Decompyle incomplete

    
    def create_device_decoder(self, info_list, filler_bits, id_bits):
        '''
        info_list is a sequence of tuples of (stream_id, stream_info,
        channel_info_list).
        '''
        decoder_ptr = POINTER(self.AsphodelDeviceDecoder)()
        array_size = len(info_list)
        info_array = self.AsphodelStreamAndChannels * array_size()
    # WARNING: Decompyle incomplete

    
    def get_streaming_counts(self, streams, response_time, buffer_time, timeout):
        '''
        returns (packet_count, transfer_count, timeout)
        '''
        packet_count = c_int()
        transfer_count = c_int()
        timeout = c_uint(timeout)
        array_size = len(streams)
        info_array = self.AsphodelStreamAndChannels * array_size()
        for i, stream_info in enumerate(streams):
            info_array[i].stream_info = pointer(stream_info)
            self.lib.asphodel_get_streaming_counts(cast(info_array, POINTER(self.AsphodelStreamAndChannels)), array_size, response_time, buffer_time, byref(packet_count), byref(transfer_count), byref(timeout))
            return (packet_count.value, transfer_count.value, timeout.value)

    
    def create_unit_formatter(self, unit_type, minimum, maximum, resolution, use_metric = (True,)):
        use_metric_int = 1 if use_metric else 0
        formatter = self.lib.asphodel_create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric_int)
        if not formatter:
            raise AsphodelError(0, 'asphodel_create_unit_formatter returned NULL')
        recreate = (recreate_unit_formatter, (unit_type, minimum, maximum, resolution, use_metric))
        return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)

    
    def create_custom_unit_formatter(self, scale, offset, resolution, unit_ascii, unit_utf8, unit_html):
        formatter = self.lib.asphodel_create_custom_unit_formatter(scale, offset, resolution, unit_ascii.encode('ascii'), unit_utf8.encode('UTF-8'), unit_html.encode('ascii'))
        if not formatter:
            raise AsphodelError(0, 'asphodel_create_custom_unit_formatter returned NULL')
        recreate = (recreate_custom_unit_formatter, (scale, offset, resolution, unit_ascii, unit_utf8, unit_html))
        return AsphodelNativeUnitFormatter(self, formatter.contents, recreate)

    
    def _format_value(self, lib_func, unit_type, resolution, value, use_metric):
        use_metric_int = 1 if use_metric else 0
        buffer = create_string_buffer(256)
        lib_func(buffer, len(buffer), unit_type, resolution, use_metric_int, value)
        return buffer.value

    
    def format_value_ascii(self, unit_type, resolution, value, use_metric = (True,)):
        b = self._format_value(self.lib.asphodel_format_value_ascii, unit_type, resolution, value, use_metric)
        return b.decode('ascii')

    
    def format_value_utf8(self, unit_type, resolution, value, use_metric = (True,)):
        b = self._format_value(self.lib.asphodel_format_value_utf8, unit_type, resolution, value, use_metric)
        return b.decode('UTF-8')

    
    def format_value_html(self, unit_type, resolution, value, use_metric = (True,)):
        b = self._format_value(self.lib.asphodel_format_value_html, unit_type, resolution, value, use_metric)
        return b.decode('ascii')

    
    def mem_test_set_limit(self, limit):
        self.lib.asphodel_mem_test_set_limit(limit)

    
    def mem_test_get_limit(self):
        return self.lib.asphodel_mem_test_get_limit()



def asphodel_command(func_base):
    pass
# WARNING: Decompyle incomplete


class AsphodelNativeDevice:
    MAX_STRING_LENGTH = 128
    
    def __init__(self, lib, device):
        self.lib = lib
        self.device = device
        self._callbacks = []
        self._remote = None
        if self.get_transport_type() == 'usb':
            self.reconnect_time = 5
        else:
            self.reconnect_time = 10
        if self.lib:
            self.lib.device_list.add(self)
            return None

    
    def open(self):
        ret = self.device.open_device(self.device)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    
    def close(self):
        if self.device:
            self.device.close_device(self.device)
            return None

    
    def free(self):
        self.close()
        if self.device:
            self.device.free_device(self.device)
        self.device = None
        self.lib = None

    
    def __del__(self):
        self.free()

    
    def get_location_string(self):
        return self.device.location_string.decode('UTF-8')

    
    def get_transport_type(self):
        if self.lib.protocol_version >= 515:
            return self.device.transport_type.decode('UTF-8')

    
    def get_serial_number(self):
        buffer = create_string_buffer(64)
        ret = self.device.get_serial_number(self.device, buffer, len(buffer))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return buffer.value.decode('UTF-8')

    
    def do_transfer(self, cmd, params, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def do_transfer_blocking(self, cmd, params = (None,)):
        '''
        This function is for testing purposes only!
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def do_transfer_reset(self, cmd, params, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def do_transfer_reset_blocking(self, cmd, params = (None,)):
        '''
        This function is for testing purposes only!
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def start_streaming_packets(self, packet_count, transfer_count, timeout, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def stop_streaming_packets(self):
        self.device.stop_streaming_packets(self.device)
        
        try:
            del self._streaming_callback
            return None
        except AttributeError:
            return None


    
    def get_stream_packets_blocking(self, byte_count, timeout):
        buffer = c_uint8 * byte_count()
        count_int = c_int(byte_count)
        ret = self.device.get_stream_packets_blocking(self.device, buffer, byref(count_int), timeout)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return bytes(buffer[0:count_int.value])

    
    def get_max_incoming_param_length(self):
        v = self.device.get_max_incoming_param_length(self.device)
        return v

    
    def get_max_outgoing_param_length(self):
        v = self.device.get_max_outgoing_param_length(self.device)
        return v

    
    def get_stream_packet_length(self):
        v = self.device.get_stream_packet_length(self.device)
        return v

    
    def poll_device(self, milliseconds):
        ret = self.device.poll_device(self.device, milliseconds, None)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    
    def set_connect_callback(self, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def wait_for_connect(self, timeout):
        ret = self.device.wait_for_connect(self.device, timeout)
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)

    
    def _get_raw_remote_device(self):
        remote_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.get_remote_device(self.device, byref(remote_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        return remote_ptr.contents

    
    def get_remote_device(self):
        pass
    # WARNING: Decompyle incomplete

    
    def reconnect(self, bootloader, application, serial_number = (False, False, None)):
        if bootloader and application:
            raise ValueError('cannot set both application and bootloader')
        if bootloader:
            reconnect_func = self.reconnect_device_bootloader
        elif application:
            reconnect_func = self.reconnect_device_application
        else:
            reconnect_func = self.reconnect_device
        if not serial_number:
            
            try:
                serial_number = self.get_serial_number()
            except AsphodelError:
                pass

            end_time = time.monotonic() + self.reconnect_time
            time.sleep(0.5)
            
            try:
                reconnect_func(reopen = True)
            except AsphodelError:
                if time.monotonic() >= end_time:
                    raise 

            if serial_number:
                device = find_device_by_serial(serial_number)
                if device:
                    time.sleep(0.5)
                    
                    try:
                        reconnect_func(reopen = True)
                    except AsphodelError:
                        pass

                    time.sleep(0.5)
                    
                    try:
                        reconnect_func(reopen = True)
                    except AsphodelError:
                        pass

                    native_device = device.device
                    device.device = None
                    self._reconnect_helper(native_device, reopen = True)
                else:
                    time.sleep(0.25)
                self.wait_for_connect(int(self.reconnect_time * 1000))
                return None

    
    def _reconnect_helper(self, new_device, reopen):
        if addressof(new_device) == addressof(self.device):
            return None
        None.close()
        if self.device:
            self.device.free_device(self.device)
        self.device = new_device
        if reopen:
            self.open()
    # WARNING: Decompyle incomplete

    
    def reconnect_device(self, reopen = (False,)):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    
    def reconnect_device_bootloader(self, reopen = (False,)):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device_bootloader(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    
    def reconnect_device_application(self, reopen = (False,)):
        reconnected_ptr = POINTER(self.lib.AsphodelDeviceStruct)()
        ret = self.device.reconnect_device_application(self.device, byref(reconnected_ptr))
        if ret != 0:
            error_name = self.lib.lib.asphodel_error_name(ret)
            raise AsphodelError(ret, error_name)
        self._reconnect_helper(reconnected_ptr.contents, reopen)

    
    def supports_rf_power_commands(self):
        v = self.lib.lib.asphodel_supports_rf_power_commands(self.device)
        return bool(v)

    
    def supports_radio_commands(self):
        v = self.lib.lib.asphodel_supports_radio_commands(self.device)
        return bool(v)

    
    def supports_remote_commands(self):
        v = self.lib.lib.asphodel_supports_remote_commands(self.device)
        return bool(v)

    
    def supports_bootloader_commands(self):
        v = self.lib.lib.asphodel_supports_bootloader_commands(self.device)
        return bool(v)

    
    def set_error_callback(self, callback):
        pass
    # WARNING: Decompyle incomplete

    
    def tcp_get_advertisement(self):
        return self.lib.tcp_get_advertisement(self.device)

    get_protocol_version = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_protocol_version_string = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_board_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_user_tag_locations = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_build_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_build_date = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_commit_id = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_repo_branch = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_repo_name = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_chip_family = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_chip_model = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_chip_id = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_nvm_size = (lambda self: pass# WARNING: Decompyle incomplete
)()
    erase_nvm = (lambda self: pass# WARNING: Decompyle incomplete
)()
    write_nvm_raw = (lambda self, address, values: pass# WARNING: Decompyle incomplete
)()
    write_nvm_section = (lambda self, address, values: pass# WARNING: Decompyle incomplete
)()
    read_nvm_raw = (lambda self, address: pass# WARNING: Decompyle incomplete
)()
    read_nvm_section = (lambda self, address, length: pass# WARNING: Decompyle incomplete
)()
    read_user_tag_string = (lambda self, offset, length: pass# WARNING: Decompyle incomplete
)()
    write_user_tag_string = (lambda self, offset, length, string: pass# WARNING: Decompyle incomplete
)()
    get_nvm_modified = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_nvm_hash = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_setting_hash = (lambda self: pass# WARNING: Decompyle incomplete
)()
    flush = (lambda self: pass# WARNING: Decompyle incomplete
)()
    reset = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_bootloader_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    bootloader_jump = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_reset_flag = (lambda self: pass# WARNING: Decompyle incomplete
)()
    clear_reset_flag = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_rgb_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_rgb_values = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    set_rgb_values = (lambda self, index, values, instant = (False,): pass# WARNING: Decompyle incomplete
)()
    set_rgb_values_hex = (lambda self, index, hex_color, instant = (False,): pass# WARNING: Decompyle incomplete
)()
    get_led_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_led_value = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    set_led_value = (lambda self, index, value, instant = (False,): pass# WARNING: Decompyle incomplete
)()
    set_device_mode = (lambda self, mode: pass# WARNING: Decompyle incomplete
)()
    get_device_mode = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_stream_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_stream = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_stream_channels = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_stream_format = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    enable_stream = (lambda self, index, enable = (True,): pass# WARNING: Decompyle incomplete
)()
    warm_up_stream = (lambda self, index, enable = (True,): pass# WARNING: Decompyle incomplete
)()
    get_stream_status = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_stream_rate_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_channel_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_channel = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_channel_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_channel_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_channel_coefficients = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_channel_chunk = (lambda self, index, chunk_number: pass# WARNING: Decompyle incomplete
)()
    channel_specific = (lambda self, index, values: pass# WARNING: Decompyle incomplete
)()
    get_channel_calibration = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_supply_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_supply_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_supply_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    check_supply = (lambda self, index, tries = (20,): pass# WARNING: Decompyle incomplete
)()
    get_ctrl_var_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_ctrl_var_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_ctrl_var_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_ctrl_var = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    set_ctrl_var = (lambda self, index, value: pass# WARNING: Decompyle incomplete
)()
    get_setting_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_setting_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_setting_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_setting_default = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_custom_enum_counts = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_custom_enum_value_name = (lambda self, index, value: pass# WARNING: Decompyle incomplete
)()
    get_setting_category_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_setting_category_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_setting_category_settings = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_gpio_port_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_gpio_port_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_gpio_port_info = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_gpio_port_values = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    set_gpio_port_modes = (lambda self, index, mode, pins: pass# WARNING: Decompyle incomplete
)()
    disable_gpio_overrides = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_bus_counts = (lambda self: pass# WARNING: Decompyle incomplete
)()
    set_spi_cs_mode = (lambda self, index, mode: pass# WARNING: Decompyle incomplete
)()
    do_spi_transfer = (lambda self, index, write_bytes: pass# WARNING: Decompyle incomplete
)()
    do_i2c_write = (lambda self, index, addr, write_bytes: pass# WARNING: Decompyle incomplete
)()
    do_i2c_read = (lambda self, index, addr, read_length: pass# WARNING: Decompyle incomplete
)()
    do_i2c_write_read = (lambda self, index, addr, write_bytes, read_length: pass# WARNING: Decompyle incomplete
)()
    do_radio_fixed_test = (lambda self, channel, duration, mode: pass# WARNING: Decompyle incomplete
)()
    do_radio_sweep_test = (lambda self, start, stop, hop_interval, hop_count, mode: pass# WARNING: Decompyle incomplete
)()
    get_info_region_count = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_info_region_name = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_info_region = (lambda self, index: pass# WARNING: Decompyle incomplete
)()
    get_stack_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    echo_raw = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
    echo_transaction = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
    echo_params = (lambda self, values: pass# WARNING: Decompyle incomplete
)()
    enable_rf_power = (lambda self, enable = (True,): pass# WARNING: Decompyle incomplete
)()
    get_rf_power_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_rf_power_ctrl_vars = (lambda self: pass# WARNING: Decompyle incomplete
)()
    reset_rf_power_timeout = (lambda self, timeout: pass# WARNING: Decompyle incomplete
)()
    stop_radio = (lambda self: pass# WARNING: Decompyle incomplete
)()
    start_radio_scan = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_raw_radio_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_radio_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_raw_radio_extra_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_radio_extra_scan_results = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_radio_scan_power = (lambda self, serial_numbers: pass# WARNING: Decompyle incomplete
)()
    connect_radio = (lambda self, serial_number: pass# WARNING: Decompyle incomplete
)()
    get_radio_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_radio_ctrl_vars = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_radio_default_serial = (lambda self: pass# WARNING: Decompyle incomplete
)()
    start_radio_scan_boot = (lambda self: pass# WARNING: Decompyle incomplete
)()
    connect_radio_boot = (lambda self, serial_number: pass# WARNING: Decompyle incomplete
)()
    stop_remote = (lambda self: pass# WARNING: Decompyle incomplete
)()
    restart_remote = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_remote_status = (lambda self: pass# WARNING: Decompyle incomplete
)()
    restart_remote_app = (lambda self: pass# WARNING: Decompyle incomplete
)()
    restart_remote_boot = (lambda self: pass# WARNING: Decompyle incomplete
)()
    bootloader_start_program = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_bootloader_page_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    get_bootloader_block_sizes = (lambda self: pass# WARNING: Decompyle incomplete
)()
    start_bootloader_page = (lambda self, page_number, nonce: pass# WARNING: Decompyle incomplete
)()
    write_bootloader_code_block = (lambda self, data: pass# WARNING: Decompyle incomplete
)()
    write_bootloader_page = (lambda self, data, block_sizes: pass# WARNING: Decompyle incomplete
)()
    finish_bootloader_page = (lambda self, mac_tag = (None,): pass# WARNING: Decompyle incomplete
)()
    verify_bootloader_page = (lambda self, mac_tag = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def get_strain_bridge_count(self, channel_info):
        count = c_int()
        self.lib.lib.asphodel_get_strain_bridge_count(channel_info, byref(count))
        return count.value

    
    def get_strain_bridge_subchannel(self, channel_info, bridge_index):
        subchannel = c_size_t()
        self.lib.lib.asphodel_get_strain_bridge_subchannel(channel_info, bridge_index, byref(subchannel))
        return subchannel.value

    
    def get_strain_bridge_values(self, channel_info, bridge_index):
        array = c_float * 5()
        self.lib.lib.asphodel_get_strain_bridge_values(channel_info, bridge_index, array)
    # WARNING: Decompyle incomplete

    set_strain_outputs = (lambda self, channel_index, bridge_index, pos, neg: pass# WARNING: Decompyle incomplete
)()
    
    def check_strain_resistances(self, channel_info, bridge_index, baseline, pos_high, neg_high):
        '''
        Return (passed, pos_res, neg_res)
        '''
        passed = c_int(0)
        pos_res = c_double()
        neg_res = c_double()
        self.lib.lib.asphodel_check_strain_resistances(channel_info, bridge_index, baseline, pos_high, neg_high, byref(pos_res), byref(neg_res), byref(passed))
        return (bool(passed.value), pos_res.value, neg_res.value)

    
    def get_accel_self_test_limits(self, channel_info):
        array = c_float * 6()
        self.lib.lib.asphodel_get_accel_self_test_limits(channel_info, array)
    # WARNING: Decompyle incomplete

    enable_accel_self_test = (lambda self, channel_index, enable = (True,): pass# WARNING: Decompyle incomplete
)()
    
    def check_accel_self_test(self, channel_info, disabled, enabled):
        '''
        Return passed
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_channel_decoder(self, index, bit_offset):
        channel_info = self.get_channel(index)
        return self.lib.create_channel_decoder(channel_info, bit_offset)

    
    def get_stream_decoder(self, index, bit_offset):
        stream_info = self.get_stream(index)
        channel_info_list = []
        indexes = stream_info.channel_index_list[0:stream_info.channel_count]
        for ch_index in indexes:
            channel_info_list.append(self.get_channel(ch_index))
            return self.lib.create_stream_decoder(stream_info, channel_info_list, bit_offset)

    
    def get_device_decoder(self):
        (stream_count, filler_bits, id_bits) = self.get_stream_count()
        info_list = []
        for i in range(stream_count):
            stream_struct = self.get_stream(i)
            channel_info_list = []
            channels = stream_struct.channel_count
            indexes = stream_struct.channel_index_list[0:channels]
            for ch_index in indexes:
                channel_info_list.append(self.get_channel(ch_index))
                info_list.append((i, stream_struct, channel_info_list))
                return self.lib.create_device_decoder(info_list, filler_bits, id_bits)

    
    def get_streaming_counts(self, response_time, buffer_time, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def get_channel_unit_formatter(self, index, use_metric):
        info = self.get_channel_info(index)
        return self.lib.create_unit_formatter(info.unit_type, info.minimum, info.maximum, info.resolution, use_metric)

    
    def get_ctrl_var_unit_formatter(self, index, use_metric):
        info = self.get_ctrl_var_info(index)
        (unit_type, minimum, maximum, scale, offset) = info
        return self.lib.create_unit_formatter(unit_type, minimum * scale + offset, maximum * scale + offset, scale, use_metric)

    
    def get_setting(self, index):
        info = self.get_setting_info(index)
        name = self.get_setting_name(index)
        default = self.get_setting_default(index)
        name_bytes = name.encode('UTF-8')
        info.name = name_bytes
        info.name_length = len(name_bytes)
    # WARNING: Decompyle incomplete



def recreate_channel_decoder(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


class AsphodelNativeChannelDecoder:
    
    def __init__(self, lib, decoder, channel_info, stream_decoder = (None,)):
        self.lib = lib
        self._decoder = decoder
        self.channel_info = channel_info
        self.stream_decoder = stream_decoder
        self.auto_free = False if stream_decoder else True
        self.channel_bit_offset = self._decoder.channel_bit_offset
        self.samples = self._decoder.samples
        
        try:
            self.channel_name = self._decoder.channel_name.decode('UTF-8')
        except UnicodeDecodeError:
            self.channel_name = '<ERROR>'

        self.subchannels = self._decoder.subchannels
        self.subchannel_names = []
        for i in range(self.subchannels):
            s = self._decoder.subchannel_names[i].decode('UTF-8')
            self.subchannel_names.append(s)
            except UnicodeDecodeError:
                self.subchannel_names.append('<ERROR>')
                continue
            return None

    
    def __del__(self):
        if self.auto_free:
            self.free()
            return None

    
    def __reduce__(self):
        if self._decoder.callback:
            raise Exception('Cannot reduce channel decoder with callback')
        args = (self.channel_info, self._decoder.channel_bit_offset)
        return (recreate_channel_decoder, args)

    
    def free(self):
        if self._decoder:
            self._decoder.free_decoder(self._decoder)
            self._decoder = None
            return None

    
    def reset(self):
        self._decoder.reset(self._decoder)

    
    def decode(self, counter, buffer):
        b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
        self._decoder.decode(self._decoder, counter, cast(b, POINTER(c_uint8)))

    
    def set_conversion_factor(self, scale, offset):
        self._decoder.set_conversion_factor(self._decoder, scale, offset)

    
    def set_callback(self, cb):
        pass
    # WARNING: Decompyle incomplete



def recreate_stream_decoder(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


class AsphodelNativeStreamDecoder:
    
    def __init__(self, lib, decoder, stream_info, channel_info_list, bit_offset, device_decoder = (None,)):
        self.lib = lib
        self._decoder = decoder
        self.stream_info = stream_info
        self._channel_info_list = channel_info_list[:]
        self.bit_offset = bit_offset
        self.device_decoder = device_decoder
        self.auto_free = False if device_decoder else True
        self.counter_byte_offset = self._decoder.counter_byte_offset
        self.used_bits = self._decoder.used_bits
        self.channels = self._decoder.channels
        self.decoders = []
        for i in range(self.channels):
            d = AsphodelNativeChannelDecoder(self.lib, self._decoder.decoders[i].contents, channel_info_list[i], self)
            self.decoders.append(d)
            return None

    
    def __del__(self):
        if self.auto_free:
            self.free()
            return None

    
    def __reduce__(self):
        if self._decoder.lost_packet_callback:
            raise Exception('Cannot reduce stream decoder with callback')
        for d in self.decoders:
            if d._decoder.callback:
                raise Exception('Cannot reduce channel decoder with callback')
            args = (self.stream_info, self._channel_info_list, self.bit_offset)
            return (recreate_stream_decoder, args)

    
    def free(self):
        if self._decoder:
            self._decoder.free_decoder(self._decoder)
            self._decoder = None
            return None

    
    def reset(self):
        self._decoder.reset(self._decoder)

    last_count = (lambda self: self._decoder.last_count)()
    
    def decode(self, buffer):
        b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
        self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))

    
    def set_lost_packet_callback(self, cb):
        pass
    # WARNING: Decompyle incomplete



def recreate_device_decoder(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


class AsphodelNativeDeviceDecoder:
    
    def __init__(self, lib, decoder, info_list, filler_bits, id_bits):
        self.lib = lib
        self._decoder = decoder
        self._info_list = info_list
        self._filler_bits = filler_bits
        self._id_bits = id_bits
        bit_offset = self._filler_bits + self._id_bits
        self.id_byte_offset = self._decoder.id_byte_offset
        self.used_bits = self._decoder.used_bits
        self.streams = self._decoder.streams
        self.stream_ids = self._decoder.stream_ids[0:self.streams]
        self.decoders = []
        for i in range(self.streams):
            d = AsphodelNativeStreamDecoder(self.lib, self._decoder.decoders[i].contents, info_list[i][1], info_list[i][2], bit_offset, self)
            self.decoders.append(d)
            return None

    
    def __del__(self):
        self.free()

    
    def __reduce__(self):
        if self._decoder.unknown_id_callback:
            raise Exception('Cannot reduce device decoder with callback')
        for d in self.decoders:
            if d._decoder.lost_packet_callback:
                raise Exception('Cannot reduce stream decoder with callback')
            for cd in d.decoders:
                if cd._decoder.callback:
                    raise Exception('Cannot reduce channel decoder with callback')
                args = (self._info_list, self._filler_bits, self._id_bits)
                return (recreate_device_decoder, args)

    
    def free(self):
        if self._decoder:
            self._decoder.free_decoder(self._decoder)
            self._decoder = None
            return None

    
    def reset(self):
        self._decoder.reset(self._decoder)

    
    def decode(self, buffer):
        b = (c_uint8 * len(buffer)).from_buffer_copy(buffer)
        self._decoder.decode(self._decoder, cast(b, POINTER(c_uint8)))

    
    def set_unknown_id_callback(self, cb):
        pass
    # WARNING: Decompyle incomplete



def recreate_unit_formatter(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def recreate_custom_unit_formatter(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete


class AsphodelNativeUnitFormatter:
    
    def __init__(self, lib, formatter, recreate):
        self.lib = lib
        self.formatter = formatter
        self._recreate = recreate
        self.unit_ascii = self.formatter.unit_ascii.decode('ascii')
        self.unit_utf8 = self.formatter.unit_utf8.decode('UTF-8')
        self.unit_html = self.formatter.unit_html.decode('ascii')
        self.conversion_scale = self.formatter.conversion_scale
        self.conversion_offset = self.formatter.conversion_offset

    
    def __del__(self):
        self.free()

    
    def __reduce__(self):
        return self._recreate

    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            self_tuple = (self.unit_ascii, self.unit_utf8, self.unit_html, self.conversion_scale, self.conversion_offset)
            other_tuple = (other.unit_ascii, other.unit_utf8, other.unit_html, other.conversion_scale, other.conversion_offset)
            return self_tuple == other_tuple

    
    def free(self):
        if self.formatter:
            self.formatter.free(self.formatter)
            self.formatter = None
            return None

    
    def format_bare(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_bare(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')

    
    def format_ascii(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_ascii(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')

    
    def format_utf8(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_utf8(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('UTF-8')

    
    def format_html(self, value):
        buffer = create_string_buffer(256)
        self.formatter.format_html(self.formatter, buffer, len(buffer), value)
        return buffer.value.decode('ascii')



def format_nvm_data(data, size = (16,)):
    
    def to_ascii(c):
        c = chr(c)
        if c in string.whitespace:
            return ' '
        if None in string.printable:
            return c

    output = []
    for i in range(0, len(data), size):
        data_chunk = data[i:min(len(data), i + size)]
        hex_values = ' '.join(map('{:02x}'.format, data_chunk))
        filler = '   ' * (size - len(data_chunk))
        ascii_values = ''.join(map(to_ascii, data_chunk))
        output.append(hex_values + filler + ' ' + ascii_values)
        return output


def find_devices():
    usb_devices = find_usb_devices()
    tcp_devices = find_tcp_devices()
    return usb_devices + tcp_devices


def find_device_by_serial(serial = None):
    for device in nativelib.find_tcp_devices():
        adv = device.tcp_get_advertisement()
        if adv.serial_number == serial:
            
            return None, device
        for None in nativelib.find_usb_devices():
            if device.get_serial_number() == serial:
                device.close()
                
                return None, device
            except AsphodelError:
                device.close()
                continue
            device.close()
            device.close()
            return None

nativelib = AsphodelNative()
asphodel_error_name = nativelib.lib.asphodel_error_name
protocol_version = nativelib.protocol_version
protocol_version_string = nativelib.protocol_version_string
build_info = nativelib.build_info
build_date = nativelib.build_date
usb_backend_version = nativelib.usb_backend_version
find_usb_devices = nativelib.find_usb_devices
find_tcp_devices = nativelib.find_tcp_devices
create_tcp_device = nativelib.create_tcp_device
unit_type_names = nativelib.unit_type_names
for type_index, type_name in enumerate(unit_type_names):
    globals()[type_name] = type_index
    channel_type_names = nativelib.channel_type_names
    for type_index, type_name in enumerate(channel_type_names):
        globals()[type_name] = type_index
        setting_type_names = nativelib.setting_type_names
        for type_index, type_name in enumerate(setting_type_names):
            globals()[type_name] = type_index
            format_value_ascii = nativelib.format_value_ascii
            format_value_utf8 = nativelib.format_value_utf8
            format_value_html = nativelib.format_value_html
            return None
