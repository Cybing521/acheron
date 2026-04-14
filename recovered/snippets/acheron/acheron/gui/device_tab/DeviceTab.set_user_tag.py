# Source Generated with Decompyle++
# File: tmpdmiu186i.marshal (Python 3.11)

if not self.controller.device_info:
    return None
tag_key = None + str(index + 1)
old_str = getattr(self.controller.device_info, tag_key)
(new_str, ok) = QtWidgets.QInputDialog.getText(self, self.tr('New Tag'), self.tr('New Tag:'), QtWidgets.QLineEdit.EchoMode.Normal, old_str)
if not ok:
    return None
new_str = None.strip()
self.controller.set_user_tag(index, new_str)
