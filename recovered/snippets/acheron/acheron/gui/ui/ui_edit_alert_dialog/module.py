# Source Generated with Decompyle++
# File: tmpyran2qly.marshal (Python 3.11)

from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt
from PySide6.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide6.QtWidgets import QAbstractButton, QApplication, QCheckBox, QDialog, QDialogButtonBox, QFormLayout, QSizePolicy, QWidget
from hyperborea.unit_formatter_spinbox import UnitFormatterDoubleSpinBox

class Ui_EditAlertDialog(object):
    
    def setupUi(self, EditAlertDialog):
        if not EditAlertDialog.objectName():
            EditAlertDialog.setObjectName('EditAlertDialog')
        EditAlertDialog.resize(323, 145)
        self.formLayout = QFormLayout(EditAlertDialog)
        self.formLayout.setObjectName('formLayout')
        self.meanHighEnabled = QCheckBox(EditAlertDialog)
        self.meanHighEnabled.setObjectName('meanHighEnabled')
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.meanHighEnabled)
        self.meanHigh = UnitFormatterDoubleSpinBox(EditAlertDialog)
        self.meanHigh.setObjectName('meanHigh')
        self.meanHigh.setEnabled(False)
        self.meanHigh.setMinimumSize(QSize(200, 0))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.meanHigh)
        self.meanLowEnabled = QCheckBox(EditAlertDialog)
        self.meanLowEnabled.setObjectName('meanLowEnabled')
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.meanLowEnabled)
        self.meanLow = UnitFormatterDoubleSpinBox(EditAlertDialog)
        self.meanLow.setObjectName('meanLow')
        self.meanLow.setEnabled(False)
        self.meanLow.setMinimumSize(QSize(200, 0))
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.meanLow)
        self.stdHighEnabled = QCheckBox(EditAlertDialog)
        self.stdHighEnabled.setObjectName('stdHighEnabled')
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.stdHighEnabled)
        self.stdHigh = UnitFormatterDoubleSpinBox(EditAlertDialog)
        self.stdHigh.setObjectName('stdHigh')
        self.stdHigh.setEnabled(False)
        self.stdHigh.setMinimumSize(QSize(200, 0))
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.stdHigh)
        self.stdLowEnabled = QCheckBox(EditAlertDialog)
        self.stdLowEnabled.setObjectName('stdLowEnabled')
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.stdLowEnabled)
        self.stdLow = UnitFormatterDoubleSpinBox(EditAlertDialog)
        self.stdLow.setObjectName('stdLow')
        self.stdLow.setEnabled(False)
        self.stdLow.setMinimumSize(QSize(200, 0))
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.stdLow)
        self.buttonBox = QDialogButtonBox(EditAlertDialog)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.buttonBox)
        self.retranslateUi(EditAlertDialog)
        self.buttonBox.accepted.connect(EditAlertDialog.accept)
        self.buttonBox.rejected.connect(EditAlertDialog.reject)
        self.meanHighEnabled.toggled.connect(self.meanHigh.setEnabled)
        self.meanLowEnabled.toggled.connect(self.meanLow.setEnabled)
        self.stdHighEnabled.toggled.connect(self.stdHigh.setEnabled)
        self.stdLowEnabled.toggled.connect(self.stdLow.setEnabled)
        QMetaObject.connectSlotsByName(EditAlertDialog)

    
    def retranslateUi(self, EditAlertDialog):
        EditAlertDialog.setWindowTitle(QCoreApplication.translate('EditAlertDialog', 'Edit Alerts', None))
        self.meanHighEnabled.setText(QCoreApplication.translate('EditAlertDialog', 'Mean High Alert', None))
        self.meanLowEnabled.setText(QCoreApplication.translate('EditAlertDialog', 'Mean Low Alert', None))
        self.stdHighEnabled.setText(QCoreApplication.translate('EditAlertDialog', 'Std High Alert', None))
        self.stdLowEnabled.setText(QCoreApplication.translate('EditAlertDialog', 'Std Low Alert', None))


