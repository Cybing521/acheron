# Source Generated with Decompyle++
# File: tmp14ddscqi.marshal (Python 3.11)

self.statusLabel.setText(message)
if state == DeviceControllerState.DISCONNECTED:
    self.statusProgressBar.setVisible(False)
    self.stackedWidget.setCurrentIndex(0)
    self.plotmain.set_tab_disconnected(self)
    self.disable_interaction()
    return None
if None == DeviceControllerState.CONNECTING:
    self.stackedWidget.setCurrentIndex(0)
    self.plotmain.set_tab_disconnected(self)
    self.disable_interaction()
    self.statusProgressBar.setMinimum(0)
    self.statusProgressBar.setMaximum(0)
    self.statusProgressBar.setValue(0)
    self.statusProgressBar.setVisible(True)
    return None
if None == DeviceControllerState.STREAMING_STARTING:
    self.statusProgressBar.setValue(self.statusProgressBar.maximum())
    if self.controller.device_info:
        manual_control = self.controller.get_manual_control()
        self.device_info_updated(self.controller.device_info, manual_control)
    if not self.controller.active_streams:
        if self.buffering:
            self.bufferingLabel.setVisible(False)
            self.buffering = False
        self.noChannelsTimeLabel.setVisible(True)
        self.noChannelsFreqLabel.setVisible(True)
        return None
    None.noChannelsTimeLabel.setVisible(False)
    self.noChannelsFreqLabel.setVisible(False)
    return None
if None == DeviceControllerState.RUNNING:
    self.stackedWidget.setCurrentIndex(1)
    self.plotmain.set_tab_connected(self)
    self.statusProgressBar.setVisible(False)
    return None
if None == DeviceControllerState.RUNNING_FUNCTION:
    return None
