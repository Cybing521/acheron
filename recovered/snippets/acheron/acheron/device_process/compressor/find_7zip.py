# Source Generated with Decompyle++
# File: tmp3xnbsv1o.marshal (Python 3.11)

if sys.platform == 'win32':
    is_64bit = sys.maxsize > 0x100000000
    if is_64bit:
        d = os.path.join(os.path.dirname(acheron.__file__), '7zip_64bit')
    else:
        d = os.path.join(os.path.dirname(acheron.__file__), '7zip_32bit')
    result = _find('7za.exe', frozenset([
        d]))
    if result:
        return result
    paths = None.environ['PATH'].split(os.pathsep)
    if sys.platform == 'win32':
        program_files_keys = [
            'PROGRAMW6432',
            'PROGRAMFILES',
            'PROGRAMFILES(X86)']
        program_files_dirs = []
        for key in program_files_keys:
            path = os.environ[key]
            if path:
                program_files_dirs.append(path)
            except KeyError:
                continue
            for program_files in program_files_dirs:
                paths.append(os.path.join(program_files, '7-Zip'))
                progs = [
                    '7zr.exe',
                    '7za.exe',
                    '7z.exe']
            progs = [
                '7zr',
                '7za',
                '7z']
            for prog in progs:
                result = _find(prog, frozenset(paths))
                if result:
                    
                    return None, result
                return None
