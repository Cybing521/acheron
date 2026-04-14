# Source Generated with Decompyle++
# File: tmp1h_fslqh.marshal (Python 3.11)


try:
    (path, name) = os.path.split(filename)
    lockfilename = os.path.join(path, '.' + name + UPLOAD_EXTENSION)
    LockFile(lockfilename)
    file = open(filename, 'rb')
    file.seek(0, os.SEEK_END)
    filelen = file.tell()
    file.seek(0, os.SEEK_SET)
    self._do_upload_s3(file, filelen)
except Exception:
    logger.exception('Error uploading: %s', filename)
    None(None, None)
    
    try:
        None(None, None)
        return None
        None(None, None)
    with None:
        if not None:
            pass


# WARNING: Decompyle incomplete
