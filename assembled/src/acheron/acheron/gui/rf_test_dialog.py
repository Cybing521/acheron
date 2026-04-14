# Source Generated with Decompyle++
# File: rf_test_dialog.pyc (Python 3.11)

import logging
from typing import Optional, Union
from PySide6 import QtCore, QtWidgets
from ..device_process.stream_controller import RFFixedTestParams, RFSweepTestParams
from .ui.ui_rf_test_dialog import Ui_RFTestDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RFTestDialog(Ui_RFTestDialog, QtWidgets.QDialog):

    def __init__(self, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST parent
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST self
        #   72 LOAD_METHOD setupUi
        #   94 LOAD_FAST self
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_FAST self
        #  114 LOAD_METHOD extra_ui_setup
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 LOAD_CONST None
        #  154 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        self.test_type_group = QtWidgets.QButtonGroup(self)
        self.test_type_group.addButton(self.fixedRadioButton)
        self.test_type_group.addButton(self.sweepRadioButton)
        self.test_mode_group = QtWidgets.QButtonGroup(self)
        self.test_mode_group.addButton(self.txCarrierRadioButton)
        self.test_mode_group.addButton(self.rxCarrierRadioButton)
        self.test_mode_group.addButton(self.txModulatedRadioButton)
        self.fixedChannel.editingFinished.connect(self.check_channels)
        self.startChannel.editingFinished.connect(self.check_channels)
        self.stopChannel.editingFinished.connect(self.check_channels)
        self.fixedChannel.valueChanged.connect(self.update_frequencies)
        self.startChannel.valueChanged.connect(self.update_frequencies)
        self.stopChannel.valueChanged.connect(self.update_frequencies)
        self.fixedRadioButton.setChecked(True)
        self.txCarrierRadioButton.setChecked(True)

    def check_channels(self):
        fixed_channel = self.fixedChannel.value()
        if fixed_channel % 2 != 0:
            fixed_channel -= 1
            self.fixedChannel.setValue(fixed_channel)
        start_channel = self.startChannel.value()
        if start_channel % 2 != 0:
            start_channel -= 1
            self.startChannel.setValue(start_channel)
        stop_channel = self.stopChannel.value()
        if stop_channel % 2 != 0:
            stop_channel -= 1
            self.stopChannel.setValue(stop_channel)
            return None

    def update_frequencies(self):
        fixed_channel = self.fixedChannel.value()
        self.centerFreq.setText('{} MHz'.format(fixed_channel + 2400))
        start_channel = self.startChannel.value()
        self.startFreq.setText('{} MHz'.format(start_channel + 2400))
        stop_channel = self.stopChannel.value()
        self.stopFreq.setText('{} MHz'.format(stop_channel + 2400))

    def get_test_params(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR txCarrierRadioButton
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_FALSE to 58
        #   52 LOAD_CONST 0
        #   54 STORE_FAST mode
        #   56 JUMP_FORWARD to 118
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR rxCarrierRadioButton
        #   70 LOAD_METHOD isChecked
        #   92 PRECALL
        #   96 CALL
        #  106 POP_JUMP_FORWARD_IF_FALSE to 114
        #  108 LOAD_CONST 1
        #  110 STORE_FAST mode
        #  112 JUMP_FORWARD to 118
        #  114 LOAD_CONST 2
        #  116 STORE_FAST mode
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR fixedRadioButton
        #  130 LOAD_METHOD isChecked
        #  152 PRECALL
        #  156 CALL
        #  166 POP_JUMP_FORWARD_IF_FALSE to 296
        #  168 LOAD_GLOBAL NULL + RFFixedTestParams
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR fixedChannel
        #  192 LOAD_METHOD value
        #  214 PRECALL
        #  218 CALL
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR fixedDuration
        #  240 LOAD_METHOD value
        #  262 PRECALL
        #  266 CALL
        #  276 LOAD_FAST mode
        #  278 KW_NAMES
        #  280 PRECALL
        #  284 CALL
        #  294 RETURN_VALUE
        #  296 LOAD_GLOBAL NULL + RFSweepTestParams
        #  308 LOAD_FAST self
        #  310 LOAD_ATTR startChannel
        #  320 LOAD_METHOD value
        #  342 PRECALL
        #  346 CALL
        #  356 LOAD_FAST self
        #  358 LOAD_ATTR stopChannel
        #  368 LOAD_METHOD value
        #  390 PRECALL
        #  394 CALL
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR hopInterval
        #  416 LOAD_METHOD value
        #  438 PRECALL
        #  442 CALL
        #  452 LOAD_FAST self
        #  454 LOAD_ATTR hopCount
        #  464 LOAD_METHOD value
        #  486 PRECALL
        #  490 CALL
        #  500 LOAD_FAST mode
        #  502 KW_NAMES
        #  504 PRECALL
        #  508 CALL
        #  518 RETURN_VALUE
        pass
