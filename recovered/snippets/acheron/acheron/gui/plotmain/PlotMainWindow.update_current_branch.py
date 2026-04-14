# Source Generated with Decompyle++
# File: tmpqvhfcojb.marshal (Python 3.11)

branch_name = build_info.get_branch_name()
if not branch_name:
    return None
if None in ('master', 'develop'):
    fallback = None
else:
    fallback = 'develop'
self.find_update(branch = branch_name, fallback_branch = fallback)
