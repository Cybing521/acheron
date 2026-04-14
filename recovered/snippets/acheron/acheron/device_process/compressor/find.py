# Source Generated with Decompyle++
# File: tmp2e92bvwu.marshal (Python 3.11)

for path in paths:
    exe_file = os.path.join(path, prog)
    if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
        
        return None, exe_file
    return None
