# Source Generated with Decompyle++
# File: tmpgyjsqbhz.marshal (Python 3.11)

instance = instance_weakref()
if instance:
    device_logger.debug('Waiting for streaming instance to finish')
    instance.join()
    device_logger.debug('Finished streaming instance')
else:
    device_logger.debug('Streaming instance already garbage collected')
proxy_remote.unregister_device_cleanup(device, join_streaming, instance_weakref, device_logger)
