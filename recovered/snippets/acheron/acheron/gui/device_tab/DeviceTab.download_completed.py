# Source Generated with Decompyle++
# File: tmp_vo1j9kw.marshal (Python 3.11)

self.firmware_progress.reset()
firmware_bytes = file.getvalue()

try:
    firm_data = bootloader.decode_firm_bytes(firmware_bytes)
    
    try:
        pass
    except Exception:
        self.logger.exception('Error decoding downloaded firmware')
        m = self.tr('Error decoding downloaded firmware!')
        QtWidgets.QMessageBox.critical(self, self.tr('Error'), m)
        
        try:
            file.close()
            return None
            
            try:
                file.close()
            except:
                file.close()

            self.firmware_cache.set(url, firmware_bytes)
            self.controller.load_firmware(firm_data, url)
            return None



