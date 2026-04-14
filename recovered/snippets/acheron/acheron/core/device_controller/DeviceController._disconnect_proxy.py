# Source Generated with Decompyle++
# File: tmpvuvlvgy1.marshal (Python 3.11)

if self.proxy:
    self.proxy.send_job(self.close_device_op)
    self.proxy.close_connection()
    self.dispatcher.register_old_proxy(self.proxy)
    self.proxy = None
    self.proxy_finished.set()
    return None
