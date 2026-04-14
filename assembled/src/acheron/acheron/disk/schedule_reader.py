# Source Generated with Decompyle++
# File: schedule_reader.pyc (Python 3.11)

from collections import deque
from datetime import datetime, timedelta, timezone
from functools import cache
import logging
import os
import threading
from zoneinfo import ZoneInfo
from PySide6 import QtCore
from croniter import croniter, CroniterBadDateError
from pydantic import TypeAdapter
from .disk_schedule import DiskSchedule
from .disk_trigger import DiskTrigger
from ..calc_process.types import Trigger
from ..core.device_controller import DeviceController
from ..core.dispatcher import Dispatcher
from ..device_process.schedule import ScheduleItem
logger = logging.getLogger(__name__)
SCHEDULE_READER_KEY = 'schedule_reader'
GlobalSchedule = dict[(tuple[(str, ...)], list[DiskSchedule])]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ScheduleReader(QtCore.QObject):

    error = QtCore.Signal(str)

    warning = QtCore.Signal(str)

    _cron_schedule_updated = QtCore.Signal()

    def __init__(self, basedir, dispatcher):
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
        #   68 LOAD_FAST dispatcher
        #   70 LOAD_FAST self
        #   72 STORE_ATTR dispatcher
        #   82 LOAD_FAST basedir
        #   84 LOAD_FAST self
        #   86 STORE_ATTR basedir
        #   96 LOAD_GLOBAL os
        #  108 LOAD_ATTR path
        #  118 LOAD_METHOD join
        #  140 LOAD_FAST self
        #  142 LOAD_ATTR basedir
        #  152 LOAD_CONST 'triggers.json'
        #  154 PRECALL
        #  158 CALL
        #  168 LOAD_FAST self
        #  170 STORE_ATTR trigger_filename
        #  180 LOAD_GLOBAL os
        #  192 LOAD_ATTR path
        #  202 LOAD_METHOD join
        #  224 LOAD_FAST self
        #  226 LOAD_ATTR basedir
        #  236 LOAD_CONST 'schedule_items.json'
        #  238 PRECALL
        #  242 CALL
        #  252 LOAD_FAST self
        #  254 STORE_ATTR schedule_filename
        #  264 LOAD_GLOBAL NULL + timedelta
        #  276 LOAD_CONST 120
        #  278 KW_NAMES
        #  280 PRECALL
        #  284 CALL
        #  294 LOAD_FAST self
        #  296 STORE_ATTR timedelta
        #  306 LOAD_GLOBAL NULL + threading
        #  318 LOAD_ATTR Lock
        #  328 PRECALL
        #  332 CALL
        #  342 LOAD_FAST self
        #  344 STORE_ATTR lock
        #  354 BUILD_MAP
        #  356 LOAD_FAST self
        #  358 STORE_ATTR controllers
        #  368 BUILD_MAP
        #  370 LOAD_FAST self
        #  372 STORE_ATTR cron_schedule
        #  382 LOAD_GLOBAL NULL + datetime
        #  394 LOAD_ATTR now
        #  404 LOAD_GLOBAL timezone
        #  416 LOAD_ATTR utc
        #  426 PRECALL
        #  430 CALL
        #  440 LOAD_FAST self
        #  442 STORE_ATTR last_cron_stop
        #  452 LOAD_GLOBAL NULL + threading
        #  464 LOAD_ATTR Event
        #  474 PRECALL
        #  478 CALL
        #  488 LOAD_FAST self
        #  490 STORE_ATTR finished
        #  500 LOAD_GLOBAL NULL + deque
        #  512 PRECALL
        #  516 CALL
        #  526 LOAD_FAST self
        #  528 STORE_ATTR cron_deque
        #  538 LOAD_GLOBAL NULL + threading
        #  550 LOAD_ATTR Thread
        #  560 LOAD_FAST self
        #  562 LOAD_ATTR _cron_thread_run
        #  572 KW_NAMES
        #  574 PRECALL
        #  578 CALL
        # ... bytecode truncated ...
        pass

    def start(self):
        self._read_all()

    def stop(self):
        self.finished.set()
        self.cron_thread.join()

    def reload(self):
        self._read_all()

    def _read_triggers(trigger_filename):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + open
        #   16 LOAD_FAST trigger_filename
        #   18 LOAD_CONST 'rt'
        #   20 PRECALL
        #   24 CALL
        #   34 BEFORE_WITH
        #   36 STORE_FAST f
        #   38 LOAD_FAST f
        #   40 LOAD_METHOD read
        #   62 PRECALL
        #   66 CALL
        #   76 STORE_FAST contents
        #   78 LOAD_CONST None
        #   80 LOAD_CONST None
        #   82 LOAD_CONST None
        #   84 PRECALL
        #   88 CALL
        #   98 POP_TOP
        #  100 JUMP_FORWARD to 124
        #  102 PUSH_EXC_INFO
        #  104 WITH_EXCEPT_START
        #  106 POP_JUMP_FORWARD_IF_TRUE to 116
        #  108 RERAISE
        #  110 COPY
        #  112 POP_EXCEPT
        #  114 RERAISE
        #  116 POP_TOP
        #  118 POP_EXCEPT
        #  120 POP_TOP
        #  122 POP_TOP
        #  124 JUMP_FORWARD to 190
        #  126 PUSH_EXC_INFO
        #  128 LOAD_GLOBAL FileNotFoundError
        #  140 CHECK_EXC_MATCH
        #  142 POP_JUMP_FORWARD_IF_FALSE to 182
        #  144 POP_TOP
        #  146 BUILD_MAP
        #  148 LOAD_GLOBAL NULL + set
        #  160 PRECALL
        #  164 CALL
        #  174 BUILD_TUPLE
        #  176 SWAP
        #  178 POP_EXCEPT
        #  180 RETURN_VALUE
        #  182 RERAISE
        #  184 COPY
        #  186 POP_EXCEPT
        #  188 RERAISE
        #  190 LOAD_GLOBAL NULL + TypeAdapter
        #  202 LOAD_GLOBAL list
        #  214 LOAD_GLOBAL DiskTrigger
        #  226 BINARY_SUBSCR
        #  236 PRECALL
        #  240 CALL
        #  250 STORE_FAST ta
        #  252 LOAD_FAST ta
        #  254 LOAD_METHOD validate_json
        #  276 LOAD_FAST contents
        #  278 PRECALL
        #  282 CALL
        #  292 STORE_FAST triggers
        #  294 BUILD_MAP
        #  296 STORE_FAST trigger_dict
        #  298 LOAD_GLOBAL NULL + set
        #  310 PRECALL
        #  314 CALL
        #  324 STORE_FAST trigger_names
        #  326 LOAD_FAST triggers
        #  328 GET_ITER
        #  330 FOR_ITER to 612
        #  332 STORE_FAST t
        #  334 LOAD_FAST trigger_names
        #  336 LOAD_METHOD add
        #  358 LOAD_FAST t
        #  360 LOAD_ATTR id
        #  370 PRECALL
        #  374 CALL
        #  384 POP_TOP
        # ... bytecode truncated ...
        pass

    def _read_schedule_items(schedule_filename):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + open
        #   16 LOAD_FAST schedule_filename
        #   18 LOAD_CONST 'rt'
        #   20 PRECALL
        #   24 CALL
        #   34 BEFORE_WITH
        #   36 STORE_FAST f
        #   38 LOAD_FAST f
        #   40 LOAD_METHOD read
        #   62 PRECALL
        #   66 CALL
        #   76 STORE_FAST contents
        #   78 LOAD_CONST None
        #   80 LOAD_CONST None
        #   82 LOAD_CONST None
        #   84 PRECALL
        #   88 CALL
        #   98 POP_TOP
        #  100 JUMP_FORWARD to 124
        #  102 PUSH_EXC_INFO
        #  104 WITH_EXCEPT_START
        #  106 POP_JUMP_FORWARD_IF_TRUE to 116
        #  108 RERAISE
        #  110 COPY
        #  112 POP_EXCEPT
        #  114 RERAISE
        #  116 POP_TOP
        #  118 POP_EXCEPT
        #  120 POP_TOP
        #  122 POP_TOP
        #  124 JUMP_FORWARD to 192
        #  126 PUSH_EXC_INFO
        #  128 LOAD_GLOBAL FileNotFoundError
        #  140 CHECK_EXC_MATCH
        #  142 POP_JUMP_FORWARD_IF_FALSE to 184
        #  144 POP_TOP
        #  146 BUILD_MAP
        #  148 BUILD_MAP
        #  150 LOAD_GLOBAL NULL + set
        #  162 PRECALL
        #  166 CALL
        #  176 BUILD_TUPLE
        #  178 SWAP
        #  180 POP_EXCEPT
        #  182 RETURN_VALUE
        #  184 RERAISE
        #  186 COPY
        #  188 POP_EXCEPT
        #  190 RERAISE
        #  192 LOAD_GLOBAL NULL + TypeAdapter
        #  204 LOAD_GLOBAL list
        #  216 LOAD_GLOBAL DiskSchedule
        #  228 BINARY_SUBSCR
        #  238 PRECALL
        #  242 CALL
        #  252 STORE_FAST ta
        #  254 LOAD_FAST ta
        #  256 LOAD_METHOD validate_json
        #  278 LOAD_FAST contents
        #  280 PRECALL
        #  284 CALL
        #  294 STORE_FAST schedule_items
        #  296 LOAD_GLOBAL NULL + datetime
        #  308 LOAD_ATTR now
        #  318 LOAD_GLOBAL timezone
        #  330 LOAD_ATTR utc
        #  340 PRECALL
        #  344 CALL
        #  354 STORE_FAST now
        #  356 BUILD_MAP
        #  358 STORE_FAST single_schedule
        #  360 BUILD_MAP
        #  362 STORE_FAST cron_schedule
        #  364 LOAD_GLOBAL NULL + set
        #  376 PRECALL
        #  380 CALL
        #  390 STORE_FAST all_serials
        #  392 LOAD_FAST schedule_items
        # ... bytecode truncated ...
        pass

    def _check_missing_triggers(schedule_items, trigger_names):
        for schedule_list in schedule_items.values():
            for schedule_item in schedule_list:
                if schedule_item.trigger and schedule_item.trigger not in trigger_names:
                    logger.warning('Unknown trigger name %s', schedule_item.trigger)
                return None

    def _read_all(self):
        try:
            (triggers, trigger_names) = self._read_triggers(self.trigger_filename)
        except Exception:
            message = 'Could not parse triggers'
            logger.exception(message)
            self.error.emit(message)
            return None


        try:
            (single_schedule, cron_schedule, schedule_serials) = self._read_schedule_items(self.schedule_filename)
        except Exception:
            message = 'Could not parse schedule items'
            logger.exception(message)
            self.error.emit(message)
            return None

        self._check_missing_triggers(single_schedule, trigger_names)
        self._check_missing_triggers(cron_schedule, trigger_names)
        self.lock
        serials = set(triggers) | schedule_serials
        old_serials = set(self.controllers)
        unused_serials = old_serials.difference(serials)
        new_serials = serials.difference(old_serials)

    def _croniter_range(start, stop, expr_format, hash_id):
        ic = croniter(expr_format, start, ret_type = datetime, max_years_between_matches = 1, hash_id = hash_id)
        values = []

    def _get_tz(timezone_name):
        return ZoneInfo(timezone_name)

    def _single_pass(self, start, stop):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL schedule_item
        #    2 RESUME
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR cron_schedule
        #   16 LOAD_METHOD items
        #   38 PRECALL
        #   42 CALL
        #   52 GET_ITER
        #   54 FOR_ITER to 500
        #   56 UNPACK_SEQUENCE
        #   60 STORE_FAST serial_number
        #   62 STORE_FAST schedule_list
        #   64 LOAD_FAST schedule_list
        #   66 GET_ITER
        #   68 FOR_ITER to 498
        #   70 STORE_DEREF schedule_item
        #   72 LOAD_DEREF schedule_item
        #   74 LOAD_METHOD get_base_id
        #   96 PRECALL
        #  100 CALL
        #  110 STORE_FAST base_id
        #  112 LOAD_FAST base_id
        #  114 LOAD_METHOD encode
        #  136 LOAD_CONST 'utf-8'
        #  138 PRECALL
        #  142 CALL
        #  152 STORE_FAST hash_id
        #  154 LOAD_DEREF schedule_item
        #  156 LOAD_ATTR cron_start
        #  166 STORE_FAST expr_format
        #  168 LOAD_DEREF schedule_item
        #  170 LOAD_ATTR cron_timezone
        #  180 POP_JUMP_FORWARD_IF_FALSE to 360
        #  182 LOAD_FAST self
        #  184 LOAD_METHOD _get_tz
        #  206 LOAD_DEREF schedule_item
        #  208 LOAD_ATTR cron_timezone
        #  218 PRECALL
        #  222 CALL
        #  232 STORE_FAST tz
        #  234 LOAD_FAST self
        #  236 LOAD_METHOD _croniter_range
        #  258 LOAD_FAST start
        #  260 LOAD_METHOD astimezone
        #  282 LOAD_FAST tz
        #  284 PRECALL
        #  288 CALL
        #  298 LOAD_FAST stop
        #  300 LOAD_METHOD astimezone
        #  322 LOAD_FAST tz
        #  324 PRECALL
        #  328 CALL
        #  338 LOAD_FAST expr_format
        #  340 LOAD_FAST hash_id
        #  342 PRECALL
        #  346 CALL
        #  356 STORE_FAST datetimes
        #  358 JUMP_FORWARD to 408
        #  360 LOAD_FAST self
        #  362 LOAD_METHOD _croniter_range
        #  384 LOAD_FAST start
        #  386 LOAD_FAST stop
        #  388 LOAD_FAST expr_format
        #  390 LOAD_FAST hash_id
        #  392 PRECALL
        #  396 CALL
        #  406 STORE_FAST datetimes
        #  408 LOAD_CLOSURE schedule_item
        #  410 BUILD_TUPLE
        #  412 LOAD_CONST <code object <listcomp> at 0x105ab7e30, file "acheron\disk\schedule_reader.py", line 242>
        #  414 MAKE_FUNCTION closure
        #  416 LOAD_FAST datetimes
        #  418 GET_ITER
        #  420 PRECALL
        #  424 CALL
        #  434 STORE_FAST new_items
        #  436 LOAD_FAST new_items
        #  438 POP_JUMP_FORWARD_IF_FALSE to 496
        #  440 LOAD_FAST self
        #  442 LOAD_ATTR cron_deque
        # ... bytecode truncated ...
        pass

    def _cron_thread_run(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR finished
        #   14 LOAD_METHOD wait
        #   36 LOAD_CONST 60
        #   38 KW_NAMES
        #   40 PRECALL
        #   44 CALL
        #   54 POP_JUMP_FORWARD_IF_TRUE to 418
        #   56 LOAD_FAST self
        #   58 LOAD_ATTR lock
        #   68 BEFORE_WITH
        #   70 POP_TOP
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR last_cron_stop
        #   84 STORE_FAST start
        #   86 LOAD_GLOBAL NULL + datetime
        #   98 LOAD_ATTR now
        #  108 LOAD_GLOBAL timezone
        #  120 LOAD_ATTR utc
        #  130 PRECALL
        #  134 CALL
        #  144 LOAD_FAST self
        #  146 LOAD_ATTR timedelta
        #  156 BINARY_OP +
        #  160 STORE_FAST stop
        #  162 LOAD_FAST stop
        #  164 LOAD_FAST self
        #  166 STORE_ATTR last_cron_stop
        #  176 LOAD_FAST self
        #  178 LOAD_METHOD _single_pass
        #  200 LOAD_FAST start
        #  202 LOAD_FAST stop
        #  204 PRECALL
        #  208 CALL
        #  218 POP_TOP
        #  220 LOAD_GLOBAL NULL + bool
        #  232 LOAD_FAST self
        #  234 LOAD_ATTR cron_deque
        #  244 PRECALL
        #  248 CALL
        #  258 STORE_FAST updated
        #  260 LOAD_CONST None
        #  262 LOAD_CONST None
        #  264 LOAD_CONST None
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 JUMP_FORWARD to 306
        #  284 PUSH_EXC_INFO
        #  286 WITH_EXCEPT_START
        #  288 POP_JUMP_FORWARD_IF_TRUE to 298
        #  290 RERAISE
        #  292 COPY
        #  294 POP_EXCEPT
        #  296 RERAISE
        #  298 POP_TOP
        #  300 POP_EXCEPT
        #  302 POP_TOP
        #  304 POP_TOP
        #  306 LOAD_FAST updated
        #  308 POP_JUMP_FORWARD_IF_FALSE to 360
        #  310 LOAD_FAST self
        #  312 LOAD_ATTR _cron_schedule_updated
        #  322 LOAD_METHOD emit
        #  344 PRECALL
        #  348 CALL
        #  358 POP_TOP
        #  360 LOAD_FAST self
        #  362 LOAD_ATTR finished
        #  372 LOAD_METHOD wait
        #  394 LOAD_CONST 60
        #  396 KW_NAMES
        #  398 PRECALL
        #  402 CALL
        #  412 POP_JUMP_BACKWARD_IF_FALSE to 56
        #  414 LOAD_CONST None
        #  416 RETURN_VALUE
        #  418 LOAD_CONST None
        #  420 RETURN_VALUE
        pass

    def _cron_schedule_updated_cb(self):
        self.lock
