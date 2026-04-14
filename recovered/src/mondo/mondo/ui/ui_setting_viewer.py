# Source Generated with Decompyle++
# File: ui_setting_viewer.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QSizePolicy, QTabWidget, QVBoxLayout, QWidget

class Ui_SettingViewerDialog(object):
    
    def setupUi(self, SettingViewerDialog):
        if not SettingViewerDialog.objectName():
            SettingViewerDialog.setObjectName('SettingViewerDialog')
        SettingViewerDialog.resize(400, 53)
        self.verticalLayout = QVBoxLayout(SettingViewerDialog)
        self.verticalLayout.setObjectName('verticalLayout')
        self.tabWidget = QTabWidget(SettingViewerDialog)
        self.tabWidget.setObjectName('tabWidget')
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QDialogButtonBox(SettingViewerDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(SettingViewerDialog)
        self.buttonBox.accepted.connect(SettingViewerDialog.accept)
        self.buttonBox.rejected.connect(SettingViewerDialog.reject)
        QMetaObject.connectSlotsByName(SettingViewerDialog)

    
    def retranslateUi(self, SettingViewerDialog):
        SettingViewerDialog.setWindowTitle(QCoreApplication.translate('SettingViewerDialog', 'Device Settings', None))


