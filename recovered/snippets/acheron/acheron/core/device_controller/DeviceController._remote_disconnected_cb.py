# Source Generated with Decompyle++
# File: tmpw2o8o4tm.marshal (Python 3.11)

if self.remote_controller:
    self.remote_controller.release_party(REMOTE_CONTROL)
    self.remote_connected.emit(False)
    self.remote_controller = None
self.remote_target_connected.emit(False)
