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
# INVALID FROM DECOMPILER: CompressorArgs = <NODE:12>()
# INVALID FROM DECOMPILER: _find = (lambda prog = None, paths = dataclass(): for path in paths:
# INVALID FROM DECOMPILER: exe_file = os.path.join(path, prog)if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
# INVALID FROM DECOMPILER: None, exe_fileNone)()
# INVALID FROM DECOMPILER: _find_7zip = (lambda : if sys.platform == 'win32':
# INVALID FROM DECOMPILER: is_64bit = sys.maxsize > 0x100000000if is_64bit:
# INVALID FROM DECOMPILER: d = os.path.join(os.path.dirname(acheron.__file__), '7zip_64bit')else:
# INVALID FROM DECOMPILER: d = os.path.join(os.path.dirname(acheron.__file__), '7zip_32bit')result = _find('7za.exe', frozenset([
# INVALID FROM DECOMPILER: d]))if result:
# INVALID FROM DECOMPILER: resultpaths = None.environ['PATH'].split(os.pathsep)if sys.platform == 'win32':
# INVALID FROM DECOMPILER: program_files_keys = [
'PROGRAMW6432',
'PROGRAMFILES',
# INVALID FROM DECOMPILER: 'PROGRAMFILES(X86)']program_files_dirs = []for key in program_files_keys:
# INVALID FROM DECOMPILER: path = os.environ[key]if path:
# INVALID FROM DECOMPILER: program_files_dirs.append(path)except KeyError:
# INVALID FROM DECOMPILER: continuefor program_files in program_files_dirs:
# INVALID FROM DECOMPILER: paths.append(os.path.join(program_files, '7-Zip'))progs = [
'7zr.exe',
'7za.exe',
# INVALID FROM DECOMPILER: '7z.exe']progs = [
'7zr',
'7za',
# INVALID FROM DECOMPILER: '7z']for prog in progs:
# INVALID FROM DECOMPILER: result = _find(prog, frozenset(paths))if result:
# INVALID FROM DECOMPILER: None, resultNone)()
# INVALID FROM DECOMPILER: _find_xz = (lambda : paths = frozenset(os.environ['PATH'].split(os.pathsep))if sys.platform == 'win32':
# INVALID FROM DECOMPILER: _find('xz.exe', paths)None('xz', paths))()
# INVALID FROM DECOMPILER: get_compressor_args = (lambda compression_level = None: if sys.platform == 'win32':
# INVALID FROM DECOMPILER: startupinfo = subprocess.STARTUPINFO()subprocess.SW_HIDE = startupinfo, startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW, .dwFlagspopen_extras = {
# INVALID FROM DECOMPILER: 'startupinfo': startupinfo,
# INVALID FROM DECOMPILER: 'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.BELOW_NORMAL_PRIORITY_CLASS }else:
# INVALID FROM DECOMPILER: popen_extras = {
# INVALID FROM DECOMPILER: 'preexec_fn': (lambda : os.nice(10)) }
# INVALID FROM DECOMPILER:     compressor_path = _find_7zip()
# INVALID FROM DECOMPILER:     if compressor_path:
# INVALID FROM DECOMPILER:         return CompressorArgs(args = [
# INVALID FROM DECOMPILER:             compressor_path,
# INVALID FROM DECOMPILER:             'a',
# INVALID FROM DECOMPILER:             '-si',
# INVALID FROM DECOMPILER:             '-txz',
# INVALID FROM DECOMPILER:             '-m0=lzma2',
# INVALID FROM DECOMPILER:             '-mx={}'.format(compression_level)], uses_stdout = False, popen_extras = popen_extras)
# INVALID FROM DECOMPILER:     compressor_path = None()
# INVALID FROM DECOMPILER:     if compressor_path:
# INVALID FROM DECOMPILER:         return CompressorArgs(args = [
# INVALID FROM DECOMPILER:             compressor_path,
# INVALID FROM DECOMPILER:             '-z',
# INVALID FROM DECOMPILER:             '-{}'.format(compression_level)], uses_stdout = True, popen_extras = popen_extras)
# INVALID FROM DECOMPILER:     return None(args = None, uses_stdout = False, popen_extras = popen_extras)
# INVALID FROM DECOMPILER: )()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class CompressorArgs:

    uses_stdout: bool

    popen_extras: dict

def _find(prog, paths):
    for path in paths:
        exe_file = os.path.join(path, prog)
        if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            
            return None, exe_file
        return None

def _find_7zip():
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL sys
    #   14 LOAD_ATTR platform
    #   24 LOAD_CONST 'win32'
    #   26 COMPARE_OP ==
    #   32 POP_JUMP_FORWARD_IF_FALSE to 424
    #   34 LOAD_GLOBAL sys
    #   46 LOAD_ATTR maxsize
    #   56 LOAD_CONST 4294967296
    #   58 COMPARE_OP >
    #   64 STORE_FAST is_64bit
    #   66 LOAD_FAST is_64bit
    #   68 POP_JUMP_FORWARD_IF_FALSE to 214
    #   70 LOAD_GLOBAL os
    #   82 LOAD_ATTR path
    #   92 LOAD_METHOD join
    #  114 LOAD_GLOBAL os
    #  126 LOAD_ATTR path
    #  136 LOAD_METHOD dirname
    #  158 LOAD_GLOBAL acheron
    #  170 LOAD_ATTR __file__
    #  180 PRECALL
    #  184 CALL
    #  194 LOAD_CONST '7zip_64bit'
    #  196 PRECALL
    #  200 CALL
    #  210 STORE_FAST d
    #  212 JUMP_FORWARD to 356
    #  214 LOAD_GLOBAL os
    #  226 LOAD_ATTR path
    #  236 LOAD_METHOD join
    #  258 LOAD_GLOBAL os
    #  270 LOAD_ATTR path
    #  280 LOAD_METHOD dirname
    #  302 LOAD_GLOBAL acheron
    #  314 LOAD_ATTR __file__
    #  324 PRECALL
    #  328 CALL
    #  338 LOAD_CONST '7zip_32bit'
    #  340 PRECALL
    #  344 CALL
    #  354 STORE_FAST d
    #  356 LOAD_GLOBAL NULL + _find
    #  368 LOAD_CONST '7za.exe'
    #  370 LOAD_GLOBAL NULL + frozenset
    #  382 LOAD_FAST d
    #  384 BUILD_LIST
    #  386 PRECALL
    #  390 CALL
    #  400 PRECALL
    #  404 CALL
    #  414 STORE_FAST result
    #  416 LOAD_FAST result
    #  418 POP_JUMP_FORWARD_IF_FALSE to 424
    #  420 LOAD_FAST result
    #  422 RETURN_VALUE
    #  424 LOAD_GLOBAL os
    #  436 LOAD_ATTR environ
    #  446 LOAD_CONST 'PATH'
    #  448 BINARY_SUBSCR
    #  458 LOAD_METHOD split
    #  480 LOAD_GLOBAL os
    #  492 LOAD_ATTR pathsep
    #  502 PRECALL
    #  506 CALL
    #  516 STORE_FAST paths
    #  518 LOAD_GLOBAL sys
    #  530 LOAD_ATTR platform
    #  540 LOAD_CONST 'win32'
    #  542 COMPARE_OP ==
    #  548 POP_JUMP_FORWARD_IF_FALSE to 810
    #  550 BUILD_LIST
    #  552 LOAD_CONST ('PROGRAMW6432', 'PROGRAMFILES', 'PROGRAMFILES(X86)')
    #  554 LIST_EXTEND
    #  556 STORE_FAST program_files_keys
    #  558 BUILD_LIST
    #  560 STORE_FAST program_files_dirs
    #  562 LOAD_FAST program_files_keys
    #  564 GET_ITER
    #  566 FOR_ITER to 688
    # ... bytecode truncated ...
    pass

def _find_xz():
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + frozenset
    #   14 LOAD_GLOBAL os
    #   26 LOAD_ATTR environ
    #   36 LOAD_CONST 'PATH'
    #   38 BINARY_SUBSCR
    #   48 LOAD_METHOD split
    #   70 LOAD_GLOBAL os
    #   82 LOAD_ATTR pathsep
    #   92 PRECALL
    #   96 CALL
    #  106 PRECALL
    #  110 CALL
    #  120 STORE_FAST paths
    #  122 LOAD_GLOBAL sys
    #  134 LOAD_ATTR platform
    #  144 LOAD_CONST 'win32'
    #  146 COMPARE_OP ==
    #  152 POP_JUMP_FORWARD_IF_FALSE to 186
    #  154 LOAD_GLOBAL NULL + _find
    #  166 LOAD_CONST 'xz.exe'
    #  168 LOAD_FAST paths
    #  170 PRECALL
    #  174 CALL
    #  184 RETURN_VALUE
    #  186 LOAD_GLOBAL NULL + _find
    #  198 LOAD_CONST 'xz'
    #  200 LOAD_FAST paths
    #  202 PRECALL
    #  206 CALL
    #  216 RETURN_VALUE
    pass

def get_compressor_args(compression_level):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL sys
    #   14 LOAD_ATTR platform
    #   24 LOAD_CONST 'win32'
    #   26 COMPARE_OP ==
    #   32 POP_JUMP_FORWARD_IF_FALSE to 216
    #   34 LOAD_GLOBAL NULL + subprocess
    #   46 LOAD_ATTR STARTUPINFO
    #   56 PRECALL
    #   60 CALL
    #   70 STORE_FAST startupinfo
    #   72 LOAD_FAST startupinfo
    #   74 COPY
    #   76 LOAD_ATTR dwFlags
    #   86 LOAD_GLOBAL subprocess
    #   98 LOAD_ATTR STARTF_USESHOWWINDOW
    #  108 BINARY_OP |=
    #  112 SWAP
    #  114 STORE_ATTR dwFlags
    #  124 LOAD_GLOBAL subprocess
    #  136 LOAD_ATTR SW_HIDE
    #  146 LOAD_FAST startupinfo
    #  148 STORE_ATTR wShowWindow
    #  158 LOAD_FAST startupinfo
    #  160 LOAD_GLOBAL subprocess
    #  172 LOAD_ATTR CREATE_NEW_PROCESS_GROUP
    #  182 LOAD_GLOBAL subprocess
    #  194 LOAD_ATTR BELOW_NORMAL_PRIORITY_CLASS
    #  204 BINARY_OP |
    #  208 LOAD_CONST ('startupinfo', 'creationflags')
    #  210 BUILD_CONST_KEY_MAP
    #  212 STORE_FAST popen_extras
    #  214 JUMP_FORWARD to 226
    #  216 LOAD_CONST 'preexec_fn'
    #  218 LOAD_CONST <code object <lambda> at 0x105abfe10, file "acheron\device_process\compressor.py", line 94>
    #  220 MAKE_FUNCTION
    #  222 BUILD_MAP
    #  224 STORE_FAST popen_extras
    #  226 LOAD_GLOBAL NULL + _find_7zip
    #  238 PRECALL
    #  242 CALL
    #  252 STORE_FAST compressor_path
    #  254 LOAD_FAST compressor_path
    #  256 POP_JUMP_FORWARD_IF_FALSE to 344
    #  258 LOAD_GLOBAL NULL + CompressorArgs
    #  270 LOAD_FAST compressor_path
    #  272 LOAD_CONST 'a'
    #  274 LOAD_CONST '-si'
    #  276 LOAD_CONST '-txz'
    #  278 LOAD_CONST '-m0=lzma2'
    #  280 LOAD_CONST '-mx={}'
    #  282 LOAD_METHOD format
    #  304 LOAD_FAST compression_level
    #  306 PRECALL
    #  310 CALL
    #  320 BUILD_LIST
    #  322 LOAD_CONST False
    #  324 LOAD_FAST popen_extras
    #  326 KW_NAMES
    #  328 PRECALL
    #  332 CALL
    #  342 RETURN_VALUE
    #  344 LOAD_GLOBAL NULL + _find_xz
    #  356 PRECALL
    #  360 CALL
    #  370 STORE_FAST compressor_path
    #  372 LOAD_FAST compressor_path
    #  374 POP_JUMP_FORWARD_IF_FALSE to 456
    #  376 LOAD_GLOBAL NULL + CompressorArgs
    #  388 LOAD_FAST compressor_path
    #  390 LOAD_CONST '-z'
    #  392 LOAD_CONST '-{}'
    #  394 LOAD_METHOD format
    #  416 LOAD_FAST compression_level
    #  418 PRECALL
    #  422 CALL
    #  432 BUILD_LIST
    #  434 LOAD_CONST True
    #  436 LOAD_FAST popen_extras
    #  438 KW_NAMES
    # ... bytecode truncated ...
    pass

def open_compressor(filename, compression_level):
    compressor_args = get_compressor_args(compression_level)
