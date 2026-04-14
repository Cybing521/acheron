# Source Generated with Decompyle++
# File: preferences.pyc (Python 3.11)

from typing import TypeVar, Union
from PySide6 import QtCore
T = TypeVar('T')

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def read_bool_setting(settings, setting_name, default):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 NOP
    #    4 LOAD_FAST settings
    #    6 LOAD_METHOD value
    #   28 LOAD_FAST setting_name
    #   30 PRECALL
    #   34 CALL
    #   44 STORE_FAST s
    #   46 LOAD_FAST s
    #   48 POP_JUMP_FORWARD_IF_NONE to 100
    #   50 LOAD_GLOBAL NULL + int
    #   62 LOAD_FAST s
    #   64 PRECALL
    #   68 CALL
    #   78 STORE_FAST s_int
    #   80 LOAD_FAST s_int
    #   82 LOAD_CONST 0
    #   84 COMPARE_OP ==
    #   90 POP_JUMP_FORWARD_IF_FALSE to 96
    #   92 LOAD_CONST False
    #   94 JUMP_FORWARD to 98
    #   96 LOAD_CONST True
    #   98 RETURN_VALUE
    #  100 LOAD_FAST default
    #  102 RETURN_VALUE
    #  104 PUSH_EXC_INFO
    #  106 LOAD_GLOBAL ValueError
    #  118 CHECK_EXC_MATCH
    #  120 POP_JUMP_FORWARD_IF_FALSE to 132
    #  122 POP_TOP
    #  124 LOAD_FAST default
    #  126 SWAP
    #  128 POP_EXCEPT
    #  130 RETURN_VALUE
    #  132 RERAISE
    #  134 COPY
    #  136 POP_EXCEPT
    #  138 RERAISE
    pass

def read_int_setting(settings, setting_name, default):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 NOP
    #    4 LOAD_FAST settings
    #    6 LOAD_METHOD value
    #   28 LOAD_FAST setting_name
    #   30 PRECALL
    #   34 CALL
    #   44 STORE_FAST s
    #   46 LOAD_FAST s
    #   48 POP_JUMP_FORWARD_IF_NONE to 80
    #   50 LOAD_GLOBAL NULL + int
    #   62 LOAD_FAST s
    #   64 PRECALL
    #   68 CALL
    #   78 RETURN_VALUE
    #   80 LOAD_FAST default
    #   82 RETURN_VALUE
    #   84 PUSH_EXC_INFO
    #   86 LOAD_GLOBAL ValueError
    #   98 CHECK_EXC_MATCH
    #  100 POP_JUMP_FORWARD_IF_FALSE to 112
    #  102 POP_TOP
    #  104 LOAD_FAST default
    #  106 SWAP
    #  108 POP_EXCEPT
    #  110 RETURN_VALUE
    #  112 RERAISE
    #  114 COPY
    #  116 POP_EXCEPT
    #  118 RERAISE
    pass

def write_bool_setting(settings, setting_name, value):
    settings.setValue(setting_name, 1 if value else 0)
