# Source Generated with Decompyle++
# File: ui_remote_panel.pyc (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QGroupBox, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

class Ui_RemotePanel(object):
    
    def setupUi(self, RemotePanel):
        if not RemotePanel.objectName():
            RemotePanel.setObjectName('RemotePanel')
        RemotePanel.resize(112, 182)
        self.verticalLayout = QVBoxLayout(RemotePanel)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)
        self.goToParentButton = QPushButton(RemotePanel)
        self.goToParentButton.setObjectName('goToParentButton')
        self.verticalLayout.addWidget(self.goToParentButton)
        self.retranslateUi(RemotePanel)
        QMetaObject.connectSlotsByName(RemotePanel)

    
    def retranslateUi(self, RemotePanel):
        RemotePanel.setWindowTitle(QCoreApplication.translate('RemotePanel', 'Remote Device Panel', None))
        RemotePanel.setTitle(QCoreApplication.translate('RemotePanel', 'Remote Device', None))
        self.goToParentButton.setText(QCoreApplication.translate('RemotePanel', 'Go To Radio Tab', None))


