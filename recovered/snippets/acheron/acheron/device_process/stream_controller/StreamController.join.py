# Source Generated with Decompyle++
# File: tmpvjx5nnlc.marshal (Python 3.11)

if not self.stop_finished.is_set():
    self.stop()
self.device_lock.release()
self.background_join_thread.join()
self.device_lock.acquire()
