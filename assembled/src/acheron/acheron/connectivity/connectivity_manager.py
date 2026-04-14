# Source Generated with Decompyle++
# File: connectivity_manager.pyc (Python 3.11)

import logging
import multiprocessing
from multiprocessing.connection import Connection, wait
import threading
from typing import Callable, Optional, Protocol
import numpy
from numpy.typing import NDArray
from ..calc_process.types import ChannelInformation
from ..core.preferences import Preferences
logger = logging.getLogger(__name__)
DeviceCallback = Callable[[int, NDArray[numpy.float64]], None]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ConnectivityHandler(Protocol):

    def stop_device(self, serial_number):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def get_device_callback(self, serial_number, channel_info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def stop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def join(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def update_preferences(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

class ConnectivityManager:

    def __init__(self, preferences):
        self.preferences = preferences
        self.stopped = False
        self.pipe_lock = threading.Lock()
        self.all_pipes = set()
        self.pipe_callbacks = { }
        self.device_pipes = { }
        self.pipe_thread_finished = threading.Event()
        self.pipe_thread = threading.Thread(target = self._pipe_loop)
        self.pipe_thread.start()
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def stop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST True
        #    4 LOAD_FAST self
        #    6 STORE_ATTR stopped
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR handlers
        #   28 GET_ITER
        #   30 FOR_ITER to 76
        #   32 STORE_FAST handler
        #   34 LOAD_FAST handler
        #   36 LOAD_METHOD stop
        #   58 PRECALL
        #   62 CALL
        #   72 POP_TOP
        #   74 JUMP_BACKWARD to 30
        #   76 LOAD_FAST self
        #   78 LOAD_ATTR pipe_lock
        #   88 BEFORE_WITH
        #   90 POP_TOP
        #   92 LOAD_FAST self
        #   94 LOAD_ATTR device_pipes
        #  104 LOAD_METHOD clear
        #  126 PRECALL
        #  130 CALL
        #  140 POP_TOP
        #  142 LOAD_FAST self
        #  144 LOAD_ATTR pipe_callbacks
        #  154 LOAD_METHOD clear
        #  176 PRECALL
        #  180 CALL
        #  190 POP_TOP
        #  192 LOAD_CONST None
        #  194 LOAD_CONST None
        #  196 LOAD_CONST None
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_CONST None
        #  216 RETURN_VALUE
        #  218 PUSH_EXC_INFO
        #  220 WITH_EXCEPT_START
        #  222 POP_JUMP_FORWARD_IF_TRUE to 232
        #  224 RERAISE
        #  226 COPY
        #  228 POP_EXCEPT
        #  230 RERAISE
        #  232 POP_TOP
        #  234 POP_EXCEPT
        #  236 POP_TOP
        #  238 POP_TOP
        #  240 LOAD_CONST None
        #  242 RETURN_VALUE
        pass

    def join(self):
        for handler in self.handlers:
            handler.join()
            self.pipe_thread_finished.set()
            self.pipe_thread.join()
            return None

    def create_device_pipe(self, serial_number, channel_info):
        self.stop_device(serial_number)
        if self.stopped:
            return None
        callbacks = None

    def stop_device(self, serial_number):
        self.pipe_lock
        pipe = self.device_pipes.pop(serial_number, None)

    def update_preferences(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR stopped
        #   14 POP_JUMP_FORWARD_IF_FALSE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR handlers
        #   32 GET_ITER
        #   34 FOR_ITER to 80
        #   36 STORE_FAST handler
        #   38 LOAD_FAST handler
        #   40 LOAD_METHOD update_preferences
        #   62 PRECALL
        #   66 CALL
        #   76 POP_TOP
        #   78 JUMP_BACKWARD to 34
        #   80 LOAD_CONST None
        #   82 RETURN_VALUE
        pass

    def _remove_pipe(self, pipe):
        self.all_pipes.discard(pipe)
        self.pipe_callbacks.pop(pipe, None)
        for serial_number, other_pipe in self.device_pipes.items():
            if pipe == other_pipe:
                del self.device_pipes[serial_number]
                return None
            return None

    def _pipe_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR pipe_thread_finished
        #   16 LOAD_METHOD is_set
        #   38 PRECALL
        #   42 CALL
        #   52 EXTENDED_ARG
        #   54 POP_JUMP_FORWARD_IF_TRUE to 630
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR pipe_lock
        #   68 BEFORE_WITH
        #   70 POP_TOP
        #   72 LOAD_GLOBAL NULL + list
        #   84 LOAD_FAST self
        #   86 LOAD_ATTR all_pipes
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST all_pipes_copy
        #  112 LOAD_CONST None
        #  114 LOAD_CONST None
        #  116 LOAD_CONST None
        #  118 PRECALL
        #  122 CALL
        #  132 POP_TOP
        #  134 JUMP_FORWARD to 158
        #  136 PUSH_EXC_INFO
        #  138 WITH_EXCEPT_START
        #  140 POP_JUMP_FORWARD_IF_TRUE to 150
        #  142 RERAISE
        #  144 COPY
        #  146 POP_EXCEPT
        #  148 RERAISE
        #  150 POP_TOP
        #  152 POP_EXCEPT
        #  154 POP_TOP
        #  156 POP_TOP
        #  158 LOAD_FAST all_pipes_copy
        #  160 POP_JUMP_FORWARD_IF_TRUE to 216
        #  162 LOAD_FAST self
        #  164 LOAD_ATTR pipe_thread_finished
        #  174 LOAD_METHOD wait
        #  196 LOAD_CONST 0.1
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 JUMP_BACKWARD to 4
        #  216 LOAD_GLOBAL NULL + wait
        #  228 LOAD_FAST all_pipes_copy
        #  230 LOAD_CONST 0.1
        #  232 KW_NAMES
        #  234 PRECALL
        #  238 CALL
        #  248 STORE_FAST ready
        #  250 LOAD_FAST self
        #  252 LOAD_ATTR pipe_lock
        #  262 BEFORE_WITH
        #  264 POP_TOP
        #  266 LOAD_FAST ready
        #  268 GET_ITER
        #  270 FOR_ITER to 526
        #  272 STORE_FAST pipe
        #  274 NOP
        #  276 LOAD_FAST pipe
        #  278 LOAD_METHOD recv
        #  300 PRECALL
        #  304 CALL
        #  314 STORE_FAST data
        #  316 LOAD_FAST data
        #  318 POP_JUMP_FORWARD_IF_NOT_NONE to 364
        #  320 LOAD_FAST self
        #  322 LOAD_METHOD _remove_pipe
        #  344 LOAD_FAST pipe
        #  346 PRECALL
        #  350 CALL
        #  360 POP_TOP
        #  362 JUMP_FORWARD to 450
        #  364 LOAD_FAST self
        #  366 LOAD_ATTR pipe_callbacks
        #  376 LOAD_METHOD get
        # ... bytecode truncated ...
        pass
