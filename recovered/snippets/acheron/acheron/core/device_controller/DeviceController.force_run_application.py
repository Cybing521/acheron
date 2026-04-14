# Source Generated with Decompyle++
# File: tmpho63yh_n.marshal (Python 3.11)

if self.calc_process:
    message = self.tr('Connecting to application...')
    self.logger.info(message)
    self._set_state(DeviceControllerState.CONNECTING, message)
    self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RUN_APPLICATION,))
    return None
