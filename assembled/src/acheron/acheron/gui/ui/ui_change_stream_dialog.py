# Source Generated with Decompyle++
# File: ui_change_stream_dialog.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QSizePolicy, QVBoxLayout, QWidget

class Ui_ChangeStreamDialog(object):
    
    def setupUi(self, ChangeStreamDialog):
        if not ChangeStreamDialog.objectName():
            ChangeStreamDialog.setObjectName('ChangeStreamDialog')
        ChangeStreamDialog.resize(403, 49)
        self.verticalLayout_2 = QVBoxLayout(ChangeStreamDialog)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QDialogButtonBox(ChangeStreamDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(ChangeStreamDialog)
        self.buttonBox.accepted.connect(ChangeStreamDialog.accept)
        self.buttonBox.rejected.connect(ChangeStreamDialog.reject)
        QMetaObject.connectSlotsByName(ChangeStreamDialog)

    
    def retranslateUi(self, ChangeStreamDialog):
        ChangeStreamDialog.setWindowTitle(QCoreApplication.translate('ChangeStreamDialog', 'Change Streams', None))


