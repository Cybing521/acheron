# Source Generated with Decompyle++
# File: tmp0lcl7qh2.marshal (Python 3.11)

self.preferences = preferences
self.stopped = False
self.pipe_lock = threading.Lock()
self.all_pipes = set()
self.pipe_callbacks = { }
self.device_pipes = { }
self.pipe_thread_finished = threading.Event()
self.pipe_thread = threading.Thread(target = self._pipe_loop)
self.pipe_thread.start()
self.handlers = []
