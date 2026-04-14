# Source Generated with Decompyle++
# File: s3upload.pyc (Python 3.11)

from collections import deque
import ctypes
import datetime
import hashlib
import logging
import os
import re
import sys
import time
import threading
from types import TracebackType
from typing import BinaryIO, Optional
import boto3
from PySide6 import QtCore
from device_process.writer import UPLOAD_EXTENSION
if sys.platform == 'win32':
    import msvcrt
else:
    import fcntl
logger = logging.getLogger(__name__)

def mark_file_for_upload(apd_filename = None):
    (root, name) = os.path.split(apd_filename)
    upload_filename = os.path.join(root, '.' + name + UPLOAD_EXTENSION)
    if not os.path.exists(upload_filename):
        upload_file = open(upload_filename, 'w', encoding = 'ascii')
        upload_file.close()
        if sys.platform == 'win32':
            ctypes.windll.kernel32.SetFileAttributesW(upload_filename, 2)
            return None
        return None


class LockFile:
    
    def __init__(self = None, lockfilename = None):
        self.lockfilename = lockfilename

    
    def __enter__(self = None):
        self.lockfile = open(self.lockfilename, 'r+', encoding = 'ascii')
        if sys.platform == 'win32':
            msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_NBLCK, 1)
            return None
        None.lockf(self.lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)

    
    def __exit__(self = None, _exc_type = None, _exc_value = None, _traceback = ('_exc_type', Optional[type[BaseException]], '_exc_value', Optional[BaseException], '_traceback', Optional[TracebackType], 'return', None)):
        if sys.platform == 'win32':
            msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            fcntl.lockf(self.lockfile, fcntl.LOCK_UN)
        self.lockfile.close()
        del self.lockfile



class S3UploadManager(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

