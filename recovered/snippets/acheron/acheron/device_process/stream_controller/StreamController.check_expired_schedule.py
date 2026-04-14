# Source Generated with Decompyle++
# File: tmpavkk98vf.marshal (Python 3.11)

expired_items = self.schedule.get_expired_items()
if expired_items:
    for item in expired_items:
        self.writer_stopped(item.id, False)
    return True
