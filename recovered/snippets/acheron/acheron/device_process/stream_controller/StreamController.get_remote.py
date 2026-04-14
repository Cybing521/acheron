# Source Generated with Decompyle++
# File: tmpzq9ajmji.marshal (Python 3.11)

remote_info = RemoteInfo(serial_number, bootloader)
wrapper = RemoteWrapper(self.remote, self, remote_info)
self.remote.set_connect_callback(None)
self.remote.stop_streaming_packets()
self.remote.poll_device(0)
proxy_remote.register_device_cleanup(cast(asphodel.AsphodelNativeDevice, wrapper), self.clean_up_remote)
self.remote_wrapper = wrapper
return wrapper
