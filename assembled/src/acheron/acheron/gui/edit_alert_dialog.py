# Source Generated with Decompyle++
# File: edit_alert_dialog.pyc (Python 3.11)

import logging
import math
from typing import Optional
from PySide6 import QtWidgets
import asphodel
from ..calc_process.types import LimitType
from .ui.ui_edit_alert_dialog import Ui_EditAlertDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class EditAlertDialog(Ui_EditAlertDialog, QtWidgets.QDialog):

    def __init__(self, alert_limits, unit_formatter, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST unit_formatter
        #    6 LOAD_FAST self
        #    8 STORE_ATTR unit_formatter
        #   18 LOAD_GLOBAL NULL + super
        #   30 PRECALL
        #   34 CALL
        #   44 LOAD_METHOD __init__
        #   66 LOAD_FAST parent
        #   68 PRECALL
        #   72 CALL
        #   82 POP_TOP
        #   84 LOAD_FAST self
        #   86 LOAD_METHOD setupUi
        #  108 LOAD_FAST self
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_FAST self
        #  128 LOAD_METHOD extra_ui_setup
        #  150 LOAD_FAST alert_limits
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_CONST None
        #  170 RETURN_VALUE
        pass

    def extra_ui_setup(self, alert_limits):
        mean_formatter = asphodel.nativelib.create_custom_unit_formatter(self.unit_formatter.conversion_scale, self.unit_formatter.conversion_offset, 0, self.unit_formatter.unit_ascii, self.unit_formatter.unit_utf8, self.unit_formatter.unit_html)
        std_formatter = asphodel.nativelib.create_custom_unit_formatter(self.unit_formatter.conversion_scale, 0, 0, self.unit_formatter.unit_ascii, self.unit_formatter.unit_utf8, self.unit_formatter.unit_html)
        self.meanHigh.set_unit_formatter(mean_formatter)
        self.meanLow.set_unit_formatter(mean_formatter)
        self.stdHigh.set_unit_formatter(std_formatter)
        self.stdLow.set_unit_formatter(std_formatter)
        self.meanHigh.setMaximum(math.inf)
        self.meanHigh.setMinimum(-(math.inf))
        self.meanLow.setMaximum(math.inf)
        self.meanLow.setMinimum(-(math.inf))
        self.stdHigh.setMaximum(math.inf)
        self.stdHigh.setMinimum(0)
        self.stdLow.setMaximum(math.inf)
        self.stdLow.setMinimum(0)
        self.limit_type_widgets = ((LimitType.MEAN_HIGH_LIMIT, self.meanHighEnabled, self.meanHigh), (LimitType.MEAN_LOW_LIMIT, self.meanLowEnabled, self.meanLow), (LimitType.STD_HIGH_LIMIT, self.stdHighEnabled, self.stdHigh), (LimitType.STD_LOW_LIMIT, self.stdLowEnabled, self.stdLow))

    def get_alert_limits(self):
        alert_limits = { }
        for limit_type, enabled, spinbox in self.limit_type_widgets:
            if enabled.isChecked():
                alert_limits[limit_type] = spinbox.value()
            return alert_limits
