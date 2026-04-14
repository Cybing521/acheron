# Source Generated with Decompyle++
# File: update_func_limiter.pyc (Python 3.11)

import logging
import time
from typing import Any, Callable, Optional
from PySide6 import QtCore
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: SetFunction = Callable[([
# INVALID FROM DECOMPILER:     Any], None)]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class UpdateFuncLimiter:

    def __init__(self, set_func, update_ms, parent):
        self.set_func = set_func
        self.update_delay = update_ms / 1000
        self.last_set_time = None
        self.next_value = None
        self.timer = QtCore.QTimer(parent)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_cb)

    def update(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR next_value
        #   14 LOAD_FAST value
        #   16 COMPARE_OP ==
        #   22 POP_JUMP_FORWARD_IF_FALSE to 32
        #   24 LOAD_FAST value
        #   26 POP_JUMP_FORWARD_IF_NONE to 32
        #   28 LOAD_CONST None
        #   30 RETURN_VALUE
        #   32 LOAD_FAST value
        #   34 LOAD_FAST self
        #   36 STORE_ATTR next_value
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR timer
        #   58 LOAD_METHOD isActive
        #   80 PRECALL
        #   84 CALL
        #   94 POP_JUMP_FORWARD_IF_TRUE to 402
        #   96 LOAD_GLOBAL NULL + time
        #  108 LOAD_ATTR monotonic
        #  118 PRECALL
        #  122 CALL
        #  132 STORE_FAST now
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR last_set_time
        #  146 POP_JUMP_FORWARD_IF_NONE to 186
        #  148 LOAD_FAST self
        #  150 LOAD_ATTR last_set_time
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR update_delay
        #  172 BINARY_OP +
        #  176 LOAD_FAST now
        #  178 COMPARE_OP <
        #  184 POP_JUMP_FORWARD_IF_FALSE to 246
        #  186 LOAD_FAST now
        #  188 LOAD_FAST self
        #  190 STORE_ATTR last_set_time
        #  200 LOAD_FAST self
        #  202 LOAD_METHOD set_func
        #  224 LOAD_FAST value
        #  226 PRECALL
        #  230 CALL
        #  240 POP_TOP
        #  242 LOAD_CONST None
        #  244 RETURN_VALUE
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR last_set_time
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR update_delay
        #  270 BINARY_OP +
        #  274 LOAD_FAST now
        #  276 BINARY_OP -
        #  280 STORE_FAST delay
        #  282 LOAD_GLOBAL NULL + max
        #  294 LOAD_CONST 0
        #  296 LOAD_GLOBAL NULL + int
        #  308 LOAD_FAST delay
        #  310 LOAD_CONST 1000
        #  312 BINARY_OP *
        #  316 PRECALL
        #  320 CALL
        #  330 PRECALL
        #  334 CALL
        #  344 STORE_FAST delay_ms
        #  346 LOAD_FAST self
        #  348 LOAD_ATTR timer
        #  358 LOAD_METHOD start
        #  380 LOAD_FAST delay_ms
        #  382 PRECALL
        #  386 CALL
        #  396 POP_TOP
        #  398 LOAD_CONST None
        #  400 RETURN_VALUE
        #  402 LOAD_CONST None
        #  404 RETURN_VALUE
        pass

    def timer_cb(self):
        self.last_set_time = time.monotonic()
        self.set_func(self.next_value)
