# Source Generated with Decompyle++
# File: tmpvv0o29mh.marshal (Python 3.11)

keys = [
    'listrefs=1']
if board_info:
    if repo:
        raise ValueError('Cannot specify both board_info and repo')
    (board_name, board_rev) = board_info
    keys.append('boardname={}'.format(urllib.parse.quote(board_name)))
    keys.append('boardrev={}'.format(board_rev))
elif repo:
    keys.append('repo={}'.format(urllib.parse.quote(repo)))
else:
    raise ValueError('Must specify one of board_info or repo')
base_url = 'https://api.suprocktech.com/firmwareinfo/findfirmware'
url = base_url + '?' + '&'.join(keys)
self.fetcher.start(url, 'listrefs')
