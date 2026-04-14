# Source Generated with Decompyle++
# File: ringbuffer.pyc (Python 3.11)

import collections
import threading
import numpy
from numpy.typing import NDArray

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RingBuffer:

    def __init__(self, maxlen, element_size):
        self.maxlen = maxlen
        self.element_size = element_size
        self.lock = threading.Lock()
        self.length = 0
        self.index = 0
        shape = (maxlen, element_size)
        self.data = numpy.empty(shape, dtype = numpy.float64)
        self.pending = collections.deque(maxlen = maxlen)

    def _handle_pending(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_CONST None
        #    4 RETURN_VALUE
        pass

    def __len__(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR length
        #   30 SWAP
        #   32 LOAD_CONST None
        #   34 LOAD_CONST None
        #   36 LOAD_CONST None
        #   38 PRECALL
        #   42 CALL
        #   52 POP_TOP
        #   54 RETURN_VALUE
        #   56 PUSH_EXC_INFO
        #   58 WITH_EXCEPT_START
        #   60 POP_JUMP_FORWARD_IF_TRUE to 70
        #   62 RERAISE
        #   64 COPY
        #   66 POP_EXCEPT
        #   68 RERAISE
        #   70 POP_TOP
        #   72 POP_EXCEPT
        #   74 POP_TOP
        #   76 POP_TOP
        #   78 LOAD_CONST None
        #   80 RETURN_VALUE
        pass

    def clear(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_CONST 0
        #   20 LOAD_FAST self
        #   22 STORE_ATTR length
        #   32 LOAD_CONST 0
        #   34 LOAD_FAST self
        #   36 STORE_ATTR index
        #   46 LOAD_CONST None
        #   48 LOAD_CONST None
        #   50 LOAD_CONST None
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_CONST None
        #   70 RETURN_VALUE
        #   72 PUSH_EXC_INFO
        #   74 WITH_EXCEPT_START
        #   76 POP_JUMP_FORWARD_IF_TRUE to 86
        #   78 RERAISE
        #   80 COPY
        #   82 POP_EXCEPT
        #   84 RERAISE
        #   86 POP_TOP
        #   88 POP_EXCEPT
        #   90 POP_TOP
        #   92 POP_TOP
        #   94 LOAD_CONST None
        #   96 RETURN_VALUE
        pass

    def get_contents(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR data
        #   30 LOAD_CONST 0
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR length
        #   44 BUILD_SLICE
        #   46 BINARY_SUBSCR
        #   56 SWAP
        #   58 LOAD_CONST None
        #   60 LOAD_CONST None
        #   62 LOAD_CONST None
        #   64 PRECALL
        #   68 CALL
        #   78 POP_TOP
        #   80 RETURN_VALUE
        #   82 PUSH_EXC_INFO
        #   84 WITH_EXCEPT_START
        #   86 POP_JUMP_FORWARD_IF_TRUE to 96
        #   88 RERAISE
        #   90 COPY
        #   92 POP_EXCEPT
        #   94 RERAISE
        #   96 POP_TOP
        #   98 POP_EXCEPT
        #  100 POP_TOP
        #  102 POP_TOP
        #  104 LOAD_CONST None
        #  106 RETURN_VALUE
        pass

    def append(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST value
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR data
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR index
        #   44 STORE_SUBSCR
        #   48 LOAD_FAST self
        #   50 COPY
        #   52 LOAD_ATTR index
        #   62 LOAD_CONST 1
        #   64 BINARY_OP +=
        #   68 SWAP
        #   70 STORE_ATTR index
        #   80 LOAD_FAST self
        #   82 COPY
        #   84 LOAD_ATTR length
        #   94 LOAD_CONST 1
        #   96 BINARY_OP +=
        #  100 SWAP
        #  102 STORE_ATTR length
        #  112 LOAD_FAST self
        #  114 LOAD_ATTR length
        #  124 LOAD_FAST self
        #  126 LOAD_ATTR maxlen
        #  136 COMPARE_OP ==
        #  142 POP_JUMP_FORWARD_IF_FALSE to 182
        #  144 LOAD_CONST 0
        #  146 LOAD_FAST self
        #  148 STORE_ATTR index
        #  158 LOAD_GLOBAL RingBufferFull
        #  170 LOAD_FAST self
        #  172 STORE_ATTR __class__
        #  182 LOAD_CONST None
        #  184 LOAD_CONST None
        #  186 LOAD_CONST None
        #  188 PRECALL
        #  192 CALL
        #  202 POP_TOP
        #  204 LOAD_CONST None
        #  206 RETURN_VALUE
        #  208 PUSH_EXC_INFO
        #  210 WITH_EXCEPT_START
        #  212 POP_JUMP_FORWARD_IF_TRUE to 222
        #  214 RERAISE
        #  216 COPY
        #  218 POP_EXCEPT
        #  220 RERAISE
        #  222 POP_TOP
        #  224 POP_EXCEPT
        #  226 POP_TOP
        #  228 POP_TOP
        #  230 LOAD_CONST None
        #  232 RETURN_VALUE
        pass

    def extend(self, array):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_GLOBAL NULL + len
        #   30 LOAD_FAST array
        #   32 PRECALL
        #   36 CALL
        #   46 LOAD_FAST self
        #   48 LOAD_ATTR maxlen
        #   58 COMPARE_OP >=
        #   64 POP_JUMP_FORWARD_IF_FALSE to 222
        #   66 LOAD_FAST array
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR maxlen
        #   80 UNARY_NEGATIVE
        #   82 LOAD_CONST None
        #   84 BUILD_SLICE
        #   86 BINARY_SUBSCR
        #   96 LOAD_FAST self
        #   98 STORE_ATTR data
        #  108 LOAD_CONST 0
        #  110 LOAD_FAST self
        #  112 STORE_ATTR index
        #  122 LOAD_FAST self
        #  124 LOAD_ATTR maxlen
        #  134 LOAD_FAST self
        #  136 STORE_ATTR length
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR pending
        #  158 LOAD_METHOD clear
        #  180 PRECALL
        #  184 CALL
        #  194 POP_TOP
        #  196 LOAD_GLOBAL RingBufferFull
        #  208 LOAD_FAST self
        #  210 STORE_ATTR __class__
        #  220 JUMP_FORWARD to 714
        #  222 LOAD_GLOBAL NULL + len
        #  234 LOAD_FAST array
        #  236 PRECALL
        #  240 CALL
        #  250 LOAD_FAST self
        #  252 LOAD_ATTR index
        #  262 BINARY_OP +
        #  266 LOAD_FAST self
        #  268 LOAD_ATTR maxlen
        #  278 COMPARE_OP >=
        #  284 POP_JUMP_FORWARD_IF_FALSE to 556
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR maxlen
        #  298 LOAD_FAST self
        #  300 LOAD_ATTR index
        #  310 BINARY_OP -
        #  314 STORE_FAST end_length
        #  316 LOAD_GLOBAL NULL + len
        #  328 LOAD_FAST array
        #  330 PRECALL
        #  334 CALL
        #  344 LOAD_FAST end_length
        #  346 BINARY_OP -
        #  350 STORE_FAST start_length
        #  352 LOAD_FAST array
        #  354 LOAD_CONST 0
        #  356 LOAD_FAST end_length
        #  358 BUILD_SLICE
        #  360 BINARY_SUBSCR
        #  370 LOAD_FAST self
        #  372 LOAD_ATTR data
        #  382 LOAD_FAST self
        #  384 LOAD_ATTR index
        #  394 LOAD_CONST None
        #  396 BUILD_SLICE
        #  398 STORE_SUBSCR
        #  402 LOAD_FAST array
        #  404 LOAD_FAST end_length
        #  406 LOAD_CONST None
        #  408 BUILD_SLICE
        #  410 BINARY_SUBSCR
        # ... bytecode truncated ...
        pass

class RingBufferFull(RingBuffer):

    def _handle_pending(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR pending
        #   14 EXTENDED_ARG
        #   16 POP_JUMP_FORWARD_IF_FALSE to 602
        #   18 LOAD_GLOBAL NULL + numpy
        #   30 LOAD_ATTR concatenate
        #   40 LOAD_FAST self
        #   42 LOAD_ATTR pending
        #   52 PRECALL
        #   56 CALL
        #   66 STORE_FAST array
        #   68 LOAD_FAST self
        #   70 LOAD_ATTR pending
        #   80 LOAD_METHOD clear
        #  102 PRECALL
        #  106 CALL
        #  116 POP_TOP
        #  118 LOAD_GLOBAL NULL + len
        #  130 LOAD_FAST array
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_FAST self
        #  148 LOAD_ATTR index
        #  158 BINARY_OP +
        #  162 LOAD_FAST self
        #  164 LOAD_ATTR maxlen
        #  174 COMPARE_OP >
        #  180 POP_JUMP_FORWARD_IF_FALSE to 464
        #  182 LOAD_GLOBAL NULL + len
        #  194 LOAD_FAST array
        #  196 PRECALL
        #  200 CALL
        #  210 LOAD_FAST self
        #  212 LOAD_ATTR maxlen
        #  222 COMPARE_OP >=
        #  228 POP_JUMP_FORWARD_IF_FALSE to 290
        #  230 LOAD_FAST array
        #  232 LOAD_FAST self
        #  234 LOAD_ATTR maxlen
        #  244 UNARY_NEGATIVE
        #  246 LOAD_CONST None
        #  248 BUILD_SLICE
        #  250 BINARY_SUBSCR
        #  260 LOAD_FAST self
        #  262 STORE_ATTR data
        #  272 LOAD_CONST 0
        #  274 LOAD_FAST self
        #  276 STORE_ATTR index
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        #  290 LOAD_FAST self
        #  292 LOAD_ATTR maxlen
        #  302 LOAD_FAST self
        #  304 LOAD_ATTR index
        #  314 BINARY_OP -
        #  318 STORE_FAST end_length
        #  320 LOAD_GLOBAL NULL + len
        #  332 LOAD_FAST array
        #  334 PRECALL
        #  338 CALL
        #  348 LOAD_FAST end_length
        #  350 BINARY_OP -
        #  354 STORE_FAST start_length
        #  356 LOAD_FAST array
        #  358 LOAD_CONST 0
        #  360 LOAD_FAST end_length
        #  362 BUILD_SLICE
        #  364 BINARY_SUBSCR
        #  374 LOAD_FAST self
        #  376 LOAD_ATTR data
        #  386 LOAD_FAST self
        #  388 LOAD_ATTR index
        #  398 LOAD_CONST None
        #  400 BUILD_SLICE
        #  402 STORE_SUBSCR
        #  406 LOAD_FAST array
        #  408 LOAD_FAST end_length
        #  410 LOAD_CONST None
        #  412 BUILD_SLICE
        # ... bytecode truncated ...
        pass

    def clear(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR pending
        #   30 LOAD_METHOD clear
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_CONST 0
        #   70 LOAD_FAST self
        #   72 STORE_ATTR length
        #   82 LOAD_CONST 0
        #   84 LOAD_FAST self
        #   86 STORE_ATTR index
        #   96 LOAD_GLOBAL RingBuffer
        #  108 LOAD_FAST self
        #  110 STORE_ATTR __class__
        #  120 LOAD_CONST None
        #  122 LOAD_CONST None
        #  124 LOAD_CONST None
        #  126 PRECALL
        #  130 CALL
        #  140 POP_TOP
        #  142 LOAD_CONST None
        #  144 RETURN_VALUE
        #  146 PUSH_EXC_INFO
        #  148 WITH_EXCEPT_START
        #  150 POP_JUMP_FORWARD_IF_TRUE to 160
        #  152 RERAISE
        #  154 COPY
        #  156 POP_EXCEPT
        #  158 RERAISE
        #  160 POP_TOP
        #  162 POP_EXCEPT
        #  164 POP_TOP
        #  166 POP_TOP
        #  168 LOAD_CONST None
        #  170 RETURN_VALUE
        pass

    def get_contents(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_METHOD _handle_pending
        #   42 PRECALL
        #   46 CALL
        #   56 POP_TOP
        #   58 LOAD_GLOBAL NULL + numpy
        #   70 LOAD_ATTR roll
        #   80 LOAD_FAST self
        #   82 LOAD_ATTR data
        #   92 LOAD_FAST self
        #   94 LOAD_ATTR index
        #  104 UNARY_NEGATIVE
        #  106 LOAD_CONST 0
        #  108 KW_NAMES
        #  110 PRECALL
        #  114 CALL
        #  124 SWAP
        #  126 LOAD_CONST None
        #  128 LOAD_CONST None
        #  130 LOAD_CONST None
        #  132 PRECALL
        #  136 CALL
        #  146 POP_TOP
        #  148 RETURN_VALUE
        #  150 PUSH_EXC_INFO
        #  152 WITH_EXCEPT_START
        #  154 POP_JUMP_FORWARD_IF_TRUE to 164
        #  156 RERAISE
        #  158 COPY
        #  160 POP_EXCEPT
        #  162 RERAISE
        #  164 POP_TOP
        #  166 POP_EXCEPT
        #  168 POP_TOP
        #  170 POP_TOP
        #  172 LOAD_CONST None
        #  174 RETURN_VALUE
        pass

    def append(self, value):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST value
        #   20 LOAD_FAST self
        #   22 LOAD_ATTR data
        #   32 LOAD_FAST self
        #   34 LOAD_ATTR index
        #   44 STORE_SUBSCR
        #   48 LOAD_FAST self
        #   50 COPY
        #   52 LOAD_ATTR index
        #   62 LOAD_CONST 1
        #   64 BINARY_OP +=
        #   68 SWAP
        #   70 STORE_ATTR index
        #   80 LOAD_FAST self
        #   82 LOAD_ATTR index
        #   92 LOAD_FAST self
        #   94 LOAD_ATTR maxlen
        #  104 COMPARE_OP ==
        #  110 POP_JUMP_FORWARD_IF_FALSE to 126
        #  112 LOAD_CONST 0
        #  114 LOAD_FAST self
        #  116 STORE_ATTR index
        #  126 LOAD_CONST None
        #  128 LOAD_CONST None
        #  130 LOAD_CONST None
        #  132 PRECALL
        #  136 CALL
        #  146 POP_TOP
        #  148 LOAD_CONST None
        #  150 RETURN_VALUE
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
        #  174 LOAD_CONST None
        #  176 RETURN_VALUE
        pass

    def extend(self, array):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR lock
        #   14 BEFORE_WITH
        #   16 POP_TOP
        #   18 LOAD_FAST self
        #   20 LOAD_ATTR pending
        #   30 LOAD_METHOD append
        #   52 LOAD_FAST array
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_CONST None
        #   72 LOAD_CONST None
        #   74 LOAD_CONST None
        #   76 PRECALL
        #   80 CALL
        #   90 POP_TOP
        #   92 LOAD_CONST None
        #   94 RETURN_VALUE
        #   96 PUSH_EXC_INFO
        #   98 WITH_EXCEPT_START
        #  100 POP_JUMP_FORWARD_IF_TRUE to 110
        #  102 RERAISE
        #  104 COPY
        #  106 POP_EXCEPT
        #  108 RERAISE
        #  110 POP_TOP
        #  112 POP_EXCEPT
        #  114 POP_TOP
        #  116 POP_TOP
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass
