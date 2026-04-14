# Source Generated with Decompyle++
# File: tmpgp2wz5nt.marshal (Python 3.11)


def setupUi(self, SelectSynchronousDialog):
    if not SelectSynchronousDialog.objectName():
        SelectSynchronousDialog.setObjectName('SelectSynchronousDialog')
    SelectSynchronousDialog.resize(400, 49)
    self.verticalLayout_2 = QVBoxLayout(SelectSynchronousDialog)
    self.verticalLayout_2.setObjectName('verticalLayout_2')
    self.verticalLayout = QVBoxLayout()
    self.verticalLayout.setObjectName('verticalLayout')
    self.verticalLayout_2.addLayout(self.verticalLayout)
    self.buttonBox = QDialogButtonBox(SelectSynchronousDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    self.verticalLayout_2.addWidget(self.buttonBox)
    self.retranslateUi(SelectSynchronousDialog)
    self.buttonBox.accepted.connect(SelectSynchronousDialog.accept)
    self.buttonBox.rejected.connect(SelectSynchronousDialog.reject)
    QMetaObject.connectSlotsByName(SelectSynchronousDialog)


def retranslateUi(self, SelectSynchronousDialog):
    SelectSynchronousDialog.setWindowTitle(QCoreApplication.translate('SelectSynchronousDialog', 'Select Synchronous Channels', None))

