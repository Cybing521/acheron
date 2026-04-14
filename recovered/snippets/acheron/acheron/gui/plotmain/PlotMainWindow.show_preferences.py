# Source Generated with Decompyle++
# File: tmpamjtw92e.marshal (Python 3.11)

dialog = PreferencesDialog(self.preferences, self)

try:
    if dialog.exec():
        self.dispatcher.update_preferences()
        for device_tab in self.tab_widgets:
            device_tab.update_preferences()
            dialog.deleteLater()
            return None
            dialog.deleteLater()

