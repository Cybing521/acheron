# Source Generated with Decompyle++
# File: tmpr5ljpwb2.marshal (Python 3.11)


def setupUi(self, RemotePanel):
    if not RemotePanel.objectName():
        RemotePanel.setObjectName('RemotePanel')
    RemotePanel.resize(112, 182)
    self.verticalLayout = QVBoxLayout(RemotePanel)
    self.verticalLayout.setObjectName('verticalLayout')
    self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    self.verticalLayout.addItem(self.verticalSpacer)
    self.goToParentButton = QPushButton(RemotePanel)
    self.goToParentButton.setObjectName('goToParentButton')
    self.verticalLayout.addWidget(self.goToParentButton)
    self.retranslateUi(RemotePanel)
    QMetaObject.connectSlotsByName(RemotePanel)


def retranslateUi(self, RemotePanel):
    RemotePanel.setWindowTitle(QCoreApplication.translate('RemotePanel', 'Remote Device Panel', None))
    RemotePanel.setTitle(QCoreApplication.translate('RemotePanel', 'Remote Device', None))
    self.goToParentButton.setText(QCoreApplication.translate('RemotePanel', 'Go To Radio Tab', None))

