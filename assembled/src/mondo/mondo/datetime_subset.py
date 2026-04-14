# Source Generated with Decompyle++
# File: datetime_subset.pyc (Python 3.11)

import datetime
import logging
from typing import cast, Optional
from PySide6 import QtCore, QtWidgets
from .ui.ui_datetime_subset import Ui_DateTimeSubsetDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DateTimeSubsetDialog(Ui_DateTimeSubsetDialog, QtWidgets.QDialog):

    def __init__(self, start_qdt, end_qdt, parent):
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
        #   54 LOAD_GLOBAL QtCore
        #   66 LOAD_ATTR Qt
        #   76 LOAD_ATTR WindowType
        #   86 LOAD_ATTR MSWindowsFixedSizeDialogHint
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_FAST start_qdt
        #  114 LOAD_FAST self
        #  116 STORE_ATTR start_qdt
        #  126 LOAD_FAST end_qdt
        #  128 LOAD_FAST self
        #  130 STORE_ATTR end_qdt
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD setupUi
        #  164 LOAD_FAST self
        #  166 PRECALL
        #  170 CALL
        #  180 POP_TOP
        #  182 LOAD_GLOBAL NULL + cast
        #  194 LOAD_GLOBAL datetime
        #  206 LOAD_ATTR datetime
        #  216 LOAD_FAST start_qdt
        #  218 LOAD_METHOD toPython
        #  240 PRECALL
        #  244 CALL
        #  254 PRECALL
        #  258 CALL
        #  268 STORE_FAST start_py
        #  270 LOAD_GLOBAL NULL + cast
        #  282 LOAD_GLOBAL datetime
        #  294 LOAD_ATTR datetime
        #  304 LOAD_FAST end_qdt
        #  306 LOAD_METHOD toPython
        #  328 PRECALL
        #  332 CALL
        #  342 PRECALL
        #  346 CALL
        #  356 STORE_FAST end_py
        #  358 LOAD_FAST end_py
        #  360 LOAD_FAST start_py
        #  362 COMPARE_OP >=
        #  368 POP_JUMP_FORWARD_IF_FALSE to 444
        #  370 LOAD_GLOBAL NULL + int
        #  382 LOAD_FAST end_py
        #  384 LOAD_FAST start_py
        #  386 BINARY_OP -
        #  390 LOAD_METHOD total_seconds
        #  412 PRECALL
        #  416 CALL
        #  426 PRECALL
        #  430 CALL
        #  440 STORE_FAST duration
        #  442 JUMP_FORWARD to 500
        #  444 LOAD_CONST 0
        #  446 STORE_FAST duration
        #  448 LOAD_FAST self
        #  450 LOAD_ATTR useSubset
        #  460 LOAD_METHOD setEnabled
        #  482 LOAD_CONST False
        #  484 PRECALL
        #  488 CALL
        #  498 POP_TOP
        #  500 LOAD_FAST self
        #  502 LOAD_ATTR allStart
        #  512 LOAD_METHOD setText
        #  534 LOAD_FAST self
        #  536 LOAD_ATTR startDateTime
        #  546 LOAD_METHOD textFromDateTime
        #  568 LOAD_FAST start_qdt
        #  570 PRECALL
        #  574 CALL
        #  584 PRECALL
        # ... bytecode truncated ...
        pass

    def should_use_all(self):
        return self.useAllData.isChecked()

    def trim_datetime_to_range(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST value
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR start_qdt
        #   16 COMPARE_OP <
        #   22 POP_JUMP_FORWARD_IF_FALSE to 38
        #   24 LOAD_FAST self
        #   26 LOAD_ATTR start_qdt
        #   36 RETURN_VALUE
        #   38 LOAD_FAST value
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR end_qdt
        #   52 COMPARE_OP >
        #   58 POP_JUMP_FORWARD_IF_FALSE to 74
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR end_qdt
        #   72 RETURN_VALUE
        #   74 LOAD_FAST value
        #   76 RETURN_VALUE
        pass

    def datetime_in_range(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR start_qdt
        #   14 LOAD_FAST value
        #   16 COMPARE_OP <=
        #   22 JUMP_IF_FALSE_OR_POP to 44
        #   24 LOAD_FAST value
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR end_qdt
        #   38 COMPARE_OP <=
        #   44 RETURN_VALUE
        pass

    def get_subset(self):
        start_qdt = self.trim_datetime_to_range(self.startDateTime.dateTime())
        end_qdt = self.trim_datetime_to_range(self.endDateTime.dateTime())
        return (start_qdt, end_qdt)

    def start_changed(self, new_date_time):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD update_duration
        #   26 LOAD_CONST True
        #   28 KW_NAMES
        #   30 PRECALL
        #   34 CALL
        #   44 POP_TOP
        #   46 LOAD_FAST self
        #   48 LOAD_METHOD datetime_in_range
        #   70 LOAD_FAST new_date_time
        #   72 PRECALL
        #   76 CALL
        #   86 POP_JUMP_FORWARD_IF_FALSE to 258
        #   88 LOAD_FAST self
        #   90 LOAD_ATTR endDateTime
        #  100 LOAD_METHOD dateTime
        #  122 PRECALL
        #  126 CALL
        #  136 LOAD_FAST new_date_time
        #  138 COMPARE_OP <
        #  144 POP_JUMP_FORWARD_IF_FALSE to 202
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR startDateTime
        #  158 LOAD_METHOD setStyleSheet
        #  180 LOAD_CONST '* { color: black; background-color: yellow; }'
        #  182 PRECALL
        #  186 CALL
        #  196 POP_TOP
        #  198 LOAD_CONST None
        #  200 RETURN_VALUE
        #  202 LOAD_FAST self
        #  204 LOAD_ATTR startDateTime
        #  214 LOAD_METHOD setStyleSheet
        #  236 LOAD_CONST ''
        #  238 PRECALL
        #  242 CALL
        #  252 POP_TOP
        #  254 LOAD_CONST None
        #  256 RETURN_VALUE
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR startDateTime
        #  270 LOAD_METHOD setStyleSheet
        #  292 LOAD_CONST '* { color: black; background-color: red; }'
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 LOAD_CONST None
        #  312 RETURN_VALUE
        pass

    def end_changed(self, new_date_time):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD update_duration
        #   26 LOAD_CONST False
        #   28 KW_NAMES
        #   30 PRECALL
        #   34 CALL
        #   44 POP_TOP
        #   46 LOAD_FAST self
        #   48 LOAD_METHOD datetime_in_range
        #   70 LOAD_FAST new_date_time
        #   72 PRECALL
        #   76 CALL
        #   86 POP_JUMP_FORWARD_IF_FALSE to 258
        #   88 LOAD_FAST new_date_time
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR startDateTime
        #  102 LOAD_METHOD dateTime
        #  124 PRECALL
        #  128 CALL
        #  138 COMPARE_OP <
        #  144 POP_JUMP_FORWARD_IF_FALSE to 202
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR endDateTime
        #  158 LOAD_METHOD setStyleSheet
        #  180 LOAD_CONST '* { color: black; background-color: yellow; }'
        #  182 PRECALL
        #  186 CALL
        #  196 POP_TOP
        #  198 LOAD_CONST None
        #  200 RETURN_VALUE
        #  202 LOAD_FAST self
        #  204 LOAD_ATTR endDateTime
        #  214 LOAD_METHOD setStyleSheet
        #  236 LOAD_CONST ''
        #  238 PRECALL
        #  242 CALL
        #  252 POP_TOP
        #  254 LOAD_CONST None
        #  256 RETURN_VALUE
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR endDateTime
        #  270 LOAD_METHOD setStyleSheet
        #  292 LOAD_CONST '* { color: black; background-color: red }'
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 LOAD_CONST None
        #  312 RETURN_VALUE
        pass

    def start_editing_finished(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD datetime_in_range
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR startDateTime
        #   38 LOAD_METHOD dateTime
        #   60 PRECALL
        #   64 CALL
        #   74 PRECALL
        #   78 CALL
        #   88 POP_JUMP_FORWARD_IF_FALSE to 398
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR endDateTime
        #  102 LOAD_METHOD dateTime
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR startDateTime
        #  150 LOAD_METHOD dateTime
        #  172 PRECALL
        #  176 CALL
        #  186 COMPARE_OP <=
        #  192 POP_JUMP_FORWARD_IF_FALSE to 394
        #  194 LOAD_FAST self
        #  196 LOAD_ATTR endDateTime
        #  206 LOAD_METHOD setDateTime
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR startDateTime
        #  240 LOAD_METHOD dateTime
        #  262 PRECALL
        #  266 CALL
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_FAST self
        #  294 LOAD_ATTR startDateTime
        #  304 LOAD_METHOD setDateTime
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR startDateTime
        #  338 LOAD_METHOD dateTime
        #  360 PRECALL
        #  364 CALL
        #  374 PRECALL
        #  378 CALL
        #  388 POP_TOP
        #  390 LOAD_CONST None
        #  392 RETURN_VALUE
        #  394 LOAD_CONST None
        #  396 RETURN_VALUE
        #  398 LOAD_FAST self
        #  400 LOAD_ATTR startDateTime
        #  410 LOAD_METHOD setDateTime
        #  432 LOAD_FAST self
        #  434 LOAD_ATTR start_qdt
        #  444 PRECALL
        #  448 CALL
        #  458 POP_TOP
        #  460 LOAD_CONST None
        #  462 RETURN_VALUE
        pass

    def end_editing_finished(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD datetime_in_range
        #   26 LOAD_FAST self
        #   28 LOAD_ATTR endDateTime
        #   38 LOAD_METHOD dateTime
        #   60 PRECALL
        #   64 CALL
        #   74 PRECALL
        #   78 CALL
        #   88 POP_JUMP_FORWARD_IF_FALSE to 398
        #   90 LOAD_FAST self
        #   92 LOAD_ATTR endDateTime
        #  102 LOAD_METHOD dateTime
        #  124 PRECALL
        #  128 CALL
        #  138 LOAD_FAST self
        #  140 LOAD_ATTR startDateTime
        #  150 LOAD_METHOD dateTime
        #  172 PRECALL
        #  176 CALL
        #  186 COMPARE_OP <=
        #  192 POP_JUMP_FORWARD_IF_FALSE to 394
        #  194 LOAD_FAST self
        #  196 LOAD_ATTR startDateTime
        #  206 LOAD_METHOD setDateTime
        #  228 LOAD_FAST self
        #  230 LOAD_ATTR endDateTime
        #  240 LOAD_METHOD dateTime
        #  262 PRECALL
        #  266 CALL
        #  276 PRECALL
        #  280 CALL
        #  290 POP_TOP
        #  292 LOAD_FAST self
        #  294 LOAD_ATTR endDateTime
        #  304 LOAD_METHOD setDateTime
        #  326 LOAD_FAST self
        #  328 LOAD_ATTR endDateTime
        #  338 LOAD_METHOD dateTime
        #  360 PRECALL
        #  364 CALL
        #  374 PRECALL
        #  378 CALL
        #  388 POP_TOP
        #  390 LOAD_CONST None
        #  392 RETURN_VALUE
        #  394 LOAD_CONST None
        #  396 RETURN_VALUE
        #  398 LOAD_FAST self
        #  400 LOAD_ATTR endDateTime
        #  410 LOAD_METHOD setDateTime
        #  432 LOAD_FAST self
        #  434 LOAD_ATTR end_qdt
        #  444 PRECALL
        #  448 CALL
        #  458 POP_TOP
        #  460 LOAD_CONST None
        #  462 RETURN_VALUE
        pass

    def update_duration(self, moving_start):
        start_qdt = self.startDateTime.dateTime()
        end_qdt = self.endDateTime.dateTime()
        if start_qdt < self.start_qdt:
            start_py = cast(datetime.datetime, self.start_qdt.toPython())
        elif self.end_qdt < start_qdt:
            start_py = cast(datetime.datetime, self.end_qdt.toPython())
        else:
            start_py = cast(datetime.datetime, start_qdt.toPython())
        if end_qdt < self.start_qdt:
            end_py = cast(datetime.datetime, self.start_qdt.toPython())
        elif self.end_qdt < end_qdt:
            end_py = cast(datetime.datetime, self.end_qdt.toPython())
        else:
            end_py = cast(datetime.datetime, end_qdt.toPython())
        if end_py < start_py:
            if moving_start:
                end_py = start_py
            else:
                start_py = end_py
        start_seconds = (start_py - cast(datetime.datetime, self.start_qdt.toPython())).total_seconds()
        self.startSeconds.setValue(int(start_seconds))
        end_seconds = (end_py - cast(datetime.datetime, self.end_qdt.toPython())).total_seconds()
        self.endSeconds.setValue(int(end_seconds))
        self.duration.setValue(int((end_py - start_py).total_seconds()))

    def start_seconds_changed(self):
        new_start = self.start_qdt.addSecs(self.startSeconds.value())
        if new_start > self.endDateTime.dateTime():
            self.endDateTime.setDateTime(new_start)
        self.startDateTime.setDateTime(new_start)

    def end_seconds_changed(self):
        new_end = self.end_qdt.addSecs(self.endSeconds.value())
        if new_end < self.startDateTime.dateTime():
            self.startDateTime.setDateTime(new_end)
        self.endDateTime.setDateTime(new_end)

    def duration_changed(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR duration
        #   14 LOAD_METHOD value
        #   36 PRECALL
        #   40 CALL
        #   50 STORE_FAST duration
        #   52 LOAD_GLOBAL NULL + cast
        #   64 LOAD_GLOBAL datetime
        #   76 LOAD_ATTR datetime
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR startDateTime
        #   98 LOAD_METHOD dateTime
        #  120 PRECALL
        #  124 CALL
        #  134 LOAD_METHOD toPython
        #  156 PRECALL
        #  160 CALL
        #  170 PRECALL
        #  174 CALL
        #  184 STORE_FAST current_start
        #  186 LOAD_GLOBAL NULL + cast
        #  198 LOAD_GLOBAL datetime
        #  210 LOAD_ATTR datetime
        #  220 LOAD_FAST self
        #  222 LOAD_ATTR end_qdt
        #  232 LOAD_METHOD toPython
        #  254 PRECALL
        #  258 CALL
        #  268 PRECALL
        #  272 CALL
        #  282 STORE_FAST end_py
        #  284 LOAD_GLOBAL NULL + int
        #  296 LOAD_FAST end_py
        #  298 LOAD_FAST current_start
        #  300 BINARY_OP -
        #  304 LOAD_METHOD total_seconds
        #  326 PRECALL
        #  330 CALL
        #  340 PRECALL
        #  344 CALL
        #  354 STORE_FAST headroom
        #  356 LOAD_FAST duration
        #  358 LOAD_FAST headroom
        #  360 COMPARE_OP <=
        #  366 POP_JUMP_FORWARD_IF_FALSE to 430
        #  368 LOAD_FAST self
        #  370 LOAD_ATTR endSeconds
        #  380 LOAD_METHOD setValue
        #  402 LOAD_FAST duration
        #  404 LOAD_FAST headroom
        #  406 BINARY_OP -
        #  410 PRECALL
        #  414 CALL
        #  424 POP_TOP
        #  426 LOAD_CONST None
        #  428 RETURN_VALUE
        #  430 LOAD_FAST self
        #  432 LOAD_ATTR endDateTime
        #  442 LOAD_METHOD setDateTime
        #  464 LOAD_FAST self
        #  466 LOAD_ATTR end_qdt
        #  476 PRECALL
        #  480 CALL
        #  490 POP_TOP
        #  492 LOAD_FAST self
        #  494 LOAD_ATTR startDateTime
        #  504 LOAD_METHOD setDateTime
        #  526 LOAD_FAST self
        #  528 LOAD_ATTR end_qdt
        #  538 LOAD_METHOD addSecs
        #  560 LOAD_FAST duration
        #  562 UNARY_NEGATIVE
        #  564 PRECALL
        #  568 CALL
        #  578 PRECALL
        #  582 CALL
        #  592 POP_TOP
        #  594 LOAD_CONST None
        #  596 RETURN_VALUE
        pass
