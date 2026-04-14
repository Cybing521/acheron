# Source Generated with Decompyle++
# File: download.pyc (Python 3.11)

import logging
import threading
import urllib.parse as urllib
from typing import Any, BinaryIO, Optional, Union
from PySide6 import QtCore
import requests
from packaging.version import InvalidVersion, parse, Version
Logger = Union[(logging.Logger, logging.LoggerAdapter)]

def ref_sort_key(value = None):
    
    try:
        return (True, parse(value))
    except InvalidVersion:
        return 



class _Fetcher(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class FirmwareFinder(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class SoftwareFinder(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class RefFinder(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete


class Downloader(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

