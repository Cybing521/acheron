# Source Generated with Decompyle++
# File: tmpyvi41arb.marshal (Python 3.11)

self.plot = cast(pyqtgraph.PlotItem, self.graphicsView.getPlotItem())
self.plot.showGrid(x = True, y = True)
self.plot.setLabel('bottom', 'Time (s)')
self.plot.setTitle('Linear Fit')
self.plot.setLabel('bottom', self.dc_formatter.unit_html)
self.points_curve = self.plot.plot(pen = None, symbol = 'o', symbolBrush = (255, 0, 0), symbolPen = 'w', name = 'Data')
self.regression_curve = self.plot.plot(pen = (0, 0, 255), name = 'Fit')
self.text_items = []
