# Source Generated with Decompyle++
# File: tmpjq2ouaw4.marshal (Python 3.11)


def __init__(self = None, set_func = None, update_ms = None, parent = (None,)):
    self.set_func = set_func
    self.update_delay = update_ms / 1000
    self.last_set_time = None
    self.next_value = None
    self.timer = QtCore.QTimer(parent)
    self.timer.setSingleShot(True)
    self.timer.timeout.connect(self.timer_cb)


def update(self = None, value = None):
    pass
# WARNING: Decompyle incomplete

timer_cb = (lambda self = None: self.last_set_time = time.monotonic()self.set_func(self.next_value))()
