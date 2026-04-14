# Source Generated with Decompyle++
# File: event_upload.pyc (Python 3.11)

from dataclasses import dataclass
import logging
import queue
import threading
from typing import Any
from hyperborea.event_database import log_event
from ..device_logging import DeviceLoggerAdapter
from ..core.preferences import Preferences
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: Event = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class Event:

    serial_number: str

    category: str

    description: str

class EventUploader:

    def __init__(self, preferences):
        self.preferences = preferences
        self.event_queue = queue.Queue()
        self.is_finished = threading.Event()
        self.upload_thread = threading.Thread(target = self._upload_loop)
        self.upload_thread.start()

    def stop(self):
        self.is_finished.set()

    def join(self):
        self.upload_thread.join()

    def firmware_updated(self, serial_number, success, event_data):
        event_data['success'] = success
        if not success:
            description = 'Firmware Update Failed'
        else:
            build_info = event_data.get('build_info')
            if build_info:
                description = f'''Firmware Update with {build_info}'''
            else:
                description = 'Firmware Update'
        event = Event(serial_number = serial_number, category = 'Firmware Update', description = description, data = event_data)
        if self.preferences.event_upload_enabled:
            self.event_queue.put_nowait(event)
            return None

    def calibration_finished(self, serial_number, event_data):
        event = Event(serial_number = serial_number, category = 'Calibration', description = 'Calibration', data = event_data)
        if self.preferences.event_upload_enabled:
            self.event_queue.put_nowait(event)
            return None

    def _upload_event(self, event):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + log_event
        #   16 LOAD_FAST event
        #   18 LOAD_ATTR serial_number
        #   28 LOAD_FAST event
        #   30 LOAD_ATTR category
        #   40 LOAD_FAST event
        #   42 LOAD_ATTR description
        #   52 BUILD_TUPLE
        #   54 BUILD_MAP
        #   56 LOAD_FAST event
        #   58 LOAD_ATTR data
        #   68 DICT_MERGE
        #   70 CALL_FUNCTION_EX
        #   72 POP_TOP
        #   74 LOAD_CONST None
        #   76 RETURN_VALUE
        #   78 PUSH_EXC_INFO
        #   80 LOAD_GLOBAL Exception
        #   92 CHECK_EXC_MATCH
        #   94 POP_JUMP_FORWARD_IF_FALSE to 198
        #   96 POP_TOP
        #   98 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #  110 LOAD_GLOBAL logger
        #  122 LOAD_FAST event
        #  124 LOAD_ATTR serial_number
        #  134 PRECALL
        #  138 CALL
        #  148 STORE_FAST device_logger
        #  150 LOAD_FAST device_logger
        #  152 LOAD_METHOD exception
        #  174 LOAD_CONST 'Error uploading event'
        #  176 PRECALL
        #  180 CALL
        #  190 POP_TOP
        #  192 POP_EXCEPT
        #  194 LOAD_CONST None
        #  196 RETURN_VALUE
        #  198 RERAISE
        #  200 COPY
        #  202 POP_EXCEPT
        #  204 RERAISE
        pass

    def _upload_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR is_finished
        #   16 LOAD_METHOD is_set
        #   38 PRECALL
        #   42 CALL
        #   52 POP_JUMP_FORWARD_IF_TRUE to 250
        #   54 NOP
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR event_queue
        #   68 LOAD_METHOD get
        #   90 LOAD_CONST True
        #   92 LOAD_CONST 0.5
        #   94 PRECALL
        #   98 CALL
        #  108 STORE_FAST event
        #  110 JUMP_FORWARD to 154
        #  112 PUSH_EXC_INFO
        #  114 LOAD_GLOBAL queue
        #  126 LOAD_ATTR Empty
        #  136 CHECK_EXC_MATCH
        #  138 POP_JUMP_FORWARD_IF_FALSE to 146
        #  140 POP_TOP
        #  142 POP_EXCEPT
        #  144 JUMP_BACKWARD to 4
        #  146 RERAISE
        #  148 COPY
        #  150 POP_EXCEPT
        #  152 RERAISE
        #  154 LOAD_FAST self
        #  156 LOAD_METHOD _upload_event
        #  178 LOAD_FAST event
        #  180 PRECALL
        #  184 CALL
        #  194 POP_TOP
        #  196 LOAD_FAST self
        #  198 LOAD_ATTR is_finished
        #  208 LOAD_METHOD is_set
        #  230 PRECALL
        #  234 CALL
        #  244 POP_JUMP_BACKWARD_IF_FALSE to 54
        #  246 LOAD_CONST None
        #  248 RETURN_VALUE
        #  250 LOAD_CONST None
        #  252 RETURN_VALUE
        #  254 PUSH_EXC_INFO
        #  256 LOAD_GLOBAL Exception
        #  268 CHECK_EXC_MATCH
        #  270 POP_JUMP_FORWARD_IF_FALSE to 332
        #  272 POP_TOP
        #  274 LOAD_GLOBAL logger
        #  286 LOAD_METHOD exception
        #  308 LOAD_CONST 'Uncaught exception in event_upload_loop'
        #  310 PRECALL
        #  314 CALL
        #  324 POP_TOP
        #  326 POP_EXCEPT
        #  328 LOAD_CONST None
        #  330 RETURN_VALUE
        #  332 RERAISE
        #  334 COPY
        #  336 POP_EXCEPT
        #  338 RERAISE
        pass
