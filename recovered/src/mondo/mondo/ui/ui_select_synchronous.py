# Source Generated with Decompyle++
# File: ui_select_synchronous.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QSizePolicy, QVBoxLayout, QWidget

class Ui_SelectSynchronousDialog(object):
    
    def setupUi(self, SelectSynchronousDialog):
        if not SelectSynchronousDialog.objectName():
            SelectSynchronousDialog.setObjectName('SelectSynchronousDialog')
        SelectSynchronousDialog.resize(400, 49)
        self.verticalLayout_2 = QVBoxLayout(SelectSynchronousDialog)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QDialogButtonBox(SelectSynchronousDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(SelectSynchronousDialog)
        self.buttonBox.accepted.connect(SelectSynchronousDialog.accept)
        self.buttonBox.rejected.connect(SelectSynchronousDialog.reject)
        QMetaObject.connectSlotsByName(SelectSynchronousDialog)

    
    def retranslateUi(self, SelectSynchronousDialog):
        SelectSynchronousDialog.setWindowTitle(QCoreApplication.translate('SelectSynchronousDialog', 'Select Synchronous Channels', None))


