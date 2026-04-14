# Source Generated with Decompyle++
# File: tmp4s9pupqa.marshal (Python 3.11)

if self.modbus_server:
    logger.debug('Stopping modbus server')
    self.modbus_server.shutdown()
    self.modbus_server = None
    return None
