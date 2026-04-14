# Source Generated with Decompyle++
# File: tmpypd2ncuv.marshal (Python 3.11)


def setupUi(self, UnitPreferencesWidget):
    if not UnitPreferencesWidget.objectName():
        UnitPreferencesWidget.setObjectName('UnitPreferencesWidget')
    UnitPreferencesWidget.resize(207, 17)
    self.unitGridLayout = QGridLayout(UnitPreferencesWidget)
    self.unitGridLayout.setObjectName('unitGridLayout')
    self.unitGridLayout.setContentsMargins(0, 0, 0, 0)
    self.metricUnits = QRadioButton(UnitPreferencesWidget)
    self.metricUnits.setObjectName('metricUnits')
    font = QFont()
    font.setBold(True)
    self.metricUnits.setFont(font)
    self.unitGridLayout.addWidget(self.metricUnits, 0, 0, 1, 1)
    self.usUnits = QRadioButton(UnitPreferencesWidget)
    self.usUnits.setObjectName('usUnits')
    self.usUnits.setFont(font)
    self.unitGridLayout.addWidget(self.usUnits, 0, 1, 1, 1)
    self.mixedUnits = QRadioButton(UnitPreferencesWidget)
    self.mixedUnits.setObjectName('mixedUnits')
    self.mixedUnits.setFont(font)
    self.unitGridLayout.addWidget(self.mixedUnits, 0, 2, 1, 1)
    self.retranslateUi(UnitPreferencesWidget)
    QMetaObject.connectSlotsByName(UnitPreferencesWidget)


def retranslateUi(self, UnitPreferencesWidget):
    self.metricUnits.setText(QCoreApplication.translate('UnitPreferencesWidget', 'SI', None))
    self.usUnits.setText(QCoreApplication.translate('UnitPreferencesWidget', 'US Customary', None))
    self.mixedUnits.setText(QCoreApplication.translate('UnitPreferencesWidget', 'Mixed', None))

