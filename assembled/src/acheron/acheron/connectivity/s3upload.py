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
from ..device_process.writer import UPLOAD_EXTENSION
if sys.platform == 'win32':
    import msvcrt
else:
    import fcntl
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def mark_file_for_upload(apd_filename):
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

    def __init__(self, lockfilename):
        self.lockfilename = lockfilename

    def __enter__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + open
        #   14 LOAD_FAST self
        #   16 LOAD_ATTR lockfilename
        #   26 LOAD_CONST 'r+'
        #   28 LOAD_CONST 'ascii'
        #   30 KW_NAMES
        #   32 PRECALL
        #   36 CALL
        #   46 LOAD_FAST self
        #   48 STORE_ATTR lockfile
        #   58 LOAD_GLOBAL sys
        #   70 LOAD_ATTR platform
        #   80 LOAD_CONST 'win32'
        #   82 COMPARE_OP ==
        #   88 POP_JUMP_FORWARD_IF_FALSE to 204
        #   90 LOAD_GLOBAL NULL + msvcrt
        #  102 LOAD_ATTR locking
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR lockfile
        #  124 LOAD_METHOD fileno
        #  146 PRECALL
        #  150 CALL
        #  160 LOAD_GLOBAL msvcrt
        #  172 LOAD_ATTR LK_NBLCK
        #  182 LOAD_CONST 1
        #  184 PRECALL
        #  188 CALL
        #  198 POP_TOP
        #  200 LOAD_CONST None
        #  202 RETURN_VALUE
        #  204 LOAD_GLOBAL NULL + fcntl
        #  216 LOAD_ATTR lockf
        #  226 LOAD_FAST self
        #  228 LOAD_ATTR lockfile
        #  238 LOAD_GLOBAL fcntl
        #  250 LOAD_ATTR LOCK_EX
        #  260 LOAD_GLOBAL fcntl
        #  272 LOAD_ATTR LOCK_NB
        #  282 BINARY_OP |
        #  286 PRECALL
        #  290 CALL
        #  300 POP_TOP
        #  302 LOAD_CONST None
        #  304 RETURN_VALUE
        pass

    def __exit__(self, _exc_type, _exc_value, _traceback):
        if sys.platform == 'win32':
            msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            fcntl.lockf(self.lockfile, fcntl.LOCK_UN)
        self.lockfile.close()
        del self.lockfile

class S3UploadManager(QtCore.QObject):

    upload_status = QtCore.Signal(str, object, object)

    rate_status = QtCore.Signal(bool, float)

    error = QtCore.Signal()

    def __init__(self, base_dir, s3_bucket, key_prefix, access_key_id, secret_access_key, aws_region, delete_after_upload, archive_interval):
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
        #   68 LOAD_FAST base_dir
        #   70 LOAD_FAST self
        #   72 STORE_ATTR base_dir
        #   82 LOAD_FAST s3_bucket
        #   84 LOAD_FAST self
        #   86 STORE_ATTR s3_bucket
        #   96 LOAD_FAST access_key_id
        #   98 LOAD_FAST self
        #  100 STORE_ATTR access_key_id
        #  110 LOAD_FAST secret_access_key
        #  112 LOAD_FAST self
        #  114 STORE_ATTR secret_access_key
        #  124 LOAD_FAST delete_after_upload
        #  126 LOAD_FAST self
        #  128 STORE_ATTR delete_after_upload
        #  138 LOAD_CONST 0.5
        #  140 LOAD_FAST self
        #  142 STORE_ATTR rate_update_interval
        #  152 LOAD_CONST 5.0
        #  154 LOAD_FAST self
        #  156 STORE_ATTR rate_average_period
        #  166 LOAD_CONST True
        #  168 LOAD_FAST self
        #  170 STORE_ATTR rate_enabled
        #  180 LOAD_FAST key_prefix
        #  182 LOAD_METHOD strip
        #  204 LOAD_CONST '\\/'
        #  206 PRECALL
        #  210 CALL
        #  220 LOAD_FAST self
        #  222 STORE_ATTR key_prefix
        #  232 LOAD_GLOBAL NULL + boto3
        #  244 LOAD_ATTR client
        #  254 LOAD_CONST 's3'
        #  256 LOAD_FAST access_key_id
        #  258 LOAD_FAST secret_access_key
        #  260 LOAD_FAST aws_region
        #  262 KW_NAMES
        #  264 PRECALL
        #  268 CALL
        #  278 LOAD_FAST self
        #  280 STORE_ATTR s3_client
        #  290 LOAD_CONST 300
        #  292 LOAD_FAST self
        #  294 STORE_ATTR scan_interval
        #  304 LOAD_GLOBAL NULL + min
        #  316 LOAD_CONST 2
        #  318 LOAD_FAST archive_interval
        #  320 LOAD_METHOD total_seconds
        #  342 PRECALL
        #  346 CALL
        #  356 BINARY_OP *
        #  360 LOAD_CONST 1200
        #  362 PRECALL
        #  366 CALL
        #  376 LOAD_FAST self
        #  378 STORE_ATTR scan_ignore_newer
        #  388 LOAD_GLOBAL NULL + threading
        #  400 LOAD_ATTR Event
        #  410 PRECALL
        #  414 CALL
        #  424 LOAD_FAST self
        #  426 STORE_ATTR is_finished
        #  436 LOAD_GLOBAL NULL + threading
        #  448 LOAD_ATTR Lock
        #  458 PRECALL
        #  462 CALL
        #  472 LOAD_FAST self
        #  474 STORE_ATTR upload_lock
        #  484 LOAD_GLOBAL NULL + deque
        #  496 PRECALL
        # ... bytecode truncated ...
        pass

    def _scan_dir(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + time
        #   14 LOAD_ATTR time
        #   24 PRECALL
        #   28 CALL
        #   38 STORE_FAST now
        #   40 BUILD_LIST
        #   42 STORE_FAST found
        #   44 LOAD_GLOBAL NULL + os
        #   56 LOAD_ATTR walk
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR base_dir
        #   78 PRECALL
        #   82 CALL
        #   92 GET_ITER
        #   94 EXTENDED_ARG
        #   96 FOR_ITER to 876
        #   98 UNPACK_SEQUENCE
        #  102 STORE_FAST root
        #  104 STORE_FAST _dirs
        #  106 STORE_FAST files
        #  108 LOAD_FAST files
        #  110 GET_ITER
        #  112 EXTENDED_ARG
        #  114 FOR_ITER to 872
        #  116 STORE_FAST name
        #  118 LOAD_FAST name
        #  120 LOAD_METHOD endswith
        #  142 LOAD_GLOBAL UPLOAD_EXTENSION
        #  154 PRECALL
        #  158 CALL
        #  168 EXTENDED_ARG
        #  170 POP_JUMP_FORWARD_IF_FALSE to 868
        #  172 LOAD_GLOBAL os
        #  184 LOAD_ATTR path
        #  194 LOAD_METHOD join
        #  216 LOAD_FAST root
        #  218 LOAD_FAST name
        #  220 PRECALL
        #  224 CALL
        #  234 STORE_FAST uploadfilename
        #  236 LOAD_FAST name
        #  238 LOAD_METHOD startswith
        #  260 LOAD_CONST '.'
        #  262 PRECALL
        #  266 CALL
        #  276 POP_JUMP_FORWARD_IF_FALSE to 298
        #  278 LOAD_FAST name
        #  280 LOAD_CONST 1
        #  282 LOAD_CONST None
        #  284 BUILD_SLICE
        #  286 BINARY_SUBSCR
        #  296 STORE_FAST name
        #  298 LOAD_GLOBAL os
        #  310 LOAD_ATTR path
        #  320 LOAD_METHOD join
        #  342 LOAD_FAST root
        #  344 LOAD_FAST name
        #  346 LOAD_CONST None
        #  348 LOAD_GLOBAL NULL + len
        #  360 LOAD_GLOBAL UPLOAD_EXTENSION
        #  372 PRECALL
        #  376 CALL
        #  386 UNARY_NEGATIVE
        #  388 BUILD_SLICE
        #  390 BINARY_SUBSCR
        #  400 PRECALL
        #  404 CALL
        #  414 STORE_FAST filename
        #  416 LOAD_FAST filename
        #  418 LOAD_FAST self
        #  420 LOAD_ATTR upload_order
        #  430 CONTAINS_OP
        #  432 POP_JUMP_FORWARD_IF_FALSE to 868
        #  434 NOP
        #  436 LOAD_GLOBAL os
        #  448 LOAD_ATTR path
        #  458 LOAD_METHOD getmtime
        #  480 LOAD_FAST filename
        #  482 PRECALL
        # ... bytecode truncated ...
        pass

    def _scan_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 NOP
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR is_finished
        #   18 LOAD_METHOD wait
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR scan_interval
        #   52 PRECALL
        #   56 CALL
        #   66 POP_JUMP_FORWARD_IF_FALSE to 72
        #   68 LOAD_CONST None
        #   70 RETURN_VALUE
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR upload_lock
        #   84 BEFORE_WITH
        #   86 POP_TOP
        #   88 LOAD_FAST self
        #   90 LOAD_METHOD _scan_dir
        #  112 PRECALL
        #  116 CALL
        #  126 POP_TOP
        #  128 LOAD_CONST None
        #  130 LOAD_CONST None
        #  132 LOAD_CONST None
        #  134 PRECALL
        #  138 CALL
        #  148 POP_TOP
        #  150 JUMP_FORWARD to 174
        #  152 PUSH_EXC_INFO
        #  154 WITH_EXCEPT_START
        #  156 POP_JUMP_FORWARD_IF_TRUE to 166
        #  158 RERAISE
        #  160 COPY
        #  162 POP_EXCEPT
        #  164 RERAISE
        #  166 POP_TOP
        #  168 POP_EXCEPT
        #  170 POP_TOP
        #  172 POP_TOP
        #  174 JUMP_BACKWARD to 6
        #  176 PUSH_EXC_INFO
        #  178 LOAD_GLOBAL Exception
        #  190 CHECK_EXC_MATCH
        #  192 POP_JUMP_FORWARD_IF_FALSE to 344
        #  194 POP_TOP
        #  196 LOAD_GLOBAL logger
        #  208 LOAD_METHOD exception
        #  230 LOAD_CONST 'Uncaught exception in scan_loop'
        #  232 PRECALL
        #  236 CALL
        #  246 POP_TOP
        #  248 LOAD_FAST self
        #  250 LOAD_METHOD stop
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_FAST self
        #  290 LOAD_ATTR error
        #  300 LOAD_METHOD emit
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 POP_EXCEPT
        #  340 LOAD_CONST None
        #  342 RETURN_VALUE
        #  344 RERAISE
        #  346 COPY
        #  348 POP_EXCEPT
        #  350 RERAISE
        pass

    def _upload_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_CONST False
        #    6 STORE_FAST emitted_error
        #    8 NOP
        #   10 LOAD_FAST self
        #   12 LOAD_ATTR is_finished
        #   22 LOAD_METHOD is_set
        #   44 PRECALL
        #   48 CALL
        #   58 POP_JUMP_FORWARD_IF_FALSE to 64
        #   60 LOAD_CONST None
        #   62 RETURN_VALUE
        #   64 NOP
        #   66 LOAD_FAST self
        #   68 LOAD_ATTR s3_client
        #   78 LOAD_METHOD head_bucket
        #  100 LOAD_FAST self
        #  102 LOAD_ATTR s3_bucket
        #  112 KW_NAMES
        #  114 PRECALL
        #  118 CALL
        #  128 POP_TOP
        #  130 JUMP_FORWARD to 332
        #  132 PUSH_EXC_INFO
        #  134 LOAD_GLOBAL Exception
        #  146 CHECK_EXC_MATCH
        #  148 POP_JUMP_FORWARD_IF_FALSE to 324
        #  150 POP_TOP
        #  152 LOAD_FAST emitted_error
        #  154 POP_JUMP_FORWARD_IF_TRUE to 262
        #  156 LOAD_CONST True
        #  158 STORE_FAST emitted_error
        #  160 LOAD_GLOBAL logger
        #  172 LOAD_METHOD exception
        #  194 LOAD_CONST 'Error connecting to S3 bucket'
        #  196 PRECALL
        #  200 CALL
        #  210 POP_TOP
        #  212 LOAD_FAST self
        #  214 LOAD_ATTR error
        #  224 LOAD_METHOD emit
        #  246 PRECALL
        #  250 CALL
        #  260 POP_TOP
        #  262 LOAD_FAST self
        #  264 LOAD_ATTR is_finished
        #  274 LOAD_METHOD wait
        #  296 LOAD_CONST 20.0
        #  298 PRECALL
        #  302 CALL
        #  312 POP_JUMP_FORWARD_IF_FALSE to 320
        #  314 POP_EXCEPT
        #  316 LOAD_CONST None
        #  318 RETURN_VALUE
        #  320 POP_EXCEPT
        #  322 JUMP_BACKWARD to 8
        #  324 RERAISE
        #  326 COPY
        #  328 POP_EXCEPT
        #  330 RERAISE
        #  332 NOP
        #  334 NOP
        #  336 LOAD_FAST self
        #  338 LOAD_ATTR upload_lock
        #  348 BEFORE_WITH
        #  350 POP_TOP
        #  352 LOAD_FAST self
        #  354 LOAD_ATTR upload_order
        #  364 LOAD_METHOD popleft
        #  386 PRECALL
        #  390 CALL
        #  400 STORE_FAST filename
        #  402 LOAD_FAST self
        #  404 LOAD_METHOD _do_upload
        #  426 LOAD_FAST filename
        #  428 PRECALL
        #  432 CALL
        #  442 POP_TOP
        #  444 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def _get_rate(self):
        rate_average_period = self.rate_average_period
        now = datetime.datetime.now(tz = datetime.timezone.utc)
        bytes_too_old = 0
        cutoff_time = now - datetime.timedelta(seconds = rate_average_period)
        if len(self.rate_deque):
            (sent_dt, sent_bytes) = self.rate_deque[0]
            if sent_dt < cutoff_time:
                bytes_too_old += sent_bytes
                self.rate_deque.popleft()

    def _rate_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 NOP
        #    6 LOAD_FAST self
        #    8 LOAD_ATTR is_finished
        #   18 LOAD_METHOD wait
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR rate_update_interval
        #   52 PRECALL
        #   56 CALL
        #   66 POP_JUMP_FORWARD_IF_FALSE to 72
        #   68 LOAD_CONST None
        #   70 RETURN_VALUE
        #   72 LOAD_FAST self
        #   74 LOAD_ATTR uploading
        #   84 POP_JUMP_FORWARD_IF_FALSE to 176
        #   86 LOAD_FAST self
        #   88 LOAD_ATTR rate_status
        #   98 LOAD_METHOD emit
        #  120 LOAD_CONST True
        #  122 LOAD_FAST self
        #  124 LOAD_METHOD _get_rate
        #  146 PRECALL
        #  150 CALL
        #  160 PRECALL
        #  164 CALL
        #  174 POP_TOP
        #  176 JUMP_BACKWARD to 6
        #  178 PUSH_EXC_INFO
        #  180 LOAD_GLOBAL Exception
        #  192 CHECK_EXC_MATCH
        #  194 POP_JUMP_FORWARD_IF_FALSE to 346
        #  196 POP_TOP
        #  198 LOAD_GLOBAL logger
        #  210 LOAD_METHOD exception
        #  232 LOAD_CONST 'Uncaught exception in rate_loop'
        #  234 PRECALL
        #  238 CALL
        #  248 POP_TOP
        #  250 LOAD_FAST self
        #  252 LOAD_METHOD stop
        #  274 PRECALL
        #  278 CALL
        #  288 POP_TOP
        #  290 LOAD_FAST self
        #  292 LOAD_ATTR error
        #  302 LOAD_METHOD emit
        #  324 PRECALL
        #  328 CALL
        #  338 POP_TOP
        #  340 POP_EXCEPT
        #  342 LOAD_CONST None
        #  344 RETURN_VALUE
        #  346 RERAISE
        #  348 COPY
        #  350 POP_EXCEPT
        #  352 RERAISE
        pass

    def _get_file_md5(self, file):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL file
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + hashlib
        #   16 LOAD_ATTR md5
        #   26 PRECALL
        #   30 CALL
        #   40 STORE_FAST md5
        #   42 LOAD_GLOBAL NULL + iter
        #   54 LOAD_CLOSURE file
        #   56 BUILD_TUPLE
        #   58 LOAD_CONST <code object <lambda> at 0x105abfa50, file "acheron\connectivity\s3upload.py", line 275>
        #   60 MAKE_FUNCTION closure
        #   62 LOAD_CONST b''
        #   64 PRECALL
        #   68 CALL
        #   78 GET_ITER
        #   80 FOR_ITER to 128
        #   82 STORE_FAST chunk
        #   84 LOAD_FAST md5
        #   86 LOAD_METHOD update
        #  108 LOAD_FAST chunk
        #  110 PRECALL
        #  114 CALL
        #  124 POP_TOP
        #  126 JUMP_BACKWARD to 80
        #  128 LOAD_DEREF file
        #  130 LOAD_METHOD seek
        #  152 LOAD_CONST 0
        #  154 LOAD_CONST 0
        #  156 PRECALL
        #  160 CALL
        #  170 POP_TOP
        #  172 LOAD_FAST md5
        #  174 LOAD_METHOD hexdigest
        #  196 PRECALL
        #  200 CALL
        #  210 RETURN_VALUE
        pass

    def _do_upload_s3(self, file, filelen):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 MAKE_CELL self
        #    2 MAKE_CELL filelen
        #    4 MAKE_CELL basename
        #    6 MAKE_CELL total_sent_bytes
        #    8 RESUME
        #   10 LOAD_GLOBAL os
        #   22 LOAD_ATTR path
        #   32 LOAD_METHOD relpath
        #   54 LOAD_FAST file
        #   56 LOAD_ATTR name
        #   66 LOAD_DEREF self
        #   68 LOAD_ATTR base_dir
        #   78 KW_NAMES
        #   80 PRECALL
        #   84 CALL
        #   94 STORE_FAST relpath
        #   96 LOAD_GLOBAL os
        #  108 LOAD_ATTR path
        #  118 LOAD_METHOD join
        #  140 LOAD_DEREF self
        #  142 LOAD_ATTR key_prefix
        #  152 LOAD_FAST relpath
        #  154 PRECALL
        #  158 CALL
        #  168 STORE_FAST relpath
        #  170 LOAD_FAST relpath
        #  172 LOAD_METHOD replace
        #  194 LOAD_CONST '\\'
        #  196 LOAD_CONST '/'
        #  198 PRECALL
        #  202 CALL
        #  212 STORE_FAST keyname
        #  214 LOAD_GLOBAL os
        #  226 LOAD_ATTR path
        #  236 LOAD_METHOD basename
        #  258 LOAD_FAST file
        #  260 LOAD_ATTR name
        #  270 PRECALL
        #  274 CALL
        #  284 STORE_DEREF basename
        #  286 LOAD_CONST 1
        #  288 STORE_FAST next_index
        #  290 LOAD_GLOBAL os
        #  302 LOAD_ATTR path
        #  312 LOAD_METHOD splitext
        #  334 LOAD_FAST keyname
        #  336 PRECALL
        #  340 CALL
        #  350 UNPACK_SEQUENCE
        #  354 STORE_FAST prefix
        #  356 STORE_FAST prefix_ext
        #  358 LOAD_FAST prefix
        #  360 LOAD_METHOD endswith
        #  382 LOAD_CONST ')'
        #  384 PRECALL
        #  388 CALL
        #  398 POP_JUMP_FORWARD_IF_FALSE to 562
        #  400 LOAD_GLOBAL NULL + re
        #  412 LOAD_ATTR match
        #  422 LOAD_CONST '^(.*)\\(([0-9]*?)\\)$'
        #  424 LOAD_FAST prefix
        #  426 PRECALL
        #  430 CALL
        #  440 STORE_FAST m
        #  442 LOAD_FAST m
        #  444 POP_JUMP_FORWARD_IF_FALSE to 562
        #  446 LOAD_FAST m
        #  448 LOAD_METHOD group
        #  470 LOAD_CONST 1
        #  472 PRECALL
        #  476 CALL
        #  486 STORE_FAST prefix
        #  488 LOAD_GLOBAL NULL + int
        #  500 LOAD_FAST m
        #  502 LOAD_METHOD group
        #  524 LOAD_CONST 2
        #  526 PRECALL
        #  530 CALL
        #  540 PRECALL
        #  544 CALL
        # ... bytecode truncated ...
        pass

    def _do_upload(self, filename):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL os
        #   16 LOAD_ATTR path
        #   26 LOAD_METHOD split
        #   48 LOAD_FAST filename
        #   50 PRECALL
        #   54 CALL
        #   64 UNPACK_SEQUENCE
        #   68 STORE_FAST path
        #   70 STORE_FAST name
        #   72 LOAD_GLOBAL os
        #   84 LOAD_ATTR path
        #   94 LOAD_METHOD join
        #  116 LOAD_FAST path
        #  118 LOAD_CONST '.'
        #  120 LOAD_FAST name
        #  122 BINARY_OP +
        #  126 LOAD_GLOBAL UPLOAD_EXTENSION
        #  138 BINARY_OP +
        #  142 PRECALL
        #  146 CALL
        #  156 STORE_FAST lockfilename
        #  158 LOAD_GLOBAL NULL + LockFile
        #  170 LOAD_FAST lockfilename
        #  172 PRECALL
        #  176 CALL
        #  186 BEFORE_WITH
        #  188 POP_TOP
        #  190 LOAD_GLOBAL NULL + open
        #  202 LOAD_FAST filename
        #  204 LOAD_CONST 'rb'
        #  206 PRECALL
        #  210 CALL
        #  220 BEFORE_WITH
        #  222 STORE_FAST file
        #  224 LOAD_FAST file
        #  226 LOAD_METHOD seek
        #  248 LOAD_CONST 0
        #  250 LOAD_GLOBAL os
        #  262 LOAD_ATTR SEEK_END
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 LOAD_FAST file
        #  290 LOAD_METHOD tell
        #  312 PRECALL
        #  316 CALL
        #  326 STORE_FAST filelen
        #  328 LOAD_FAST file
        #  330 LOAD_METHOD seek
        #  352 LOAD_CONST 0
        #  354 LOAD_GLOBAL os
        #  366 LOAD_ATTR SEEK_SET
        #  376 PRECALL
        #  380 CALL
        #  390 POP_TOP
        #  392 NOP
        #  394 LOAD_FAST self
        #  396 LOAD_METHOD _do_upload_s3
        #  418 LOAD_FAST file
        #  420 LOAD_FAST filelen
        #  422 PRECALL
        #  426 CALL
        #  436 POP_TOP
        #  438 JUMP_FORWARD to 572
        #  440 PUSH_EXC_INFO
        #  442 LOAD_GLOBAL Exception
        #  454 CHECK_EXC_MATCH
        #  456 POP_JUMP_FORWARD_IF_FALSE to 564
        #  458 POP_TOP
        #  460 LOAD_GLOBAL logger
        #  472 LOAD_METHOD exception
        #  494 LOAD_CONST 'Error uploading: %s'
        #  496 LOAD_FAST filename
        #  498 PRECALL
        #  502 CALL
        #  512 POP_TOP
        #  514 POP_EXCEPT
        #  516 LOAD_CONST None
        # ... bytecode truncated ...
        pass

    def upload(self, filename):
        if filename not in self.upload_order:
            logger.debug('File ready for upload: %s', filename)
            self.upload_order.append(filename)
            return None

    def stop(self):
        self.is_finished.set()

    def join(self):
        self.upload_thread.join()
        self.scan_thread.join()

    def rescan(self):
        self._scan_dir()
