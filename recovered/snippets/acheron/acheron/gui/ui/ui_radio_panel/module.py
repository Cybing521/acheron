# Source Generated with Decompyle++
# File: tmpm0e3wiib.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QAction, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QApplication, QFrame, QGroupBox, QHBoxLayout, QListWidget, QListWidgetItem, QPushButton, QSizePolicy, QToolButton, QVBoxLayout, QWidget

class Ui_RadioPanel(object):
    
    def setupUi(self, RadioPanel):
        if not RadioPanel.objectName():
            RadioPanel.setObjectName('RadioPanel')
        RadioPanel.resize(143, 278)
        self.actionConnectSpecificBootloader = QAction(RadioPanel)
        self.actionConnectSpecificBootloader.setObjectName('actionConnectSpecificBootloader')
        self.actionConnectNoStreaming = QAction(RadioPanel)
        self.actionConnectNoStreaming.setObjectName('actionConnectNoStreaming')
        self.actionConnectSpecificSerial = QAction(RadioPanel)
        self.actionConnectSpecificSerial.setObjectName('actionConnectSpecificSerial')
        self.actionClear = QAction(RadioPanel)
        self.actionClear.setObjectName('actionClear')
        self.verticalLayout = QVBoxLayout(RadioPanel)
        self.verticalLayout.setObjectName('verticalLayout')
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.detailScanButton = QPushButton(RadioPanel)
        self.detailScanButton.setObjectName('detailScanButton')
        self.horizontalLayout.addWidget(self.detailScanButton)
        self.clearButton = QToolButton(RadioPanel)
        self.clearButton.setObjectName('clearButton')
        self.horizontalLayout.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.deviceList = QListWidget(RadioPanel)
        self.deviceList.setObjectName('deviceList')
        self.deviceList.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.verticalLayout.addWidget(self.deviceList)
        self.connectButton = QPushButton(RadioPanel)
        self.connectButton.setObjectName('connectButton')
        self.verticalLayout.addWidget(self.connectButton)
        self.disconnectButton = QPushButton(RadioPanel)
        self.disconnectButton.setObjectName('disconnectButton')
        self.verticalLayout.addWidget(self.disconnectButton)
        self.advancedMenuButton = QPushButton(RadioPanel)
        self.advancedMenuButton.setObjectName('advancedMenuButton')
        self.verticalLayout.addWidget(self.advancedMenuButton)
        self.ctrlVarLayout = QVBoxLayout()
        self.ctrlVarLayout.setObjectName('ctrlVarLayout')
        self.verticalLayout.addLayout(self.ctrlVarLayout)
        self.line = QFrame(RadioPanel)
        self.line.setObjectName('line')
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)
        self.goToRemoteButton = QPushButton(RadioPanel)
        self.goToRemoteButton.setObjectName('goToRemoteButton')
        self.verticalLayout.addWidget(self.goToRemoteButton)
        self.retranslateUi(RadioPanel)
        QMetaObject.connectSlotsByName(RadioPanel)

    
    def retranslateUi(self, RadioPanel):
        RadioPanel.setWindowTitle(QCoreApplication.translate('RadioPanel', 'Radio Panel', None))
        RadioPanel.setTitle(QCoreApplication.translate('RadioPanel', 'Radio', None))
        self.actionConnectSpecificBootloader.setText(QCoreApplication.translate('RadioPanel', 'Connect Specific Bootloader...', None))
        self.actionConnectNoStreaming.setText(QCoreApplication.translate('RadioPanel', 'Connect (No Streaming)', None))
        self.actionConnectSpecificSerial.setText(QCoreApplication.translate('RadioPanel', 'Connect Specific Serial...', None))
        self.actionClear.setText(QCoreApplication.translate('RadioPanel', 'Clear Scan List', None))
        self.actionClear.setToolTip(QCoreApplication.translate('RadioPanel', 'Clear Scan List', None))
        self.detailScanButton.setText(QCoreApplication.translate('RadioPanel', 'Detail Scan...', None))
        self.clearButton.setText(QCoreApplication.translate('RadioPanel', 'Clear', None))
        self.connectButton.setText(QCoreApplication.translate('RadioPanel', 'Connect', None))
        self.disconnectButton.setText(QCoreApplication.translate('RadioPanel', 'Disconnect', None))
        self.advancedMenuButton.setText(QCoreApplication.translate('RadioPanel', 'Advanced Menu', None))
        self.goToRemoteButton.setText(QCoreApplication.translate('RadioPanel', 'Go To Remote Tab', None))


