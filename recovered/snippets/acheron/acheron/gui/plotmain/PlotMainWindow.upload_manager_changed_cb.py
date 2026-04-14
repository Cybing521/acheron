# Source Generated with Decompyle++
# File: tmp0c1ba478.marshal (Python 3.11)

if upload_manager:
    self.uploadRateLabel.setVisible(True)
    self.uploadProgress.setVisible(False)
    self.uploadNameLabel.setVisible(True)
    self.uploadRateLabel.setText('0.0 kB/s')
    self.uploadNameLabel.setText('Waiting for file to upload')
    upload_manager.rate_status.connect(self.rate_status_cb)
    upload_manager.upload_status.connect(self.upload_status_cb)
    upload_manager.error.connect(self.upload_manager_error)
    return None
None.uploadRateLabel.setVisible(False)
self.uploadProgress.setVisible(False)
self.uploadNameLabel.setVisible(False)
