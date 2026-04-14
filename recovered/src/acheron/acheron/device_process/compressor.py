# Source Generated with Decompyle++
# File: compressor.pyc (Python 3.11)

from dataclasses import dataclass
from functools import cache
import lzma
import os
import subprocess
import sys
from typing import IO, Optional
import acheron
CompressorArgs = <NODE:12>()
_find = (lambda prog = None, paths = dataclass(): for path in paths:
exe_file = os.path.join(path, prog)if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
None, exe_fileNone)()
_find_7zip = (lambda : if sys.platform == 'win32':
is_64bit = sys.maxsize > 0x100000000if is_64bit:
d = os.path.join(os.path.dirname(acheron.__file__), '7zip_64bit')else:
d = os.path.join(os.path.dirname(acheron.__file__), '7zip_32bit')result = _find('7za.exe', frozenset([
d]))if result:
resultpaths = None.environ['PATH'].split(os.pathsep)if sys.platform == 'win32':
program_files_keys = [
'PROGRAMW6432',
'PROGRAMFILES',
'PROGRAMFILES(X86)']program_files_dirs = []for key in program_files_keys:
path = os.environ[key]if path:
program_files_dirs.append(path)except KeyError:
continuefor program_files in program_files_dirs:
paths.append(os.path.join(program_files, '7-Zip'))progs = [
'7zr.exe',
'7za.exe',
'7z.exe']progs = [
'7zr',
'7za',
'7z']for prog in progs:
result = _find(prog, frozenset(paths))if result:
None, resultNone)()
_find_xz = (lambda : paths = frozenset(os.environ['PATH'].split(os.pathsep))if sys.platform == 'win32':
_find('xz.exe', paths)None('xz', paths))()
get_compressor_args = (lambda compression_level = None: if sys.platform == 'win32':
startupinfo = subprocess.STARTUPINFO()subprocess.SW_HIDE = startupinfo, startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW, .dwFlagspopen_extras = {
'startupinfo': startupinfo,
'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.BELOW_NORMAL_PRIORITY_CLASS }else:
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
)()

def open_compressor(filename = None, compression_level = None):
    compressor_args = get_compressor_args(compression_level)
# WARNING: Decompyle incomplete

