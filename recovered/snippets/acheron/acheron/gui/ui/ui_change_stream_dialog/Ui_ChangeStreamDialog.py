# Source Generated with Decompyle++
# File: tmp0u37ow30.marshal (Python 3.11)


def setupUi(self, ChangeStreamDialog):
    if not ChangeStreamDialog.objectName():
        ChangeStreamDialog.setObjectName('ChangeStreamDialog')
    ChangeStreamDialog.resize(403, 49)
    self.verticalLayout_2 = QVBoxLayout(ChangeStreamDialog)
    self.verticalLayout_2.setObjectName('verticalLayout_2')
    self.verticalLayout = QVBoxLayout()
    self.verticalLayout.setObjectName('verticalLayout')
    self.verticalLayout_2.addLayout(self.verticalLayout)
    self.buttonBox = QDialogButtonBox(ChangeStreamDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    self.verticalLayout_2.addWidget(self.buttonBox)
    self.retranslateUi(ChangeStreamDialog)
    self.buttonBox.accepted.connect(ChangeStreamDialog.accept)
    self.buttonBox.rejected.connect(ChangeStreamDialog.reject)
    QMetaObject.connectSlotsByName(ChangeStreamDialog)


def retranslateUi(self, ChangeStreamDialog):
    ChangeStreamDialog.setWindowTitle(QCoreApplication.translate('ChangeStreamDialog', 'Change Streams', None))

