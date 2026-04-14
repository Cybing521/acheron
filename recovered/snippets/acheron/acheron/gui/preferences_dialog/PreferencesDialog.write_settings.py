# Source Generated with Decompyle++
# File: tmpvqfdgtnr.marshal (Python 3.11)

self.preferences.dark_mode = self.darkMode.isChecked()
self.preferences.show_supplies = self.showSupplyChecks.isChecked()
self.preferences.auto_rgb = self.automaticRGBCheckBox.isChecked()
self.preferences.downsample = self.downsampleCheckBox.isChecked()
self.preferences.plot_mean = self.plotMeanCheckBox.isChecked()
self.unitPreferences.write_settings()
self.preferences.base_dir = self.outputLocation.text()
self.preferences.compression_level = self.compressionLevel.value()
self.preferences.modbus_enable = self.runModbusCheckBox.isChecked()
self.preferences.modbus_port = self.modbusPort.value()
self.preferences.upload_enabled = self.enableUpload.isChecked()
self.preferences.s3_bucket = self.s3Bucket.text()
self.preferences.aws_region = self.awsRegion.text()
self.preferences.upload_directory = self.uploadDirectory.text()
self.preferences.access_key_id = self.uploadAccessKeyID.text()
self.preferences.secret_access_key = self.uploadSecretAccessKey.text()
self.preferences.delete_original = self.uploadDeleteOriginal.isChecked()
self.preferences.event_upload_enabled = self.eventUploadEnabled.isChecked()
self.preferences.alert_email_enabled = self.enableAlertEmail.isChecked()
self.preferences.alert_from_address = self.fromAddress.text()
self.preferences.alert_to_address = self.toAddress.text()
self.preferences.alert_smtp_host = self.smtpHost.text()
self.preferences.alert_smtp_port = self.smtpPort.value()
if self.useSTARTTLS.isChecked():
    self.preferences.alert_security = 'starttls'
elif self.useSSL.isChecked():
    self.preferences.alert_security = 'ssl'
else:
    self.preferences.alert_security = ''
use_auth = self.useAuthentication.isChecked()
self.preferences.alert_use_auth = use_auth
if use_auth:
    self.preferences.alert_smtp_user = self.smtpUser.text()
    self.preferences.alert_smtp_password = self.smtpPassword.text()
    return None
self.preferences.alert_smtp_user = None
self.preferences.alert_smtp_password = ''
