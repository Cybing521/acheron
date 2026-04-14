# Source Generated with Decompyle++
# File: tmpnkp2smkn.marshal (Python 3.11)

from collections import deque
from datetime import datetime, timedelta, timezone
from functools import cache
import logging
import os
import threading
from zoneinfo import ZoneInfo
from PySide6 import QtCore
from croniter import croniter, CroniterBadDateError
from pydantic import TypeAdapter
from disk_schedule import DiskSchedule
from disk_trigger import DiskTrigger
from calc_process.types import Trigger
from core.device_controller import DeviceController
from core.dispatcher import Dispatcher
from device_process.schedule import ScheduleItem
logger = logging.getLogger(__name__)
SCHEDULE_READER_KEY = 'schedule_reader'
GlobalSchedule = dict[(tuple[(str, ...)], list[DiskSchedule])]

class ScheduleReader(QtCore.QObject):
    pass
# WARNING: Decompyle incomplete

