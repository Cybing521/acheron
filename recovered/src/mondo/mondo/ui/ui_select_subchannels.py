# Source Generated with Decompyle++
# File: ui_select_subchannels.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QSizePolicy, QVBoxLayout, QWidget

class Ui_SelectSubchannelsDialog(object):
    
    def setupUi(self, SelectSubchannelsDialog):
        if not SelectSubchannelsDialog.objectName():
            SelectSubchannelsDialog.setObjectName('SelectSubchannelsDialog')
        SelectSubchannelsDialog.resize(400, 49)
        self.verticalLayout_2 = QVBoxLayout(SelectSubchannelsDialog)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QDialogButtonBox(SelectSubchannelsDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(SelectSubchannelsDialog)
        self.buttonBox.accepted.connect(SelectSubchannelsDialog.accept)
        self.buttonBox.rejected.connect(SelectSubchannelsDialog.reject)
        QMetaObject.connectSlotsByName(SelectSubchannelsDialog)

    
    def retranslateUi(self, SelectSubchannelsDialog):
        SelectSubchannelsDialog.setWindowTitle(QCoreApplication.translate('SelectSubchannelsDialog', 'Select Subchannels Channels', None))


