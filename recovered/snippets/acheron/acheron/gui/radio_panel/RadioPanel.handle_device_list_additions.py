# Source Generated with Decompyle++
# File: tmp123roevg.marshal (Python 3.11)

updated = False

try:
    (index, list_item) = self.device_list_additions.popleft()
    if not updated:
        updated = True
        self.deviceList.setUpdatesEnabled(False)
    self.deviceList.insertItem(index, list_item)
    continue
except IndexError:
    pass

if updated:
    self.deviceList.setUpdatesEnabled(True)
    return None
