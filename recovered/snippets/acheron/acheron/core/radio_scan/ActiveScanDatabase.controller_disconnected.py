# Source Generated with Decompyle++
# File: tmperbobo9s.marshal (Python 3.11)


try:
    remote = self.controller_remotes.pop(controller)
    self.remote_connecting.emit(remote, None)
except KeyError:
    pass


try:
    del self.active_scan_ongoing[controller]
    return None
except KeyError:
    return None

