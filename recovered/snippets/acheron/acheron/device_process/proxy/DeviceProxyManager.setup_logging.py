# Source Generated with Decompyle++
# File: tmp9ywdmrcl.marshal (Python 3.11)

local_handler = RemoteToLocalLogHandler(__name__ + '.remote')
self.log_queue = multiprocessing.Queue()
self.log_listener = QueueListener(self.log_queue, local_handler)
self.log_listener.start()
