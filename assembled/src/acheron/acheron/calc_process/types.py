# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from dataclasses import dataclass
import enum
from typing import Any
from asphodel import AsphodelChannelInfo, StreamRateInfo
# INVALID FROM DECOMPILER: ChannelInformation = <NODE:12>()
# INVALID FROM DECOMPILER: CalcData = <NODE:12>()
# INVALID FROM DECOMPILER: CalcControl = <NODE:12>()
# INVALID FROM DECOMPILER: CalcSettings = <NODE:12>()
# INVALID FROM DECOMPILER: LimitType = <NODE:12>()
# INVALID FROM DECOMPILER: Trigger = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class ChannelInformation:

    name: str

    channel_id: int

    stream_id: int

    channel: AsphodelChannelInfo

    rate_info: StreamRateInfo

    samples: int

    rate: float

    downsample_factor: int

    mean_len: int

    plot_len: int

    fft_shortened: bool

    fft_sample_len: int

    fft_freq_axis: Any

    fft_size: int

class CalcData(enum.Enum):

    PROCESSING_START = enum.auto()

    PROCESSING_STOP = enum.auto()

    CHANNEL_UPDATE = enum.auto()

    PLOT_UPDATE = enum.auto()

    FFT_UPDATE = enum.auto()

    LOST_PACKET_UPDATE = enum.auto()

    UNKNOWN_ID = enum.auto()

    ACTIVE_TRIGGERS_CHANGED = enum.auto()

class CalcControl(enum.Enum):

    STOP = enum.auto()

    CLOSE = enum.auto()

    SET_SHOWN = enum.auto()

    PLOT_CHANGE = enum.auto()

    RESET_LOST_PACKETS = enum.auto()

    CHANGE_SETTINGS = enum.auto()

    CHANGE_TRIGGERS = enum.auto()

    SET_CONNECTIVITY_PIPE = enum.auto()

@dataclass
class CalcSettings:

    channel_interval: float

    plot_interval: float

    fft_interval: float

    downsample: bool

class LimitType:

    MEAN_HIGH_LIMIT = 'mean high'

    MEAN_LOW_LIMIT = 'mean low'

    STD_HIGH_LIMIT = 'std high'

    STD_LOW_LIMIT = 'std low'

@dataclass
class Trigger:

    id: str

    channel_id: int

    subchannel_index: int

    limit_type: LimitType

    activate_limit: float

    deactivate_limit: float
