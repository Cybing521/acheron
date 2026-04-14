# Source Generated with Decompyle++
# File: tmpvfrtwwn3.marshal (Python 3.11)

if not self.controller.device_info:
    return None
current_length = None(self.controller.device_info.nvm)
apd_dir = self.preferences.base_dir
caption = self.tr('Open Data File')
file_filter = self.tr('Data Files (*.apd);;All Files (*.*)')
val = QtWidgets.QFileDialog.getOpenFileName(self, caption, apd_dir, file_filter)
filename = val[0]
if filename == '':
    return None
fp = None.open(filename, 'rb')
leader_bytes = fp.read(12)
header_leader = struct.unpack('>dI', leader_bytes)
header_bytes = fp.read(header_leader[1])
header_str = header_bytes.decode('UTF-8')
header = json.loads(header_str)
new_nvm = bytes.fromhex(header['nvm'])
new_length = len(new_nvm)
if new_length != current_length:
    message = self.tr('NVM sizes do not match!')
    QtWidgets.QMessageBox.critical(self, self.tr('Error'), message)
    return None
None.controller.write_nvm(new_nvm)
