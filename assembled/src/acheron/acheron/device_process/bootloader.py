# Source Generated with Decompyle++
# File: bootloader.pyc (Python 3.11)

import binascii
import io
import json
import logging
import lzma
import os
from typing import Any, Callable, Optional
import asphodel
from asphodel.device_info import DeviceInfo
# INVALID FROM DECOMPILER: BootloaderCallback = Callable[([
# INVALID FROM DECOMPILER:     int,
# INVALID FROM DECOMPILER:     int,
# INVALID FROM DECOMPILER:     str], None)]

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def get_default_file(device_info, base_dir):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_FAST base_dir
    #    4 POP_JUMP_FORWARD_IF_TRUE to 196
    #    6 LOAD_GLOBAL os
    #   18 LOAD_ATTR path
    #   28 LOAD_METHOD abspath
    #   50 LOAD_GLOBAL os
    #   62 LOAD_ATTR path
    #   72 LOAD_METHOD join
    #   94 LOAD_GLOBAL os
    #  106 LOAD_ATTR path
    #  116 LOAD_METHOD dirname
    #  138 LOAD_GLOBAL __file__
    #  150 PRECALL
    #  154 CALL
    #  164 LOAD_CONST '../../../'
    #  166 PRECALL
    #  170 CALL
    #  180 PRECALL
    #  184 CALL
    #  194 STORE_FAST base_dir
    #  196 NOP
    #  198 LOAD_CONST 0
    #  200 LOAD_CONST None
    #  202 IMPORT_NAME firmutil.repo_info
    #  204 STORE_FAST firmutil
    #  206 LOAD_FAST device_info
    #  208 LOAD_ATTR board_info
    #  218 UNPACK_SEQUENCE
    #  222 STORE_FAST boardname
    #  224 STORE_FAST boardrev
    #  226 LOAD_FAST firmutil
    #  228 LOAD_ATTR repo_info
    #  238 LOAD_METHOD get_repo_from_board
    #  260 LOAD_FAST boardname
    #  262 LOAD_FAST boardrev
    #  264 PRECALL
    #  268 CALL
    #  278 STORE_FAST repo
    #  280 JUMP_FORWARD to 318
    #  282 PUSH_EXC_INFO
    #  284 LOAD_GLOBAL ImportError
    #  296 CHECK_EXC_MATCH
    #  298 POP_JUMP_FORWARD_IF_FALSE to 310
    #  300 POP_TOP
    #  302 LOAD_CONST None
    #  304 STORE_FAST repo
    #  306 POP_EXCEPT
    #  308 JUMP_FORWARD to 318
    #  310 RERAISE
    #  312 COPY
    #  314 POP_EXCEPT
    #  316 RERAISE
    #  318 LOAD_FAST repo
    #  320 POP_JUMP_FORWARD_IF_TRUE to 336
    #  322 LOAD_FAST device_info
    #  324 LOAD_ATTR repo_name
    #  334 STORE_FAST repo
    #  336 LOAD_FAST repo
    #  338 POP_JUMP_FORWARD_IF_TRUE to 344
    #  340 LOAD_CONST ('', '')
    #  342 RETURN_VALUE
    #  344 LOAD_GLOBAL os
    #  356 LOAD_ATTR path
    #  366 LOAD_METHOD abspath
    #  388 LOAD_GLOBAL os
    #  400 LOAD_ATTR path
    #  410 LOAD_METHOD join
    #  432 LOAD_FAST base_dir
    #  434 LOAD_FAST repo
    #  436 FORMAT_VALUE
    #  438 LOAD_CONST '/firmware/build'
    #  440 BUILD_STRING
    #  442 PRECALL
    #  446 CALL
    #  456 PRECALL
    #  460 CALL
    #  470 STORE_FAST file_dir
    #  472 LOAD_GLOBAL os
    #  484 LOAD_ATTR path
    # ... bytecode truncated ...
    pass

def decode_firm_file(firm_file):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + lzma
    #   14 LOAD_ATTR LZMAFile
    #   24 LOAD_FAST firm_file
    #   26 PRECALL
    #   30 CALL
    #   40 BEFORE_WITH
    #   42 STORE_FAST lzma_file
    #   44 LOAD_GLOBAL NULL + io
    #   56 LOAD_ATTR TextIOWrapper
    #   66 LOAD_FAST lzma_file
    #   68 PRECALL
    #   72 CALL
    #   82 BEFORE_WITH
    #   84 STORE_FAST f
    #   86 LOAD_GLOBAL NULL + json
    #   98 LOAD_ATTR load
    #  108 LOAD_FAST f
    #  110 PRECALL
    #  114 CALL
    #  124 SWAP
    #  126 LOAD_CONST None
    #  128 LOAD_CONST None
    #  130 LOAD_CONST None
    #  132 PRECALL
    #  136 CALL
    #  146 POP_TOP
    #  148 SWAP
    #  150 LOAD_CONST None
    #  152 LOAD_CONST None
    #  154 LOAD_CONST None
    #  156 PRECALL
    #  160 CALL
    #  170 POP_TOP
    #  172 RETURN_VALUE
    #  174 PUSH_EXC_INFO
    #  176 WITH_EXCEPT_START
    #  178 POP_JUMP_FORWARD_IF_TRUE to 188
    #  180 RERAISE
    #  182 COPY
    #  184 POP_EXCEPT
    #  186 RERAISE
    #  188 POP_TOP
    #  190 POP_EXCEPT
    #  192 POP_TOP
    #  194 POP_TOP
    #  196 NOP
    #  198 LOAD_CONST None
    #  200 LOAD_CONST None
    #  202 LOAD_CONST None
    #  204 PRECALL
    #  208 CALL
    #  218 POP_TOP
    #  220 LOAD_CONST None
    #  222 RETURN_VALUE
    #  224 PUSH_EXC_INFO
    #  226 WITH_EXCEPT_START
    #  228 POP_JUMP_FORWARD_IF_TRUE to 238
    #  230 RERAISE
    #  232 COPY
    #  234 POP_EXCEPT
    #  236 RERAISE
    #  238 POP_TOP
    #  240 POP_EXCEPT
    #  242 POP_TOP
    #  244 POP_TOP
    #  246 LOAD_CONST None
    #  248 RETURN_VALUE
    pass

def decode_firm_bytes(firm_bytes):
    json_str = lzma.decompress(firm_bytes).decode()
    return json.loads(json_str)

def already_programmed(firm_data, device_info):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_FAST device_info
    #    4 LOAD_ATTR supports_bootloader
    #   14 POP_JUMP_FORWARD_IF_FALSE to 20
    #   16 LOAD_CONST False
    #   18 RETURN_VALUE
    #   20 LOAD_FAST firm_data
    #   22 LOAD_METHOD get
    #   44 LOAD_CONST 'build_info'
    #   46 PRECALL
    #   50 CALL
    #   60 LOAD_FAST device_info
    #   62 LOAD_ATTR build_info
    #   72 COMPARE_OP !=
    #   78 POP_JUMP_FORWARD_IF_FALSE to 84
    #   80 LOAD_CONST False
    #   82 RETURN_VALUE
    #   84 LOAD_FAST firm_data
    #   86 LOAD_METHOD get
    #  108 LOAD_CONST 'build_date'
    #  110 PRECALL
    #  114 CALL
    #  124 LOAD_FAST device_info
    #  126 LOAD_ATTR build_date
    #  136 COMPARE_OP !=
    #  142 POP_JUMP_FORWARD_IF_FALSE to 148
    #  144 LOAD_CONST False
    #  146 RETURN_VALUE
    #  148 LOAD_FAST firm_data
    #  150 LOAD_METHOD get
    #  172 LOAD_CONST 'application'
    #  174 LOAD_CONST False
    #  176 PRECALL
    #  180 CALL
    #  190 LOAD_CONST True
    #  192 IS_OP
    #  194 POP_JUMP_FORWARD_IF_FALSE to 200
    #  196 LOAD_CONST False
    #  198 RETURN_VALUE
    #  200 LOAD_FAST firm_data
    #  202 LOAD_METHOD get
    #  224 LOAD_CONST 'bootloader'
    #  226 LOAD_CONST False
    #  228 PRECALL
    #  232 CALL
    #  242 LOAD_CONST False
    #  244 IS_OP
    #  246 POP_JUMP_FORWARD_IF_FALSE to 252
    #  248 LOAD_CONST False
    #  250 RETURN_VALUE
    #  252 LOAD_CONST True
    #  254 RETURN_VALUE
    pass

def do_bootload_page(device, done_bytes, page_data, block_sizes, total_bytes, message, callback):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL remaining
    #    2 RESUME
    #    4 LOAD_CONST 0
    #    6 STORE_FAST index
    #    8 LOAD_GLOBAL NULL + len
    #   20 LOAD_FAST page_data
    #   22 PRECALL
    #   26 CALL
    #   36 STORE_DEREF remaining
    #   38 LOAD_DEREF remaining
    #   40 LOAD_CONST 0
    #   42 COMPARE_OP >
    #   48 POP_JUMP_FORWARD_IF_FALSE to 236
    #   50 LOAD_GLOBAL NULL + max
    #   62 LOAD_CLOSURE remaining
    #   64 BUILD_TUPLE
    #   66 LOAD_CONST <code object <genexpr> at 0x105af88f0, file "acheron\device_process\bootloader.py", line 94>
    #   68 MAKE_FUNCTION closure
    #   70 LOAD_FAST block_sizes
    #   72 GET_ITER
    #   74 PRECALL
    #   78 CALL
    #   88 PRECALL
    #   92 CALL
    #  102 STORE_FAST block_size
    #  104 LOAD_FAST device
    #  106 LOAD_METHOD write_bootloader_code_block
    #  128 LOAD_FAST page_data
    #  130 LOAD_FAST index
    #  132 LOAD_FAST index
    #  134 LOAD_FAST block_size
    #  136 BINARY_OP +
    #  140 BUILD_SLICE
    #  142 BINARY_SUBSCR
    #  152 PRECALL
    #  156 CALL
    #  166 POP_TOP
    #  168 LOAD_FAST index
    #  170 LOAD_FAST block_size
    #  172 BINARY_OP +=
    #  176 STORE_FAST index
    #  178 LOAD_DEREF remaining
    #  180 LOAD_FAST block_size
    #  182 BINARY_OP -=
    #  186 STORE_DEREF remaining
    #  188 PUSH_NULL
    #  190 LOAD_FAST callback
    #  192 LOAD_FAST done_bytes
    #  194 LOAD_FAST index
    #  196 BINARY_OP +
    #  200 LOAD_FAST total_bytes
    #  202 LOAD_FAST message
    #  204 PRECALL
    #  208 CALL
    #  218 POP_TOP
    #  220 LOAD_DEREF remaining
    #  222 LOAD_CONST 0
    #  224 COMPARE_OP >
    #  230 POP_JUMP_BACKWARD_IF_TRUE to 50
    #  232 LOAD_CONST None
    #  234 RETURN_VALUE
    #  236 LOAD_CONST None
    #  238 RETURN_VALUE
    pass

def do_bootload_pass(device, firm_data, block_sizes, verify_size, total_bytes, callback):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_CONST 0
    #    4 STORE_FAST done_bytes
    #    6 LOAD_FAST firm_data
    #    8 LOAD_CONST 'data'
    #   10 BINARY_SUBSCR
    #   20 GET_ITER
    #   22 EXTENDED_ARG
    #   24 FOR_ITER to 632
    #   26 STORE_FAST page_info
    #   28 LOAD_FAST page_info
    #   30 LOAD_CONST 0
    #   32 BINARY_SUBSCR
    #   42 STORE_FAST page_number
    #   44 LOAD_GLOBAL NULL + binascii
    #   56 LOAD_ATTR a2b_hex
    #   66 LOAD_FAST page_info
    #   68 LOAD_CONST 1
    #   70 BINARY_SUBSCR
    #   80 PRECALL
    #   84 CALL
    #   94 STORE_FAST nonce
    #   96 LOAD_GLOBAL NULL + binascii
    #  108 LOAD_ATTR a2b_hex
    #  118 LOAD_FAST page_info
    #  120 LOAD_CONST 2
    #  122 BINARY_SUBSCR
    #  132 PRECALL
    #  136 CALL
    #  146 STORE_FAST page_data
    #  148 LOAD_GLOBAL NULL + binascii
    #  160 LOAD_ATTR a2b_hex
    #  170 LOAD_FAST page_info
    #  172 LOAD_CONST 3
    #  174 BINARY_SUBSCR
    #  184 PRECALL
    #  188 CALL
    #  198 STORE_FAST digest
    #  200 LOAD_CONST 'Writing Page {}'
    #  202 LOAD_METHOD format
    #  224 LOAD_FAST page_number
    #  226 PRECALL
    #  230 CALL
    #  240 STORE_FAST message
    #  242 PUSH_NULL
    #  244 LOAD_FAST callback
    #  246 LOAD_FAST done_bytes
    #  248 LOAD_FAST total_bytes
    #  250 LOAD_FAST message
    #  252 PRECALL
    #  256 CALL
    #  266 POP_TOP
    #  268 LOAD_FAST device
    #  270 LOAD_METHOD start_bootloader_page
    #  292 LOAD_FAST page_number
    #  294 LOAD_FAST nonce
    #  296 PRECALL
    #  300 CALL
    #  310 POP_TOP
    #  312 NOP
    #  314 LOAD_FAST device
    #  316 LOAD_METHOD verify_bootloader_page
    #  338 LOAD_FAST digest
    #  340 PRECALL
    #  344 CALL
    #  354 POP_TOP
    #  356 LOAD_CONST False
    #  358 STORE_FAST different
    #  360 JUMP_FORWARD to 460
    #  362 PUSH_EXC_INFO
    #  364 LOAD_GLOBAL asphodel
    #  376 LOAD_ATTR AsphodelError
    #  386 CHECK_EXC_MATCH
    #  388 POP_JUMP_FORWARD_IF_FALSE to 452
    #  390 STORE_FAST e
    #  392 LOAD_FAST e
    #  394 LOAD_ATTR args
    #  404 LOAD_CONST 1
    #  406 BINARY_SUBSCR
    #  416 LOAD_CONST 'ERROR_CODE_INVALID_DATA'
    # ... bytecode truncated ...
    pass

def do_bootload(device, serial_number, logger, firm_data, callback):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_CONST 3
    #    4 STORE_FAST tries
    #    6 LOAD_CONST None
    #    8 STORE_FAST block_sizes
    #   10 LOAD_GLOBAL NULL + sum
    #   22 LOAD_CONST <code object <genexpr> at 0x105a73750, file "acheron\device_process\bootloader.py", line 157>
    #   24 MAKE_FUNCTION
    #   26 LOAD_FAST firm_data
    #   28 LOAD_CONST 'data'
    #   30 BINARY_SUBSCR
    #   40 GET_ITER
    #   42 PRECALL
    #   46 CALL
    #   56 PRECALL
    #   60 CALL
    #   70 STORE_FAST write_bytes
    #   72 LOAD_FAST device
    #   74 LOAD_METHOD supports_bootloader_commands
    #   96 PRECALL
    #  100 CALL
    #  110 POP_JUMP_FORWARD_IF_TRUE to 266
    #  112 PUSH_NULL
    #  114 LOAD_FAST callback
    #  116 LOAD_CONST 0
    #  118 LOAD_CONST 0
    #  120 LOAD_CONST 'Switching to bootloader...'
    #  122 PRECALL
    #  126 CALL
    #  136 POP_TOP
    #  138 LOAD_FAST device
    #  140 LOAD_METHOD bootloader_jump
    #  162 PRECALL
    #  166 CALL
    #  176 POP_TOP
    #  178 LOAD_FAST device
    #  180 LOAD_METHOD reconnect
    #  202 LOAD_CONST True
    #  204 LOAD_FAST serial_number
    #  206 KW_NAMES
    #  208 PRECALL
    #  212 CALL
    #  222 POP_TOP
    #  224 LOAD_FAST logger
    #  226 LOAD_METHOD info
    #  248 LOAD_CONST 'Switched to bootloader'
    #  250 PRECALL
    #  254 CALL
    #  264 POP_TOP
    #  266 NOP
    #  268 NOP
    #  270 LOAD_FAST block_sizes
    #  272 POP_JUMP_FORWARD_IF_NOT_NONE to 314
    #  274 LOAD_FAST device
    #  276 LOAD_METHOD get_bootloader_block_sizes
    #  298 PRECALL
    #  302 CALL
    #  312 STORE_FAST block_sizes
    #  314 LOAD_GLOBAL NULL + max
    #  326 LOAD_FAST block_sizes
    #  328 PRECALL
    #  332 CALL
    #  342 STORE_FAST verify_size
    #  344 LOAD_FAST verify_size
    #  346 LOAD_GLOBAL NULL + len
    #  358 LOAD_FAST firm_data
    #  360 LOAD_CONST 'data'
    #  362 BINARY_SUBSCR
    #  372 PRECALL
    #  376 CALL
    #  386 BINARY_OP *
    #  390 STORE_FAST verify_bytes
    #  392 LOAD_FAST write_bytes
    #  394 LOAD_FAST verify_bytes
    #  396 BINARY_OP +
    #  400 STORE_FAST total_bytes
    #  402 LOAD_GLOBAL NULL + do_bootload_pass
    #  414 LOAD_FAST device
    #  416 LOAD_FAST firm_data
    #  418 LOAD_FAST block_sizes
    # ... bytecode truncated ...
    pass
