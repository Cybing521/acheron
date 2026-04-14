# Source Generated with Decompyle++
# File: tmpcecnvrc7.marshal (Python 3.11)


try:
    if self.is_finished.wait(self.scan_interval):
        return None
    None.upload_lock
    self._scan_dir()
    
    try:
        None(None, None)
    with None:
        if not None:
            
            try:
                
                try:
                    continue
                except Exception:
                    logger.exception('Uncaught exception in scan_loop')
                    self.stop()
                    self.error.emit()
                    return None




