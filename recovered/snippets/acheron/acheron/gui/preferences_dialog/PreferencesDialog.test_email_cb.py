# Source Generated with Decompyle++
# File: tmp3cbv7y8s.marshal (Python 3.11)

if self.useSTARTTLS.isChecked():
    security = 'starttls'
elif self.useSSL.isChecked():
    security = 'ssl'
else:
    security = ''
email_settings = EmailSettings(from_address = self.fromAddress.text().strip(), to_address = self.toAddress.text().strip(), smtp_host = self.smtpHost.text().strip(), smtp_port = self.smtpPort.value(), security = security, use_auth = self.useAuthentication.isChecked(), smtp_user = self.smtpUser.text().strip(), smtp_password = self.smtpPassword.text().strip())

try:
    QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
    send_test_email(email_settings)
    QtWidgets.QApplication.restoreOverrideCursor()
    logger.info('Sent test email successfully')
    QtWidgets.QMessageBox.information(self, self.tr('Sent'), self.tr('Email Sent!'))
    return None
except Exception:
    e = None
    QtWidgets.QApplication.restoreOverrideCursor()
    logger.exception('Error sending test email.')
    error_str = str(e) + '\nSee log for more details.'
    QtWidgets.QMessageBox.critical(self, self.tr('Error'), error_str)
    e = None
    del e
    return None
    e = None
    del e

