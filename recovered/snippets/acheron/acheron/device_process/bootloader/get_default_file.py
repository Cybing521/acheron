# Source Generated with Decompyle++
# File: tmpxqm2_a8d.marshal (Python 3.11)

if not base_dir:
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))

try:
    import firmutil.repo_info as firmutil
    (boardname, boardrev) = device_info.board_info
    repo = firmutil.repo_info.get_repo_from_board(boardname, boardrev)
except ImportError:
    repo = None

if not repo:
    repo = device_info.repo_name
if not repo:
    return ('', '')
file_dir = None.path.abspath(os.path.join(base_dir, f'''{repo}/firmware/build'''))
if not os.path.exists(file_dir):
    return ('', '')
for file_name in None.listdir(file_dir):
    if os.path.splitext(file_name)[1] == '.firmware':
        
        return None, (file_dir, file_name)
    return ('', '')
