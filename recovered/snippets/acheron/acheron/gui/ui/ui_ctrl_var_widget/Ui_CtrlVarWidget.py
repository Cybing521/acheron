# Source Generated with Decompyle++
# File: tmpcvg43zr9.marshal (Python 3.11)


def setupUi(self, CtrlVarWidget):
    if not CtrlVarWidget.objectName():
        CtrlVarWidget.setObjectName('CtrlVarWidget')
    CtrlVarWidget.resize(121, 19)
    self.horizontalLayout = QHBoxLayout(CtrlVarWidget)
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setObjectName('horizontalLayout')
    self.nameLabel = QLabel(CtrlVarWidget)
    self.nameLabel.setObjectName('nameLabel')
    self.horizontalLayout.addWidget(self.nameLabel)
    self.slider = QSlider(CtrlVarWidget)
    self.slider.setObjectName('slider')
    self.slider.setMinimumSize(QSize(50, 0))
    self.slider.setOrientation(Qt.Horizontal)
    self.horizontalLayout.addWidget(self.slider)
    self.retranslateUi(CtrlVarWidget)
    QMetaObject.connectSlotsByName(CtrlVarWidget)


def retranslateUi(self, CtrlVarWidget):
    CtrlVarWidget.setWindowTitle(QCoreApplication.translate('CtrlVarWidget', 'Ctrl Var Widget', None))
    self.nameLabel.setText(QCoreApplication.translate('CtrlVarWidget', 'Ctrl Var Name', None))

