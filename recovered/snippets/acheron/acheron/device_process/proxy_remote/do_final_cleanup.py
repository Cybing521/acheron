# Source Generated with Decompyle++
# File: tmp3c39u41q.marshal (Python 3.11)

subproxy_devices = set(device_cleanup.keys())
subproxy_devices.discard(device)
subproxy_devices.discard(None)
for subproxy_device in subproxy_devices:
    do_device_cleanup(subproxy_device)
    do_device_cleanup(device)
    do_device_cleanup(None)
    return None
