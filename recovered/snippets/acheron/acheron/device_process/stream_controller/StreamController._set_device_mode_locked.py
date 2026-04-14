# Source Generated with Decompyle++
# File: tmp8t6txaf9.marshal (Python 3.11)


try:
    self.device.set_device_mode(mode)
    success = True
except asphodel.AsphodelError:
    success = False

self.status_pipe_lock
self.status_pipe.send((StreamStatus.DEVICE_MODE_UPDATE, success, mode))
None(None, None)
return None
with None:
    if not None:
        pass
