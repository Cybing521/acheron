# Source Generated with Decompyle++
# File: tmpi179jvgu.marshal (Python 3.11)

if not self.finished.wait(timeout = 60):
    self.lock
    start = self.last_cron_stop
    stop = datetime.now(timezone.utc) + self.timedelta
    self.last_cron_stop = stop
    self._single_pass(start, stop)
    updated = bool(self.cron_deque)
    None(None, None)
else:
    with None:
        if not None:
            pass
if updated:
    self._cron_schedule_updated.emit()
# WARNING: Decompyle incomplete
