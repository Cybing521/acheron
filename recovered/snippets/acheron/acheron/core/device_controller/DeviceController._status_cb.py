# Source Generated with Decompyle++
# File: tmph0oa0fcz.marshal (Python 3.11)

status_type = status[0]
if status_type == StreamStatus.RECONNECTING:
    self._set_state(DeviceControllerState.CONNECTING, self.tr('Reconnecting...'))
    return None
if None == StreamStatus.DEVICE_INFO_START:
    self._set_state(DeviceControllerState.CONNECTING, self.tr('Loading device information...'))
    return None
if None == StreamStatus.DEVICE_INFO_PROGRESS:
    (finished, total, _section_name) = status[1:]
    message = self.tr('Loading device information...')
    self.progress_signal.emit(finished, total, message)
    return None
if None == StreamStatus.WRITE_NVM_PROGRESS:
    return None
if None == StreamStatus.DEVICE_INFO_READY:
    return None
if None == StreamStatus.STREAMING_STARTED:
    return None
if None == StreamStatus.STREAMING_ERROR_TIMEOUT:
    self.logger.warning('Stream Timeout')
    return None
if None == StreamStatus.STREAMING_ERROR_DISCONNECT:
    self.logger.warning('Stream Disconnect')
    return None
if None == StreamStatus.STREAMING_ERROR_OTHER:
    self.logger.warning('Stream Error')
    self._error(self.tr('Stream Error'))
    return None
if None == StreamStatus.BOOTLOADER_PROGRESS:
    (finished, total, status_str) = status[1:]
    self.progress_signal.emit(finished, total, status_str)
    return None
if None == StreamStatus.BOOTLOADER_FINISHED:
    (success, event_data) = status[1:]
    self.dispatcher.event_uploader.firmware_updated(self.serial_number, success, event_data)
    return None
if None == StreamStatus.DISCONNECTED:
    self._error(self.tr('Disconnected'))
    return None
if None == StreamStatus.RGB_UPDATE:
    (index, values) = status[1:]
    if self.device_info or len(self.device_info.rgb_settings) > index:
        self.device_info.rgb_settings[index] = values
        self.rgb_updated.emit(index, values)
        return None
    return None
return None
if status_type == StreamStatus.DEVICE_MODE_UPDATE:
    (success, mode) = status[1:]
    if success:
        if self.device_info:
            self.device_info.device_mode = mode
            return None
        return None
    None.logger.error('Bad device mode {}'.format(mode))
    return None
if None == StreamStatus.STARTED_FILE:
    (file_path, schedule_id, marked_for_upload) = status[1:]
    self.logger.debug('Starting file %s', file_path)
    return None
if None == StreamStatus.FINISHED_FILE:
    (file_path, schedule_id, marked_for_upload) = status[1:]
    self.logger.debug('Finished file %s', file_path)
    if marked_for_upload:
        self.dispatcher.upload_file(file_path)
        return None
    return None
if None == StreamStatus.ONGOING_ITEMS:
    schedule_ids_set = status[1]
    rf_power_needed = status[2]
    schedule_count = status[3]
    self.rf_power_needed.emit(self, rf_power_needed)
    self.ongoing_items.emit(schedule_ids_set)
    self._set_schedule_count(schedule_count)
    return None
if None == StreamStatus.FINISHED_ITEM:
    (schedule_id, success) = status[1:]
    self.schedule.mark_finished(schedule_id, success)
    return None
# WARNING: Decompyle incomplete
