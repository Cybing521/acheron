# Source Generated with Decompyle++
# File: tmp_qyklz7e.marshal (Python 3.11)


try:
    del self.active_scan_ongoing[controller]
except KeyError:
    pass

if active_scan:
    self.active_scans[remote] = active_scan
    self.active_scan_ready.emit(remote, active_scan)
    return None
