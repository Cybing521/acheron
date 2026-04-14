# Source Generated with Decompyle++
# File: tmp3ub43uk5.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QSizePolicy, QSpinBox, QWidget

class Ui_TCPConnectDialog(object):
    
    def setupUi(self, TCPConnectDialog):
        if not TCPConnectDialog.objectName():
            TCPConnectDialog.setObjectName('TCPConnectDialog')
        TCPConnectDialog.resize(341, 119)
        self.formLayout = QFormLayout(TCPConnectDialog)
        self.formLayout.setObjectName('formLayout')
        self.hostnameLabel = QLabel(TCPConnectDialog)
        self.hostnameLabel.setObjectName('hostnameLabel')
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.hostnameLabel)
        self.hostname = QLineEdit(TCPConnectDialog)
        self.hostname.setObjectName('hostname')
        self.hostname.setMinimumSize(QSize(200, 0))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hostname)
        self.portLabel = QLabel(TCPConnectDialog)
        self.portLabel.setObjectName('portLabel')
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.portLabel)
        self.port = QSpinBox(TCPConnectDialog)
        self.port.setObjectName('port')
        self.port.setMinimum(1)
        self.port.setMaximum(65535)
        self.port.setValue(5760)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.port)
        self.serialLabel = QLabel(TCPConnectDialog)
        self.serialLabel.setObjectName('serialLabel')
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.serialLabel)
        self.serial = QLineEdit(TCPConnectDialog)
        self.serial.setObjectName('serial')
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.serial)
        self.buttonBox = QDialogButtonBox(TCPConnectDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.buttonBox)
        self.retranslateUi(TCPConnectDialog)
        self.buttonBox.accepted.connect(TCPConnectDialog.accept)
        self.buttonBox.rejected.connect(TCPConnectDialog.reject)
        QMetaObject.connectSlotsByName(TCPConnectDialog)

    
    def retranslateUi(self, TCPConnectDialog):
        TCPConnectDialog.setWindowTitle(QCoreApplication.translate('TCPConnectDialog', 'Connect TCP Device', None))
        self.hostnameLabel.setText(QCoreApplication.translate('TCPConnectDialog', 'Hostname', None))
        self.portLabel.setToolTip(QCoreApplication.translate('TCPConnectDialog', 'Default: 5760', None))
        self.portLabel.setText(QCoreApplication.translate('TCPConnectDialog', 'Port', None))
        self.port.setToolTip(QCoreApplication.translate('TCPConnectDialog', 'Default: 5760', None))
        self.serialLabel.setText(QCoreApplication.translate('TCPConnectDialog', 'Serial Number (Optional)', None))


