# Source Generated with Decompyle++
# File: tmpluv719b8.marshal (Python 3.11)


def setupUi(self, LEDControlWidget):
    if not LEDControlWidget.objectName():
        LEDControlWidget.setObjectName('LEDControlWidget')
    LEDControlWidget.resize(176, 20)
    self.horizontalLayout_3 = QHBoxLayout(LEDControlWidget)
    self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout_3.setObjectName('horizontalLayout_3')
    self.slider = QSlider(LEDControlWidget)
    self.slider.setObjectName('slider')
    self.slider.setMinimumSize(QSize(128, 0))
    self.slider.setMaximum(255)
    self.slider.setOrientation(Qt.Horizontal)
    self.horizontalLayout_3.addWidget(self.slider)
    self.spinBox = QSpinBox(LEDControlWidget)
    self.spinBox.setObjectName('spinBox')
    self.spinBox.setMaximum(255)
    self.horizontalLayout_3.addWidget(self.spinBox)
    QWidget.setTabOrder(self.slider, self.spinBox)
    self.retranslateUi(LEDControlWidget)
    self.slider.valueChanged.connect(self.spinBox.setValue)
    self.spinBox.valueChanged.connect(self.slider.setValue)
    QMetaObject.connectSlotsByName(LEDControlWidget)


def retranslateUi(self, LEDControlWidget):
    LEDControlWidget.setWindowTitle(QCoreApplication.translate('LEDControlWidget', 'LED Control Widget', None))

