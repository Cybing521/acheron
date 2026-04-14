# Source Generated with Decompyle++
# File: tmpfaev9jy_.marshal (Python 3.11)


try:
    self.logger.debug('Requesting %s from url %s', log_type, url)
    response = requests.get(url)
    if not response.ok:
        self.logger.error('Error requesting %s: %s', log_type, response.text)
        self.error.emit(f'''Error requesting {log_type}!''')
        return None
    data = None.json()
    if not data:
        self.logger.error('Empty response for %s request!', log_type)
        self.error.emit(f'''Error requesting {log_type}!''')
        return None
    None.completed.emit(data, self.extra)
    return None
except Exception:
    self.logger.exception('Error requesting %s', log_type)
    self.error.emit(f'''Error requesting {log_type}!''')
    return None

