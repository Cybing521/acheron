# Source Generated with Decompyle++
# File: tmpnc93i0es.marshal (Python 3.11)

self.logger.info('Starting disconnect from %s', serial_number)
self._stop_subcontroller_locked(serial_number)
self.device.stop_radio()
self.status_pipe_lock
self.status_pipe.send((StreamStatus.REMOTE_DISCONNECTED,))
None(None, None)
return None
with None:
    if not None:
        pass
