# Source Generated with Decompyle++
# File: tmptgpgeog8.marshal (Python 3.11)

if not self.controller.device_info:
    return None
dialog = None(self.controller.device_info.streams, self.controller.device_info.channels, self.controller.active_streams, self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    stream_list = None.get_new_stream_list()
    dialog.deleteLater()
except:
    dialog.deleteLater()

self.controller.set_active_streams(stream_list)
