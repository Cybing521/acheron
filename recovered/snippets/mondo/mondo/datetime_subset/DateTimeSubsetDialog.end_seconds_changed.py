# Source Generated with Decompyle++
# File: tmp5jcsy94s.marshal (Python 3.11)

new_end = self.end_qdt.addSecs(self.endSeconds.value())
if new_end < self.startDateTime.dateTime():
    self.startDateTime.setDateTime(new_end)
self.endDateTime.setDateTime(new_end)
