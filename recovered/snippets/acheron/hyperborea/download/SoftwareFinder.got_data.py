# Source Generated with Decompyle++
# File: tmprpkcs75q.marshal (Python 3.11)


try:
    if 'url' not in values:
        self.logger.error('Empty response to findsoftware!')
        self.error.emit('Error requesting software information!')
        return None
    url = None['url']
    commit = values.get('commit', None)
    state = values.get('state', 'SUCCESSFUL')
    ready = state == 'SUCCESSFUL'
    self.completed.emit((url, commit, ready))
    return None
except Exception:
    self.logger.exception('Error finding software')
    self.error.emit('Unknown error finding software!')
    return None

