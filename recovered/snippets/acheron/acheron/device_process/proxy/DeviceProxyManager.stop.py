# Source Generated with Decompyle++
# File: tmp89zcqw2c.marshal (Python 3.11)

for proxy in self.proxies:
    proxy.close_connection()
    for proxy in self.proxies:
        proxy.wait_for_close()
        self.log_listener.stop()
        return None
