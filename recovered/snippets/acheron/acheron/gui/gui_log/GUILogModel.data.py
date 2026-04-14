# Source Generated with Decompyle++
# File: tmpjfn9s468.marshal (Python 3.11)

row = index.row()
if row < 0 or row >= len(self.list):
    return ''
if None == QtCore.Qt.ItemDataRole.DisplayRole or role == QtCore.Qt.ItemDataRole.EditRole:
    return self.list[row]
