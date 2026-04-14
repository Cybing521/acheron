# Source Generated with Decompyle++
# File: tmpz2b1t_ds.marshal (Python 3.11)

rate_average_period = self.rate_average_period
now = datetime.datetime.now(tz = datetime.timezone.utc)
bytes_too_old = 0
cutoff_time = now - datetime.timedelta(seconds = rate_average_period)
if len(self.rate_deque):
    (sent_dt, sent_bytes) = self.rate_deque[0]
    if sent_dt < cutoff_time:
        bytes_too_old += sent_bytes
        self.rate_deque.popleft()
    
# WARNING: Decompyle incomplete
