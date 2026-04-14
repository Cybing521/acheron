# Source Generated with Decompyle++
# File: tmpcu7v6de7.marshal (Python 3.11)

self.update_fallback_branch = fallback_branch
self.update_progress.setMinimum(0)
self.update_progress.setMaximum(0)
self.update_progress.setValue(0)
self.update_progress.setLabelText(self.tr('Checking for update...'))
self.update_progress.forceShow()
self.software_finder.find_software('mondo', self.build_key, branch, commit)
