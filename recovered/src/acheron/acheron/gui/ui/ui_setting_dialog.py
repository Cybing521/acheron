# Source Generated with Decompyle++
# File: ui_setting_dialog.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QSizePolicy, QTabWidget, QVBoxLayout, QWidget

class Ui_SettingDialog(object):
    
    def setupUi(self, SettingDialog):
        if not SettingDialog.objectName():
            SettingDialog.setObjectName('SettingDialog')
        SettingDialog.resize(400, 53)
        self.verticalLayout = QVBoxLayout(SettingDialog)
        self.verticalLayout.setObjectName('verticalLayout')
        self.tabWidget = QTabWidget(SettingDialog)
        self.tabWidget.setObjectName('tabWidget')
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QDialogButtonBox(SettingDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.RestoreDefaults)
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(SettingDialog)
        self.buttonBox.accepted.connect(SettingDialog.accept)
        self.buttonBox.rejected.connect(SettingDialog.reject)
        QMetaObject.connectSlotsByName(SettingDialog)

    
    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QCoreApplication.translate('SettingDialog', 'Device Settings', None))


