# Source Generated with Decompyle++
# File: ui_calibration_panel.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialogButtonBox, QGroupBox, QSizePolicy, QVBoxLayout, QWidget

class Ui_CalibrationPanel(object):
    
    def setupUi(self, CalibrationPanel):
        if not CalibrationPanel.objectName():
            CalibrationPanel.setObjectName('CalibrationPanel')
        CalibrationPanel.resize(95, 158)
        self.verticalLayout = QVBoxLayout(CalibrationPanel)
        self.verticalLayout.setObjectName('verticalLayout')
        self.buttonBox = QDialogButtonBox(CalibrationPanel)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(CalibrationPanel)
        QMetaObject.connectSlotsByName(CalibrationPanel)

    
    def retranslateUi(self, CalibrationPanel):
        CalibrationPanel.setWindowTitle(QCoreApplication.translate('CalibrationPanel', 'Calibration', None))
        CalibrationPanel.setTitle(QCoreApplication.translate('CalibrationPanel', 'Calibration', None))


