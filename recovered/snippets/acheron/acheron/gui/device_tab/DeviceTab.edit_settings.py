# Source Generated with Decompyle++
# File: tmpestrsrn7.marshal (Python 3.11)

if not self.controller.device_info:
    return None
dialog = None(self.controller.device_info, self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    
    try:
        new_nvm = dialog.get_updated_nvm()
        
        try:
            pass
        except Exception:
            self.logger.exception('Unhandled Exception in edit_settings')
            QtWidgets.QMessageBox.critical(self, self.tr('Error'), self.tr('Error parsing settings!'))
            
            try:
                dialog.deleteLater()
                return None
                
                try:
                    dialog.deleteLater()
                except:
                    dialog.deleteLater()

                self.controller.write_nvm(new_nvm)
                return None




