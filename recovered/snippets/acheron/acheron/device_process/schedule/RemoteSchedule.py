# Source Generated with Decompyle++
# File: tmpzkanaszc.marshal (Python 3.11)


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

