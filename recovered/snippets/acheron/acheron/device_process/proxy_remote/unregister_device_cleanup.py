# Source Generated with Decompyle++
# File: tmpuz0fvvh5.marshal (Python 3.11)

cleanup_list = device_cleanup.get(device, None)
if cleanup_list:
    
    try:
        cleanup_list.remove((cleanup_func, args, kwargs))
    except ValueError:
        pass

    if not cleanup_list:
        del device_cleanup[device]
        return None
    return None
    return None
