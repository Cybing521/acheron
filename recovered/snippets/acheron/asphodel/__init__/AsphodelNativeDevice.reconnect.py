# Source Generated with Decompyle++
# File: tmp4uv77f3a.marshal (Python 3.11)

if bootloader and application:
    raise ValueError('cannot set both application and bootloader')
if bootloader:
    reconnect_func = self.reconnect_device_bootloader
elif application:
    reconnect_func = self.reconnect_device_application
else:
    reconnect_func = self.reconnect_device
if not serial_number:
    
    try:
        serial_number = self.get_serial_number()
    except AsphodelError:
        pass

    end_time = time.monotonic() + self.reconnect_time
    time.sleep(0.5)
    
    try:
        reconnect_func(reopen = True)
    except AsphodelError:
        if time.monotonic() >= end_time:
            raise 

    if serial_number:
        device = find_device_by_serial(serial_number)
        if device:
            time.sleep(0.5)
            
            try:
                reconnect_func(reopen = True)
            except AsphodelError:
                pass

            time.sleep(0.5)
            
            try:
                reconnect_func(reopen = True)
            except AsphodelError:
                pass

            native_device = device.device
            device.device = None
            self._reconnect_helper(native_device, reopen = True)
        else:
            time.sleep(0.25)
        self.wait_for_connect(int(self.reconnect_time * 1000))
        return None
