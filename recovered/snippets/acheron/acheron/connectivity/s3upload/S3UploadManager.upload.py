# Source Generated with Decompyle++
# File: tmpwaf7bfh7.marshal (Python 3.11)

if filename not in self.upload_order:
    logger.debug('File ready for upload: %s', filename)
    self.upload_order.append(filename)
    return None
