# Source Generated with Decompyle++
# File: tmp7b09mocr.marshal (Python 3.11)

self.detail_scan_dialog = DetailScanDialog(self.active_scan_database, self.preferences, self)
self.menu = QtWidgets.QMenu(self)
self.menu.addAction(self.actionConnectNoStreaming)
self.menu.addSeparator()
self.menu.addAction(self.actionConnectSpecificBootloader)
self.menu.addAction(self.actionConnectSpecificSerial)
self.advancedMenuButton.setMenu(self.menu)
self.deviceList.addAction(self.actionClear)
self.actionClear.setIcon(QtGui.QIcon.fromTheme('delete'))
self.clearButton.setDefaultAction(self.actionClear)
