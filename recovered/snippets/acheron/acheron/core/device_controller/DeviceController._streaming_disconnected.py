# Source Generated with Decompyle++
# File: tmpppvhh4ne.marshal (Python 3.11)

self.dispatcher.connectivity_manager.stop_device(self.serial_number)
self.active_triggers_changed.emit(self, frozenset(), self.trigger_names)
self.last_emitted_active_triggers = frozenset()
self._set_state(DeviceControllerState.DISCONNECTED, message)
self._stop_rf_power_handling()
self.rf_power_needed.emit(self, False)
self._set_schedule_count(0)
