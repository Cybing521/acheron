# Source Generated with Decompyle++
# File: tmpkg0qfe_k.marshal (Python 3.11)

import bisect
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
import logging
import threading
from typing import Any, Iterable, Literal, Optional, Union
import asphodel.device_config as asphodel
from asphodel.device_info import DeviceInfo
logger = logging.getLogger(__name__)
min_dt = datetime.min.replace(tzinfo = timezone.utc)
OutputConfig = <NODE:12>()
ScheduleItem = <NODE:12>()

def get_compatible_set(items = None, device_info = dataclass(frozen = True), nvm = dataclass(eq = True, frozen = True)):
    items = sorted(items, key = ScheduleItem.priority_key)
    best_nvm = nvm
    current_items = set()
    remote = None
# WARNING: Decompyle incomplete


class Schedule:
    
    def __init__(self = None, schedule_items = None, active_triggers = None):
        self.active_triggers = active_triggers
        self.lock = threading.Lock()
        self.schedule_items = sorted(schedule_items)

    
    def __len__(self = None):
        self.lock
        None(None, None)
        return 
        with None:
            if not None, len(self.schedule_items):
                pass

    
    def remote_len(self = None, remote = None):
        total = 0
        self.lock
        for schedule_item in self.schedule_items:
            if schedule_item.remote_sn == remote:
                total += 1
            None(None, None)
        with None:
            if not None:
                pass
        return total

    
    def _delete_item_id(self = None, item_id = None):
        for i, check_item in enumerate(self.schedule_items):
            if check_item.id == item_id:
                del self.schedule_items[i]
                return None
            return None

    
    def delete_item_id(self = None, item_id = None):
        self.lock
        self._delete_item_id(item_id)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _update_item(self = None, item = None):
        self._delete_item_id(item.id)
        bisect.insort(self.schedule_items, item)

    
    def update_item(self = None, item = None):
        self.lock
        self._update_item(item)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def update_items(self = None, schedule_items = None):
        self.lock
        for item in schedule_items:
            bisect.insort(self.schedule_items, item)
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def get_ready_items(self = None, remote = None):
        self.lock
        ready = set()
        now = None
    # WARNING: Decompyle incomplete

    
    def set_active_triggers(self = None, active_triggers = None):
        self.lock
        self.active_triggers = active_triggers
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get_expired_items(self = None):
        expired = set()
        self.lock
        now = datetime.now(timezone.utc)
        stop_time = now - timedelta(seconds = 10)
        for item in self.schedule_items:
            if item.failure_time and item.failure_time < now:
                expired.add(item)
                continue
            if item.stop_time and item.stop_time < stop_time:
                expired.add(item)
            None(None, None)
        with None:
            if not None:
                pass
        return expired



class RemoteSchedule:
    
    def __init__(self, schedule = None, remote_sn = None, remote_bootloader = None, schedule_items = ('schedule', Schedule, 'remote_sn', int, 'remote_bootloader', bool, 'schedule_items', Iterable[ScheduleItem])):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self = None):
        return self.schedule.remote_len(self.remote_sn)

    
    def delete_item_id(self = None, item_id = None):
        self.schedule.delete_item_id(item_id)

    
    def _convert_item_to_remote(self = None, item = None):
        return replace(item, remote_sn = self.remote_sn, remote_bootloader = self.remote_bootloader)

    
    def _convert_item_from_remote(self = None, item = None):
        return replace(item, remote_sn = None)

    
    def update_item(self = None, item = None):
        self.schedule.update_item(self._convert_item_to_remote(item))

    
    def get_ready_items(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_active_triggers(self = None, active_triggers = None):
        pass

    
    def get_expired_items(self = None):
        return set()


