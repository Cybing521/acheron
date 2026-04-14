from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Any, Optional


class HardwareTestFunction(enum.Enum):

    UNKNOWN = enum.auto()


@dataclass
class RFTestParams:

    frequency: Optional[float] = None

    power: Optional[float] = None


@dataclass
class RFFixedTestParams(RFTestParams):

    duration: Optional[float] = None


@dataclass
class RFSweepTestParams(RFTestParams):

    start_frequency: Optional[float] = None

    stop_frequency: Optional[float] = None

    step_frequency: Optional[float] = None


class StreamControl(enum.Enum):

    ACTIVE_TRIGGERS_CHANGED = enum.auto()

    DELETE_SCHEDULE_IDS = enum.auto()

    FORCE_RESET = enum.auto()

    FORCE_RUN_APPLICATION = enum.auto()

    FORCE_RUN_BOOTLOADER = enum.auto()

    UPDATE_SCHEDULE_ITEM = enum.auto()


@dataclass
class StreamSettings:

    auto_rgb: bool

    response_time: int

    buffer_time: int

    timeout: int

    default_output_config: Any = None


class StreamStatus(enum.Enum):

    STARTING = enum.auto()

    RUNNING = enum.auto()

    STOPPED = enum.auto()

    ERROR = enum.auto()


@dataclass
class StreamRemote:

    control: Any = None

    packet: Any = None

    status: Any = None


@dataclass
class ScanResult:

    serial_number: str = ''

    board_info: Any = None

    bootloader: bool = False

    remote: Any = None


def create_remote(*args, **kwargs):
    return StreamRemote()


def start_stream_controller(*args, **kwargs):
    return None


def stop_stream_controller(*args, **kwargs):
    return None
