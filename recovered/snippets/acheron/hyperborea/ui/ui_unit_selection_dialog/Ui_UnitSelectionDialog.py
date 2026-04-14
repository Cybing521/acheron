# Source Generated with Decompyle++
# File: tmpd1aklpfl.marshal (Python 3.11)


def setupUi(self, UnitSelectionDialog):
    if not UnitSelectionDialog.objectName():
        UnitSelectionDialog.setObjectName('UnitSelectionDialog')
    UnitSelectionDialog.resize(184, 68)
    self.verticalLayout = QVBoxLayout(UnitSelectionDialog)
    self.verticalLayout.setObjectName('verticalLayout')
    self.unitGridLayout = QGridLayout()
    self.unitGridLayout.setObjectName('unitGridLayout')
    self.unitGridLayout.setHorizontalSpacing(20)
    self.unitGridLayout.setVerticalSpacing(1)
    self.metricLabel = QLabel(UnitSelectionDialog)
    self.metricLabel.setObjectName('metricLabel')
    font = QFont()
    font.setBold(True)
    self.metricLabel.setFont(font)
    self.unitGridLayout.addWidget(self.metricLabel, 0, 0, 1, 1)
    self.usLabel = QLabel(UnitSelectionDialog)
    self.usLabel.setObjectName('usLabel')
    self.usLabel.setFont(font)
    self.unitGridLayout.addWidget(self.usLabel, 0, 1, 1, 1)
    self.otherLabel = QLabel(UnitSelectionDialog)
    self.otherLabel.setObjectName('otherLabel')
    self.otherLabel.setFont(font)
    self.unitGridLayout.addWidget(self.otherLabel, 0, 2, 1, 1)
    self.verticalLayout.addLayout(self.unitGridLayout)
    self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)
    self.verticalLayout.addItem(self.verticalSpacer)
    self.buttonBox = QDialogButtonBox(UnitSelectionDialog)
    self.buttonBox.setObjectName('buttonBox')
    self.buttonBox.setOrientation(Qt.Horizontal)
    self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    self.verticalLayout.addWidget(self.buttonBox)
    self.retranslateUi(UnitSelectionDialog)
    self.buttonBox.accepted.connect(UnitSelectionDialog.accept)
    self.buttonBox.rejected.connect(UnitSelectionDialog.reject)
    QMetaObject.connectSlotsByName(UnitSelectionDialog)


def retranslateUi(self, UnitSelectionDialog):
    UnitSelectionDialog.setWindowTitle(QCoreApplication.translate('UnitSelectionDialog', 'Select Unit', None))
    self.metricLabel.setText(QCoreApplication.translate('UnitSelectionDialog', 'SI', None))
    self.usLabel.setText(QCoreApplication.translate('UnitSelectionDialog', 'US Customary', None))
    self.otherLabel.setText(QCoreApplication.translate('UnitSelectionDialog', 'Other', None))

