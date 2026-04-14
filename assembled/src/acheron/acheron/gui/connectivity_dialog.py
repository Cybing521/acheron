# Source Generated with Decompyle++
# File: connectivity_dialog.pyc (Python 3.11)

import logging
import os
import re
from xml.dom.minidom import getDOMImplementation
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
from hyperborea.preferences import read_int_setting
from ..connectivity.modbus import get_numeric_serial
from ..calc_process.types import ChannelInformation
from ..core.preferences import DevicePreferences
from .ui.ui_connectivity_dialog import Ui_ConnectivityDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ConnectivityDialog(Ui_ConnectivityDialog, QtWidgets.QDialog):

    def __init__(self, serial_number, device_info, channel_info, device_prefs, parent):
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
        #   70 LOAD_FAST serial_number
        #   72 LOAD_FAST self
        #   74 STORE_ATTR serial_number
        #   84 LOAD_FAST device_info
        #   86 LOAD_FAST self
        #   88 STORE_ATTR device_info
        #   98 LOAD_GLOBAL NULL + get_numeric_serial
        #  110 LOAD_FAST serial_number
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_FAST self
        #  128 STORE_ATTR numeric_serial_number
        #  138 LOAD_FAST channel_info
        #  140 LOAD_FAST self
        #  142 STORE_ATTR channel_info
        #  152 LOAD_FAST device_prefs
        #  154 LOAD_FAST self
        #  156 STORE_ATTR device_prefs
        #  166 LOAD_GLOBAL NULL + QtCore
        #  178 LOAD_ATTR QSettings
        #  188 PRECALL
        #  192 CALL
        #  202 LOAD_FAST self
        #  204 STORE_ATTR settings
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR settings
        #  226 LOAD_METHOD beginGroup
        #  248 LOAD_FAST self
        #  250 LOAD_ATTR serial_number
        #  260 PRECALL
        #  264 CALL
        #  274 POP_TOP
        #  276 BUILD_MAP
        #  278 LOAD_FAST self
        #  280 STORE_ATTR setting_names
        #  290 LOAD_FAST self
        #  292 LOAD_METHOD setupUi
        #  314 LOAD_FAST self
        #  316 PRECALL
        #  320 CALL
        #  330 POP_TOP
        #  332 LOAD_FAST self
        #  334 LOAD_METHOD add_channel_check_boxes
        #  356 PRECALL
        #  360 CALL
        #  370 POP_TOP
        #  372 LOAD_FAST self
        #  374 LOAD_METHOD read_settings
        #  396 PRECALL
        #  400 CALL
        #  410 POP_TOP
        #  412 LOAD_FAST self
        #  414 LOAD_ATTR accepted
        #  424 LOAD_METHOD connect
        #  446 LOAD_FAST self
        #  448 LOAD_ATTR write_settings
        #  458 PRECALL
        #  462 CALL
        #  472 POP_TOP
        #  474 LOAD_FAST self
        #  476 LOAD_ATTR modbusDetails
        #  486 LOAD_ATTR clicked
        #  496 LOAD_METHOD connect
        #  518 LOAD_FAST self
        #  520 LOAD_ATTR show_modbus_details
        #  530 PRECALL
        #  534 CALL
        #  544 POP_TOP
        #  546 LOAD_CONST None
        #  548 RETURN_VALUE
        pass

    def add_channel_check_boxes(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL sort_keys
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + re
        #   16 LOAD_ATTR compile
        #   26 LOAD_CONST 'Channel([0-9]+)_([0-9]+)_Port'
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST pattern
        #   44 BUILD_MAP
        #   46 STORE_DEREF sort_keys
        #   48 LOAD_CONST 0
        #   50 STORE_FAST total_channels
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR channel_info
        #   64 LOAD_METHOD values
        #   86 PRECALL
        #   90 CALL
        #  100 GET_ITER
        #  102 FOR_ITER to 394
        #  104 STORE_FAST channel_info
        #  106 LOAD_GLOBAL NULL + enumerate
        #  118 LOAD_FAST channel_info
        #  120 LOAD_ATTR subchannel_names
        #  130 PRECALL
        #  134 CALL
        #  144 GET_ITER
        #  146 FOR_ITER to 392
        #  148 UNPACK_SEQUENCE
        #  152 STORE_FAST i
        #  154 STORE_FAST subchannel
        #  156 LOAD_CONST 'Channel{}_{}_Port'
        #  158 LOAD_METHOD format
        #  180 LOAD_FAST channel_info
        #  182 LOAD_ATTR channel_id
        #  192 LOAD_FAST i
        #  194 PRECALL
        #  198 CALL
        #  208 STORE_FAST setting_name
        #  210 LOAD_GLOBAL NULL + QtWidgets
        #  222 LOAD_ATTR QCheckBox
        #  232 LOAD_FAST self
        #  234 PRECALL
        #  238 CALL
        #  248 STORE_FAST checkbox
        #  250 LOAD_FAST checkbox
        #  252 LOAD_METHOD setText
        #  274 LOAD_FAST subchannel
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_GLOBAL NULL + QtWidgets
        #  304 LOAD_ATTR QSpinBox
        #  314 LOAD_FAST self
        #  316 PRECALL
        #  320 CALL
        #  330 STORE_FAST spinbox
        #  332 LOAD_FAST checkbox
        #  334 LOAD_FAST spinbox
        #  336 BUILD_TUPLE
        #  338 LOAD_FAST self
        #  340 LOAD_ATTR setting_names
        #  350 LOAD_FAST setting_name
        #  352 STORE_SUBSCR
        #  356 LOAD_FAST channel_info
        #  358 LOAD_ATTR channel_id
        #  368 LOAD_FAST i
        #  370 BUILD_TUPLE
        #  372 LOAD_DEREF sort_keys
        #  374 LOAD_FAST setting_name
        #  376 STORE_SUBSCR
        #  380 LOAD_FAST total_channels
        #  382 LOAD_CONST 1
        #  384 BINARY_OP +=
        #  388 STORE_FAST total_channels
        #  390 JUMP_BACKWARD to 146
        #  392 JUMP_BACKWARD to 102
        #  394 LOAD_FAST self
        #  396 LOAD_ATTR modbusChannelCount
        #  406 LOAD_METHOD setText
        #  428 LOAD_GLOBAL NULL + str
        # ... bytecode truncated ...
        pass

    def done(self, r):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + set
        #   16 PRECALL
        #   20 CALL
        #   30 STORE_FAST chosen_ports
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR setting_names
        #   44 LOAD_METHOD items
        #   66 PRECALL
        #   70 CALL
        #   80 GET_ITER
        #   82 FOR_ITER to 382
        #   84 UNPACK_SEQUENCE
        #   88 STORE_FAST _setting_name
        #   90 UNPACK_SEQUENCE
        #   94 STORE_FAST checkbox
        #   96 STORE_FAST spinbox
        #   98 LOAD_FAST checkbox
        #  100 LOAD_METHOD isChecked
        #  122 PRECALL
        #  126 CALL
        #  136 POP_JUMP_FORWARD_IF_FALSE to 380
        #  138 LOAD_FAST spinbox
        #  140 LOAD_METHOD value
        #  162 PRECALL
        #  166 CALL
        #  176 STORE_FAST port
        #  178 LOAD_FAST port
        #  180 LOAD_FAST chosen_ports
        #  182 CONTAINS_OP
        #  184 POP_JUMP_FORWARD_IF_FALSE to 338
        #  186 LOAD_FAST self
        #  188 LOAD_METHOD tr
        #  210 LOAD_CONST 'Cannot have duplicate ports!'
        #  212 PRECALL
        #  216 CALL
        #  226 STORE_FAST m
        #  228 LOAD_GLOBAL QtWidgets
        #  240 LOAD_ATTR QMessageBox
        #  250 LOAD_METHOD warning
        #  272 LOAD_FAST self
        #  274 LOAD_FAST self
        #  276 LOAD_METHOD tr
        #  298 LOAD_CONST 'Error'
        #  300 PRECALL
        #  304 CALL
        #  314 LOAD_FAST m
        #  316 PRECALL
        #  320 CALL
        #  330 POP_TOP
        #  332 POP_TOP
        #  334 LOAD_CONST None
        #  336 RETURN_VALUE
        #  338 LOAD_FAST chosen_ports
        #  340 LOAD_METHOD add
        #  362 LOAD_FAST port
        #  364 PRECALL
        #  368 CALL
        #  378 POP_TOP
        #  380 JUMP_BACKWARD to 82
        #  382 LOAD_GLOBAL NULL + super
        #  394 PRECALL
        #  398 CALL
        #  408 LOAD_METHOD done
        #  430 LOAD_FAST r
        #  432 PRECALL
        #  436 CALL
        #  446 POP_TOP
        #  448 LOAD_CONST None
        #  450 RETURN_VALUE
        pass

    def read_settings(self):
        self.modbusCheckBox.setChecked(self.device_prefs.modbus_enable)
        self.modbusOffset.setValue(self.device_prefs.modbus_register_offset)
        for checkbox, spinbox in self.setting_names.items():
            port = read_int_setting(self.settings, setting_name, 0)
            if not port:
                checkbox.setChecked(False)
                spinbox.setValue(12345)
                continue
            checkbox.setChecked(True)
            spinbox.setValue(port)
            return None

    def write_settings(self):
        self.device_prefs.modbus_enable = self.modbusCheckBox.isChecked()
        self.device_prefs.modbus_register_offset = self.modbusOffset.value()
        for checkbox, spinbox in self.setting_names.items():
            if checkbox.isChecked():
                port = spinbox.value()
                self.settings.setValue(setting_name, port)
                continue
            self.settings.remove(setting_name)
            return None

    def show_modbus_details(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + getDOMImplementation
        #   14 PRECALL
        #   18 CALL
        #   28 STORE_FAST impl
        #   30 LOAD_FAST impl
        #   32 POP_JUMP_FORWARD_IF_TRUE to 236
        #   34 LOAD_FAST self
        #   36 LOAD_METHOD tr
        #   58 LOAD_CONST 'Error loading serializer!'
        #   60 PRECALL
        #   64 CALL
        #   74 STORE_FAST m
        #   76 LOAD_GLOBAL QtWidgets
        #   88 LOAD_ATTR QMessageBox
        #   98 LOAD_METHOD critical
        #  120 LOAD_FAST self
        #  122 LOAD_FAST self
        #  124 LOAD_METHOD tr
        #  146 LOAD_CONST 'Error'
        #  148 PRECALL
        #  152 CALL
        #  162 LOAD_FAST m
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_GLOBAL logger
        #  192 LOAD_METHOD error
        #  214 LOAD_FAST m
        #  216 PRECALL
        #  220 CALL
        #  230 POP_TOP
        #  232 LOAD_CONST None
        #  234 RETURN_VALUE
        #  236 LOAD_FAST impl
        #  238 LOAD_METHOD createDocumentType
        #  260 LOAD_CONST 'html'
        #  262 LOAD_CONST '-//W3C//DTD XHTML 1.0 Strict//EN'
        #  264 LOAD_CONST 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'
        #  266 PRECALL
        #  270 CALL
        #  280 STORE_FAST dt
        #  282 LOAD_FAST impl
        #  284 LOAD_METHOD createDocument
        #  306 LOAD_CONST 'http://www.w3.org/1999/xhtml'
        #  308 LOAD_CONST 'html'
        #  310 LOAD_FAST dt
        #  312 PRECALL
        #  316 CALL
        #  326 STORE_FAST dom
        #  328 LOAD_FAST dom
        #  330 LOAD_ATTR documentElement
        #  340 STORE_FAST html
        #  342 LOAD_FAST dom
        #  344 LOAD_METHOD createElement
        #  366 LOAD_CONST 'head'
        #  368 PRECALL
        #  372 CALL
        #  382 STORE_FAST head
        #  384 LOAD_FAST html
        #  386 LOAD_METHOD appendChild
        #  408 LOAD_FAST head
        #  410 PRECALL
        #  414 CALL
        #  424 POP_TOP
        #  426 LOAD_FAST dom
        #  428 LOAD_METHOD createElement
        #  450 LOAD_CONST 'title'
        #  452 PRECALL
        #  456 CALL
        #  466 STORE_FAST title
        #  468 LOAD_FAST self
        #  470 LOAD_ATTR serial_number
        #  480 FORMAT_VALUE
        #  482 LOAD_CONST ' Modbus Details'
        #  484 BUILD_STRING
        #  486 STORE_FAST title_string
        #  488 LOAD_FAST title
        #  490 LOAD_METHOD appendChild
        #  512 LOAD_FAST dom
        # ... bytecode truncated ...
        pass
