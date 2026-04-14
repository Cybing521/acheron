# Source Generated with Decompyle++
# File: tmpqa7v8jat.marshal (Python 3.11)

start_index = self.tableWidget.rowCount()
self.tableWidget.insertRow(start_index)
serial_number_item = SortableTableWidgetItem()
serial_number_item.sort_value = serial_number
serial_number_item.setData(QtCore.Qt.ItemDataRole.DisplayRole, serial_number)
self.tableWidget.setItem(start_index, 0, serial_number_item)
table_items = [
    serial_number_item]
# WARNING: Decompyle incomplete
