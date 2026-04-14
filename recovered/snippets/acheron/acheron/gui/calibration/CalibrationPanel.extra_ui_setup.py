# Source Generated with Decompyle++
# File: tmp8w6f57kc.marshal (Python 3.11)

self.unit_selection_dialog = UnitSelectionDialog(self)
self.saveButton = self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Save)
self.saveButton.setText(self.tr('Write NVM'))
self.saveButton.clicked.connect(self.save)
self.channel_widgets = []
for cal in self.cals:
    channel_widget = CalibrationChannel(cal, self.unit_selection_dialog, self)
    self.channel_widgets.append((cal.name, channel_widget))
    self.setup_channel_signals(channel_widget)
    if len(self.channel_widgets) == 1:
        channel_widget = self.channel_widgets[0][1]
        channel_widget.calibrationEnabled.setChecked(True)
        channel_widget.calibrationEnabled.setVisible(False)
        self.verticalLayout.insertWidget(0, channel_widget)
        return None
    if None(self.channel_widgets) > 1:
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.verticalLayout.insertWidget(0, self.tabWidget)
        for name, channel_widget in self.channel_widgets:
            channel_widget.calibrationEnabled.setChecked(False)
            cal_str = self.tr('Calibrate {}').format(name)
            channel_widget.calibrationEnabled.setText(cal_str)
            self.tabWidget.addTab(channel_widget, name)
            return None
            return None
