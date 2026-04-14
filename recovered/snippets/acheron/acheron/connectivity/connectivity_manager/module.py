# Source Generated with Decompyle++
# File: tmph4_xslr4.marshal (Python 3.11)

import logging
import multiprocessing
from multiprocessing.connection import Connection, wait
import threading
from typing import Callable, Optional, Protocol
import numpy
from numpy.typing import NDArray
from calc_process.types import ChannelInformation
from core.preferences import Preferences
logger = logging.getLogger(__name__)
DeviceCallback = Callable[([
    int,
    NDArray[numpy.float64]], None)]

class ConnectivityHandler(Protocol):
    
    def stop_device(self = None, serial_number = None):
        pass

    
    def get_device_callback(self = None, serial_number = None, channel_info = None):
        pass

    
    def stop(self = None):
        pass

    
    def join(self = None):
        pass

    
    def update_preferences(self = None):
        pass



class ConnectivityManager:
    
    def __init__(self = None, preferences = None):
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

    
    def add_handler(self = None, handler = None):
        self.handlers.append(handler)

    
    def stop(self = None):
        self.stopped = True
        for handler in self.handlers:
            handler.stop()
            self.pipe_lock
            self.device_pipes.clear()
            self.pipe_callbacks.clear()
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def join(self = None):
        for handler in self.handlers:
            handler.join()
            self.pipe_thread_finished.set()
            self.pipe_thread.join()
            return None

    
    def create_device_pipe(self = None, serial_number = None, channel_info = None):
        self.stop_device(serial_number)
        if self.stopped:
            return None
        callbacks = None
    # WARNING: Decompyle incomplete

    
    def stop_device(self = None, serial_number = None):
        self.pipe_lock
        pipe = self.device_pipes.pop(serial_number, None)
    # WARNING: Decompyle incomplete

    
    def update_preferences(self = None):
        if self.stopped:
            return None
        for handler in None.handlers:
            handler.update_preferences()
            return None

    
    def _remove_pipe(self = None, pipe = None):
        self.all_pipes.discard(pipe)
        self.pipe_callbacks.pop(pipe, None)
        for serial_number, other_pipe in self.device_pipes.items():
            if pipe == other_pipe:
                del self.device_pipes[serial_number]
                return None
            return None

    
    def _pipe_loop(self = None):
        pass
    # WARNING: Decompyle incomplete


