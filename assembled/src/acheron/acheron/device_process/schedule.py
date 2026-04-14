# Source Generated with Decompyle++
# File: schedule.pyc (Python 3.11)

import bisect
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
import logging
import threading
from typing import Any, Iterable, Literal, Optional, Union
import asphodel.device_config as asphodel
from asphodel.device_info import DeviceInfo
logger = logging.getLogger(__name__)
min_dt = datetime.min.replace(tzinfo = timezone.utc)
# INVALID FROM DECOMPILER: OutputConfig = <NODE:12>()
# INVALID FROM DECOMPILER: ScheduleItem = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class OutputConfig:

    compression_level: int

    base_directory: str

    date_dir_structure: bool

    datetime_filename: bool

    upload_marker: bool

class ScheduleItem:

    id: str

    remote_sn = None

    remote_bootloader = False

    remote_bootloader: bool

    trigger = None

    needs_rf_power = False

    needs_rf_power: bool

    active_streams = frozenset()

    device_config = frozenset()

    start_time = None

    collection_time = None

    stop_time = None

    duration = None

    failure_time = None

    output_config = None

    def configure_nvm(self, device_info, nvm):
        return asphodel.device_config.configure_nvm(self.device_config, device_info, nvm)

    def nvm_valid(self, device_info, nvm):
        new_nvm = self.configure_nvm(device_info, nvm)
        return new_nvm == nvm

    def priority_key(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR stop_time
        #   14 LOAD_CONST None
        #   16 IS_OP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR stop_time
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR duration
        #   42 LOAD_CONST None
        #   44 IS_OP
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR duration
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR remote_sn
        #   70 POP_JUMP_FORWARD_IF_NOT_NONE to 102
        #   72 LOAD_GLOBAL NULL + float
        #   84 LOAD_CONST 'inf'
        #   86 PRECALL
        #   90 CALL
        #  100 JUMP_FORWARD to 114
        #  102 LOAD_FAST self
        #  104 LOAD_ATTR remote_sn
        #  114 BUILD_TUPLE
        #  116 RETURN_VALUE
        pass

    def sort_key(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR start_time
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 30
        #   16 LOAD_GLOBAL min_dt
        #   28 JUMP_FORWARD to 42
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR start_time
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR remote_sn
        #   54 POP_JUMP_FORWARD_IF_NOT_NONE to 86
        #   56 LOAD_GLOBAL NULL + float
        #   68 LOAD_CONST 'inf'
        #   70 PRECALL
        #   74 CALL
        #   84 JUMP_FORWARD to 98
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR remote_sn
        #   98 BUILD_TUPLE
        #  100 RETURN_VALUE
        pass

    def __lt__(self, other):
        return self.sort_key() < other.sort_key()

    def __le__(self, other):
        return self.sort_key() <= other.sort_key()

    def __gt__(self, other):
        return self.sort_key() > other.sort_key()

    def __ge__(self, other):
        return self.sort_key() >= other.sort_key()

def get_compatible_set(items, device_info, nvm):
    items = sorted(items, key = ScheduleItem.priority_key)
    best_nvm = nvm
    current_items = set()
    remote = None

class Schedule:

    def __init__(self, schedule_items, active_triggers):
        self.active_triggers = active_triggers
        self.lock = threading.Lock()
        self.schedule_items = sorted(schedule_items)

    def __len__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + len
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR schedule_items
        #   42 PRECALL
        #   46 CALL
        #   56 SWAP
        #   58 LOAD_CONST None
        #   60 LOAD_CONST None
        #   62 LOAD_CONST None
        #   64 PRECALL
        #   68 CALL
        #   78 POP_TOP
        #   80 RETURN_VALUE
        #   82 PUSH_EXC_INFO
        #   84 WITH_EXCEPT_START
        #   86 POP_JUMP_FORWARD_IF_TRUE to 96
        #   88 RERAISE
        #   90 COPY
        #   92 POP_EXCEPT
        #   94 RERAISE
        #   96 POP_TOP
        #   98 POP_EXCEPT
        #  100 POP_TOP
        #  102 POP_TOP
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        pass

    def remote_len(self, remote):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST 0
        #    4 STORE_FAST total
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR lock
        #   18 BEFORE_WITH
        #   20 POP_TOP
        #   22 LOAD_FAST self
        #   24 LOAD_ATTR schedule_items
        #   34 GET_ITER
        #   36 FOR_ITER to 74
        #   38 STORE_FAST schedule_item
        #   40 LOAD_FAST schedule_item
        #   42 LOAD_ATTR remote_sn
        #   52 LOAD_FAST remote
        #   54 COMPARE_OP ==
        #   60 POP_JUMP_FORWARD_IF_FALSE to 72
        #   62 LOAD_FAST total
        #   64 LOAD_CONST 1
        #   66 BINARY_OP +=
        #   70 STORE_FAST total
        #   72 JUMP_BACKWARD to 36
        #   74 NOP
        #   76 LOAD_CONST None
        #   78 LOAD_CONST None
        #   80 LOAD_CONST None
        #   82 PRECALL
        #   86 CALL
        #   96 POP_TOP
        #   98 JUMP_FORWARD to 122
        #  100 PUSH_EXC_INFO
        #  102 WITH_EXCEPT_START
        #  104 POP_JUMP_FORWARD_IF_TRUE to 114
        #  106 RERAISE
        #  108 COPY
        #  110 POP_EXCEPT
        #  112 RERAISE
        #  114 POP_TOP
        #  116 POP_EXCEPT
        #  118 POP_TOP
        #  120 POP_TOP
        #  122 LOAD_FAST total
        #  124 RETURN_VALUE
        pass

    def _delete_item_id(self, item_id):
        for i, check_item in enumerate(self.schedule_items):
            if check_item.id == item_id:
                del self.schedule_items[i]
                return None
            return None

    def delete_item_id(self, item_id):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_METHOD _delete_item_id
        #   42 LOAD_FAST item_id
        #   44 PRECALL
        #   48 CALL
        #   58 POP_TOP
        #   60 LOAD_CONST None
        #   62 LOAD_CONST None
        #   64 LOAD_CONST None
        #   66 PRECALL
        #   70 CALL
        #   80 POP_TOP
        #   82 LOAD_CONST None
        #   84 RETURN_VALUE
        #   86 PUSH_EXC_INFO
        #   88 WITH_EXCEPT_START
        #   90 POP_JUMP_FORWARD_IF_TRUE to 100
        #   92 RERAISE
        #   94 COPY
        #   96 POP_EXCEPT
        #   98 RERAISE
        #  100 POP_TOP
        #  102 POP_EXCEPT
        #  104 POP_TOP
        #  106 POP_TOP
        #  108 LOAD_CONST None
        #  110 RETURN_VALUE
        pass

    def _update_item(self, item):
        self._delete_item_id(item.id)
        bisect.insort(self.schedule_items, item)

    def update_item(self, item):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_METHOD _update_item
        #   42 LOAD_FAST item
        #   44 PRECALL
        #   48 CALL
        #   58 POP_TOP
        #   60 LOAD_CONST None
        #   62 LOAD_CONST None
        #   64 LOAD_CONST None
        #   66 PRECALL
        #   70 CALL
        #   80 POP_TOP
        #   82 LOAD_CONST None
        #   84 RETURN_VALUE
        #   86 PUSH_EXC_INFO
        #   88 WITH_EXCEPT_START
        #   90 POP_JUMP_FORWARD_IF_TRUE to 100
        #   92 RERAISE
        #   94 COPY
        #   96 POP_EXCEPT
        #   98 RERAISE
        #  100 POP_TOP
        #  102 POP_EXCEPT
        #  104 POP_TOP
        #  106 POP_TOP
        #  108 LOAD_CONST None
        #  110 RETURN_VALUE
        pass

    def update_items(self, schedule_items):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST schedule_items
        #   20 GET_ITER
        #   22 FOR_ITER to 80
        #   24 STORE_FAST item
        #   26 LOAD_GLOBAL NULL + bisect
        #   38 LOAD_ATTR insort
        #   48 LOAD_FAST self
        #   50 LOAD_ATTR schedule_items
        #   60 LOAD_FAST item
        #   62 PRECALL
        #   66 CALL
        #   76 POP_TOP
        #   78 JUMP_BACKWARD to 22
        #   80 NOP
        #   82 LOAD_CONST None
        #   84 LOAD_CONST None
        #   86 LOAD_CONST None
        #   88 PRECALL
        #   92 CALL
        #  102 POP_TOP
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        #  108 PUSH_EXC_INFO
        #  110 WITH_EXCEPT_START
        #  112 POP_JUMP_FORWARD_IF_TRUE to 122
        #  114 RERAISE
        #  116 COPY
        #  118 POP_EXCEPT
        #  120 RERAISE
        #  122 POP_TOP
        #  124 POP_EXCEPT
        #  126 POP_TOP
        #  128 POP_TOP
        #  130 LOAD_CONST None
        #  132 RETURN_VALUE
        pass

    def get_ready_items(self, remote):
        self.lock
        ready = set()
        now = None

    def set_active_triggers(self, active_triggers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST active_triggers
        #   20 LOAD_FAST self
        #   22 STORE_ATTR active_triggers
        #   32 LOAD_CONST None
        #   34 LOAD_CONST None
        #   36 LOAD_CONST None
        #   38 PRECALL
        #   42 CALL
        #   52 POP_TOP
        #   54 LOAD_CONST None
        #   56 RETURN_VALUE
        #   58 PUSH_EXC_INFO
        #   60 WITH_EXCEPT_START
        #   62 POP_JUMP_FORWARD_IF_TRUE to 72
        #   64 RERAISE
        #   66 COPY
        #   68 POP_EXCEPT
        #   70 RERAISE
        #   72 POP_TOP
        #   74 POP_EXCEPT
        #   76 POP_TOP
        #   78 POP_TOP
        #   80 LOAD_CONST None
        #   82 RETURN_VALUE
        pass

    def get_expired_items(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + set
        #   14 PRECALL
        #   18 CALL
        #   28 STORE_FAST expired
        #   30 LOAD_FAST self
        #   32 LOAD_ATTR lock
        #   42 BEFORE_WITH
        #   44 POP_TOP
        #   46 LOAD_GLOBAL NULL + datetime
        #   58 LOAD_ATTR now
        #   68 LOAD_GLOBAL timezone
        #   80 LOAD_ATTR utc
        #   90 PRECALL
        #   94 CALL
        #  104 STORE_FAST now
        #  106 LOAD_FAST now
        #  108 LOAD_GLOBAL NULL + timedelta
        #  120 LOAD_CONST 10
        #  122 KW_NAMES
        #  124 PRECALL
        #  128 CALL
        #  138 BINARY_OP -
        #  142 STORE_FAST stop_time
        #  144 LOAD_FAST self
        #  146 LOAD_ATTR schedule_items
        #  156 GET_ITER
        #  158 FOR_ITER to 322
        #  160 STORE_FAST item
        #  162 LOAD_FAST item
        #  164 LOAD_ATTR failure_time
        #  174 POP_JUMP_FORWARD_IF_FALSE to 242
        #  176 LOAD_FAST item
        #  178 LOAD_ATTR failure_time
        #  188 LOAD_FAST now
        #  190 COMPARE_OP <
        #  196 POP_JUMP_FORWARD_IF_FALSE to 242
        #  198 LOAD_FAST expired
        #  200 LOAD_METHOD add
        #  222 LOAD_FAST item
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 JUMP_BACKWARD to 158
        #  242 LOAD_FAST item
        #  244 LOAD_ATTR stop_time
        #  254 POP_JUMP_FORWARD_IF_FALSE to 320
        #  256 LOAD_FAST item
        #  258 LOAD_ATTR stop_time
        #  268 LOAD_FAST stop_time
        #  270 COMPARE_OP <
        #  276 POP_JUMP_FORWARD_IF_FALSE to 320
        #  278 LOAD_FAST expired
        #  280 LOAD_METHOD add
        #  302 LOAD_FAST item
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 JUMP_BACKWARD to 158
        #  322 NOP
        #  324 LOAD_CONST None
        #  326 LOAD_CONST None
        #  328 LOAD_CONST None
        #  330 PRECALL
        #  334 CALL
        #  344 POP_TOP
        #  346 JUMP_FORWARD to 370
        #  348 PUSH_EXC_INFO
        #  350 WITH_EXCEPT_START
        #  352 POP_JUMP_FORWARD_IF_TRUE to 362
        #  354 RERAISE
        #  356 COPY
        #  358 POP_EXCEPT
        #  360 RERAISE
        #  362 POP_TOP
        #  364 POP_EXCEPT
        #  366 POP_TOP
        #  368 POP_TOP
        #  370 LOAD_FAST expired
        #  372 RETURN_VALUE
        pass

class RemoteSchedule:

    def __init__(self, schedule, remote_sn, remote_bootloader, schedule_items):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_FAST schedule
        #    6 LOAD_DEREF self
        #    8 STORE_ATTR schedule
        #   18 LOAD_FAST remote_sn
        #   20 LOAD_DEREF self
        #   22 STORE_ATTR remote_sn
        #   32 LOAD_FAST remote_bootloader
        #   34 LOAD_DEREF self
        #   36 STORE_ATTR remote_bootloader
        #   46 LOAD_CLOSURE self
        #   48 BUILD_TUPLE
        #   50 LOAD_CONST <code object <listcomp> at 0x105b60030, file "acheron\device_process\schedule.py", line 249>
        #   52 MAKE_FUNCTION closure
        #   54 LOAD_FAST schedule_items
        #   56 GET_ITER
        #   58 PRECALL
        #   62 CALL
        #   72 STORE_FAST new_items
        #   74 LOAD_DEREF self
        #   76 LOAD_ATTR schedule
        #   86 LOAD_METHOD update_items
        #  108 LOAD_FAST new_items
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 LOAD_CONST None
        #  128 RETURN_VALUE
        pass

    def __len__(self):
        return self.schedule.remote_len(self.remote_sn)

    def delete_item_id(self, item_id):
        self.schedule.delete_item_id(item_id)

    def _convert_item_to_remote(self, item):
        return replace(item, remote_sn = self.remote_sn, remote_bootloader = self.remote_bootloader)

    def _convert_item_from_remote(self, item):
        return replace(item, remote_sn = None)

    def update_item(self, item):
        self.schedule.update_item(self._convert_item_to_remote(item))

    def get_ready_items(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 RESUME
        #    4 LOAD_DEREF self
        #    6 LOAD_ATTR schedule
        #   16 LOAD_METHOD get_ready_items
        #   38 LOAD_DEREF self
        #   40 LOAD_ATTR remote_sn
        #   50 KW_NAMES
        #   52 PRECALL
        #   56 CALL
        #   66 UNPACK_SEQUENCE
        #   70 STORE_FAST ready
        #   72 STORE_FAST next_change
        #   74 LOAD_GLOBAL NULL + set
        #   86 LOAD_CLOSURE self
        #   88 BUILD_TUPLE
        #   90 LOAD_CONST <code object <genexpr> at 0x105b60230, file "acheron\device_process\schedule.py", line 271>
        #   92 MAKE_FUNCTION closure
        #   94 LOAD_FAST ready
        #   96 GET_ITER
        #   98 PRECALL
        #  102 CALL
        #  112 PRECALL
        #  116 CALL
        #  126 LOAD_FAST next_change
        #  128 BUILD_TUPLE
        #  130 RETURN_VALUE
        pass

    def set_active_triggers(self, active_triggers):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def get_expired_items(self):
        return set()
