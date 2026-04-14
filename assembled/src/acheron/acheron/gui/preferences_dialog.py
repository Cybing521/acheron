# Source Generated with Decompyle++
# File: preferences_dialog.pyc (Python 3.11)

import logging
from PySide6 import QtCore, QtWidgets
from hyperborea.dark_mode import set_style
from ..core.preferences import Preferences
from ..connectivity.alert_emailer import EmailSettings, send_test_email
from .ui.ui_preferences_dialog import Ui_PreferencesDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class PreferencesDialog(Ui_PreferencesDialog, QtWidgets.QDialog):

    def __init__(self, preferences, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST parent
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST preferences
        #   72 LOAD_FAST self
        #   74 STORE_ATTR preferences
        #   84 LOAD_FAST self
        #   86 LOAD_METHOD setupUi
        #  108 LOAD_FAST self
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_ATTR tabWidget
        #  138 LOAD_METHOD setCurrentIndex
        #  160 LOAD_CONST 0
        #  162 PRECALL
        #  166 CALL
        #  176 POP_TOP
        #  178 LOAD_FAST self
        #  180 LOAD_ATTR accepted
        #  190 LOAD_METHOD connect
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR write_settings
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR rejected
        #  252 LOAD_METHOD connect
        #  274 LOAD_FAST self
        #  276 LOAD_ATTR restore_dark_mode
        #  286 PRECALL
        #  290 CALL
        #  300 POP_TOP
        #  302 LOAD_FAST self
        #  304 LOAD_ATTR browseButton
        #  314 LOAD_ATTR clicked
        #  324 LOAD_METHOD connect
        #  346 LOAD_FAST self
        #  348 LOAD_ATTR browse_cb
        #  358 PRECALL
        #  362 CALL
        #  372 POP_TOP
        #  374 LOAD_FAST self
        #  376 LOAD_ATTR testEmail
        #  386 LOAD_ATTR clicked
        #  396 LOAD_METHOD connect
        #  418 LOAD_FAST self
        #  420 LOAD_ATTR test_email_cb
        #  430 PRECALL
        #  434 CALL
        #  444 POP_TOP
        #  446 LOAD_FAST self
        #  448 LOAD_METHOD read_settings
        #  470 PRECALL
        #  474 CALL
        #  484 POP_TOP
        #  486 LOAD_FAST self
        #  488 LOAD_ATTR darkMode
        #  498 LOAD_ATTR toggled
        #  508 LOAD_METHOD connect
        #  530 LOAD_FAST self
        #  532 LOAD_ATTR dark_mode_updated
        #  542 PRECALL
        #  546 CALL
        #  556 POP_TOP
        #  558 LOAD_FAST self
        #  560 LOAD_ATTR lightMode
        #  570 LOAD_ATTR toggled
        #  580 LOAD_METHOD connect
        #  602 LOAD_FAST self
        #  604 LOAD_ATTR dark_mode_updated
        # ... bytecode truncated ...
        pass

    def browse_cb(self):
        base_dir = self.outputLocation.text()
        base_dir = QtWidgets.QFileDialog.getExistingDirectory(self, dir = base_dir)
        if base_dir:
            self.outputLocation.setText(base_dir)
            return None

    def test_email_cb(self):
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

    def dark_mode_updated(self):
        dark_mode = self.darkMode.isChecked()
        set_style(QtWidgets.QApplication.instance(), dark_mode)

    def restore_dark_mode(self):
        set_style(QtWidgets.QApplication.instance(), self.preferences.dark_mode)

    def read_settings(self):
        self.darkMode.setChecked(self.preferences.dark_mode)
        self.showSupplyChecks.setChecked(self.preferences.show_supplies)
        self.automaticRGBCheckBox.setChecked(self.preferences.auto_rgb)
        self.downsampleCheckBox.setChecked(self.preferences.downsample)
        self.plotMeanCheckBox.setChecked(self.preferences.plot_mean)
        self.unitPreferences.read_settings()
        self.outputLocation.setText(self.preferences.base_dir)
        self.outputLocation.setCursorPosition(0)
        self.compressionLevel.setValue(self.preferences.compression_level)
        self.runModbusCheckBox.setChecked(self.preferences.modbus_enable)
        self.modbusPort.setValue(self.preferences.modbus_port)
        self.enableUpload.setChecked(self.preferences.upload_enabled)
        self.s3Bucket.setText(self.preferences.s3_bucket)
        self.awsRegion.setText(self.preferences.aws_region)
        self.uploadDirectory.setText(self.preferences.upload_directory)
        self.uploadAccessKeyID.setText(self.preferences.access_key_id)
        self.uploadSecretAccessKey.setText(self.preferences.secret_access_key)
        self.uploadDeleteOriginal.setChecked(self.preferences.delete_original)
        self.eventUploadEnabled.setChecked(self.preferences.event_upload_enabled)
        self.enableAlertEmail.setChecked(self.preferences.alert_email_enabled)
        self.fromAddress.setText(self.preferences.alert_from_address)
        self.toAddress.setText(self.preferences.alert_to_address)
        self.smtpHost.setText(self.preferences.alert_smtp_host)
        self.smtpPort.setValue(self.preferences.alert_smtp_port)
        security = self.preferences.alert_security.lower()
        if security == 'starttls':
            self.useSTARTTLS.setChecked(True)
        elif security == 'ssl':
            self.useSSL.setChecked(True)
        elif security == '':
            self.noSecurity.setChecked(True)
        else:
            self.useSTARTTLS.setChecked(True)
        self.useAuthentication.setChecked(self.preferences.alert_use_auth)
        self.smtpUser.setText(self.preferences.alert_smtp_user)
        self.smtpPassword.setText(self.preferences.alert_smtp_password)

    def write_settings(self):
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
