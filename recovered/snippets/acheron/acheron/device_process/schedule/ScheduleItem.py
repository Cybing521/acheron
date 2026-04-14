# Source Generated with Decompyle++
# File: tmp69zpituz.marshal (Python 3.11)

id: str = 'ScheduleItem'
remote_sn: Optional[int] = None
remote_bootloader: bool = False
trigger: Optional[str] = None
needs_rf_power: bool = False
active_streams: Optional[frozenset[int]] = frozenset()
device_config: frozenset[tuple[(str, Any)]] = frozenset()
start_time: Optional[datetime] = None
collection_time: Optional[datetime] = None
stop_time: Optional[datetime] = None
duration: Optional[timedelta] = None
failure_time: Optional[datetime] = None
output_config: Union[(OutputConfig, None, Literal[True])] = None

def configure_nvm(self = None, device_info = None, nvm = None):
    return asphodel.device_config.configure_nvm(self.device_config, device_info, nvm)


def nvm_valid(self = None, device_info = None, nvm = None):
    new_nvm = self.configure_nvm(device_info, nvm)
    return new_nvm == nvm


def priority_key(self = None):
    pass
# WARNING: Decompyle incomplete


def sort_key(self = None):
    pass
# WARNING: Decompyle incomplete


def __lt__(self = None, other = None):
    return self.sort_key() < other.sort_key()


def __le__(self = None, other = None):
    return self.sort_key() <= other.sort_key()


def __gt__(self = None, other = None):
    return self.sort_key() > other.sort_key()


def __ge__(self = None, other = None):
    return self.sort_key() >= other.sort_key()

