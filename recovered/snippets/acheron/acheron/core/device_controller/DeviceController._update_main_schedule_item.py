# Source Generated with Decompyle++
# File: tmpa21lc3xj.marshal (Python 3.11)

if MANUAL_CONTROL not in self.parties:
    self.schedule.clear_partition(self.main_schedule_id)
    return None
if None.disable_streaming:
    active_streams = frozenset()
else:
    active_streams = self.desired_streams
schedule_item = ScheduleItem(id = self.main_schedule_id, active_streams = active_streams, start_time = None, collection_time = None, stop_time = None, duration = None, failure_time = None, output_config = None if self.disable_archiving else True)
self.schedule.add_item(self.main_schedule_id, schedule_item)
