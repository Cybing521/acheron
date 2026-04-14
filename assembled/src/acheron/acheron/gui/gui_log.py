# Source Generated with Decompyle++
# File: gui_log.pyc (Python 3.11)

from collections import deque
import logging
import logging.handlers
import threading
from typing import Any, Optional, Union
from PySide6 import QtCore
logger = logging.getLogger(__name__)
GUI_LOG_SIZE = 1000

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class GUILogModel(QtCore.QAbstractListModel):

    def __init__(self, global_deque):
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
        #   68 LOAD_GLOBAL NULL + list
        #   80 LOAD_FAST global_deque
        #   82 PRECALL
        #   86 CALL
        #   96 LOAD_FAST self
        #   98 STORE_ATTR list
        #  108 LOAD_GLOBAL NULL + deque
        #  120 LOAD_GLOBAL GUI_LOG_SIZE
        #  132 KW_NAMES
        #  134 PRECALL
        #  138 CALL
        #  148 LOAD_FAST self
        #  150 STORE_ATTR deque
        #  160 LOAD_GLOBAL NULL + threading
        #  172 LOAD_ATTR Lock
        #  182 PRECALL
        #  186 CALL
        #  196 LOAD_FAST self
        #  198 STORE_ATTR lock
        #  208 LOAD_CONST None
        #  210 RETURN_VALUE
        pass

    def log_message(self, message):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR deque
        #   30 LOAD_METHOD append
        #   52 LOAD_FAST message
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_CONST None
        #   72 LOAD_CONST None
        #   74 LOAD_CONST None
        #   76 PRECALL
        #   80 CALL
        #   90 POP_TOP
        #   92 LOAD_CONST None
        #   94 RETURN_VALUE
        #   96 PUSH_EXC_INFO
        #   98 WITH_EXCEPT_START
        #  100 POP_JUMP_FORWARD_IF_TRUE to 110
        #  102 RERAISE
        #  104 COPY
        #  106 POP_EXCEPT
        #  108 RERAISE
        #  110 POP_TOP
        #  112 POP_EXCEPT
        #  114 POP_TOP
        #  116 POP_TOP
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass

    def update_messages(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + list
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR deque
        #   42 PRECALL
        #   46 CALL
        #   56 STORE_FAST new_messages
        #   58 LOAD_FAST new_messages
        #   60 POP_JUMP_FORWARD_IF_TRUE to 90
        #   62 NOP
        #   64 LOAD_CONST None
        #   66 LOAD_CONST None
        #   68 LOAD_CONST None
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 LOAD_CONST None
        #   88 RETURN_VALUE
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR deque
        #  102 LOAD_METHOD clear
        #  124 PRECALL
        #  128 CALL
        #  138 POP_TOP
        #  140 LOAD_CONST None
        #  142 LOAD_CONST None
        #  144 LOAD_CONST None
        #  146 PRECALL
        #  150 CALL
        #  160 POP_TOP
        #  162 JUMP_FORWARD to 186
        #  164 PUSH_EXC_INFO
        #  166 WITH_EXCEPT_START
        #  168 POP_JUMP_FORWARD_IF_TRUE to 178
        #  170 RERAISE
        #  172 COPY
        #  174 POP_EXCEPT
        #  176 RERAISE
        #  178 POP_TOP
        #  180 POP_EXCEPT
        #  182 POP_TOP
        #  184 POP_TOP
        #  186 LOAD_GLOBAL NULL + len
        #  198 LOAD_FAST new_messages
        #  200 PRECALL
        #  204 CALL
        #  214 STORE_FAST messages_len
        #  216 LOAD_FAST messages_len
        #  218 LOAD_GLOBAL NULL + len
        #  230 LOAD_FAST self
        #  232 LOAD_ATTR list
        #  242 PRECALL
        #  246 CALL
        #  256 BINARY_OP +
        #  260 LOAD_GLOBAL GUI_LOG_SIZE
        #  272 BINARY_OP -
        #  276 STORE_FAST remove_count
        #  278 LOAD_FAST remove_count
        #  280 LOAD_CONST 0
        #  282 COMPARE_OP >
        #  288 POP_JUMP_FORWARD_IF_FALSE to 436
        #  290 LOAD_FAST self
        #  292 LOAD_METHOD beginRemoveRows
        #  314 LOAD_GLOBAL NULL + QtCore
        #  326 LOAD_ATTR QModelIndex
        #  336 PRECALL
        #  340 CALL
        #  350 LOAD_CONST 0
        #  352 LOAD_FAST remove_count
        #  354 LOAD_CONST 1
        #  356 BINARY_OP -
        #  360 PRECALL
        #  364 CALL
        #  374 POP_TOP
        #  376 LOAD_FAST self
        #  378 LOAD_ATTR list
        # ... bytecode truncated ...
        pass

    def rowCount(self, parent):
        return len(self.list)

    def data(self, index, role):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST index
        #    4 LOAD_METHOD row
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST row
        #   42 LOAD_FAST row
        #   44 LOAD_CONST 0
        #   46 COMPARE_OP <
        #   52 POP_JUMP_FORWARD_IF_TRUE to 102
        #   54 LOAD_FAST row
        #   56 LOAD_GLOBAL NULL + len
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR list
        #   80 PRECALL
        #   84 CALL
        #   94 COMPARE_OP >=
        #  100 POP_JUMP_FORWARD_IF_FALSE to 106
        #  102 LOAD_CONST ''
        #  104 RETURN_VALUE
        #  106 LOAD_FAST role
        #  108 LOAD_GLOBAL QtCore
        #  120 LOAD_ATTR Qt
        #  130 LOAD_ATTR ItemDataRole
        #  140 LOAD_ATTR DisplayRole
        #  150 COMPARE_OP ==
        #  156 POP_JUMP_FORWARD_IF_TRUE to 210
        #  158 LOAD_FAST role
        #  160 LOAD_GLOBAL QtCore
        #  172 LOAD_ATTR Qt
        #  182 LOAD_ATTR ItemDataRole
        #  192 LOAD_ATTR EditRole
        #  202 COMPARE_OP ==
        #  208 POP_JUMP_FORWARD_IF_FALSE to 236
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR list
        #  222 LOAD_FAST row
        #  224 BINARY_SUBSCR
        #  234 RETURN_VALUE
        #  236 LOAD_CONST None
        #  238 RETURN_VALUE
        pass

class GUILogHandler(logging.Handler):

    def __init__(self):
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
        #   68 LOAD_GLOBAL NULL + QtCore
        #   80 LOAD_ATTR QTimer
        #   90 PRECALL
        #   94 CALL
        #  104 LOAD_FAST self
        #  106 STORE_ATTR timer
        #  116 LOAD_FAST self
        #  118 LOAD_ATTR timer
        #  128 LOAD_ATTR timeout
        #  138 LOAD_METHOD connect
        #  160 LOAD_FAST self
        #  162 LOAD_ATTR timer_cb
        #  172 PRECALL
        #  176 CALL
        #  186 POP_TOP
        #  188 LOAD_FAST self
        #  190 LOAD_ATTR timer
        #  200 LOAD_METHOD start
        #  222 LOAD_CONST 20
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 LOAD_CONST None
        #  242 RETURN_VALUE
        pass

    def emit(self, record):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD format
        #   26 LOAD_FAST record
        #   28 PRECALL
        #   32 CALL
        #   42 STORE_FAST message
        #   44 NOP
        #   46 LOAD_FAST record
        #   48 LOAD_ATTR serial_number
        #   58 STORE_FAST serial_number
        #   60 NOP
        #   62 LOAD_GLOBAL _models
        #   74 LOAD_FAST serial_number
        #   76 BINARY_SUBSCR
        #   86 STORE_FAST model
        #   88 JUMP_FORWARD to 182
        #   90 PUSH_EXC_INFO
        #   92 LOAD_GLOBAL KeyError
        #  104 CHECK_EXC_MATCH
        #  106 POP_JUMP_FORWARD_IF_FALSE to 174
        #  108 POP_TOP
        #  110 LOAD_GLOBAL NULL + GUILogModel
        #  122 LOAD_GLOBAL _global_deque
        #  134 PRECALL
        #  138 CALL
        #  148 STORE_FAST model
        #  150 LOAD_FAST model
        #  152 LOAD_GLOBAL _models
        #  164 LOAD_FAST serial_number
        #  166 STORE_SUBSCR
        #  170 POP_EXCEPT
        #  172 JUMP_FORWARD to 182
        #  174 RERAISE
        #  176 COPY
        #  178 POP_EXCEPT
        #  180 RERAISE
        #  182 LOAD_FAST model
        #  184 LOAD_METHOD log_message
        #  206 LOAD_FAST message
        #  208 PRECALL
        #  212 CALL
        #  222 POP_TOP
        #  224 LOAD_CONST None
        #  226 RETURN_VALUE
        #  228 PUSH_EXC_INFO
        #  230 LOAD_GLOBAL AttributeError
        #  242 CHECK_EXC_MATCH
        #  244 POP_JUMP_FORWARD_IF_FALSE to 404
        #  246 POP_TOP
        #  248 LOAD_GLOBAL _global_deque
        #  260 LOAD_METHOD append
        #  282 LOAD_FAST message
        #  284 PRECALL
        #  288 CALL
        #  298 POP_TOP
        #  300 LOAD_GLOBAL _models
        #  312 LOAD_METHOD values
        #  334 PRECALL
        #  338 CALL
        #  348 GET_ITER
        #  350 FOR_ITER to 398
        #  352 STORE_FAST model
        #  354 LOAD_FAST model
        #  356 LOAD_METHOD log_message
        #  378 LOAD_FAST message
        #  380 PRECALL
        #  384 CALL
        #  394 POP_TOP
        #  396 JUMP_BACKWARD to 350
        #  398 POP_EXCEPT
        #  400 LOAD_CONST None
        #  402 RETURN_VALUE
        #  404 RERAISE
        #  406 COPY
        #  408 POP_EXCEPT
        #  410 RERAISE
        pass

    def timer_cb(self):
        for serial_number, model in _models.items():
            model.update_messages()

def get_log_list_model(serial_number):
    try:
        model = _models[serial_number]
    except KeyError:
        model = GUILogModel(_global_deque)
        _models[serial_number] = model

    return model
