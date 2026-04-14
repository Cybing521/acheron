# Source Generated with Decompyle++
# File: tmplj4442d8.marshal (Python 3.11)

if self.automaticRescan.isChecked():
    self.preferences.automatic_rescan = True
    self.rescan_timer.start(1000)
    return None
self.preferences.automatic_rescan = None
self.rescan_timer.stop()
