# Source Generated with Decompyle++
# File: tmpd6ahztvx.marshal (Python 3.11)

settings = QtCore.QSettings()
(board_name, board_rev) = device_info.board_info
short_board_name = board_name.replace(' ', '')
keys = [
    f'''firmDirectory/{short_board_name}/Rev{board_rev}''',
    f'''firmDirectory/{short_board_name}/last''',
    'firmDirectory/last']
firm_dir = None
for key in keys:
    test_dir = settings.value(key)
    if test_dir and isinstance(test_dir, str) and os.path.isdir(test_dir):
        firm_dir = test_dir
    
    if not firm_dir:
        firm_dir = ''
caption = self.tr('Open Firmware File')
file_filter = self.tr('Firmware Files (*.firmware);;All Files (*.*)')
val = QtWidgets.QFileDialog.getOpenFileName(self, caption, firm_dir, file_filter)
output_path = val[0]
if output_path:
    output_dir = os.path.dirname(output_path)
    for key in keys:
        settings.setValue(key, output_dir)
        return output_path
        return None
