# Source Generated with Decompyle++
# File: tmptuzgyux3.marshal (Python 3.11)

self.lockfile = open(self.lockfilename, 'r+', encoding = 'ascii')
if sys.platform == 'win32':
    msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_NBLCK, 1)
    return None
None.lockf(self.lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
