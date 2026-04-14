# Source Generated with Decompyle++
# File: disk_trigger.pyc (Python 3.11)

from typing import Any, Optional
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo
from ..calc_process.types import LimitType, Trigger

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DiskTrigger(BaseModel):

    id: str

    channel_id: int

    subchannel_index = 0

    subchannel_index: int

    limit_type: LimitType

    activate_limit: float

    deactivate_limit = None

    hysteresis = Field(ge=0.0, default=None, exclude=True, repr=False)

    def ensure_list(cls, v, info):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL NULL + isinstance
        #   14 LOAD_FAST v
        #   16 LOAD_GLOBAL str
        #   28 PRECALL
        #   32 CALL
        #   42 POP_JUMP_FORWARD_IF_FALSE to 118
        #   44 LOAD_GLOBAL NULL + len
        #   56 LOAD_FAST v
        #   58 PRECALL
        #   62 CALL
        #   72 LOAD_CONST 0
        #   74 COMPARE_OP >
        #   80 POP_JUMP_FORWARD_IF_FALSE to 88
        #   82 LOAD_FAST v
        #   84 BUILD_TUPLE
        #   86 RETURN_VALUE
        #   88 LOAD_GLOBAL NULL + ValueError
        #  100 LOAD_CONST 'Empty serial number string'
        #  102 PRECALL
        #  106 CALL
        #  116 RAISE_VARARGS
        #  118 LOAD_GLOBAL NULL + len
        #  130 LOAD_FAST v
        #  132 PRECALL
        #  136 CALL
        #  146 LOAD_CONST 0
        #  148 COMPARE_OP ==
        #  154 POP_JUMP_FORWARD_IF_FALSE to 186
        #  156 LOAD_GLOBAL NULL + ValueError
        #  168 LOAD_CONST 'Empty serial number'
        #  170 PRECALL
        #  174 CALL
        #  184 RAISE_VARARGS
        #  186 LOAD_FAST v
        #  188 RETURN_VALUE
        pass

    def has_deactivate(cls, data):
        if isinstance(data, dict) and 'deactivate_limit' in data and 'hysteresis' in data:
            raise ValueError('deactivate_limit and hysteresis both set')
        return data

    def convert_hysteresis(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR deactivate_limit
        #   14 POP_JUMP_FORWARD_IF_NOT_NONE to 338
        #   16 LOAD_FAST self
        #   18 LOAD_ATTR hysteresis
        #   28 POP_JUMP_FORWARD_IF_NOT_NONE to 60
        #   30 LOAD_GLOBAL NULL + ValueError
        #   42 LOAD_CONST 'deactivate_limit or hysteresis missing'
        #   44 PRECALL
        #   48 CALL
        #   58 RAISE_VARARGS
        #   60 LOAD_FAST self
        #   62 LOAD_ATTR limit_type
        #   72 LOAD_GLOBAL LimitType
        #   84 LOAD_ATTR MEAN_HIGH_LIMIT
        #   94 COMPARE_OP ==
        #  100 POP_JUMP_FORWARD_IF_TRUE to 144
        #  102 LOAD_FAST self
        #  104 LOAD_ATTR limit_type
        #  114 LOAD_GLOBAL LimitType
        #  126 LOAD_ATTR STD_HIGH_LIMIT
        #  136 COMPARE_OP ==
        #  142 POP_JUMP_FORWARD_IF_FALSE to 162
        #  144 LOAD_FAST self
        #  146 LOAD_ATTR hysteresis
        #  156 UNARY_NEGATIVE
        #  158 STORE_FAST delta
        #  160 JUMP_FORWARD to 292
        #  162 LOAD_FAST self
        #  164 LOAD_ATTR limit_type
        #  174 LOAD_GLOBAL LimitType
        #  186 LOAD_ATTR MEAN_LOW_LIMIT
        #  196 COMPARE_OP ==
        #  202 POP_JUMP_FORWARD_IF_TRUE to 246
        #  204 LOAD_FAST self
        #  206 LOAD_ATTR limit_type
        #  216 LOAD_GLOBAL LimitType
        #  228 LOAD_ATTR STD_LOW_LIMIT
        #  238 COMPARE_OP ==
        #  244 POP_JUMP_FORWARD_IF_FALSE to 262
        #  246 LOAD_FAST self
        #  248 LOAD_ATTR hysteresis
        #  258 STORE_FAST delta
        #  260 JUMP_FORWARD to 292
        #  262 LOAD_GLOBAL NULL + ValueError
        #  274 LOAD_CONST 'Unknown limit type for hysteresis'
        #  276 PRECALL
        #  280 CALL
        #  290 RAISE_VARARGS
        #  292 LOAD_FAST self
        #  294 LOAD_ATTR activate_limit
        #  304 LOAD_FAST delta
        #  306 BINARY_OP +
        #  310 LOAD_FAST self
        #  312 STORE_ATTR deactivate_limit
        #  322 LOAD_CONST None
        #  324 LOAD_FAST self
        #  326 STORE_ATTR hysteresis
        #  336 JUMP_FORWARD to 636
        #  338 LOAD_FAST self
        #  340 LOAD_ATTR limit_type
        #  350 LOAD_GLOBAL LimitType
        #  362 LOAD_ATTR MEAN_HIGH_LIMIT
        #  372 COMPARE_OP ==
        #  378 POP_JUMP_FORWARD_IF_TRUE to 422
        #  380 LOAD_FAST self
        #  382 LOAD_ATTR limit_type
        #  392 LOAD_GLOBAL LimitType
        #  404 LOAD_ATTR STD_HIGH_LIMIT
        #  414 COMPARE_OP ==
        #  420 POP_JUMP_FORWARD_IF_FALSE to 486
        #  422 LOAD_FAST self
        #  424 LOAD_ATTR deactivate_limit
        #  434 LOAD_FAST self
        #  436 LOAD_ATTR activate_limit
        #  446 COMPARE_OP >
        #  452 POP_JUMP_FORWARD_IF_FALSE to 484
        #  454 LOAD_GLOBAL NULL + ValueError
        #  466 LOAD_CONST 'deactivate_limit greater than activate_limit'
        # ... bytecode truncated ...
        pass

    def convert(self):
        values = self.model_dump()
        del values['serial']
