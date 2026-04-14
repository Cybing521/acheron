# Source Generated with Decompyle++
# File: tmp2z8u6b6_.marshal (Python 3.11)

path = self.get_save_path()
if path:
    
    try:
        f = open(path, 'wt', encoding = 'utf-8')
        f.write(self.device_info_str)
        f.write('\n')
        
        try:
            None(None, None)
            return None
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            msg = f'''Error writing file {path}.'''
                            logger.exception(msg)
                            QtWidgets.QMessageBox.critical(self, self.tr('Error'), self.tr(msg))
                            return None
                            return None




