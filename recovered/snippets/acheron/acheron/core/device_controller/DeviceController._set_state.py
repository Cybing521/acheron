# Source Generated with Decompyle++
# File: tmp3avt_5rb.marshal (Python 3.11)

if self.state == state:
    return None
self.state = None
self.state_changed_signal.emit(state, message)
if state == DeviceControllerState.DISCONNECTED:
    self.logger.info('Disconnected')
    self.disconnected_signal.emit(self)
    return None
