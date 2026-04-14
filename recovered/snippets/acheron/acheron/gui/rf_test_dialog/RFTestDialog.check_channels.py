# Source Generated with Decompyle++
# File: tmpn09c8xvi.marshal (Python 3.11)

fixed_channel = self.fixedChannel.value()
if fixed_channel % 2 != 0:
    fixed_channel -= 1
    self.fixedChannel.setValue(fixed_channel)
start_channel = self.startChannel.value()
if start_channel % 2 != 0:
    start_channel -= 1
    self.startChannel.setValue(start_channel)
stop_channel = self.stopChannel.value()
if stop_channel % 2 != 0:
    stop_channel -= 1
    self.stopChannel.setValue(stop_channel)
    return None
