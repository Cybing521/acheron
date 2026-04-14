# Source Generated with Decompyle++
# File: tmp83dn6n3z.marshal (Python 3.11)

if status == RFPowerStatus.NOT_SUPPORTED:
    self.enableButton.setEnabled(False)
    self.disableButton.setEnabled(False)
    return None
if None == RFPowerStatus.ENABLED:
    self.enableButton.setEnabled(False)
    self.disableButton.setEnabled(True)
    return None
None.enableButton.setEnabled(True)
self.disableButton.setEnabled(False)
