# Source Generated with Decompyle++
# File: tmpm9aomb2o.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QDialog, QDialogButtonBox, QGridLayout, QLabel, QRadioButton, QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout, QWidget
from hyperborea.unit_preferences import UnitPreferencesWidget

class Ui_PreferencesDialog(object):
    
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName('PreferencesDialog')
        PreferencesDialog.resize(414, 379)
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName('verticalLayout')
        self.tabWidget = QTabWidget(PreferencesDialog)
        self.tabWidget.setObjectName('tabWidget')
        self.interfaceTab = QWidget()
        self.interfaceTab.setObjectName('interfaceTab')
        self.gridLayout_2 = QGridLayout(self.interfaceTab)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.ledsLabel_2 = QLabel(self.interfaceTab)
        self.ledsLabel_2.setObjectName('ledsLabel_2')
        font = QFont()
        font.setBold(True)
        self.ledsLabel_2.setFont(font)
        self.gridLayout_2.addWidget(self.ledsLabel_2, 0, 0, 1, 2)
        self.horizontalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)
        self.darkMode = QRadioButton(self.interfaceTab)
        self.darkMode.setObjectName('darkMode')
        self.gridLayout_2.addWidget(self.darkMode, 1, 1, 1, 1)
        self.lightMode = QRadioButton(self.interfaceTab)
        self.lightMode.setObjectName('lightMode')
        self.gridLayout_2.addWidget(self.lightMode, 2, 1, 1, 1)
        self.verticalSpacer_12 = QSpacerItem(369, 220, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(self.verticalSpacer_12, 3, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.tabWidget.addTab(self.interfaceTab, '')
        self.unitTab = QWidget()
        self.unitTab.setObjectName('unitTab')
        self.gridLayout = QGridLayout(self.unitTab)
        self.gridLayout.setObjectName('gridLayout')
        self.unitsLabel = QLabel(self.unitTab)
        self.unitsLabel.setObjectName('unitsLabel')
        self.unitsLabel.setFont(font)
        self.gridLayout.addWidget(self.unitsLabel, 0, 0, 1, 2)
        self.horizontalSpacer = QSpacerItem(20, 13, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)
        self.verticalSpacer_7 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_7, 4, 0, 1, 2)
        self.unitPreferences = UnitPreferencesWidget(self.unitTab)
        self.unitPreferences.setObjectName('unitPreferences')
        self.gridLayout.addWidget(self.unitPreferences, 1, 1, 1, 1)
        self.tabWidget.addTab(self.unitTab, '')
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.buttonBox)
        QWidget.setTabOrder(self.tabWidget, self.buttonBox)
        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(PreferencesDialog)

    
    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate('PreferencesDialog', 'Preferences', None))
        self.ledsLabel_2.setText(QCoreApplication.translate('PreferencesDialog', 'Display Mode', None))
        self.darkMode.setText(QCoreApplication.translate('PreferencesDialog', 'Dark Mode', None))
        self.lightMode.setText(QCoreApplication.translate('PreferencesDialog', 'Light Mode', None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.interfaceTab), QCoreApplication.translate('PreferencesDialog', 'Interface', None))
        self.unitsLabel.setText(QCoreApplication.translate('PreferencesDialog', 'Display Units', None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unitTab), QCoreApplication.translate('PreferencesDialog', 'Units', None))


