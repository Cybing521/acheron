# Source Generated with Decompyle++
# File: tmp0zngvbrp.marshal (Python 3.11)

now = time.time()
found = []
for root, _dirs, files in os.walk(self.base_dir):
    for name in files:
        if name.endswith(UPLOAD_EXTENSION):
            uploadfilename = os.path.join(root, name)
            if name.startswith('.'):
                name = name[1:]
            filename = os.path.join(root, name[:-len(UPLOAD_EXTENSION)])
            if filename not in self.upload_order:
                mtime = os.path.getmtime(filename)
                if os.path.getsize(uploadfilename) == 0:
                    found.append((mtime, filename))
                elif mtime + self.scan_ignore_newer < now:
                    found.append((mtime, filename))
                elif now + self.scan_ignore_newer < mtime:
                    logger.warning('File mtime in future: %s', filename)
                else:
                    logger.debug('File not ready: %s', filename)
                continue
                except FileNotFoundError:
                    continue
        for _mtime, filename in sorted(found):
            logger.debug('Directory scan found %s', filename)
            self.upload_order.append(filename)
            return None
