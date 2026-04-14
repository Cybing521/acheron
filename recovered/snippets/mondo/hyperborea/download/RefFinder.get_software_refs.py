# Source Generated with Decompyle++
# File: tmpnwei8m3z.marshal (Python 3.11)

base_url = 'https://api.suprocktech.com/software/findsoftware'
keys = [
    'repo={}'.format(repo),
    'listrefs=1']
url = base_url + '?' + '&'.join(keys)
self.fetcher.start(url, 'listrefs')
