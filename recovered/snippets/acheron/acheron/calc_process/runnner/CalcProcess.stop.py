# Source Generated with Decompyle++
# File: tmpy6mpwbg2.marshal (Python 3.11)

self.lock
if not self.stopped.is_set():
    self.stopped.set()
    self.calc_ctrl_tx_pipe.send((CalcControl.STOP,))
    self.logger.debug('Calc process stopping')
None(None, None)
return None
with None:
    if not None:
        pass
