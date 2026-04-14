# Source Generated with Decompyle++
# File: tmpqng7bga0.marshal (Python 3.11)


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

