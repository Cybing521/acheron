# Source Generated with Decompyle++
# File: tmp48fh343h.marshal (Python 3.11)

lost_count_too_old = 0
now = datetime.datetime.now(datetime.timezone.utc)
twenty_secs_ago = now - datetime.timedelta(seconds = 20)
if len(self.lost_packet_deque):
    (lost_dt, lost) = self.lost_packet_deque[0]
    if lost_dt < twenty_secs_ago:
        lost_count_too_old += lost
        self.lost_packet_deque.popleft()
    
# WARNING: Decompyle incomplete
