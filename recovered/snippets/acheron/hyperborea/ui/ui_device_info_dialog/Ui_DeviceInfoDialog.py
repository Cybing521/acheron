# Source Generated with Decompyle++
# File: tmpya7wst2_.marshal (Python 3.11)


def setupUi(self, DeviceInfoDialog):
    if not DeviceInfoDialog.objectName():
        DeviceInfoDialog.setObjectName('DeviceInfoDialog')
    DeviceInfoDialog.resize(736, 548)
    self.verticalLayout = QVBoxLayout(DeviceInfoDialog)
    self.verticalLayout.setObjectName('verticalLayout')
    self.plainTextEdit = QPlainTextEdit(DeviceInfoDialog)
    self.plainTextEdit.setObjectName('plainTextEdit')
    self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.plainTextEdit.setReadOnly(True)
    self.verticalLayout.addWidget(self.plainTextEdit)
    self.horizontalLayout = QHBoxLayout()
    self.horizontalLayout.setObjectName('horizontalLayout')
    self.saveButton = QPushButton(DeviceInfoDialog)
    self.saveButton.setObjectName('saveButton')
    self.horizontalLayout.addWidget(self.saveButton)
    self.buttonBox = QDialogButtonBox(DeviceInfoDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
    self.horizontalLayout.addWidget(self.buttonBox)
    self.verticalLayout.addLayout(self.horizontalLayout)
    self.retranslateUi(DeviceInfoDialog)
    self.buttonBox.accepted.connect(DeviceInfoDialog.accept)
    self.buttonBox.rejected.connect(DeviceInfoDialog.reject)
    QMetaObject.connectSlotsByName(DeviceInfoDialog)


def retranslateUi(self, DeviceInfoDialog):
    DeviceInfoDialog.setWindowTitle(QCoreApplication.translate('DeviceInfoDialog', 'Device Information', None))
    self.saveButton.setText(QCoreApplication.translate('DeviceInfoDialog', 'Save As...', None))

