# Source Generated with Decompyle++
# File: tmpt96tla63.marshal (Python 3.11)

self.collapsed = collapsed
if collapsed:
    self.collapseButton.setText(self.tr('▲ Expand ▲'))
else:
    self.collapseButton.setText(self.tr('▼ Collapse ▼'))
self.bottomGroup.setVisible(not collapsed)
