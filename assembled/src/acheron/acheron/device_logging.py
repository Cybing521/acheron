# Source Generated with Decompyle++
# File: device_logging.pyc (Python 3.11)

import logging
from typing import Optional

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class OptionalDeviceStringFilter(logging.Filter):

    def __init__(self, fmt, fallback):
        self.fmt = fmt
        self.fallback = fallback

    def filter(self, record):
        try:
            record.optdevice = self.fmt % record.proxy_string
        except AttributeError:
            record.optdevice = self.fallback

        return True

class DeviceLoggerAdapter(logging.LoggerAdapter):

    def __init__(self, logger, serial_number, proxy_string):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST proxy_string
        #    6 POP_JUMP_FORWARD_IF_TRUE to 12
        #    8 LOAD_FAST serial_number
        #   10 STORE_FAST proxy_string
        #   12 LOAD_GLOBAL NULL + super
        #   24 PRECALL
        #   28 CALL
        #   38 LOAD_METHOD __init__
        #   60 LOAD_FAST logger
        #   62 LOAD_FAST serial_number
        #   64 LOAD_FAST proxy_string
        #   66 LOAD_CONST ('serial_number', 'proxy_string')
        #   68 BUILD_CONST_KEY_MAP
        #   70 PRECALL
        #   74 CALL
        #   84 POP_TOP
        #   86 LOAD_CONST None
        #   88 RETURN_VALUE
        pass

class RemoteToLocalLogHandler(logging.Handler):

    def __init__(self, logger_name):
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
        #   68 LOAD_GLOBAL NULL + logging
        #   80 LOAD_ATTR getLogger
        #   90 LOAD_FAST logger_name
        #   92 PRECALL
        #   96 CALL
        #  106 LOAD_FAST self
        #  108 STORE_ATTR logger
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass

    def emit(self, record):
        self.logger.handle(record)
