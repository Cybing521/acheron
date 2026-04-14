# Source Generated with Decompyle++
# File: tmpl5viehw2.marshal (Python 3.11)

device_logger = proxy_remote.get_device_logger(logger, device)
device_logger.debug('Starting streaming instance')
if device in instances:
    stop_stream_controller(device)
device_lock = proxy_remote.device_lock
# WARNING: Decompyle incomplete
