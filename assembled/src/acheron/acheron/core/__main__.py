# Source Generated with Decompyle++
# File: __main__.pyc (Python 3.11)

import logging
import sys
from PySide6 import QtCore
import asphodel
from ..device_process.proxy import DeviceProxyManager
from acheron import force_exit, main_init, __version__
from acheron.logging import setup_logging
from acheron.core.dispatcher import Dispatcher
from acheron.core.preferences import create_empty_settings, Preferences
from acheron.disk.schedule_reader import ScheduleReader
logger = logging.getLogger(__name__)
MAIN_PROCESS_NAME = 'acheron-cli'
DEVICE_PROCESS_NAME = 'acheron-device'
CALC_PROCESS_NAME = 'acheron-calc'

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def main():
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + main_init
    #   14 LOAD_GLOBAL MAIN_PROCESS_NAME
    #   26 PRECALL
    #   30 CALL
    #   40 POP_TOP
    #   42 LOAD_GLOBAL NULL + QtCore
    #   54 LOAD_ATTR QCoreApplication
    #   64 LOAD_GLOBAL sys
    #   76 LOAD_ATTR argv
    #   86 PRECALL
    #   90 CALL
    #  100 STORE_FAST app
    #  102 LOAD_FAST app
    #  104 LOAD_METHOD setApplicationName
    #  126 LOAD_CONST 'Acheron'
    #  128 PRECALL
    #  132 CALL
    #  142 POP_TOP
    #  144 LOAD_FAST app
    #  146 LOAD_METHOD setOrganizationDomain
    #  168 LOAD_CONST 'suprocktech.com'
    #  170 PRECALL
    #  174 CALL
    #  184 POP_TOP
    #  186 LOAD_FAST app
    #  188 LOAD_METHOD setOrganizationName
    #  210 LOAD_CONST 'Suprock Tech'
    #  212 PRECALL
    #  216 CALL
    #  226 POP_TOP
    #  228 LOAD_FAST app
    #  230 LOAD_METHOD setApplicationVersion
    #  252 LOAD_GLOBAL __version__
    #  264 PRECALL
    #  268 CALL
    #  278 POP_TOP
    #  280 LOAD_GLOBAL NULL + setup_logging
    #  292 LOAD_CONST True
    #  294 KW_NAMES
    #  296 PRECALL
    #  300 CALL
    #  310 POP_TOP
    #  312 LOAD_GLOBAL NULL + create_empty_settings
    #  324 PRECALL
    #  328 CALL
    #  338 POP_TOP
    #  340 LOAD_GLOBAL NULL + QtCore
    #  352 LOAD_ATTR QTimer
    #  362 PRECALL
    #  366 CALL
    #  376 STORE_FAST timer
    #  378 LOAD_FAST timer
    #  380 LOAD_METHOD start
    #  402 LOAD_CONST 500
    #  404 PRECALL
    #  408 CALL
    #  418 POP_TOP
    #  420 LOAD_FAST timer
    #  422 LOAD_ATTR timeout
    #  432 LOAD_METHOD connect
    #  454 LOAD_CONST <code object <lambda> at 0x105a528b0, file "acheron\core\__main__.py", line 41>
    #  456 MAKE_FUNCTION
    #  458 PRECALL
    #  462 CALL
    #  472 POP_TOP
    #  474 LOAD_GLOBAL logger
    #  486 LOAD_METHOD info
    #  508 LOAD_CONST 'Acheron started (Version {})'
    #  510 LOAD_METHOD format
    #  532 LOAD_GLOBAL __version__
    #  544 PRECALL
    #  548 CALL
    #  558 PRECALL
    #  562 CALL
    #  572 POP_TOP
    #  574 NOP
    #  576 LOAD_GLOBAL asphodel
    #  588 LOAD_ATTR nativelib
    #  598 LOAD_ATTR missing_funcs
    # ... bytecode truncated ...
    pass
