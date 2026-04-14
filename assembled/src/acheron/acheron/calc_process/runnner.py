# Source Generated with Decompyle++
# File: runnner.pyc (Python 3.11)

import logging
from logging.handlers import QueueListener
import multiprocessing
from multiprocessing.connection import Connection
import threading
from typing import Any, Optional
from PySide6 import QtCore
from hyperborea.namedprocess import NamedProcess
from ..device_logging import DeviceLoggerAdapter, RemoteToLocalLogHandler
from .remote import run_calc_runner
from .types import CalcControl, CalcData, CalcSettings, Trigger
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class CalcProcess(QtCore.QObject):

    processing_start = QtCore.Signal(object, object, object)

    processing_stop = QtCore.Signal()

    status_received = QtCore.Signal(object)

    channel_update = QtCore.Signal(object, object, object)

    plot_update = QtCore.Signal(object, object, object)

    fft_update = QtCore.Signal(object, object, object, object)

    lost_packet_update = QtCore.Signal(object, object, object)

    unknown_id = QtCore.Signal(object)

    active_triggers_changed = QtCore.Signal(object)

    _start_plot_update = QtCore.Signal(int)

    _start_fft_update = QtCore.Signal(int)

    def __init__(self, calc_process_name, serial, is_shown, settings, triggers):
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
        #   68 LOAD_GLOBAL NULL + multiprocessing
        #   80 LOAD_ATTR Queue
        #   90 PRECALL
        #   94 CALL
        #  104 LOAD_FAST self
        #  106 STORE_ATTR log_queue
        #  116 LOAD_GLOBAL NULL + RemoteToLocalLogHandler
        #  128 LOAD_GLOBAL __name__
        #  140 LOAD_CONST '.remote'
        #  142 BINARY_OP +
        #  146 PRECALL
        #  150 CALL
        #  160 STORE_FAST local_handler
        #  162 LOAD_GLOBAL NULL + QueueListener
        #  174 LOAD_FAST self
        #  176 LOAD_ATTR log_queue
        #  186 LOAD_FAST local_handler
        #  188 PRECALL
        #  192 CALL
        #  202 LOAD_FAST self
        #  204 STORE_ATTR log_listener
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR log_listener
        #  226 LOAD_METHOD start
        #  248 PRECALL
        #  252 CALL
        #  262 POP_TOP
        #  264 LOAD_GLOBAL NULL + DeviceLoggerAdapter
        #  276 LOAD_GLOBAL logger
        #  288 LOAD_FAST serial
        #  290 PRECALL
        #  294 CALL
        #  304 LOAD_FAST self
        #  306 STORE_ATTR logger
        #  316 LOAD_GLOBAL NULL + threading
        #  328 LOAD_ATTR Lock
        #  338 PRECALL
        #  342 CALL
        #  352 LOAD_FAST self
        #  354 STORE_ATTR lock
        #  364 LOAD_GLOBAL NULL + threading
        #  376 LOAD_ATTR Event
        #  386 PRECALL
        #  390 CALL
        #  400 LOAD_FAST self
        #  402 STORE_ATTR stopped
        #  412 LOAD_GLOBAL NULL + threading
        #  424 LOAD_ATTR Event
        #  434 PRECALL
        #  438 CALL
        #  448 LOAD_FAST self
        #  450 STORE_ATTR finished
        #  460 LOAD_GLOBAL NULL + threading
        #  472 LOAD_ATTR Event
        #  482 PRECALL
        #  486 CALL
        #  496 LOAD_FAST self
        #  498 STORE_ATTR closed
        #  508 LOAD_CONST None
        #  510 LOAD_FAST self
        #  512 STORE_ATTR plot_data
        #  522 LOAD_CONST None
        #  524 LOAD_FAST self
        #  526 STORE_ATTR fft_data
        #  536 LOAD_GLOBAL NULL + QtCore
        #  548 LOAD_ATTR QTimer
        #  558 LOAD_FAST self
        #  560 PRECALL
        #  564 CALL
        #  574 LOAD_FAST self
        #  576 STORE_ATTR plot_timer
        # ... bytecode truncated ...
        pass

    def stop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR stopped
        #   30 LOAD_METHOD is_set
        #   52 PRECALL
        #   56 CALL
        #   66 POP_JUMP_FORWARD_IF_TRUE to 244
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR stopped
        #   80 LOAD_METHOD set
        #  102 PRECALL
        #  106 CALL
        #  116 POP_TOP
        #  118 LOAD_FAST self
        #  120 LOAD_ATTR calc_ctrl_tx_pipe
        #  130 LOAD_METHOD send
        #  152 LOAD_GLOBAL CalcControl
        #  164 LOAD_ATTR STOP
        #  174 BUILD_TUPLE
        #  176 PRECALL
        #  180 CALL
        #  190 POP_TOP
        #  192 LOAD_FAST self
        #  194 LOAD_ATTR logger
        #  204 LOAD_METHOD debug
        #  226 LOAD_CONST 'Calc process stopping'
        #  228 PRECALL
        #  232 CALL
        #  242 POP_TOP
        #  244 LOAD_CONST None
        #  246 LOAD_CONST None
        #  248 LOAD_CONST None
        #  250 PRECALL
        #  254 CALL
        #  264 POP_TOP
        #  266 LOAD_CONST None
        #  268 RETURN_VALUE
        #  270 PUSH_EXC_INFO
        #  272 WITH_EXCEPT_START
        #  274 POP_JUMP_FORWARD_IF_TRUE to 284
        #  276 RERAISE
        #  278 COPY
        #  280 POP_EXCEPT
        #  282 RERAISE
        #  284 POP_TOP
        #  286 POP_EXCEPT
        #  288 POP_TOP
        #  290 POP_TOP
        #  292 LOAD_CONST None
        #  294 RETURN_VALUE
        pass

    def close(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_METHOD stop
        #   26 PRECALL
        #   30 CALL
        #   40 POP_TOP
        #   42 LOAD_FAST self
        #   44 LOAD_ATTR lock
        #   54 BEFORE_WITH
        #   56 POP_TOP
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR closed
        #   70 LOAD_METHOD is_set
        #   92 PRECALL
        #   96 CALL
        #  106 POP_JUMP_FORWARD_IF_FALSE to 136
        #  108 NOP
        #  110 LOAD_CONST None
        #  112 LOAD_CONST None
        #  114 LOAD_CONST None
        #  116 PRECALL
        #  120 CALL
        #  130 POP_TOP
        #  132 LOAD_CONST None
        #  134 RETURN_VALUE
        #  136 LOAD_FAST self
        #  138 LOAD_ATTR calc_ctrl_tx_pipe
        #  148 LOAD_METHOD send
        #  170 LOAD_GLOBAL CalcControl
        #  182 LOAD_ATTR CLOSE
        #  192 BUILD_TUPLE
        #  194 PRECALL
        #  198 CALL
        #  208 POP_TOP
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR finished
        #  222 LOAD_METHOD set
        #  244 PRECALL
        #  248 CALL
        #  258 POP_TOP
        #  260 LOAD_FAST self
        #  262 LOAD_ATTR log_listener
        #  272 POP_JUMP_FORWARD_IF_FALSE to 402
        #  274 LOAD_FAST self
        #  276 LOAD_ATTR log_listener
        #  286 LOAD_METHOD stop
        #  308 PRECALL
        #  312 CALL
        #  322 POP_TOP
        #  324 LOAD_CONST None
        #  326 LOAD_FAST self
        #  328 STORE_ATTR log_listener
        #  338 LOAD_FAST self
        #  340 LOAD_ATTR log_queue
        #  350 LOAD_METHOD close
        #  372 PRECALL
        #  376 CALL
        #  386 POP_TOP
        #  388 LOAD_CONST None
        #  390 LOAD_FAST self
        #  392 STORE_ATTR log_queue
        #  402 LOAD_FAST self
        #  404 LOAD_ATTR closed
        #  414 LOAD_METHOD set
        #  436 PRECALL
        #  440 CALL
        #  450 POP_TOP
        #  452 LOAD_FAST self
        #  454 LOAD_ATTR logger
        #  464 LOAD_METHOD debug
        #  486 LOAD_CONST 'Calc process closed'
        #  488 PRECALL
        #  492 CALL
        #  502 POP_TOP
        #  504 LOAD_CONST None
        #  506 LOAD_CONST None
        #  508 LOAD_CONST None
        #  510 PRECALL
        #  514 CALL
        #  524 POP_TOP
        # ... bytecode truncated ...
        pass

    def join(self):
        self.close()
        self.remote_process.join()
        self.data_thread.join()
        self.status_thread.join()
        self.status_rx_pipe.close()
        self.status_tx_pipe.close()
        self.packet_rx_pipe.close()
        self.packet_tx_pipe.close()
        self.stream_ctrl_rx_pipe.close()
        self.stream_ctrl_tx_pipe.close()
        self.data_rx_pipe.close()
        self.data_tx_pipe.close()
        self.calc_ctrl_rx_pipe.close()
        self.calc_ctrl_tx_pipe.close()
        self.logger.debug('Calc process joined')

    def get_pipes(self):
        return (self.stream_ctrl_rx_pipe, self.packet_tx_pipe, self.status_tx_pipe)

    def status_thread_run(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR status_rx_pipe
        #   16 STORE_FAST pipe
        #   18 NOP
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR finished
        #   32 LOAD_METHOD is_set
        #   54 PRECALL
        #   58 CALL
        #   68 POP_JUMP_FORWARD_IF_FALSE to 74
        #   70 LOAD_CONST None
        #   72 RETURN_VALUE
        #   74 LOAD_FAST pipe
        #   76 LOAD_METHOD poll
        #   98 LOAD_CONST 0.1
        #  100 PRECALL
        #  104 CALL
        #  114 POP_JUMP_FORWARD_IF_FALSE to 254
        #  116 NOP
        #  118 LOAD_FAST pipe
        #  120 LOAD_METHOD recv
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST status
        #  158 JUMP_FORWARD to 194
        #  160 PUSH_EXC_INFO
        #  162 LOAD_GLOBAL EOFError
        #  174 CHECK_EXC_MATCH
        #  176 POP_JUMP_FORWARD_IF_FALSE to 186
        #  178 POP_TOP
        #  180 POP_EXCEPT
        #  182 LOAD_CONST None
        #  184 RETURN_VALUE
        #  186 RERAISE
        #  188 COPY
        #  190 POP_EXCEPT
        #  192 RERAISE
        #  194 LOAD_FAST status
        #  196 POP_JUMP_FORWARD_IF_NOT_NONE to 202
        #  198 LOAD_CONST None
        #  200 RETURN_VALUE
        #  202 LOAD_FAST self
        #  204 LOAD_ATTR status_received
        #  214 LOAD_METHOD emit
        #  236 LOAD_FAST status
        #  238 PRECALL
        #  242 CALL
        #  252 POP_TOP
        #  254 JUMP_BACKWARD to 20
        #  256 PUSH_EXC_INFO
        #  258 LOAD_GLOBAL Exception
        #  270 CHECK_EXC_MATCH
        #  272 POP_JUMP_FORWARD_IF_FALSE to 374
        #  274 POP_TOP
        #  276 LOAD_FAST self
        #  278 LOAD_ATTR logger
        #  288 LOAD_METHOD exception
        #  310 LOAD_CONST 'Unhandled exception in status_thread_run'
        #  312 PRECALL
        #  316 CALL
        #  326 POP_TOP
        #  328 LOAD_FAST self
        #  330 LOAD_METHOD stop
        #  352 PRECALL
        #  356 CALL
        #  366 POP_TOP
        #  368 POP_EXCEPT
        #  370 LOAD_CONST None
        #  372 RETURN_VALUE
        #  374 RERAISE
        #  376 COPY
        #  378 POP_EXCEPT
        #  380 RERAISE
        pass

    def data_thread_run(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR data_rx_pipe
        #   16 STORE_FAST pipe
        #   18 NOP
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR finished
        #   32 LOAD_METHOD is_set
        #   54 PRECALL
        #   58 CALL
        #   68 POP_JUMP_FORWARD_IF_FALSE to 74
        #   70 LOAD_CONST None
        #   72 RETURN_VALUE
        #   74 LOAD_FAST pipe
        #   76 LOAD_METHOD poll
        #   98 LOAD_CONST 0.1
        #  100 PRECALL
        #  104 CALL
        #  114 POP_JUMP_FORWARD_IF_FALSE to 236
        #  116 NOP
        #  118 LOAD_FAST pipe
        #  120 LOAD_METHOD recv
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST data
        #  158 JUMP_FORWARD to 194
        #  160 PUSH_EXC_INFO
        #  162 LOAD_GLOBAL EOFError
        #  174 CHECK_EXC_MATCH
        #  176 POP_JUMP_FORWARD_IF_FALSE to 186
        #  178 POP_TOP
        #  180 POP_EXCEPT
        #  182 LOAD_CONST None
        #  184 RETURN_VALUE
        #  186 RERAISE
        #  188 COPY
        #  190 POP_EXCEPT
        #  192 RERAISE
        #  194 LOAD_FAST self
        #  196 LOAD_METHOD handle_data
        #  218 LOAD_FAST data
        #  220 PRECALL
        #  224 CALL
        #  234 POP_TOP
        #  236 JUMP_BACKWARD to 20
        #  238 PUSH_EXC_INFO
        #  240 LOAD_GLOBAL Exception
        #  252 CHECK_EXC_MATCH
        #  254 POP_JUMP_FORWARD_IF_FALSE to 356
        #  256 POP_TOP
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR logger
        #  270 LOAD_METHOD exception
        #  292 LOAD_CONST 'Unhandled exception in data_thread_run'
        #  294 PRECALL
        #  298 CALL
        #  308 POP_TOP
        #  310 LOAD_FAST self
        #  312 LOAD_METHOD stop
        #  334 PRECALL
        #  338 CALL
        #  348 POP_TOP
        #  350 POP_EXCEPT
        #  352 LOAD_CONST None
        #  354 RETURN_VALUE
        #  356 RERAISE
        #  358 COPY
        #  360 POP_EXCEPT
        #  362 RERAISE
        pass

    def handle_data(self, data):
        if self.stopped.is_set():
            return None

    def set_is_shown(self, is_shown):
        self.calc_ctrl_tx_pipe.send((CalcControl.SET_SHOWN, is_shown))

    def plot_change(self, channel_id, subchannel_index):
        self.calc_ctrl_tx_pipe.send((CalcControl.PLOT_CHANGE, channel_id, subchannel_index))

    def reset_lost_packets(self):
        self.calc_ctrl_tx_pipe.send((CalcControl.RESET_LOST_PACKETS,))

    def send_stream_ctrl_message(self, message):
        self.stream_ctrl_tx_pipe.send(message)

    def change_settings(self, settings):
        self.calc_ctrl_tx_pipe.send((CalcControl.CHANGE_SETTINGS, settings))

    def change_triggers(self, triggers):
        self.calc_ctrl_tx_pipe.send((CalcControl.CHANGE_TRIGGERS, triggers))

    def set_connectivity_pipe(self, pipe):
        self.calc_ctrl_tx_pipe.send((CalcControl.SET_CONNECTIVITY_PIPE, pipe))

    def _plot_update_cb(self):
        data = self.plot_data
        self.plot_data = None

    def _fft_update_cb(self):
        data = self.fft_data
        self.fft_data = None
