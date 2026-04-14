# Source Generated with Decompyle++
# File: tmp2dwsa19h.marshal (Python 3.11)

self.lock
controller = self.controllers.get(serial_numbers)
if not controller:
    logger.debug('Creating device controller for %s', serial_numbers)
    schedule = self.main_schedule.get_schedule(serial_numbers)
    controller = DeviceController(self, serial_numbers[-1], self.preferences, self.diskcache, schedule, self.calc_process_name, self.disable_streaming, self.disable_archiving, parent_controller, parties)
    controller.rf_power_changed.connect(self.rf_power_changed_cb)
    controller.rf_power_needed.connect(self.rf_power_needed_cb)
    controller.active_triggers_changed.connect(self.active_triggers_changed_cb)
    controller.disconnected_signal.connect(self.active_scan_database.controller_disconnected)
    controller.remote_connecting.connect(self.active_scan_database.controller_remote_connecting)
    controller.scan_data.connect(self.active_scan_database.controller_scans)
    controller.active_scan_data.connect(self.active_scan_database.active_scan_finished)
    self.controllers[serial_numbers] = controller
    self.manually_disconnected.discard(serial_numbers)
    created = True
else:
    created = False
    if parties:
        controller.register_parties(parties)
if proxy:
    controller.set_proxy(proxy)
    self.disconnected_controllers.discard(controller)
elif created:
    self.disconnected_controllers.add(controller)
if reconnect_info:
    self.controller_info[controller] = reconnect_info
None(None, None)
