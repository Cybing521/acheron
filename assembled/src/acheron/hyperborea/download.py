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

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def ref_sort_key(value):
    try:
        return (True, parse(value))
    except InvalidVersion:
        return 

class _Fetcher(QtCore.QObject):

    completed = QtCore.Signal(object, object)

    error = QtCore.Signal(str)

    def __init__(self, logger, extra=None):
        super().__init__()
        self.logger = logger
        self.extra = extra

    def start(self, url, log_type):
        self.request_thread = threading.Thread(target = self.request_thread_run, args = (url, log_type))
        self.request_thread.start()

    def request_thread_run(self, url, log_type):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST self
        #    6 LOAD_ATTR logger
        #   16 LOAD_METHOD debug
        #   38 LOAD_CONST 'Requesting %s from url %s'
        #   40 LOAD_FAST log_type
        #   42 LOAD_FAST url
        #   44 PRECALL
        #   48 CALL
        #   58 POP_TOP
        #   60 LOAD_GLOBAL NULL + requests
        #   72 LOAD_ATTR get
        #   82 LOAD_FAST url
        #   84 PRECALL
        #   88 CALL
        #   98 STORE_FAST response
        #  100 LOAD_FAST response
        #  102 LOAD_ATTR ok
        #  112 POP_JUMP_FORWARD_IF_TRUE to 244
        #  114 LOAD_FAST self
        #  116 LOAD_ATTR logger
        #  126 LOAD_METHOD error
        #  148 LOAD_CONST 'Error requesting %s: %s'
        #  150 LOAD_FAST log_type
        #  152 LOAD_FAST response
        #  154 LOAD_ATTR text
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_FAST self
        #  182 LOAD_ATTR error
        #  192 LOAD_METHOD emit
        #  214 LOAD_CONST 'Error requesting '
        #  216 LOAD_FAST log_type
        #  218 FORMAT_VALUE
        #  220 LOAD_CONST '!'
        #  222 BUILD_STRING
        #  224 PRECALL
        #  228 CALL
        #  238 POP_TOP
        #  240 LOAD_CONST None
        #  242 RETURN_VALUE
        #  244 LOAD_FAST response
        #  246 LOAD_METHOD json
        #  268 PRECALL
        #  272 CALL
        #  282 STORE_FAST data
        #  284 LOAD_FAST data
        #  286 POP_JUMP_FORWARD_IF_TRUE to 406
        #  288 LOAD_FAST self
        #  290 LOAD_ATTR logger
        #  300 LOAD_METHOD error
        #  322 LOAD_CONST 'Empty response for %s request!'
        #  324 LOAD_FAST log_type
        #  326 PRECALL
        #  330 CALL
        #  340 POP_TOP
        #  342 LOAD_FAST self
        #  344 LOAD_ATTR error
        #  354 LOAD_METHOD emit
        #  376 LOAD_CONST 'Error requesting '
        #  378 LOAD_FAST log_type
        #  380 FORMAT_VALUE
        #  382 LOAD_CONST '!'
        #  384 BUILD_STRING
        #  386 PRECALL
        #  390 CALL
        #  400 POP_TOP
        #  402 LOAD_CONST None
        #  404 RETURN_VALUE
        #  406 LOAD_FAST self
        #  408 LOAD_ATTR completed
        #  418 LOAD_METHOD emit
        #  440 LOAD_FAST data
        #  442 LOAD_FAST self
        #  444 LOAD_ATTR extra
        #  454 PRECALL
        #  458 CALL
        #  468 POP_TOP
        # ... bytecode truncated ...
        pass

class FirmwareFinder(QtCore.QObject):

    completed = QtCore.Signal(object)

    error = QtCore.Signal(str)

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def find_firmware(self, build_type, board_info, repo, branch, commit):
        keys = []
        if board_info:
            if repo:
                raise ValueError('Cannot specify both board_info and repo')
            (board_name, board_rev) = board_info
            keys.append('boardname={}'.format(urllib.parse.quote(board_name)))
            keys.append('boardrev={}'.format(board_rev))
        elif repo:
            keys.append('repo={}'.format(urllib.parse.quote(repo)))
        else:
            raise ValueError('Must specify one of board_info or repo')
        if commit and branch:
            raise ValueError('Cannot specify both commit and branch')

    def got_data(self, build_urls, build_type):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_FAST build_type
        #    6 POP_JUMP_FORWARD_IF_NONE to 36
        #    8 LOAD_FAST build_type
        #   10 LOAD_FAST build_urls
        #   12 CONTAINS_OP
        #   14 POP_JUMP_FORWARD_IF_FALSE to 36
        #   16 LOAD_FAST build_type
        #   18 LOAD_FAST build_urls
        #   20 LOAD_FAST build_type
        #   22 BINARY_SUBSCR
        #   32 BUILD_MAP
        #   34 STORE_FAST build_urls
        #   36 LOAD_FAST self
        #   38 LOAD_ATTR completed
        #   48 LOAD_METHOD emit
        #   70 LOAD_FAST build_urls
        #   72 PRECALL
        #   76 CALL
        #   86 POP_TOP
        #   88 LOAD_CONST None
        #   90 RETURN_VALUE
        #   92 PUSH_EXC_INFO
        #   94 LOAD_GLOBAL Exception
        #  106 CHECK_EXC_MATCH
        #  108 POP_JUMP_FORWARD_IF_FALSE to 222
        #  110 POP_TOP
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR logger
        #  124 LOAD_METHOD exception
        #  146 LOAD_CONST 'Error finding firmware'
        #  148 PRECALL
        #  152 CALL
        #  162 POP_TOP
        #  164 LOAD_FAST self
        #  166 LOAD_ATTR error
        #  176 LOAD_METHOD emit
        #  198 LOAD_CONST 'Unknown error finding firmware!'
        #  200 PRECALL
        #  204 CALL
        #  214 POP_TOP
        #  216 POP_EXCEPT
        #  218 LOAD_CONST None
        #  220 RETURN_VALUE
        #  222 RERAISE
        #  224 COPY
        #  226 POP_EXCEPT
        #  228 RERAISE
        pass

class SoftwareFinder(QtCore.QObject):

    completed = QtCore.Signal(object)

    error = QtCore.Signal(str)

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def find_software(self, repo, build_key, branch, commit):
        base_url = 'https://api.suprocktech.com/software/findsoftware'
        keys = [
            'repo={}'.format(repo),
            'key={}'.format(build_key)]
        if commit:
            keys.append('hash={}'.format(commit))
        if branch:
            keys.append('branch={}'.format(branch))
        url = base_url + '?' + '&'.join(keys)
        self.fetcher = _Fetcher(self.logger)
        self.fetcher.error.connect(self.error)
        self.fetcher.completed.connect(self.got_data)
        self.fetcher.start(url, 'findsoftware')

    def got_data(self, values):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_CONST 'url'
        #    6 LOAD_FAST values
        #    8 CONTAINS_OP
        #   10 POP_JUMP_FORWARD_IF_FALSE to 120
        #   12 LOAD_FAST self
        #   14 LOAD_ATTR logger
        #   24 LOAD_METHOD error
        #   46 LOAD_CONST 'Empty response to findsoftware!'
        #   48 PRECALL
        #   52 CALL
        #   62 POP_TOP
        #   64 LOAD_FAST self
        #   66 LOAD_ATTR error
        #   76 LOAD_METHOD emit
        #   98 LOAD_CONST 'Error requesting software information!'
        #  100 PRECALL
        #  104 CALL
        #  114 POP_TOP
        #  116 LOAD_CONST None
        #  118 RETURN_VALUE
        #  120 LOAD_FAST values
        #  122 LOAD_CONST 'url'
        #  124 BINARY_SUBSCR
        #  134 STORE_FAST url
        #  136 LOAD_FAST values
        #  138 LOAD_METHOD get
        #  160 LOAD_CONST 'commit'
        #  162 LOAD_CONST None
        #  164 PRECALL
        #  168 CALL
        #  178 STORE_FAST commit
        #  180 LOAD_FAST values
        #  182 LOAD_METHOD get
        #  204 LOAD_CONST 'state'
        #  206 LOAD_CONST 'SUCCESSFUL'
        #  208 PRECALL
        #  212 CALL
        #  222 STORE_FAST state
        #  224 LOAD_FAST state
        #  226 LOAD_CONST 'SUCCESSFUL'
        #  228 COMPARE_OP ==
        #  234 STORE_FAST ready
        #  236 LOAD_FAST self
        #  238 LOAD_ATTR completed
        #  248 LOAD_METHOD emit
        #  270 LOAD_FAST url
        #  272 LOAD_FAST commit
        #  274 LOAD_FAST ready
        #  276 BUILD_TUPLE
        #  278 PRECALL
        #  282 CALL
        #  292 POP_TOP
        #  294 LOAD_CONST None
        #  296 RETURN_VALUE
        #  298 PUSH_EXC_INFO
        #  300 LOAD_GLOBAL Exception
        #  312 CHECK_EXC_MATCH
        #  314 POP_JUMP_FORWARD_IF_FALSE to 428
        #  316 POP_TOP
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR logger
        #  330 LOAD_METHOD exception
        #  352 LOAD_CONST 'Error finding software'
        #  354 PRECALL
        #  358 CALL
        #  368 POP_TOP
        #  370 LOAD_FAST self
        #  372 LOAD_ATTR error
        #  382 LOAD_METHOD emit
        #  404 LOAD_CONST 'Unknown error finding software!'
        #  406 PRECALL
        #  410 CALL
        #  420 POP_TOP
        #  422 POP_EXCEPT
        #  424 LOAD_CONST None
        #  426 RETURN_VALUE
        #  428 RERAISE
        #  430 COPY
        # ... bytecode truncated ...
        pass

class RefFinder(QtCore.QObject):

    completed = QtCore.Signal(object)

    error = QtCore.Signal(str)

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.fetcher = _Fetcher(self.logger)
        self.fetcher.error.connect(self.error)
        self.fetcher.completed.connect(self.completed)

    def get_software_refs(self, repo):
        base_url = 'https://api.suprocktech.com/software/findsoftware'
        keys = [
            'repo={}'.format(repo),
            'listrefs=1']
        url = base_url + '?' + '&'.join(keys)
        self.fetcher.start(url, 'listrefs')

    def get_firmware_refs(self, board_info, repo):
        keys = [
            'listrefs=1']
        if board_info:
            if repo:
                raise ValueError('Cannot specify both board_info and repo')
            (board_name, board_rev) = board_info
            keys.append('boardname={}'.format(urllib.parse.quote(board_name)))
            keys.append('boardrev={}'.format(board_rev))
        elif repo:
            keys.append('repo={}'.format(urllib.parse.quote(repo)))
        else:
            raise ValueError('Must specify one of board_info or repo')
        base_url = 'https://api.suprocktech.com/firmwareinfo/findfirmware'
        url = base_url + '?' + '&'.join(keys)
        self.fetcher.start(url, 'listrefs')

class Downloader(QtCore.QObject):

    update = QtCore.Signal(int, int)

    completed = QtCore.Signal(str, object)

    error = QtCore.Signal(object, str)

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def start_download(self, url, file):
        self.download_thread = threading.Thread(target = self.download_thread_run, args = (url, file))
        self.download_thread.start()

    def download_thread_run(self, url, file):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL NULL + requests
        #   16 LOAD_ATTR get
        #   26 LOAD_FAST url
        #   28 LOAD_CONST True
        #   30 KW_NAMES
        #   32 PRECALL
        #   36 CALL
        #   46 BEFORE_WITH
        #   48 STORE_FAST r
        #   50 LOAD_FAST r
        #   52 LOAD_METHOD raise_for_status
        #   74 PRECALL
        #   78 CALL
        #   88 POP_TOP
        #   90 LOAD_FAST r
        #   92 LOAD_ATTR headers
        #  102 LOAD_METHOD get
        #  124 LOAD_CONST 'content-length'
        #  126 PRECALL
        #  130 CALL
        #  140 STORE_FAST total_length_str
        #  142 LOAD_CONST 0
        #  144 STORE_FAST written_bytes
        #  146 LOAD_FAST total_length_str
        #  148 POP_JUMP_FORWARD_IF_FALSE to 220
        #  150 NOP
        #  152 LOAD_GLOBAL NULL + int
        #  164 LOAD_FAST total_length_str
        #  166 PRECALL
        #  170 CALL
        #  180 STORE_FAST total_length
        #  182 JUMP_FORWARD to 224
        #  184 PUSH_EXC_INFO
        #  186 LOAD_GLOBAL ValueError
        #  198 CHECK_EXC_MATCH
        #  200 POP_JUMP_FORWARD_IF_FALSE to 212
        #  202 POP_TOP
        #  204 LOAD_CONST 0
        #  206 STORE_FAST total_length
        #  208 POP_EXCEPT
        #  210 JUMP_FORWARD to 224
        #  212 RERAISE
        #  214 COPY
        #  216 POP_EXCEPT
        #  218 RERAISE
        #  220 LOAD_CONST 0
        #  222 STORE_FAST total_length
        #  224 LOAD_FAST r
        #  226 LOAD_METHOD iter_content
        #  248 LOAD_CONST 4096
        #  250 KW_NAMES
        #  252 PRECALL
        #  256 CALL
        #  266 GET_ITER
        #  268 FOR_ITER to 410
        #  270 STORE_FAST chunk
        #  272 LOAD_FAST chunk
        #  274 POP_JUMP_FORWARD_IF_FALSE to 408
        #  276 LOAD_FAST file
        #  278 LOAD_METHOD write
        #  300 LOAD_FAST chunk
        #  302 PRECALL
        #  306 CALL
        #  316 POP_TOP
        #  318 LOAD_FAST written_bytes
        #  320 LOAD_GLOBAL NULL + len
        #  332 LOAD_FAST chunk
        #  334 PRECALL
        #  338 CALL
        #  348 BINARY_OP +=
        #  352 STORE_FAST written_bytes
        #  354 LOAD_FAST self
        #  356 LOAD_ATTR update
        #  366 LOAD_METHOD emit
        #  388 LOAD_FAST written_bytes
        #  390 LOAD_FAST total_length
        #  392 PRECALL
        #  396 CALL
        # ... bytecode truncated ...
        pass
