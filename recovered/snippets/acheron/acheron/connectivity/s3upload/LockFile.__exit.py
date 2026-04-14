# Source Generated with Decompyle++
# File: tmp7551dtt3.marshal (Python 3.11)

if sys.platform == 'win32':
    msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_UNLCK, 1)
else:
    fcntl.lockf(self.lockfile, fcntl.LOCK_UN)
self.lockfile.close()
del self.lockfile
