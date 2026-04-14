# Source Generated with Decompyle++
# File: tmpllvgnf19.marshal (Python 3.11)

if not new_alert and self.alert:
    self.alert = True
    self.setStyleSheet('* { color: black; background-color: red; }')
if not self.alert or new_alert:
    self.alert = False
    self.setStyleSheet('')
    return None
return None
