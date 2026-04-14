# Source Generated with Decompyle++
# File: tmp8u53l3h4.marshal (Python 3.11)

self.setting_color = True
self.redSlider.setValue(values[0])
self.greenSlider.setValue(values[1])
self.blueSlider.setValue(values[2])
for color, button in self.buttons.items():
    checked = color == tuple(values)
    button.setDown(checked)
    self.setting_color = False
    return None
