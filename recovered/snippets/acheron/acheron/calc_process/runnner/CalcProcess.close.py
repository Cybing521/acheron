# Source Generated with Decompyle++
# File: tmp0dpbcr9b.marshal (Python 3.11)

self.stop()
self.lock
if self.closed.is_set():
    None(None, None)
    return None
None.calc_ctrl_tx_pipe.send((CalcControl.CLOSE,))
self.finished.set()
if self.log_listener:
    self.log_listener.stop()
    self.log_listener = None
    self.log_queue.close()
    self.log_queue = None
self.closed.set()
self.logger.debug('Calc process closed')
None(None, None)
return None
with None:
    if not None:
        pass
