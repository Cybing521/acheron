# Source Generated with Decompyle++
# File: tmp1p4tev9e.marshal (Python 3.11)

if sys.platform == 'win32':
    startupinfo = subprocess.STARTUPINFO()
    subprocess.SW_HIDE = startupinfo, startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW, .dwFlags
    popen_extras = {
        'startupinfo': startupinfo,
        'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.BELOW_NORMAL_PRIORITY_CLASS }
else:
    popen_extras = {
        'preexec_fn': (lambda : os.nice(10)) }
compressor_path = _find_7zip()
if compressor_path:
    return CompressorArgs(args = [
        compressor_path,
        'a',
        '-si',
        '-txz',
        '-m0=lzma2',
        '-mx={}'.format(compression_level)], uses_stdout = False, popen_extras = popen_extras)
compressor_path = None()
if compressor_path:
    return CompressorArgs(args = [
        compressor_path,
        '-z',
        '-{}'.format(compression_level)], uses_stdout = True, popen_extras = popen_extras)
return None(args = None, uses_stdout = False, popen_extras = popen_extras)
