# Source Generated with Decompyle++
# File: tmpxgqs750g.marshal (Python 3.11)

from datetime import datetime, timedelta
from functools import cache
import hashlib
import re
from typing import Any, Optional
from zoneinfo import ZoneInfo
from croniter import croniter
from pydantic import AwareDatetime, BaseModel, field_validator, model_validator, ValidationInfo
from device_process.schedule import ScheduleItem

def DiskSchedule():
    '''DiskSchedule'''
    serial: tuple[(str, ...)] = 'DiskSchedule'
    remote_bootloader: bool = False
    trigger: Optional[str] = None
    needs_rf_power: bool = False
    active_streams: Optional[frozenset[int]] = None
    device_config: frozenset[tuple[(str, Any)]] = frozenset()
    start_time: Optional[AwareDatetime] = None
    stop_time: Optional[AwareDatetime] = None
    duration: Optional[timedelta] = None
    failure_delay: Optional[timedelta] = None
    cron_start: Optional[str] = None
    cron_timezone: Optional[str] = None
    ensure_list = (lambda cls = None, v = field_validator('serial', mode = 'before'), info = classmethod: if isinstance(v, str):
if len(v) > 0:
(v,)raise None('Empty serial number string')if len(v) == 0:
raise ValueError('Empty serial number')v)()()
    _cron_exclusion = (lambda cls = None, data = model_validator(mode = 'before'): pass# WARNING: Decompyle incomplete
)()()
    _has_cron_timezone_with_start = (lambda cls = None, data = model_validator(mode = 'before'): pass# WARNING: Decompyle incomplete
)()()
    _has_failure_delay_with_start = (lambda cls = None, data = model_validator(mode = 'before'): pass# WARNING: Decompyle incomplete
)()()
    _check_timezone = (lambda cls = None, v = field_validator('cron_timezone'), _info = classmethod: pass# WARNING: Decompyle incomplete
)()()
    _cron_valid = (lambda cls = None, v = field_validator('cron_start'), _info = classmethod: if not isinstance(v, str) and croniter.is_valid(v, hash_id = b'validate'):
raise ValueError('Invalid cron string')v)()()
    
    def is_single_item(self = None):
        return self.cron_start is None

    get_base_id = (lambda self = None: json_string = self.model_dump_json()hash_object = hashlib.sha256(json_string.encode())'ds-' + hash_object.hexdigest())()
    _get_remote_sn = (lambda serial = None: if len(serial) < 2:
Nonematches = None.findall('\\d+', serial[-1])int(matches[-1]) if matches else None)()
    
    def convert_single_item(self = None):
        values = self.model_dump()
        values['remote_sn'] = self._get_remote_sn(values['serial'])
        del values['serial']
        del values['cron_start']
        del values['cron_timezone']
        failure_delay = values.pop('failure_delay', None)
        if failure_delay:
            values['failure_time'] = self.start_time + failure_delay
    # WARNING: Decompyle incomplete

    
    def convert_cron(self = None, start_time = None):
        values = self.model_dump()
        values['remote_sn'] = self._get_remote_sn(values['serial'])
        del values['serial']
        del values['cron_start']
        del values['cron_timezone']
        values['start_time'] = start_time
        failure_delay = values.pop('failure_delay', None)
        if failure_delay:
            values['failure_time'] = start_time + failure_delay
        id = self.get_base_id() + ' ' + start_time.isoformat()
    # WARNING: Decompyle incomplete

    
    def get_base_serial(self = None):
        if len(self.serial) >= 2:
            return self.serial[:-1]
        return None.serial


DiskSchedule = <NODE:27>(DiskSchedule, 'DiskSchedule', BaseModel, frozen = True)
