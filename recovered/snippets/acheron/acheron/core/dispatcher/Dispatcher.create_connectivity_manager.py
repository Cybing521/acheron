# Source Generated with Decompyle++
# File: tmp24oyk5qf.marshal (Python 3.11)

self.connectivity_manager = ConnectivityManager(self.preferences)
self.connectivity_manager.add_handler(SocketHandler(self.preferences))
self.connectivity_manager.add_handler(ModbusHandler(self.preferences))
