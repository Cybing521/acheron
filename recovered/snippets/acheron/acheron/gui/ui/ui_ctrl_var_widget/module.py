# Source Generated with Decompyle++
# File: tmpsk1eemsf.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QSizePolicy, QSlider, QWidget

class Ui_CtrlVarWidget(object):
    
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


