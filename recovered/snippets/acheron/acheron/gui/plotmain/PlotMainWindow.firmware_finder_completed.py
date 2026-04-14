# Source Generated with Decompyle++
# File: tmpi6cb5j0j.marshal (Python 3.11)

self.update_progress.reset()
build_types = sorted(build_urls.keys())
if 'firmware' in build_types:
    build_types.remove('firmware')
    build_types.insert(0, 'firmware')
if len(build_types) == 1:
    build_type = build_types[0]
else:
    (value, ok) = QtWidgets.QInputDialog.getItem(self, self.tr('Select Build Type'), self.tr('Select Build Type'), build_types, 0, editable = False)
    if not ok:
        return None
    build_type = None
url = build_urls[build_type]
u = urllib.parse.urlparse(url)
default_filename = os.path.basename(u.path)
filename = self.get_firmware_save_file(default_filename)
if not filename:
    return None
firmware_bytes = None.firmware_cache.get(url, None)
if firmware_bytes and isinstance(firmware_bytes, bytes):
    logger.info('Using cached firmware from %s', url)
    f = open(filename, 'wb')
    f.write(firmware_bytes)
    None(None, None)
    return None
with None:
    if not None:
        pass
return None
logger.info('Downloading firmware from %s', url)
self.update_progress.setMinimum(0)
self.update_progress.setMaximum(0)
self.update_progress.setValue(0)
self.update_progress.setLabelText(self.tr('Downloading firmware...'))
self.update_progress.forceShow()
file = open(filename, 'w+b')
self.firmware_downloader.start_download(url, file)
