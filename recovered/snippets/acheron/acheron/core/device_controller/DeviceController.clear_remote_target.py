# Source Generated with Decompyle++
# File: tmp1ha8r0y6.marshal (Python 3.11)

self.remote_target_serial = None
if self.remote_target_controller:
    self.remote_target_controller.manual_control_changed.disconnect(self._remote_target_manual_control_changed_cb)
    self.remote_target_controller.release_party(MANUAL_CONTROL)
    self.remote_target_connected.emit(False)
    self.remote_target_controller = None
self._update_remote_schedule_item()
self.remote_target_changed.emit(None, False, False)
