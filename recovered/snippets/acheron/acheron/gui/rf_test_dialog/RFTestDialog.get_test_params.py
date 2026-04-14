# Source Generated with Decompyle++
# File: tmpm3xbcubo.marshal (Python 3.11)

if self.txCarrierRadioButton.isChecked():
    mode = 0
elif self.rxCarrierRadioButton.isChecked():
    mode = 1
else:
    mode = 2
if self.fixedRadioButton.isChecked():
    return RFFixedTestParams(channel = self.fixedChannel.value(), duration = self.fixedDuration.value(), mode = mode)
return None(start = self.startChannel.value(), stop = self.stopChannel.value(), hop_interval = self.hopInterval.value(), hop_count = self.hopCount.value(), mode = mode)
