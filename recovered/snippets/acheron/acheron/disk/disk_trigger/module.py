# Source Generated with Decompyle++
# File: tmp6c8f6i8k.marshal (Python 3.11)

from typing import Any, Optional
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo
from calc_process.types import LimitType, Trigger

class DiskTrigger(BaseModel):
    channel_id: int = 'DiskTrigger'
    activate_limit: float = 0
    deactivate_limit: Optional[float] = None
    hysteresis: Optional[float] = Field(ge = 0, default = None, exclude = True, repr = False)
    ensure_list = (lambda cls = None, v = field_validator('serial', mode = 'before'), info = classmethod: if isinstance(v, str):
if len(v) > 0:
(v,)raise None('Empty serial number string')if len(v) == 0:
raise ValueError('Empty serial number')v)()()
    has_deactivate = (lambda cls = None, data = model_validator(mode = 'before'): if isinstance(data, dict) and 'deactivate_limit' in data and 'hysteresis' in data:
raise ValueError('deactivate_limit and hysteresis both set')data)()()
    convert_hysteresis = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def convert(self = None):
        values = self.model_dump()
        del values['serial']
    # WARNING: Decompyle incomplete


