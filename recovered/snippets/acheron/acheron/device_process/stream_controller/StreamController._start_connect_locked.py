# Source Generated with Decompyle++
# File: tmppq8qjmo8.marshal (Python 3.11)

if not remote_info.bootloader:
    self.logger.info('Starting connect to %s', remote_info.serial_number)
    self.device.connect_radio(remote_info.serial_number)
else:
    self.logger.info('Starting bootloader connect to %s', remote_info.serial_number)
    self.device.connect_radio_boot(remote_info.serial_number)
self.status_pipe_lock
self.status_pipe.send((StreamStatus.REMOTE_CONNECTING, remote_info.serial_number, remote_info.bootloader))
None(None, None)
return None
with None:
    if not None:
        pass
