# Source Generated with Decompyle++
# File: tmpd8fkd4gm.marshal (Python 3.11)

self.update_progress.reset()

try:
    file.seek(0)
    firmware_bytes = file.read()
    
    try:
        pass
    except Exception:
        firmware_bytes = None
        
        try:
            pass
        try:
            file.close()
        except:
            file.close()

        if firmware_bytes:
            self.firmware_cache.set(url, firmware_bytes)


QtWidgets.QMessageBox.information(self, self.tr('Finished'), self.tr('Finished download'))
