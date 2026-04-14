# Source Generated with Decompyle++
# File: disk_schedule.pyc (Python 3.11)

from datetime import datetime, timedelta
from functools import cache
import hashlib
import re
from typing import Any, Optional
from zoneinfo import ZoneInfo
from croniter import croniter
from pydantic import AwareDatetime, BaseModel, field_validator, model_validator, ValidationInfo
from ..device_process.schedule import ScheduleItem

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DiskSchedule(BaseModel, True):

    remote_bootloader = False

    remote_bootloader: bool

    trigger = None

    needs_rf_power = False

    needs_rf_power: bool

    active_streams = None

    device_config = frozenset()

    start_time = None

    stop_time = None

    duration = None

    failure_delay = None

    cron_start = None

    cron_timezone = None

    def ensure_list(cls, v, info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + isinstance
        #   14 LOAD_FAST v
        #   16 LOAD_GLOBAL str
        #   28 PRECALL
        #   32 CALL
        #   42 POP_JUMP_FORWARD_IF_FALSE to 118
        #   44 LOAD_GLOBAL NULL + len
        #   56 LOAD_FAST v
        #   58 PRECALL
        #   62 CALL
        #   72 LOAD_CONST 0
        #   74 COMPARE_OP >
        #   80 POP_JUMP_FORWARD_IF_FALSE to 88
        #   82 LOAD_FAST v
        #   84 BUILD_TUPLE
        #   86 RETURN_VALUE
        #   88 LOAD_GLOBAL NULL + ValueError
        #  100 LOAD_CONST 'Empty serial number string'
        #  102 PRECALL
        #  106 CALL
        #  116 RAISE_VARARGS
        #  118 LOAD_GLOBAL NULL + len
        #  130 LOAD_FAST v
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_CONST 0
        #  148 COMPARE_OP ==
        #  154 POP_JUMP_FORWARD_IF_FALSE to 186
        #  156 LOAD_GLOBAL NULL + ValueError
        #  168 LOAD_CONST 'Empty serial number'
        #  170 PRECALL
        #  174 CALL
        #  184 RAISE_VARARGS
        #  186 LOAD_FAST v
        #  188 RETURN_VALUE
        pass

    def _cron_exclusion(cls, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + isinstance
        #   14 LOAD_FAST data
        #   16 LOAD_GLOBAL dict
        #   28 PRECALL
        #   32 CALL
        #   42 POP_JUMP_FORWARD_IF_FALSE to 310
        #   44 LOAD_FAST data
        #   46 LOAD_METHOD get
        #   68 LOAD_CONST 'cron_start'
        #   70 LOAD_CONST None
        #   72 PRECALL
        #   76 CALL
        #   86 POP_JUMP_FORWARD_IF_NONE to 310
        #   88 LOAD_FAST data
        #   90 LOAD_METHOD get
        #  112 LOAD_CONST 'start_time'
        #  114 LOAD_CONST None
        #  116 PRECALL
        #  120 CALL
        #  130 POP_JUMP_FORWARD_IF_NONE to 162
        #  132 LOAD_GLOBAL NULL + ValueError
        #  144 LOAD_CONST 'cron_start set with start_time'
        #  146 PRECALL
        #  150 CALL
        #  160 RAISE_VARARGS
        #  162 LOAD_FAST data
        #  164 LOAD_METHOD get
        #  186 LOAD_CONST 'stop_time'
        #  188 LOAD_CONST None
        #  190 PRECALL
        #  194 CALL
        #  204 POP_JUMP_FORWARD_IF_NONE to 236
        #  206 LOAD_GLOBAL NULL + ValueError
        #  218 LOAD_CONST 'cron_start set with stop_time'
        #  220 PRECALL
        #  224 CALL
        #  234 RAISE_VARARGS
        #  236 LOAD_FAST data
        #  238 LOAD_METHOD get
        #  260 LOAD_CONST 'duration'
        #  262 LOAD_CONST None
        #  264 PRECALL
        #  268 CALL
        #  278 POP_JUMP_FORWARD_IF_NOT_NONE to 310
        #  280 LOAD_GLOBAL NULL + ValueError
        #  292 LOAD_CONST 'cron_start set without duration'
        #  294 PRECALL
        #  298 CALL
        #  308 RAISE_VARARGS
        #  310 LOAD_FAST data
        #  312 RETURN_VALUE
        pass

    def _has_cron_timezone_with_start(cls, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + isinstance
        #   14 LOAD_FAST data
        #   16 LOAD_GLOBAL dict
        #   28 PRECALL
        #   32 CALL
        #   42 POP_JUMP_FORWARD_IF_FALSE to 162
        #   44 LOAD_FAST data
        #   46 LOAD_METHOD get
        #   68 LOAD_CONST 'cron_timezone'
        #   70 LOAD_CONST None
        #   72 PRECALL
        #   76 CALL
        #   86 POP_JUMP_FORWARD_IF_NONE to 162
        #   88 LOAD_FAST data
        #   90 LOAD_METHOD get
        #  112 LOAD_CONST 'cron_start'
        #  114 LOAD_CONST None
        #  116 PRECALL
        #  120 CALL
        #  130 POP_JUMP_FORWARD_IF_NOT_NONE to 162
        #  132 LOAD_GLOBAL NULL + ValueError
        #  144 LOAD_CONST 'cron_timezone set without cron_start'
        #  146 PRECALL
        #  150 CALL
        #  160 RAISE_VARARGS
        #  162 LOAD_FAST data
        #  164 RETURN_VALUE
        pass

    def _has_failure_delay_with_start(cls, data):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + isinstance
        #   14 LOAD_FAST data
        #   16 LOAD_GLOBAL dict
        #   28 PRECALL
        #   32 CALL
        #   42 POP_JUMP_FORWARD_IF_FALSE to 206
        #   44 LOAD_FAST data
        #   46 LOAD_METHOD get
        #   68 LOAD_CONST 'failure_delay'
        #   70 LOAD_CONST None
        #   72 PRECALL
        #   76 CALL
        #   86 POP_JUMP_FORWARD_IF_NONE to 206
        #   88 LOAD_FAST data
        #   90 LOAD_METHOD get
        #  112 LOAD_CONST 'start_time'
        #  114 LOAD_CONST None
        #  116 PRECALL
        #  120 CALL
        #  130 POP_JUMP_FORWARD_IF_NOT_NONE to 206
        #  132 LOAD_FAST data
        #  134 LOAD_METHOD get
        #  156 LOAD_CONST 'cron_start'
        #  158 LOAD_CONST None
        #  160 PRECALL
        #  164 CALL
        #  174 POP_JUMP_FORWARD_IF_NOT_NONE to 206
        #  176 LOAD_GLOBAL NULL + ValueError
        #  188 LOAD_CONST 'failure_delay set without start_time or cron_start'
        #  190 PRECALL
        #  194 CALL
        #  204 RAISE_VARARGS
        #  206 LOAD_FAST data
        #  208 RETURN_VALUE
        pass

    def _check_timezone(cls, v, _info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST v
        #    4 POP_JUMP_FORWARD_IF_NOT_NONE to 10
        #    6 LOAD_CONST None
        #    8 RETURN_VALUE
        #   10 LOAD_GLOBAL NULL + ZoneInfo
        #   22 LOAD_FAST v
        #   24 PRECALL
        #   28 CALL
        #   38 POP_TOP
        #   40 LOAD_FAST v
        #   42 RETURN_VALUE
        pass

    def _cron_valid(cls, v, _info):
        if not isinstance(v, str) and croniter.is_valid(v, hash_id = b'validate'):
            raise ValueError('Invalid cron string')
        return v

    def is_single_item(self):
        return self.cron_start is None

    def get_base_id(self):
        json_string = self.model_dump_json()
        hash_object = hashlib.sha256(json_string.encode())
        return 'ds-' + hash_object.hexdigest()

    def _get_remote_sn(serial):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + len
        #   14 LOAD_FAST serial
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_CONST 2
        #   32 COMPARE_OP <
        #   38 POP_JUMP_FORWARD_IF_FALSE to 44
        #   40 LOAD_CONST None
        #   42 RETURN_VALUE
        #   44 LOAD_GLOBAL NULL + re
        #   56 LOAD_ATTR findall
        #   66 LOAD_CONST '\\d+'
        #   68 LOAD_FAST serial
        #   70 LOAD_CONST -1
        #   72 BINARY_SUBSCR
        #   82 PRECALL
        #   86 CALL
        #   96 STORE_FAST matches
        #   98 LOAD_FAST matches
        #  100 POP_JUMP_FORWARD_IF_FALSE to 144
        #  102 LOAD_GLOBAL NULL + int
        #  114 LOAD_FAST matches
        #  116 LOAD_CONST -1
        #  118 BINARY_SUBSCR
        #  128 PRECALL
        #  132 CALL
        #  142 JUMP_FORWARD to 146
        #  144 LOAD_CONST None
        #  146 RETURN_VALUE
        pass

    def convert_single_item(self):
        values = self.model_dump()
        values['remote_sn'] = self._get_remote_sn(values['serial'])
        del values['serial']
        del values['cron_start']
        del values['cron_timezone']
        failure_delay = values.pop('failure_delay', None)
        if failure_delay:
            values['failure_time'] = self.start_time + failure_delay

    def convert_cron(self, start_time):
        values = self.model_dump()
        values['remote_sn'] = self._get_remote_sn(values['serial'])
        del values['serial']
        del values['cron_start']
        del values['cron_timezone']
        values['start_time'] = start_time
        failure_delay = values.pop('failure_delay', None)
        if failure_delay:
            values['failure_time'] = start_time + failure_delay
        id = self.get_base_id() + ' ' + start_time.isoformat()

    def get_base_serial(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + len
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR serial
        #   26 PRECALL
        #   30 CALL
        #   40 LOAD_CONST 2
        #   42 COMPARE_OP >=
        #   48 POP_JUMP_FORWARD_IF_FALSE to 80
        #   50 LOAD_FAST self
        #   52 LOAD_ATTR serial
        #   62 LOAD_CONST None
        #   64 LOAD_CONST -1
        #   66 BUILD_SLICE
        #   68 BINARY_SUBSCR
        #   78 RETURN_VALUE
        #   80 LOAD_FAST self
        #   82 LOAD_ATTR serial
        #   92 RETURN_VALUE
        pass
