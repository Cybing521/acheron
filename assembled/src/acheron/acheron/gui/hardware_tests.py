# Source Generated with Decompyle++
# File: hardware_tests.pyc (Python 3.11)

import datetime
import functools
import logging
import os
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from asphodel import AsphodelStreamInfo, AsphodelChannelInfo, SupplyInfo
from asphodel.device_info import DeviceInfo
from ..device_logging import DeviceLoggerAdapter
from ..core.device_controller import DeviceController
from ..core.preferences import Preferences
from ..device_process.hardware_test_funcs import accel_test, bridge_test, supply_test
from ..device_process.stream_controller import HardwareTestFunction
from .ui.ui_hardware_tests import Ui_HardwareTestDialog
logger = logging.getLogger(__name__)
TestInstance = tuple[(HardwareTestFunction, str)]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class HardwareTestDialog(Ui_HardwareTestDialog, QtWidgets.QDialog):

    def __init__(self, device_info, controller, preferences, logger, parent):
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
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST device_info
        #   72 LOAD_FAST self
        #   74 STORE_ATTR device_info
        #   84 LOAD_FAST controller
        #   86 LOAD_FAST self
        #   88 STORE_ATTR controller
        #   98 LOAD_FAST preferences
        #  100 LOAD_FAST self
        #  102 STORE_ATTR preferences
        #  112 LOAD_FAST logger
        #  114 LOAD_FAST self
        #  116 STORE_ATTR logger
        #  126 LOAD_FAST self
        #  128 POP_TOP
        #  130 LOAD_FAST self
        #  132 LOAD_METHOD create_test_list
        #  154 PRECALL
        #  158 CALL
        #  168 POP_TOP
        #  170 BUILD_MAP
        #  172 LOAD_FAST self
        #  174 STORE_ATTR results
        #  184 LOAD_FAST self
        #  186 LOAD_METHOD setupUi
        #  208 LOAD_FAST self
        #  210 PRECALL
        #  214 CALL
        #  224 POP_TOP
        #  226 LOAD_CONST ''
        #  228 LOAD_FAST self
        #  230 STORE_ATTR test_log
        #  240 LOAD_FAST self
        #  242 LOAD_ATTR testOutput
        #  252 LOAD_METHOD setPlainText
        #  274 LOAD_FAST self
        #  276 LOAD_ATTR test_log
        #  286 PRECALL
        #  290 CALL
        #  300 POP_TOP
        #  302 LOAD_FAST self
        #  304 LOAD_ATTR buttonBox
        #  314 LOAD_METHOD button
        #  336 LOAD_GLOBAL QtWidgets
        #  348 LOAD_ATTR QDialogButtonBox
        #  358 LOAD_ATTR StandardButton
        #  368 LOAD_ATTR Reset
        #  378 PRECALL
        #  382 CALL
        #  392 LOAD_FAST self
        #  394 STORE_ATTR rerunButton
        #  404 LOAD_FAST self
        #  406 LOAD_ATTR rerunButton
        #  416 LOAD_METHOD setText
        #  438 LOAD_FAST self
        #  440 LOAD_METHOD tr
        #  462 LOAD_CONST 'Rerun Tests'
        #  464 PRECALL
        #  468 CALL
        #  478 PRECALL
        #  482 CALL
        #  492 POP_TOP
        #  494 LOAD_FAST self
        #  496 LOAD_ATTR rerunButton
        #  506 LOAD_ATTR clicked
        #  516 LOAD_METHOD connect
        #  538 LOAD_FAST self
        #  540 LOAD_ATTR start_tests
        #  550 PRECALL
        #  554 CALL
        #  564 POP_TOP
        # ... bytecode truncated ...
        pass

    def _create_supply_test(self, supply_id, name, info):
        func = functools.partial(supply_test, supply_id = supply_id, name = name, info = info)
        return (func, f'''supply_{supply_id}''')

    def _create_accel_test(self, stream_id, stream, channel_id, channel):
        func = functools.partial(accel_test, stream_id = stream_id, stream = stream, channel_id = channel_id, channel = channel)
        return (func, f'''accel_{stream_id}_{channel_id}''')

    def _create_bridge_test(self, stream_id, stream, channel_id, channel):
        func = functools.partial(bridge_test, stream_id = stream_id, stream = stream, channel_id = channel_id, channel = channel)
        return (func, f'''bridge_{stream_id}_{channel_id}''')

    def create_test_list(self):
        self.tests = []
        for name, supply_info in enumerate(self.device_info.supplies):
            self.tests.append(self._create_supply_test(i, name, supply_info))
            for stream_id, stream in enumerate(self.device_info.streams):
                channel_indexes = stream.channel_index_list[0:stream.channel_count]
                for channel_id in channel_indexes:
                    if channel_id < len(self.device_info.channels):
                        channel = self.device_info.channels[channel_id]
                        ch_type = channel.channel_type
                        if ch_type == asphodel.CHANNEL_TYPE_SLOW_ACCEL and ch_type == asphodel.CHANNEL_TYPE_PACKED_ACCEL or ch_type == asphodel.CHANNEL_TYPE_LINEAR_ACCEL:
                            self.tests.append(self._create_accel_test(stream_id, stream, channel_id, channel))
                            continue
                        if ch_type == asphodel.CHANNEL_TYPE_SLOW_STRAIN and ch_type == asphodel.CHANNEL_TYPE_FAST_STRAIN or ch_type == asphodel.CHANNEL_TYPE_COMPOSITE_STRAIN:
                            self.tests.append(self._create_bridge_test(stream_id, stream, channel_id, channel))
                    return None

    def start_tests(self):
        self.rerunButton.setEnabled(False)
        self.results = { }
        self.controller.run_hardware_tests(self.tests, self)
        dt = datetime.datetime.now(tz = datetime.timezone.utc)
        dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        start_message = f'''*** Start of tests {dt_str} ***\n\n'''
        self.test_log = start_message
        self.testOutput.setPlainText(self.test_log)

    def hardware_test_function_finished(self, test_id, data):
        (success, message) = data
        self.results[test_id] = success
        self.testOutput.setPlainText(self.test_log)

    def hardware_test_run_finished(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR rerunButton
        #   14 LOAD_METHOD setEnabled
        #   36 LOAD_CONST True
        #   38 PRECALL
        #   42 CALL
        #   52 POP_TOP
        #   54 LOAD_GLOBAL NULL + len
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR results
        #   78 PRECALL
        #   82 CALL
        #   92 LOAD_GLOBAL NULL + len
        #  104 LOAD_FAST self
        #  106 LOAD_ATTR tests
        #  116 PRECALL
        #  120 CALL
        #  130 COMPARE_OP !=
        #  136 POP_JUMP_FORWARD_IF_FALSE to 170
        #  138 LOAD_FAST self
        #  140 COPY
        #  142 LOAD_ATTR test_log
        #  152 LOAD_CONST '\nMissing test results!\n'
        #  154 BINARY_OP +=
        #  158 SWAP
        #  160 STORE_ATTR test_log
        #  170 LOAD_GLOBAL NULL + sum
        #  182 LOAD_CONST <code object <genexpr> at 0x105af8ab0, file "acheron\gui\hardware_tests.py", line 135>
        #  184 MAKE_FUNCTION
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR results
        #  198 LOAD_METHOD values
        #  220 PRECALL
        #  224 CALL
        #  234 GET_ITER
        #  236 PRECALL
        #  240 CALL
        #  250 PRECALL
        #  254 CALL
        #  264 STORE_FAST failures
        #  266 LOAD_FAST failures
        #  268 LOAD_CONST 1
        #  270 COMPARE_OP !=
        #  276 POP_JUMP_FORWARD_IF_FALSE to 282
        #  278 LOAD_CONST 'failures'
        #  280 JUMP_FORWARD to 284
        #  282 LOAD_CONST 'failure'
        #  284 STORE_FAST plural
        #  286 LOAD_FAST self
        #  288 COPY
        #  290 LOAD_ATTR test_log
        #  300 LOAD_CONST '\n'
        #  302 LOAD_FAST failures
        #  304 FORMAT_VALUE
        #  306 LOAD_CONST ' '
        #  308 LOAD_FAST plural
        #  310 FORMAT_VALUE
        #  312 LOAD_CONST '\n\n'
        #  314 BUILD_STRING
        #  316 BINARY_OP +=
        #  320 SWAP
        #  322 STORE_ATTR test_log
        #  332 LOAD_GLOBAL datetime
        #  344 LOAD_ATTR datetime
        #  354 LOAD_METHOD now
        #  376 LOAD_GLOBAL datetime
        #  388 LOAD_ATTR timezone
        #  398 LOAD_ATTR utc
        #  408 KW_NAMES
        #  410 PRECALL
        #  414 CALL
        #  424 STORE_FAST dt
        #  426 LOAD_FAST dt
        #  428 LOAD_METHOD strftime
        #  450 LOAD_CONST '%Y-%m-%dT%H:%M:%SZ'
        #  452 PRECALL
        #  456 CALL
        #  466 STORE_FAST dt_str
        #  468 LOAD_CONST '*** End of tests '
        # ... bytecode truncated ...
        pass

    def save_test_log(self):
        dt = datetime.datetime.now(tz = datetime.timezone.utc)
        dt_str = dt.strftime('%Y%m%dT%H%MZ_')
        directory = os.path.join(self.preferences.base_dir, 'Hardware Tests')
        base_name = os.path.join(directory, dt_str + self.controller.serial_number)
        filename = base_name + '.txt'
        index = 1
