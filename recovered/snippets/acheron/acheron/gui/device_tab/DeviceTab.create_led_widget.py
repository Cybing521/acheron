# Source Generated with Decompyle++
# File: tmp54eo14fd.marshal (Python 3.11)

set_value = functools.partial(self.controller.set_led, index)
widget = LEDControlWidget(set_value, initial_value)
widget.setEnabled(manual_control)
self.LEDLayout.addWidget(widget)
self.led_widgets.append(widget)
