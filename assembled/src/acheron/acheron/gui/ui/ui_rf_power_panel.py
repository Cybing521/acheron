# Source Generated with Decompyle++
# File: ui_rf_power_panel.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QGroupBox, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

class Ui_RFPowerPanel(object):
    
    def setupUi(self, RFPowerPanel):
        if not RFPowerPanel.objectName():
            RFPowerPanel.setObjectName('RFPowerPanel')
        RFPowerPanel.resize(111, 99)
        self.verticalLayout = QVBoxLayout(RFPowerPanel)
        self.verticalLayout.setObjectName('verticalLayout')
        self.enableButton = QPushButton(RFPowerPanel)
        self.enableButton.setObjectName('enableButton')
        self.verticalLayout.addWidget(self.enableButton)
        self.disableButton = QPushButton(RFPowerPanel)
        self.disableButton.setObjectName('disableButton')
        self.verticalLayout.addWidget(self.disableButton)
        self.ctrlVarLayout = QVBoxLayout()
        self.ctrlVarLayout.setObjectName('ctrlVarLayout')
        self.verticalLayout.addLayout(self.ctrlVarLayout)
        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.retranslateUi(RFPowerPanel)
        QMetaObject.connectSlotsByName(RFPowerPanel)

    
    def retranslateUi(self, RFPowerPanel):
        RFPowerPanel.setWindowTitle(QCoreApplication.translate('RFPowerPanel', 'RF Power Panel', None))
        RFPowerPanel.setTitle(QCoreApplication.translate('RFPowerPanel', 'RF Power', None))
        self.enableButton.setText(QCoreApplication.translate('RFPowerPanel', 'Enable RF Power', None))
        self.disableButton.setText(QCoreApplication.translate('RFPowerPanel', 'Disable RF Power', None))


