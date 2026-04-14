# Source Generated with Decompyle++
# File: tmp89zfob13.marshal (Python 3.11)

if self.output_config.roll_over_interval:
    interval = self.output_config.roll_over_interval.total_seconds()
    seconds = (dt.hour * 60 + dt.minute) * 60 + dt.second
    partial = datetime.timedelta(seconds = seconds % interval, microseconds = dt.microsecond)
    boundary = (dt - partial) + datetime.timedelta(seconds = interval)
    return boundary
return None.datetime.max
