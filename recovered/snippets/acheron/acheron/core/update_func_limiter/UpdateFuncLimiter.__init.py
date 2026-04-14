# Source Generated with Decompyle++
# File: tmppmbinvho.marshal (Python 3.11)

self.set_func = set_func
self.update_delay = update_ms / 1000
self.last_set_time = None
self.next_value = None
self.timer = QtCore.QTimer(parent)
self.timer.setSingleShot(True)
self.timer.timeout.connect(self.timer_cb)
