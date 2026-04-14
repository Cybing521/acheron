# Source Generated with Decompyle++
# File: tmpfsazb7a8.marshal (Python 3.11)

if self.boardRadioButton.isChecked():
    if not self.boardName.text().strip():
        return False
if not self.repoName.text().strip():
    return False
if None.branchRadioButton.isChecked():
    if not self.branchName.text().strip():
        return False
if not self.commitHash.text().strip():
    return False
