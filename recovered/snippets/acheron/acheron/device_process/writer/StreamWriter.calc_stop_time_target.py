# Source Generated with Decompyle++
# File: tmpcgohnrji.marshal (Python 3.11)

t = None
if self.collection_time_actual and self.schedule_item.duration:
    t = self.collection_time_actual + self.schedule_item.duration
if self.schedule_item.stop_time:
    if t:
        t = min(t, self.schedule_item.stop_time)
    else:
        t = self.schedule_item.stop_time
if self.schedule_item.failure_time:
    if t:
        t = min(t, self.schedule_item.failure_time)
    else:
        t = self.schedule_item.stop_time
self.stop_time_target = t
