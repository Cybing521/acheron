# Source Generated with Decompyle++
# File: tmp4_ndxhei.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QAbstractItemView, QApplication, QCheckBox, QDialog, QDialogButtonBox, QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class Ui_TCPScanDialog(object):
    
    def setupUi(self, TCPScanDialog):
        if not TCPScanDialog.objectName():
            TCPScanDialog.setObjectName('TCPScanDialog')
        TCPScanDialog.resize(915, 445)
        self.verticalLayout = QVBoxLayout(TCPScanDialog)
        self.verticalLayout.setObjectName('verticalLayout')
        self.tableWidget = QTableWidget(TCPScanDialog)
        if self.tableWidget.columnCount() < 8:
            self.tableWidget.setColumnCount(8)
        _Ui_TCPScanDialog__qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, _Ui_TCPScanDialog__qtablewidgetitem)
        _Ui_TCPScanDialog__qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, _Ui_TCPScanDialog__qtablewidgetitem1)
        _Ui_TCPScanDialog__qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, _Ui_TCPScanDialog__qtablewidgetitem2)
        _Ui_TCPScanDialog__qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, _Ui_TCPScanDialog__qtablewidgetitem3)
        _Ui_TCPScanDialog__qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, _Ui_TCPScanDialog__qtablewidgetitem4)
        _Ui_TCPScanDialog__qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, _Ui_TCPScanDialog__qtablewidgetitem5)
        _Ui_TCPScanDialog__qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, _Ui_TCPScanDialog__qtablewidgetitem6)
        _Ui_TCPScanDialog__qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, _Ui_TCPScanDialog__qtablewidgetitem7)
        self.tableWidget.setObjectName('tableWidget')
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty('showSortIndicator', True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.automaticRescan = QCheckBox(TCPScanDialog)
        self.automaticRescan.setObjectName('automaticRescan')
        self.verticalLayout.addWidget(self.automaticRescan)
        self.buttonBox = QDialogButtonBox(TCPScanDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(TCPScanDialog)
        self.buttonBox.accepted.connect(TCPScanDialog.accept)
        self.buttonBox.rejected.connect(TCPScanDialog.reject)
        QMetaObject.connectSlotsByName(TCPScanDialog)

    
    def retranslateUi(self, TCPScanDialog):
        TCPScanDialog.setWindowTitle(QCoreApplication.translate('TCPScanDialog', 'TCP Devices', None))
        _Ui_TCPScanDialog___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        _Ui_TCPScanDialog___qtablewidgetitem.setText(QCoreApplication.translate('TCPScanDialog', 'Serial', None))
        _Ui_TCPScanDialog___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        _Ui_TCPScanDialog___qtablewidgetitem1.setText(QCoreApplication.translate('TCPScanDialog', 'Tag 1', None))
        _Ui_TCPScanDialog___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        _Ui_TCPScanDialog___qtablewidgetitem2.setText(QCoreApplication.translate('TCPScanDialog', 'Tag 2', None))
        _Ui_TCPScanDialog___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        _Ui_TCPScanDialog___qtablewidgetitem3.setText(QCoreApplication.translate('TCPScanDialog', 'Board Info', None))
        _Ui_TCPScanDialog___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        _Ui_TCPScanDialog___qtablewidgetitem4.setText(QCoreApplication.translate('TCPScanDialog', 'Build Info', None))
        _Ui_TCPScanDialog___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        _Ui_TCPScanDialog___qtablewidgetitem5.setText(QCoreApplication.translate('TCPScanDialog', 'Build Date', None))
        _Ui_TCPScanDialog___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        _Ui_TCPScanDialog___qtablewidgetitem6.setText(QCoreApplication.translate('TCPScanDialog', 'Bootloader', None))
        _Ui_TCPScanDialog___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        _Ui_TCPScanDialog___qtablewidgetitem7.setText(QCoreApplication.translate('TCPScanDialog', 'Available', None))
        self.automaticRescan.setText(QCoreApplication.translate('TCPScanDialog', 'Automatic Rescan', None))


