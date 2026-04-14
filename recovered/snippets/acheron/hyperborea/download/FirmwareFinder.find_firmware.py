# Source Generated with Decompyle++
# File: tmpz0qo64l_.marshal (Python 3.11)

keys = []
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
if commit and branch:
    raise ValueError('Cannot specify both commit and branch')
# WARNING: Decompyle incomplete
