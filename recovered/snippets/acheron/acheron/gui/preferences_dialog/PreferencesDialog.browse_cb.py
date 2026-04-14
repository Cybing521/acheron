# Source Generated with Decompyle++
# File: tmpbtkoqv8r.marshal (Python 3.11)

base_dir = self.outputLocation.text()
base_dir = QtWidgets.QFileDialog.getExistingDirectory(self, dir = base_dir)
if base_dir:
    self.outputLocation.setText(base_dir)
    return None
