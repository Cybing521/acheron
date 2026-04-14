# Source Generated with Decompyle++
# File: tmp3yxeqd8p.marshal (Python 3.11)

base_url = 'https://api.suprocktech.com/software/findsoftware'
keys = [
    'repo={}'.format(repo),
    'key={}'.format(build_key)]
if commit:
    keys.append('hash={}'.format(commit))
if branch:
    keys.append('branch={}'.format(branch))
url = base_url + '?' + '&'.join(keys)
self.fetcher = _Fetcher(self.logger)
self.fetcher.error.connect(self.error)
self.fetcher.completed.connect(self.got_data)
self.fetcher.start(url, 'findsoftware')
