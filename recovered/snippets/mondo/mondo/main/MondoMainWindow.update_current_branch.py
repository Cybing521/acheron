# Source Generated with Decompyle++
# File: tmp03abctu8.marshal (Python 3.11)

if self.branch_name in ('master', 'develop'):
    fallback = None
else:
    fallback = 'develop'
self.find_update(branch = self.branch_name, fallback_branch = fallback)
