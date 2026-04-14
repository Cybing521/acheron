# Source Generated with Decompyle++
# File: tmp5i2oqs4v.marshal (Python 3.11)

if self.proxy:
    self._error(self.tr('Reconnecting'))
self.proxy = proxy
self.proxy_finished.clear()
self.proxy.disconnected.connect(functools.partial(self._proxy_disconnect_cb, weakref.ref(proxy)))
self._start_stream_controller()
