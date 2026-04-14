# Source Generated with Decompyle++
# File: tmp6yf44ixk.marshal (Python 3.11)


def setupUi(self, SettingViewerDialog):
    if not SettingViewerDialog.objectName():
        SettingViewerDialog.setObjectName('SettingViewerDialog')
    SettingViewerDialog.resize(400, 53)
    self.verticalLayout = QVBoxLayout(SettingViewerDialog)
    self.verticalLayout.setObjectName('verticalLayout')
    self.tabWidget = QTabWidget(SettingViewerDialog)
    self.tabWidget.setObjectName('tabWidget')
    self.verticalLayout.addWidget(self.tabWidget)
    self.buttonBox = QDialogButtonBox(SettingViewerDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
    self.verticalLayout.addWidget(self.buttonBox)
    self.retranslateUi(SettingViewerDialog)
    self.buttonBox.accepted.connect(SettingViewerDialog.accept)
    self.buttonBox.rejected.connect(SettingViewerDialog.reject)
    QMetaObject.connectSlotsByName(SettingViewerDialog)


def retranslateUi(self, SettingViewerDialog):
    SettingViewerDialog.setWindowTitle(QCoreApplication.translate('SettingViewerDialog', 'Device Settings', None))

