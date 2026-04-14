# Source Generated with Decompyle++
# File: tmp9tq1q529.marshal (Python 3.11)

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
