# Source Generated with Decompyle++
# File: tmp44ttgogd.marshal (Python 3.11)

if self.datetime_in_range(self.startDateTime.dateTime()):
    if self.endDateTime.dateTime() <= self.startDateTime.dateTime():
        self.endDateTime.setDateTime(self.startDateTime.dateTime())
        self.startDateTime.setDateTime(self.startDateTime.dateTime())
        return None
    return None
None.startDateTime.setDateTime(self.start_qdt)
