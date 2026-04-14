# Source Generated with Decompyle++
# File: tmpbxkg_o9j.marshal (Python 3.11)

if self.device_list:
    for device in self.device_list:
        device.free()
        self.device_list = None
        if self.lib:
            if self.usb_devices_supported:
                self.lib.asphodel_usb_deinit()
            if self.tcp_devices_supported:
                self.lib.asphodel_tcp_deinit()
            self.lib = None
            return None
        return None
