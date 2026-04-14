# Source Generated with Decompyle++
# File: tmplr804gg1.marshal (Python 3.11)

message_type = message[0]
if message_type == StreamControl.CHANGE_SETTINGS:
    new_settings = message[1]
    return self.update_settings(new_settings)
if None == StreamControl.UPDATE_SCHEDULE_ITEM:
    item = message[1]
    self.schedule.update_item(item)
    if self.parent_controller:
        self.parent_controller.schedule_changed()
    if self.subcontroller:
        self.subcontroller.schedule_changed()
    elif message_type == StreamControl.DELETE_SCHEDULE_IDS:
        item_ids = message[1]
        for item_id in item_ids:
            self.schedule.delete_item_id(item_id)
            if self.parent_controller:
                self.parent_controller.schedule_changed()
        if self.subcontroller:
            self.subcontroller.schedule_changed()
        elif message_type == StreamControl.SET_RGB:
            index = message[1]
            values = message[2]
            self.device_lock
            self.rgb_manager.set_rgb_locked(index, values)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
    elif message_type == StreamControl.GET_RGB_STATE:
        self.status_pipe_lock
        for index, values in enumerate(device_info.rgb_settings):
            self.status_pipe.send((StreamStatus.RGB_UPDATE, index, values))
            None(None, None)
        with None:
            if not None:
                pass
    elif message_type == StreamControl.SET_LED:
        index = message[1]
        value = message[2]
        self.device_lock
        self.device.set_led_value(index, value)
        None(None, None)
    else:
        with None:
            if not None:
                pass
elif message_type == StreamControl.SET_CTRL_VAR:
    index = message[1]
    value = message[2]
    self.device_lock
    self.device.set_ctrl_var(index, value)
    None(None, None)
else:
    with None:
        if not None:
            pass
if message_type == StreamControl.SET_DEVICE_MODE:
    mode = message[1]
    self.device_lock
    self._set_device_mode_locked(mode)
    None(None, None)
else:
    with None:
        if not None:
            pass
if message_type == StreamControl.SET_RF_POWER:
    enable = message[1]
    self.device_lock
    self.device.enable_rf_power(enable)
    None(None, None)
else:
    with None:
        if not None:
            pass
if message_type == StreamControl.WRITE_NVM:
    desired_nvm = message[1]
    return desired_nvm
if None == StreamControl.FORCE_RESET:
    self.reset_function = self._force_reset_locked
    return True
if None == StreamControl.FORCE_RUN_BOOTLOADER:
    self.reset_function = self._force_run_bootloader_locked
    return True
if None == StreamControl.FORCE_RUN_APPLICATION:
    self.reset_function = self._force_run_app_locked
    return True
if None == StreamControl.DO_BOOTLOADER:
    firmware_data = message[1]
    self.reset_function = functools.partial(self._do_bootloader_locked, firmware_data, device_info.serial_number, device_info)
    return True
if None == StreamControl.DO_HARDWARE_TESTS:
    funcs = message[1]
    run_id = message[2]
    self.hw_tests = (funcs, run_id)
    return True
if None == StreamControl.DO_RF_TEST:
    params = message[1]
    self.rf_test_params = params
    return True
if None == StreamControl.DO_ACTIVE_SCAN:
    self.radio_queue.put(message)
elif message_type == StreamControl.DO_RADIO_FUNCTION:
    self.radio_queue.put(message)
elif message_type == StreamControl.ACTIVE_TRIGGERS_CHANGED:
    active_triggers = message[1]
    self.schedule.set_active_triggers(active_triggers)
return False
