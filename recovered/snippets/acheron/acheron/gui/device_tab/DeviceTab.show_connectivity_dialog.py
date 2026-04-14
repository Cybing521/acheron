# Source Generated with Decompyle++
# File: tmpjvx5edfw.marshal (Python 3.11)

if not self.controller.device_info:
    return None
dialog = None(self.controller.serial_number, self.controller.device_info, self.controller.channel_info, self.controller.device_prefs, self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    dialog.deleteLater()
except:
    dialog.deleteLater()

self.update_preferences()
self.controller.update_preferences()
self.controller.start_connectivity()
