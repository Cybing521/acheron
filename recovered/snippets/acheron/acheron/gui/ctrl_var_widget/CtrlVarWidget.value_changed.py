# Source Generated with Decompyle++
# File: tmpn9jyhtxz.marshal (Python 3.11)

if not self.setting_value:
    value = self.slider.value()
    if self.inverted:
        value = -value
    self.updater.update(value)
    return None
