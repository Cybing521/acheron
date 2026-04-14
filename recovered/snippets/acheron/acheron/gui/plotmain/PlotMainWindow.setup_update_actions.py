# Source Generated with Decompyle++
# File: tmp25o0141w.marshal (Python 3.11)

branch_name = build_info.get_branch_name()
if not branch_name:
    self.menuCheckForUpdates.setEnabled(False)
    self.menuCheckForUpdates.setTitle(self.tr('Not Updatable'))
    self.actionUpdateLatestStable.setEnabled(False)
    self.actionUpdateCurrentBranch.setEnabled(False)
    self.actionUpdateSpecificBranch.setEnabled(False)
    self.actionUpdateSpecificCommit.setEnabled(False)
    return None
if None == 'master':
    self.actionUpdateCurrentBranch.setEnabled(False)
    self.actionUpdateCurrentBranch.setVisible(False)
    return None
action_str = None.tr('Latest {}').format(branch_name)
self.actionUpdateCurrentBranch.setText(action_str)
