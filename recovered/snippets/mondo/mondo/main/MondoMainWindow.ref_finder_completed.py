# Source Generated with Decompyle++
# File: tmpuobt2fxm.marshal (Python 3.11)

self.update_progress.reset()
default_branch = self.branch_name
branch_choices = [
    default_branch]
if default_branch != 'master':
    branch_choices.append('master')
if default_branch != 'develop':
    branch_choices.append('develop')
ref_names = []
for ref in refs:
    ref_name = ref.get('name', None)
    if ref_name and ref_name not in branch_choices:
        ref_names.append(ref_name)
    if ref_names:
        label = self.tr('Branch:')
    else:
        label = self.tr('No list of branches!\nBranch:')
branch_choices.extend(sorted(ref_names, key = hyperborea.download.ref_sort_key))
(branch, ok) = QtWidgets.QInputDialog.getItem(self, self.tr('Branch'), label, branch_choices, 0, True)
if not ok:
    return None
branch = None.strip()
self.find_update(branch = branch)
