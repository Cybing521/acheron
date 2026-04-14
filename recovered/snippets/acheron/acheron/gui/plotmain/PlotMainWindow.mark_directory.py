# Source Generated with Decompyle++
# File: tmp51utv7_x.marshal (Python 3.11)

output_dir = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr('Select Directory'), self.preferences.base_dir)
if not output_dir:
    return None
collected_files = None
for root, _dirs, files in os.walk(output_dir):
    for name in files:
        if name.endswith('.apd'):
            apd_filename = os.path.join(root, name)
            collected_files.append(apd_filename)
        self.dispatcher.mark_for_upload(collected_files)
        return None
