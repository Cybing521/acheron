# Source Generated with Decompyle++
# File: tcp_connect_dialog.pyc (Python 3.11)

import logging
from typing import Any, Optional
from PySide6 import QtCore, QtWidgets
from .ui.ui_tcp_connect_dialog import Ui_TCPConnectDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class TCPConnectDialog(Ui_TCPConnectDialog, QtWidgets.QDialog):

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
        #   70 LOAD_GLOBAL NULL + QtCore
        #   82 LOAD_ATTR QSettings
        #   92 PRECALL
        #   96 CALL
        #  106 LOAD_FAST self
        #  108 STORE_ATTR settings
        #  118 LOAD_FAST self
        #  120 LOAD_METHOD setupUi
        #  142 LOAD_FAST self
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST self
        #  162 LOAD_METHOD extra_ui_setup
        #  184 PRECALL
        #  188 CALL
        #  198 POP_TOP
        #  200 LOAD_CONST None
        #  202 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        hostname = self.settings.value('connectHostname')
        if hostname and isinstance(hostname, str):
            self.hostname.setText(hostname.strip())
        port = self.settings.value('connectPort')

    def is_valid(self):
        if not self.hostname.text().strip():
            return False

    def done(self, r):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST r
        #    6 POP_JUMP_FORWARD_IF_FALSE to 52
        #    8 LOAD_FAST self
        #   10 LOAD_METHOD is_valid
        #   32 PRECALL
        #   36 CALL
        #   46 POP_JUMP_FORWARD_IF_TRUE to 52
        #   48 LOAD_CONST None
        #   50 RETURN_VALUE
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR settings
        #   64 LOAD_METHOD setValue
        #   86 LOAD_CONST 'connectHostname'
        #   88 LOAD_FAST self
        #   90 LOAD_ATTR hostname
        #  100 LOAD_METHOD text
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_METHOD strip
        #  158 PRECALL
        #  162 CALL
        #  172 PRECALL
        #  176 CALL
        #  186 POP_TOP
        #  188 LOAD_FAST self
        #  190 LOAD_ATTR settings
        #  200 LOAD_METHOD setValue
        #  222 LOAD_CONST 'connectPort'
        #  224 LOAD_FAST self
        #  226 LOAD_ATTR port
        #  236 LOAD_METHOD value
        #  258 PRECALL
        #  262 CALL
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_FAST self
        #  290 LOAD_ATTR settings
        #  300 LOAD_METHOD setValue
        #  322 LOAD_CONST 'connectSerial'
        #  324 LOAD_FAST self
        #  326 LOAD_ATTR serial
        #  336 LOAD_METHOD text
        #  358 PRECALL
        #  362 CALL
        #  372 LOAD_METHOD strip
        #  394 PRECALL
        #  398 CALL
        #  408 PRECALL
        #  412 CALL
        #  422 POP_TOP
        #  424 LOAD_GLOBAL NULL + super
        #  436 PRECALL
        #  440 CALL
        #  450 LOAD_METHOD done
        #  472 LOAD_FAST r
        #  474 PRECALL
        #  478 CALL
        #  488 POP_TOP
        #  490 LOAD_CONST None
        #  492 RETURN_VALUE
        pass

    def values_updated(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR buttonBox
        #   14 LOAD_METHOD button
        #   36 LOAD_GLOBAL QtWidgets
        #   48 LOAD_ATTR QDialogButtonBox
        #   58 LOAD_ATTR StandardButton
        #   68 LOAD_ATTR Ok
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST ok_button
        #   94 LOAD_FAST self
        #   96 LOAD_METHOD is_valid
        #  118 PRECALL
        #  122 CALL
        #  132 POP_JUMP_FORWARD_IF_FALSE to 180
        #  134 LOAD_FAST ok_button
        #  136 LOAD_METHOD setEnabled
        #  158 LOAD_CONST True
        #  160 PRECALL
        #  164 CALL
        #  174 POP_TOP
        #  176 LOAD_CONST None
        #  178 RETURN_VALUE
        #  180 LOAD_FAST ok_button
        #  182 LOAD_METHOD setEnabled
        #  204 LOAD_CONST False
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        pass

    def get_results(self):
        results = {
            'hostname': self.hostname.text().strip(),
            'port': self.port.value() }
        sn = self.serial.text().strip()
        if len(sn) != 0:
            results['serial_number'] = sn
        else:
            results['serial_number'] = None
        return results
