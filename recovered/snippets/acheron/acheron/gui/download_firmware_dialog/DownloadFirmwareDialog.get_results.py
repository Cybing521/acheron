# Source Generated with Decompyle++
# File: tmp3309tbp_.marshal (Python 3.11)

results = { }
if self.boardRadioButton.isChecked():
    board_name = self.boardName.text().strip()
    board_rev = self.boardRev.value()
    results['board_info'] = (board_name, board_rev)
else:
    results['repo'] = self.repoName.text().strip()
if self.branchRadioButton.isChecked():
    results['branch'] = self.branchName.text().strip()
else:
    results['commit'] = self.commitHash.text().strip()
return results
