# Source Generated with Decompyle++
# File: tmpsots3_ua.marshal (Python 3.11)


def __init__(self = None, fmt = None, fallback = None):
    self.fmt = fmt
    self.fallback = fallback


def filter(self = None, record = None):
    
    try:
        record.optdevice = self.fmt % record.proxy_string
    except AttributeError:
        record.optdevice = self.fallback

    return True

