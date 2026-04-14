# Source Generated with Decompyle++
# File: tmpl7xy723w.marshal (Python 3.11)

if self.calc_process:
    message = self.tr('Resetting device...')
    self.logger.info(message)
    self._set_state(DeviceControllerState.CONNECTING, message)
    self.calc_process.send_stream_ctrl_message((StreamControl.FORCE_RESET,))
    return None
