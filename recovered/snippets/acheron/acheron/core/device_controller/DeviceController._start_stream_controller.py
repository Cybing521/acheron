# Source Generated with Decompyle++
# File: tmpptiv6qi9.marshal (Python 3.11)

self.device_info = None
if not self.proxy:
    return None
self.streaming = None
self._set_state(DeviceControllerState.CONNECTING, self.tr('Loading device information...'))
(self.stream_settings, self.calc_settings) = self._get_settings()
if self.calc_process:
    self.calc_process.stop()
    self.dispatcher.register_old_calc_process(self.calc_process)
    self.calc_process = None
self._update_schedule_items()
schedule_items = self.schedule.get_items()
self._update_alert_triggers()
self.triggers = self._get_triggers()
self.calc_process = CalcProcess(self.calc_process_name, self.serial_number, self.is_shown, self.calc_settings, self.triggers)
self.proxy.disconnected.connect(self.calc_process.close)
self.calc_process.processing_start.connect(self._processing_start_cb)
self.calc_process.processing_stop.connect(self._processing_stop_cb)
self.calc_process.status_received.connect(self._status_cb)
self.calc_process.channel_update.connect(self.channel_update)
self.calc_process.plot_update.connect(self.plot_update)
self.calc_process.fft_update.connect(self.fft_update)
self.calc_process.lost_packet_update.connect(self.lost_packet_update)
self.calc_process.unknown_id.connect(self._unknown_id_cb)
self.calc_process.active_triggers_changed.connect(self._active_triggers_changed_cb)
(ctrl_pipe, packet_pipe, status_pipe) = self.calc_process.get_pipes()
self.proxy.send_job(self.start_stream_controller_op, self.stream_settings, schedule_items, self.main_schedule_id, self.dispatcher.active_triggers, self.diskcache, ctrl_pipe, packet_pipe, status_pipe)
