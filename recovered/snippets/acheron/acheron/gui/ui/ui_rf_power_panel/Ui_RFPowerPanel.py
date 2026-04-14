# Source Generated with Decompyle++
# File: tmp_esxuy85.marshal (Python 3.11)


def setupUi(self, RFPowerPanel):
    if not RFPowerPanel.objectName():
        RFPowerPanel.setObjectName('RFPowerPanel')
    RFPowerPanel.resize(111, 99)
    self.verticalLayout = QVBoxLayout(RFPowerPanel)
    self.verticalLayout.setObjectName('verticalLayout')
    self.enableButton = QPushButton(RFPowerPanel)
    self.enableButton.setObjectName('enableButton')
    self.verticalLayout.addWidget(self.enableButton)
    self.disableButton = QPushButton(RFPowerPanel)
    self.disableButton.setObjectName('disableButton')
    self.verticalLayout.addWidget(self.disableButton)
    self.ctrlVarLayout = QVBoxLayout()
    self.ctrlVarLayout.setObjectName('ctrlVarLayout')
    self.verticalLayout.addLayout(self.ctrlVarLayout)
    self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    self.verticalLayout.addItem(self.verticalSpacer)
    self.retranslateUi(RFPowerPanel)
    QMetaObject.connectSlotsByName(RFPowerPanel)


def retranslateUi(self, RFPowerPanel):
    RFPowerPanel.setWindowTitle(QCoreApplication.translate('RFPowerPanel', 'RF Power Panel', None))
    RFPowerPanel.setTitle(QCoreApplication.translate('RFPowerPanel', 'RF Power', None))
    self.enableButton.setText(QCoreApplication.translate('RFPowerPanel', 'Enable RF Power', None))
    self.disableButton.setText(QCoreApplication.translate('RFPowerPanel', 'Disable RF Power', None))

