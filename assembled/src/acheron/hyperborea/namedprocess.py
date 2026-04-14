# Source Generated with Decompyle++
# File: namedprocess.pyc (Python 3.11)

import logging
import multiprocessing
import os
import sys
import threading
from typing import Any, Optional

try:
    import setproctitle
except ModuleNotFoundError:
    setproctitle = None

logger = logging.getLogger(__name__)
lock = threading.Lock()
# INVALID FROM DECOMPILER: if sys.platform == 'win32':

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class NamedProcess(multiprocessing.Process):

    def __init__(self, name, description, **kwargs):
        self.title = f'{name} {description}'
        self.executable = None
        if sys.platform == 'win32':
            with lock:
                original_name = multiprocessing.spawn.get_executable()
            new_name = os.path.abspath(os.path.join(os.path.dirname(original_name), name + '.exe'))
            if os.path.isfile(new_name):
                self.executable = new_name
        super().__init__(name=name, **kwargs)
        return None

    def start(self):
        if self.executable:
            with lock:
                old_name = multiprocessing.spawn.get_executable()
                try:
                    multiprocessing.spawn.set_executable(self.executable)
                    super().start()
                finally:
                    multiprocessing.spawn.set_executable(old_name)
            return None
        super().start()
        return None

    def run(self):
        if setproctitle:
            setproctitle.setproctitle(self.title)
        super().run()
        return None

class NamedProcess(multiprocessing.Process):

    def __init__(self, name, description, **kwargs):
        self.title = f'{name} {description}'
        self.executable = None
        if sys.platform == 'win32':
            with lock:
                original_name = multiprocessing.spawn.get_executable()
            new_name = os.path.abspath(os.path.join(os.path.dirname(original_name), name + '.exe'))
            if os.path.isfile(new_name):
                self.executable = new_name
        super().__init__(name=name, **kwargs)
        return None

    def run(self):
        if setproctitle:
            setproctitle.setproctitle(self.title)
        super().run()
        return None
