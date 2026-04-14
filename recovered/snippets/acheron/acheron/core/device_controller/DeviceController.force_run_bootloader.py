# Source Generated with Decompyle++
# File: tmpc1ynltnh.marshal (Python 3.11)

if self.calc_process:
    message = self.tr('Connecting to bootloader...')
    self.logger.info(message)
    self._set_state(DeviceControllerState.CONNECTING, message)
    self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RUN_BOOTLOADER,))
    return None
