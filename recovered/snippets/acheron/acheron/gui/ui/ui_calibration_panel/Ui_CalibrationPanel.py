# Source Generated with Decompyle++
# File: tmpknk53t1u.marshal (Python 3.11)


def setupUi(self, CalibrationPanel):
    if not CalibrationPanel.objectName():
        CalibrationPanel.setObjectName('CalibrationPanel')
    CalibrationPanel.resize(95, 158)
    self.verticalLayout = QVBoxLayout(CalibrationPanel)
    self.verticalLayout.setObjectName('verticalLayout')
    self.buttonBox = QDialogButtonBox(CalibrationPanel)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
    self.verticalLayout.addWidget(self.buttonBox)
    self.retranslateUi(CalibrationPanel)
    QMetaObject.connectSlotsByName(CalibrationPanel)


def retranslateUi(self, CalibrationPanel):
    CalibrationPanel.setWindowTitle(QCoreApplication.translate('CalibrationPanel', 'Calibration', None))
    CalibrationPanel.setTitle(QCoreApplication.translate('CalibrationPanel', 'Calibration', None))

