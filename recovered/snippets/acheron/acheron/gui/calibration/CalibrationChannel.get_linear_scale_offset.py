# Source Generated with Decompyle++
# File: tmph9mzfygx.marshal (Python 3.11)


try:
    row_count = self.linearTable.rowCount()
    if row_count < 2:
        return None
    x = None.zeros(row_count)
    y = numpy.zeros(row_count)
    for row in range(row_count):
        captured = cast(UnitFormatterDoubleSpinBox, self.linearTable.cellWidget(row, 0))
        actual = cast(UnitFormatterDoubleSpinBox, self.linearTable.cellWidget(row, 1))
        unscaled = (captured.value() - self.cal.calibration_info.offset) / self.cal.calibration_info.scale
        x[row] = unscaled
        y[row] = actual.value()
        self.linear_x = x
        self.linear_y = y
        A = numpy.vstack([
            x,
            numpy.ones(row_count)]).T
        (m, b) = numpy.linalg.lstsq(A, y, rcond = None)[0]
        if not m == 0 and math.isfinite(m) or math.isfinite(b):
            return None
        return (None, b)
        except Exception:
            return None

