# Source Generated with Decompyle++
# File: tmp0lepf500.marshal (Python 3.11)

if addressof(new_device) == addressof(self.device):
    return None
None.close()
if self.device:
    self.device.free_device(self.device)
self.device = new_device
if reopen:
    self.open()
# WARNING: Decompyle incomplete
