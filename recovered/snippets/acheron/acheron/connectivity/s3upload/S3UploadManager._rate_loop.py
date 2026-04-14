# Source Generated with Decompyle++
# File: tmppc9sj2ii.marshal (Python 3.11)


try:
    if self.is_finished.wait(self.rate_update_interval):
        return None
    if None.uploading:
        self.rate_status.emit(True, self._get_rate())
    continue
except Exception:
    logger.exception('Uncaught exception in rate_loop')
    self.stop()
    self.error.emit()
    return None

