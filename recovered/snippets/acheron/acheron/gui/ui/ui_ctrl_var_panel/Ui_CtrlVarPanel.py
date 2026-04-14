# Source Generated with Decompyle++
# File: tmpez1ec_6z.marshal (Python 3.11)


def setupUi(self, CtrlVarPanel):
    if not CtrlVarPanel.objectName():
        CtrlVarPanel.setObjectName('CtrlVarPanel')
    CtrlVarPanel.resize(99, 41)
    self.verticalLayout = QVBoxLayout(CtrlVarPanel)
    self.verticalLayout.setObjectName('verticalLayout')
    self.ctrlVarLayout = QVBoxLayout()
    self.ctrlVarLayout.setObjectName('ctrlVarLayout')
    self.verticalLayout.addLayout(self.ctrlVarLayout)
    self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    self.verticalLayout.addItem(self.verticalSpacer)
    self.retranslateUi(CtrlVarPanel)
    QMetaObject.connectSlotsByName(CtrlVarPanel)


def retranslateUi(self, CtrlVarPanel):
    CtrlVarPanel.setWindowTitle(QCoreApplication.translate('CtrlVarPanel', 'Control Variable Panel', None))
    CtrlVarPanel.setTitle(QCoreApplication.translate('CtrlVarPanel', 'Control Variables', None))

