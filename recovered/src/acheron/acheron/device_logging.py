# Source Generated with Decompyle++
# File: device_logging.pyc (Python 3.11)

import logging
from typing import Optional

class OptionalDeviceStringFilter(logging.Filter):
    
    def __init__(self = None, fmt = None, fallback = None):
        self.fmt = fmt
        self.fallback = fallback

    
    def filter(self = None, record = None):
        
        try:
            record.optdevice = self.fmt % record.proxy_string
        except AttributeError:
            record.optdevice = self.fallback

        return True



class DeviceLoggerAdapter(logging.LoggerAdapter):
    pass
# WARNING: Decompyle incomplete


class RemoteToLocalLogHandler(logging.Handler):
    pass
# WARNING: Decompyle incomplete

