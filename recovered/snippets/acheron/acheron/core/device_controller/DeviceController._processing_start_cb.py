# Source Generated with Decompyle++
# File: tmp86tgs4mf.marshal (Python 3.11)

self.device_info = device_info
self.channel_info = channel_info
self.active_streams = active_streams
if device_info.user_tag_1:
    self.display_name = device_info.user_tag_1
else:
    self.display_name = self.serial_number
self._set_state(DeviceControllerState.STREAMING_STARTING, self.tr('Starting streaming...'))
connected_message = self.tr('Connected')
self._set_state(DeviceControllerState.RUNNING, connected_message)
self.logger.info(connected_message)
self.start_connectivity()
rf_power_status = self._start_rf_power_handling()
if rf_power_status == RFPowerStatus.ENABLED:
    self.logger.info('RF power already running')
# WARNING: Decompyle incomplete
