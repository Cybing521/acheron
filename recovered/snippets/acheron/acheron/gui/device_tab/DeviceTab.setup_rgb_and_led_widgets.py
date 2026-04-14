# Source Generated with Decompyle++
# File: tmpt6qfk00n.marshal (Python 3.11)

item = self.LEDLayout.takeAt(0)
if not item:
    pass

for rgb_widget in self.rgb_widgets:
    rgb_widget.deleteLater()
    self.rgb_widgets.clear()
    for led_widget in self.led_widgets:
        led_widget.deleteLater()
        self.led_widgets.clear()
        for i, values in enumerate(device_info.rgb_settings):
            self.create_rgb_widget(i, values, manual_control)
            for i, value in enumerate(device_info.led_settings):
                self.create_led_widget(i, value, manual_control)
                return None
