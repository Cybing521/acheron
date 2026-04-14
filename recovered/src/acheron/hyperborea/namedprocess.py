# Source Generated with Decompyle++
# File: namedprocess.pyc (Python 3.11)

import logging
import multiprocessing.spawn as multiprocessing
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
if sys.platform == 'win32':
    
    class NamedProcess(multiprocessing.Process):
        pass
    # WARNING: Decompyle incomplete

    return None

class NamedProcess(multiprocessing.Process):
    pass
# WARNING: Decompyle incomplete

