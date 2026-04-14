# Source Generated with Decompyle++
# File: tmpfa8am2vj.marshal (Python 3.11)

if not self.proxy:
    return None
subproxy = None(DeviceProxy, self.proxy).create_subproxy(create_remote, serial_number_int, bootloader)
parties = {
    REMOTE_CONTROL}
if self.remote_target_serial == serial_number_int:
    parties.add(MANUAL_CONTROL)
self.remote_controller = self.dispatcher.create_remote(self, serial_number_str, subproxy, parties)
self.remote_connected.emit(True)
if self.remote_target_serial == serial_number_int:
    self.remote_target_controller = self.remote_controller
    self.remote_target_controller.manual_control_changed.connect(self._remote_target_manual_control_changed_cb)
    self.remote_target_connected.emit(True)
    if not self.remote_target_streaming:
        self.remote_target_controller.set_active_streams(frozenset())
        return None
    return None
if None.remote_target_controller:
    self.remote_target_controller.release_party(REMOTE_CONTROL)
    self.remote_target_controller.manual_control_changed.disconnect(self._remote_target_manual_control_changed_cb)
    self.remote_target_connected.emit(False)
    self.remote_target_controller = None
    return None
