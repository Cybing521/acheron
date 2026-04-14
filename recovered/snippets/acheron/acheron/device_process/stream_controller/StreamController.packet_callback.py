# Source Generated with Decompyle++
# File: tmpeg_2y6xi.marshal (Python 3.11)

if status == -7:
    if not self.disconnected.is_set():
        self.disconnected.set()
        self.ctrl_queue.put((StreamControl._WAKEUP,))
        self.status_pipe_lock
        self.status_pipe.send((StreamStatus.STREAMING_ERROR_TIMEOUT,))
        None(None, None)
        return None
    with None:
        if not None:
            pass
    return None
    return None
if status != 0:
    if not self.disconnected.is_set():
        self.disconnected.set()
        self.ctrl_queue.put((StreamControl._WAKEUP,))
        self.status_pipe_lock
        self.status_pipe.send((StreamStatus.STREAMING_ERROR_OTHER, status))
        None(None, None)
        return None
    with None:
        if not None:
            pass
    return None
    return None
# WARNING: Decompyle incomplete
