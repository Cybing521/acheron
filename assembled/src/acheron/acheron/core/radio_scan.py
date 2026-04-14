# Source Generated with Decompyle++
# File: radio_scan.pyc (Python 3.11)

from __future__ import annotations
import logging
from typing import Iterable, Optional, TYPE_CHECKING
from PySide6 import QtCore
from asphodel.device_info import ActiveScanInfo
from .preferences import Preferences
from ..device_process.stream_controller import ScanResult
if TYPE_CHECKING:
    from .device_controller import DeviceController
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ActiveScanDatabase(QtCore.QObject):

    cleared = QtCore.Signal()

    active_scan_ready = QtCore.Signal(int, object)

    remote_connecting = QtCore.Signal(int, object)

    def __init__(self, preferences):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_FAST preferences
        #   70 LOAD_FAST self
        #   72 STORE_ATTR preferences
        #   82 LOAD_FAST self
        #   84 LOAD_ATTR preferences
        #   94 LOAD_ATTR background_active_scan
        #  104 LOAD_FAST self
        #  106 STORE_ATTR active_scan_desired
        #  116 BUILD_MAP
        #  118 LOAD_FAST self
        #  120 STORE_ATTR controller_remotes
        #  130 BUILD_MAP
        #  132 LOAD_FAST self
        #  134 STORE_ATTR active_scan_ongoing
        #  144 BUILD_MAP
        #  146 LOAD_FAST self
        #  148 STORE_ATTR active_scans
        #  158 LOAD_CONST None
        #  160 RETURN_VALUE
        pass

    def controller_disconnected(self, controller):
        try:
            remote = self.controller_remotes.pop(controller)
            self.remote_connecting.emit(remote, None)
        except KeyError:
            pass


        try:
            del self.active_scan_ongoing[controller]
            return None
        except KeyError:
            return None

    def controller_remote_connecting(self, controller, remote, _bootloader):
        self.controller_remotes[controller] = remote
        self.remote_connecting.emit(remote, controller)

    def controller_scans(self, controller, scans):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR controller_remotes
        #   16 LOAD_METHOD pop
        #   38 LOAD_FAST controller
        #   40 PRECALL
        #   44 CALL
        #   54 STORE_FAST remote
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR remote_connecting
        #   68 LOAD_METHOD emit
        #   90 LOAD_FAST remote
        #   92 LOAD_CONST None
        #   94 PRECALL
        #   98 CALL
        #  108 POP_TOP
        #  110 JUMP_FORWARD to 144
        #  112 PUSH_EXC_INFO
        #  114 LOAD_GLOBAL KeyError
        #  126 CHECK_EXC_MATCH
        #  128 POP_JUMP_FORWARD_IF_FALSE to 136
        #  130 POP_TOP
        #  132 POP_EXCEPT
        #  134 JUMP_FORWARD to 144
        #  136 RERAISE
        #  138 COPY
        #  140 POP_EXCEPT
        #  142 RERAISE
        #  144 LOAD_FAST controller
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR active_scan_ongoing
        #  158 CONTAINS_OP
        #  160 POP_JUMP_FORWARD_IF_FALSE to 166
        #  162 LOAD_CONST None
        #  164 RETURN_VALUE
        #  166 LOAD_GLOBAL NULL + set
        #  178 LOAD_FAST self
        #  180 LOAD_ATTR active_scan_ongoing
        #  190 LOAD_METHOD values
        #  212 PRECALL
        #  216 CALL
        #  226 PRECALL
        #  230 CALL
        #  240 STORE_FAST ongoing_scan_serials
        #  242 LOAD_FAST scans
        #  244 GET_ITER
        #  246 FOR_ITER to 446
        #  248 STORE_FAST scan
        #  250 LOAD_FAST scan
        #  252 LOAD_ATTR serial_number
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR active_scans
        #  274 CONTAINS_OP
        #  276 POP_JUMP_FORWARD_IF_FALSE to 280
        #  278 JUMP_BACKWARD to 246
        #  280 LOAD_FAST scan
        #  282 LOAD_ATTR serial_number
        #  292 LOAD_FAST ongoing_scan_serials
        #  294 CONTAINS_OP
        #  296 POP_JUMP_FORWARD_IF_FALSE to 300
        #  298 JUMP_BACKWARD to 246
        #  300 LOAD_FAST scan
        #  302 LOAD_ATTR bootloader
        #  312 POP_JUMP_FORWARD_IF_FALSE to 316
        #  314 JUMP_BACKWARD to 246
        #  316 LOAD_FAST scan
        #  318 LOAD_ATTR board_info
        #  328 POP_JUMP_FORWARD_IF_FALSE to 346
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR active_scan_desired
        #  342 POP_JUMP_FORWARD_IF_TRUE to 346
        #  344 JUMP_BACKWARD to 246
        #  346 LOAD_FAST scan
        #  348 LOAD_ATTR serial_number
        #  358 LOAD_FAST self
        #  360 LOAD_ATTR active_scan_ongoing
        #  370 LOAD_FAST controller
        #  372 STORE_SUBSCR
        #  376 LOAD_FAST controller
        # ... bytecode truncated ...
        pass

    def active_scan_finished(self, controller, remote, active_scan):
        try:
            del self.active_scan_ongoing[controller]
        except KeyError:
            pass

        if active_scan:
            self.active_scans[remote] = active_scan
            self.active_scan_ready.emit(remote, active_scan)
            return None

    def clear_database(self):
        self.active_scans.clear()
        self.cleared.emit()

    def get_remote_controller(self, remote):
        for controller, r in self.controller_remotes.items():
            if r == remote:
                
                return None, controller
            return None

    def get_active_scan(self, remote):
        return self.active_scans.get(remote)

    def detail_scan_opened(self):
        self.active_scan_desired = True

    def detail_scan_closed(self):
        self.active_scan_desired = self.preferences.background_active_scan
