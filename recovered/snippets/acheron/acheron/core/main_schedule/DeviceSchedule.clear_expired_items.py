# Source Generated with Decompyle++
# File: tmpxyd6speh.marshal (Python 3.11)

now = datetime.datetime.now(datetime.timezone.utc)
stop_time = now - datetime.timedelta(seconds = 10)
all_expried = set()
for schedule_dict in self.schedule_items.values():
    expired = set()
    for schedule_id, item in schedule_dict.items():
        if item.failure_time and item.failure_time < now:
            expired.add(schedule_id)
            continue
        if item.stop_time and item.stop_time < stop_time:
            expired.add(schedule_id)
        for schedule_id in expired:
            schedule_dict.pop(schedule_id)
            self.finished_item.emit(schedule_id, False)
            all_expried.update(expired)
            if all_expried:
                self.deleted_items.emit(all_expried)
                return None
            return None
