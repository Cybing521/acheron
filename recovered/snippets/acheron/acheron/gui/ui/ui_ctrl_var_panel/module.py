# Source Generated with Decompyle++
# File: tmp2swx7njz.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QGroupBox, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

class Ui_CtrlVarPanel(object):
    
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


