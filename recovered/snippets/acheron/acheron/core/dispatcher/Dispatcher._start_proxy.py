# Source Generated with Decompyle++
# File: tmpltjpa9s3.marshal (Python 3.11)

connected = functools.partial(self._proxy_connected, weakref.ref(proxy), weakref.ref(controller))
proxy.connected.connect(connected)
disconnected = functools.partial(self._proxy_disconnected, weakref.ref(proxy), weakref.ref(controller))
proxy.disconnected.connect(disconnected)
self.opening_proxies.add(proxy)
