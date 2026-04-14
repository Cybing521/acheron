# Source Generated with Decompyle++
# File: tmpvp1hegjh.marshal (Python 3.11)


try:
    old_schedule_items = self.schedule_items.pop(partition)
except KeyError:
    old_schedule_items = { }

new_schedule_items = schedule_items()
self.schedule_items[partition] = new_schedule_items
ids_to_delete = set(old_schedule_items).difference(new_schedule_items)
if ids_to_delete:
    self.deleted_items.emit(ids_to_delete)
for schedule_item in new_schedule_items.values():
    old_schedule_item = old_schedule_items.get(schedule_item.id)
    if old_schedule_item or old_schedule_item != schedule_item:
        self.updated_item.emit(schedule_item)
    return None
