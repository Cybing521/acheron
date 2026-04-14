# Source Generated with Decompyle++
# File: tmp1w9vj1i5.marshal (Python 3.11)

nvm_bytes = bytearray(self.nvm_bytes)
for widget in self.setting_widgets:
    widget.update_nvm(nvm_bytes)
    return bytes(nvm_bytes)
