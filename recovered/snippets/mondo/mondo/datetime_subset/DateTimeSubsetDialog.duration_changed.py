# Source Generated with Decompyle++
# File: tmpuc1pn30j.marshal (Python 3.11)

duration = self.duration.value()
current_start = cast(datetime.datetime, self.startDateTime.dateTime().toPython())
end_py = cast(datetime.datetime, self.end_qdt.toPython())
headroom = int((end_py - current_start).total_seconds())
if duration <= headroom:
    self.endSeconds.setValue(duration - headroom)
    return None
None.endDateTime.setDateTime(self.end_qdt)
self.startDateTime.setDateTime(self.end_qdt.addSecs(-duration))
