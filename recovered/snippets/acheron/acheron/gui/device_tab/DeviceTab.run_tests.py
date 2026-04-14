# Source Generated with Decompyle++
# File: tmpmpr_u8hf.marshal (Python 3.11)

if self.controller.device_info:
    dialog = HardwareTestDialog(self.controller.device_info, self.controller, self.preferences, self.logger, self)
    
    try:
        dialog.start_tests()
        dialog.exec()
        dialog.deleteLater()
        return None
    except:
        dialog.deleteLater()
        return None

