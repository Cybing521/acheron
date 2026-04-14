# Source Generated with Decompyle++
# File: tmpauky4xqn.marshal (Python 3.11)

start_qdt = self.startDateTime.dateTime()
end_qdt = self.endDateTime.dateTime()
if start_qdt < self.start_qdt:
    start_py = cast(datetime.datetime, self.start_qdt.toPython())
elif self.end_qdt < start_qdt:
    start_py = cast(datetime.datetime, self.end_qdt.toPython())
else:
    start_py = cast(datetime.datetime, start_qdt.toPython())
if end_qdt < self.start_qdt:
    end_py = cast(datetime.datetime, self.start_qdt.toPython())
elif self.end_qdt < end_qdt:
    end_py = cast(datetime.datetime, self.end_qdt.toPython())
else:
    end_py = cast(datetime.datetime, end_qdt.toPython())
if end_py < start_py:
    if moving_start:
        end_py = start_py
    else:
        start_py = end_py
start_seconds = (start_py - cast(datetime.datetime, self.start_qdt.toPython())).total_seconds()
self.startSeconds.setValue(int(start_seconds))
end_seconds = (end_py - cast(datetime.datetime, self.end_qdt.toPython())).total_seconds()
self.endSeconds.setValue(int(end_seconds))
self.duration.setValue(int((end_py - start_py).total_seconds()))
