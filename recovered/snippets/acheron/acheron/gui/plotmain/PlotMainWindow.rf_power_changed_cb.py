# Source Generated with Decompyle++
# File: tmpvbmwuwzl.marshal (Python 3.11)

disabled = max(0, total - enabled)
enable_text = self.tr('Enable RF Power ({})').format(disabled)
self.actionEnableRFPower.setText(enable_text)
self.actionEnableRFPower.setEnabled(disabled > 0)
disable_text = self.tr('Disable RF Power ({})').format(enabled)
self.actionDisableRFPower.setText(disable_text)
self.actionDisableRFPower.setEnabled(enabled > 0)
