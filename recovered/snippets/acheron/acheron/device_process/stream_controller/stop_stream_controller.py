# Source Generated with Decompyle++
# File: tmpmzt75hqb.marshal (Python 3.11)

if device not in instances:
    return None
None[device].stop()
device_logger = proxy_remote.get_device_logger(logger, device)
device_logger.debug('Stopped streaming instance')
del instances[device]
proxy_remote.unregister_device_cleanup(device, stop_stream_controller)
