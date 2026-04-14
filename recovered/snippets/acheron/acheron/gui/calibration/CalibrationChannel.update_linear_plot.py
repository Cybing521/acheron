# Source Generated with Decompyle++
# File: tmp8evdhhec.marshal (Python 3.11)

row_count = self.linearTable.rowCount()
x = numpy.zeros(row_count)
y = numpy.zeros(row_count)
for row in range(row_count):
    captured = cast(UnitFormatterDoubleSpinBox, self.linearTable.cellWidget(row, 0))
    actual = cast(UnitFormatterDoubleSpinBox, self.linearTable.cellWidget(row, 1))
    x[row] = captured.value()
    y[row] = actual.value()
    x = x * self.dc_formatter.conversion_scale + self.dc_formatter.conversion_offset
    if self.unit_info:
        actual_unit_formatter = self.unit_info[1]
        y = y * actual_unit_formatter.conversion_scale + actual_unit_formatter.conversion_offset
for text_item in self.text_items:
    self.plot.removeItem(text_item)
    self.text_items.clear()
    self.points_curve.setData(x, y)
    for x_point, y_point in enumerate(zip(x, y)):
        text_item = pyqtgraph.TextItem('{}'.format(i + 1), anchor = (0.5, 1.1))
        text_item.setPos(x_point, y_point)
        self.text_items.append(text_item)
        self.plot.addItem(text_item)
        if len(x) < 2:
            self.regression_curve.clear()
            return None
        A = None.vstack([
            x,
            numpy.ones(row_count)]).T
        (scale, offset) = numpy.linalg.lstsq(A, y, rcond = None)[0]
        x_linear = numpy.array([
            x.min(),
            x.max()])
        y_linear = x_linear * scale + offset
        self.regression_curve.setData(x_linear, y_linear)
        return None
