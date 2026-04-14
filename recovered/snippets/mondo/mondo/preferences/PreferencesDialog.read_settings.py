# Source Generated with Decompyle++
# File: tmpjzvrcuma.marshal (Python 3.11)

self.unitPreferences.read_settings()
dark_mode = read_bool_setting(self.settings, 'DarkMode', True)
if dark_mode:
    self.darkMode.setChecked(True)
    return None
None.lightMode.setChecked(True)
