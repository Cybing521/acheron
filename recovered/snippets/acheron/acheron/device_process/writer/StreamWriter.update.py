# Source Generated with Decompyle++
# File: tmpczj7upwa.marshal (Python 3.11)

if self.schedule_item == schedule_item:
    return None
if None.output_config != schedule_item.output_config:
    raise ValueError("Can't update output configuration while running")
self.schedule_item = schedule_item
self.collection_time_target = schedule_item.collection_time
self.calc_stop_time_target()
