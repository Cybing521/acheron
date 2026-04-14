# Source Generated with Decompyle++
# File: tmpbrqwrkg_.marshal (Python 3.11)


try:
    modbus_server = cast(ModbusTcpServer, self.modbus_server)
    self.modbus_started.set()
    modbus_server.serve_forever()
    return None
except Exception:
    logger.exception('Uncaught exception in _thread_run')
    self._stop_modbus()
    return None

