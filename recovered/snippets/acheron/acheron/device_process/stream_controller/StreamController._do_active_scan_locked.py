# Source Generated with Decompyle++
# File: tmpdbjdxc30.marshal (Python 3.11)


try:
    if not bootloader:
        self.logger.debug('Starting active scan on %s', serial)
        self.device.connect_radio(serial)
    else:
        self.logger.debug('Starting bootloader active scan on %s', serial)
        self.device.connect_radio_boot(serial)
    self.remote.wait_for_connect(1000)
    active_scan = get_active_scan_info(self.remote, self.device_info_logger, self.diskcache)
    self.logger.debug('Finished active scan on %s', serial)
    
    try:
        pass
    except Exception:
        active_scan = None
        self.logger.debug('Failed active scan on %s', serial)
        
        try:
            pass
        try:
            self.device.stop_radio()
        except:
            self.device.stop_radio()

        self.status_pipe_lock
        self.status_pipe.send((StreamStatus.ACTIVE_SCAN_DATA, serial, active_scan))
        None(None, None)
        return None
        with None:
            if not None:
                pass


