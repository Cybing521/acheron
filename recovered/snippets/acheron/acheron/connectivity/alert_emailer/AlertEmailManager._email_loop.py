# Source Generated with Decompyle++
# File: tmpncqqnyff.marshal (Python 3.11)


try:
    logger.debug('Email loop started')
    if self.is_finished.is_set():
        return None
    
    try:
        (alert_tuple, callback) = self.alerts.popleft()
        
        try:
            pass
        except IndexError:
            time.sleep(0.1)
            
            try:
                continue
                
                try:
                    self._do_email(alert_tuple, callback)
                    continue
                except Exception:
                    logger.exception('Uncaught exception in email_loop')
                    self.stop()
                    return None





