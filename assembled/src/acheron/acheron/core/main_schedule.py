# Source Generated with Decompyle++
# File: main_schedule.pyc (Python 3.11)

import datetime
import logging
from typing import Iterable, Optional
from PySide6 import QtCore
from ..device_process.schedule import ScheduleItem
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DeviceSchedule(QtCore.QObject):

    finished_item = QtCore.Signal(str, bool)

    updated_item = QtCore.Signal(object)

    deleted_items = QtCore.Signal(object)

    def __init__(self, parent_schedule):
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
        #   68 LOAD_FAST parent_schedule
        #   70 LOAD_FAST self
        #   72 STORE_ATTR parent_schedule
        #   82 BUILD_MAP
        #   84 LOAD_FAST self
        #   86 STORE_ATTR schedule_items
        #   96 LOAD_CONST 0
        #   98 LOAD_FAST self
        #  100 STORE_ATTR schedule_count
        #  110 LOAD_CONST None
        #  112 RETURN_VALUE
        pass

    def get_items(self):
        all_values = { }
        for schedule_dict in self.schedule_items.values():
            all_values.update(schedule_dict)
            return set(all_values.values())

    def _clear_schedule_id(self, id):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR schedule_items
        #   14 LOAD_METHOD values
        #   36 PRECALL
        #   40 CALL
        #   50 GET_ITER
        #   52 FOR_ITER to 98
        #   54 STORE_FAST schedule_dict
        #   56 NOP
        #   58 LOAD_FAST schedule_dict
        #   60 LOAD_FAST id
        #   62 DELETE_SUBSCR
        #   64 JUMP_BACKWARD to 52
        #   66 PUSH_EXC_INFO
        #   68 LOAD_GLOBAL KeyError
        #   80 CHECK_EXC_MATCH
        #   82 POP_JUMP_FORWARD_IF_FALSE to 90
        #   84 POP_TOP
        #   86 POP_EXCEPT
        #   88 JUMP_BACKWARD to 52
        #   90 RERAISE
        #   92 COPY
        #   94 POP_EXCEPT
        #   96 RERAISE
        #   98 LOAD_CONST None
        #  100 RETURN_VALUE
        pass

    def add_item(self, partition, schedule_item):
        schedule_items = self.schedule_items.setdefault(partition, { })
        schedule_items[schedule_item.id] = schedule_item
        self.updated_item.emit(schedule_item)

    def set_partition_items(self, partition, schedule_items):
        try:
            old_schedule_items = self.schedule_items.pop(partition)
        except KeyError:
            old_schedule_items = { }

        new_schedule_items = schedule_items()
        self.schedule_items[partition] = new_schedule_items
        ids_to_delete = set(old_schedule_items).difference(new_schedule_items)
        if ids_to_delete:
            self.deleted_items.emit(ids_to_delete)
        for schedule_item in new_schedule_items.values():
            old_schedule_item = old_schedule_items.get(schedule_item.id)
            if old_schedule_item or old_schedule_item != schedule_item:
                self.updated_item.emit(schedule_item)
            return None

    def clear_partition(self, *partitions):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + set
        #   14 PRECALL
        #   18 CALL
        #   28 STORE_FAST ids
        #   30 LOAD_FAST partitions
        #   32 GET_ITER
        #   34 FOR_ITER to 226
        #   36 STORE_FAST partition
        #   38 NOP
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR schedule_items
        #   52 LOAD_METHOD pop
        #   74 LOAD_FAST partition
        #   76 PRECALL
        #   80 CALL
        #   90 STORE_FAST old_schedule_items
        #   92 JUMP_FORWARD to 126
        #   94 PUSH_EXC_INFO
        #   96 LOAD_GLOBAL KeyError
        #  108 CHECK_EXC_MATCH
        #  110 POP_JUMP_FORWARD_IF_FALSE to 118
        #  112 POP_TOP
        #  114 POP_EXCEPT
        #  116 JUMP_BACKWARD to 34
        #  118 RERAISE
        #  120 COPY
        #  122 POP_EXCEPT
        #  124 RERAISE
        #  126 LOAD_FAST old_schedule_items
        #  128 LOAD_METHOD values
        #  150 PRECALL
        #  154 CALL
        #  164 GET_ITER
        #  166 FOR_ITER to 224
        #  168 STORE_FAST schedule_item
        #  170 LOAD_FAST ids
        #  172 LOAD_METHOD add
        #  194 LOAD_FAST schedule_item
        #  196 LOAD_ATTR id
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 JUMP_BACKWARD to 166
        #  224 JUMP_BACKWARD to 34
        #  226 LOAD_FAST ids
        #  228 POP_JUMP_FORWARD_IF_FALSE to 286
        #  230 LOAD_FAST self
        #  232 LOAD_ATTR deleted_items
        #  242 LOAD_METHOD emit
        #  264 LOAD_FAST ids
        #  266 PRECALL
        #  270 CALL
        #  280 POP_TOP
        #  282 LOAD_CONST None
        #  284 RETURN_VALUE
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        pass

    def mark_finished(self, schedule_id, success):
        self._clear_schedule_id(schedule_id)

    def clear_expired_items(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        stop_time = now - datetime.timedelta(seconds = 10)
        all_expried = set()
        for schedule_dict in self.schedule_items.values():
            expired = set()
            for schedule_id, item in schedule_dict.items():
                if item.failure_time and item.failure_time < now:
                    expired.add(schedule_id)
                    continue
                if item.stop_time and item.stop_time < stop_time:
                    expired.add(schedule_id)
                for schedule_id in expired:
                    schedule_dict.pop(schedule_id)
                    self.finished_item.emit(schedule_id, False)
                    all_expried.update(expired)
                    if all_expried:
                        self.deleted_items.emit(all_expried)
                        return None
                    return None

class MainSchedule(QtCore.QObject):

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
        #   68 BUILD_MAP
        #   70 LOAD_FAST self
        #   72 STORE_ATTR schedules
        #   82 LOAD_GLOBAL NULL + QtCore
        #   94 LOAD_ATTR QTimer
        #  104 LOAD_FAST self
        #  106 PRECALL
        #  110 CALL
        #  120 LOAD_FAST self
        #  122 STORE_ATTR timer
        #  132 LOAD_FAST self
        #  134 LOAD_ATTR timer
        #  144 LOAD_ATTR timeout
        #  154 LOAD_METHOD connect
        #  176 LOAD_FAST self
        #  178 LOAD_ATTR timer_cb
        #  188 PRECALL
        #  192 CALL
        #  202 POP_TOP
        #  204 LOAD_FAST self
        #  206 LOAD_ATTR timer
        #  216 LOAD_METHOD start
        #  238 LOAD_CONST 1000
        #  240 PRECALL
        #  244 CALL
        #  254 POP_TOP
        #  256 LOAD_CONST None
        #  258 RETURN_VALUE
        pass

    def get_schedule(self, serial_numbers):
        try:
            return self.schedules[serial_numbers]
        except KeyError:
            pass

        if len(serial_numbers) == 0:
            raise ValueError('No serial numbers provided')
        if len(serial_numbers) == 1:
            device_schedule = DeviceSchedule(None)
        elif len(serial_numbers) == 2:
            parent = self.get_schedule(serial_numbers[:-1])
            device_schedule = DeviceSchedule(parent)
        else:
            raise ValueError('Too many serial numbers provided')
        self.schedules[serial_numbers] = device_schedule
        return device_schedule

    def timer_cb(self):
        for device_schedule in self.schedules.values():
            device_schedule.clear_expired_items()
            return None
