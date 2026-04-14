# Source Generated with Decompyle++
# File: tmp00tkdv1q.marshal (Python 3.11)


def __init__(self = None, lockfilename = None):
    self.lockfilename = lockfilename


def __enter__(self = None):
    self.lockfile = open(self.lockfilename, 'r+', encoding = 'ascii')
    if sys.platform == 'win32':
        msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_NBLCK, 1)
        return None
    None.lockf(self.lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)


def __exit__(self = None, _exc_type = None, _exc_value = None, _traceback = ('_exc_type', Optional[type[BaseException]], '_exc_value', Optional[BaseException], '_traceback', Optional[TracebackType], 'return', None)):
    if sys.platform == 'win32':
        msvcrt.locking(self.lockfile.fileno(), msvcrt.LK_UNLCK, 1)
    else:
        fcntl.lockf(self.lockfile, fcntl.LOCK_UN)
    self.lockfile.close()
    del self.lockfile

