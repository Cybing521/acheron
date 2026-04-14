# Source Generated with Decompyle++
# File: tmplcog4m8_.marshal (Python 3.11)

if self.controller.device_info:
    dialog = DeviceInfoDialog(self.controller.device_info, self)
    
    try:
        dialog.exec()
        dialog.deleteLater()
        return None
    except:
        dialog.deleteLater()
        return None

