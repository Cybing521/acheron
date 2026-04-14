# Source Generated with Decompyle++
# File: tmpb__x4iq2.marshal (Python 3.11)

for handler in self.handlers:
    handler.join()
    self.pipe_thread_finished.set()
    self.pipe_thread.join()
    return None
