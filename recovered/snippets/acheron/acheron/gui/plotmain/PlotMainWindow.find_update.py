# Source Generated with Decompyle++
# File: tmpmdti1f6q.marshal (Python 3.11)

build_key = build_info.get_build_key()
if not build_key:
    return None
self.update_fallback_branch = None
self.update_progress.setMinimum(0)
self.update_progress.setMaximum(0)
self.update_progress.setValue(0)
self.update_progress.setLabelText(self.tr('Checking for update...'))
self.update_progress.forceShow()
self.software_finder.find_software('acheron', build_key, branch, commit)
