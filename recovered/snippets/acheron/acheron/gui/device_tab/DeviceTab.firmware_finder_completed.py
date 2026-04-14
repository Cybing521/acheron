# Source Generated with Decompyle++
# File: tmpwduxpd2q.marshal (Python 3.11)

self.firmware_progress.reset()
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
firmware_bytes = cast(Optional[bytes], self.firmware_cache.get(url, None))
if firmware_bytes:
    self.logger.info('Using cached firmware from %s', url)
    
    try:
        firm_data = bootloader.decode_firm_bytes(firmware_bytes)
    except Exception:
        self.logger.exception('Error decoding cached firmware. Removing from cache.')
        self.firmware_cache.delete(url)
        firm_data = None

    if firm_data:
        self.controller.load_firmware(firm_data, url)
        return None
    None.logger.info('Downloading firmware from %s', url)
    self.firmware_progress.setMinimum(0)
    self.firmware_progress.setMaximum(0)
    self.firmware_progress.setValue(0)
    self.firmware_progress.setLabelText(self.tr('Downloading firmware...'))
    self.firmware_progress.forceShow()
    file = io.BytesIO()
    self.downloader.start_download(url, file)
    return None
