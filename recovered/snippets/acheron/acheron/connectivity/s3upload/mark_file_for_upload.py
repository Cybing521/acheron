# Source Generated with Decompyle++
# File: tmp40et2g08.marshal (Python 3.11)

(root, name) = os.path.split(apd_filename)
upload_filename = os.path.join(root, '.' + name + UPLOAD_EXTENSION)
if not os.path.exists(upload_filename):
    upload_file = open(upload_filename, 'w', encoding = 'ascii')
    upload_file.close()
    if sys.platform == 'win32':
        ctypes.windll.kernel32.SetFileAttributesW(upload_filename, 2)
        return None
    return None
