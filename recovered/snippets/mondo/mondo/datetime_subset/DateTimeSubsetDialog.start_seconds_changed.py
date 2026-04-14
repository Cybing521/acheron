# Source Generated with Decompyle++
# File: tmp8vr9jasj.marshal (Python 3.11)

new_start = self.start_qdt.addSecs(self.startSeconds.value())
if new_start > self.endDateTime.dateTime():
    self.endDateTime.setDateTime(new_start)
self.startDateTime.setDateTime(new_start)
