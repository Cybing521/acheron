# Source Generated with Decompyle++
# File: tmp8jt6nwuw.marshal (Python 3.11)

ids = set()
for partition in partitions:
    old_schedule_items = self.schedule_items.pop(partition)
except KeyError:
    continue
for schedule_item in old_schedule_items.values():
    ids.add(schedule_item.id)
    if ids:
        self.deleted_items.emit(ids)
        return None
    return None
