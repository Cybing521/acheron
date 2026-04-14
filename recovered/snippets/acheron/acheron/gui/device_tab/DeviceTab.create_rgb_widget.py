# Source Generated with Decompyle++
# File: tmpg6yzsgep.marshal (Python 3.11)

set_values = functools.partial(self.controller.set_rgb, index)
widget = RGBControlWidget(set_values, initial_values)
widget.setEnabled(manual_control)
self.LEDLayout.addWidget(widget)
self.rgb_widgets.append(widget)
