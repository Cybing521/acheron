# Source Generated with Decompyle++
# File: tmpon2o9txw.marshal (Python 3.11)

it = os.scandir(fault_dir)
for entry in it:
    if entry.name.endswith('.log') and entry.is_file():
        stat = entry.stat()
        if stat.st_size == 0:
            filename = os.path.join(fault_dir, entry.name)
            os.unlink(filename)
            continue
            except OSError:
                continue
    None(None, None)
    return None
    with None:
        if not None:
            pass
