# Source Generated with Decompyle++
# File: tmps5_s4g9c.marshal (Python 3.11)

self.preferences = preferences
self.event_queue = queue.Queue()
self.is_finished = threading.Event()
self.upload_thread = threading.Thread(target = self._upload_loop)
self.upload_thread.start()
