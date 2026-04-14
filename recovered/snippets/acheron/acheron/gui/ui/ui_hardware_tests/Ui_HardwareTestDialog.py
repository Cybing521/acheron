# Source Generated with Decompyle++
# File: tmpe90_qh7l.marshal (Python 3.11)


def setupUi(self, HardwareTestDialog):
    if not HardwareTestDialog.objectName():
        HardwareTestDialog.setObjectName('HardwareTestDialog')
    HardwareTestDialog.resize(754, 426)
    self.verticalLayout = QVBoxLayout(HardwareTestDialog)
    self.verticalLayout.setObjectName('verticalLayout')
    self.testOutput = QPlainTextEdit(HardwareTestDialog)
    self.testOutput.setObjectName('testOutput')
    self.testOutput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.testOutput.setReadOnly(True)
    self.verticalLayout.addWidget(self.testOutput)
    self.buttonBox = QDialogButtonBox(HardwareTestDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Close | QDialogButtonBox.Reset)
    self.verticalLayout.addWidget(self.buttonBox)
    self.retranslateUi(HardwareTestDialog)
    self.buttonBox.accepted.connect(HardwareTestDialog.accept)
    self.buttonBox.rejected.connect(HardwareTestDialog.reject)
    QMetaObject.connectSlotsByName(HardwareTestDialog)


def retranslateUi(self, HardwareTestDialog):
    HardwareTestDialog.setWindowTitle(QCoreApplication.translate('HardwareTestDialog', 'Hardware Tests', None))

