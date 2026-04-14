# Source Generated with Decompyle++
# File: tmp5a85jh9_.marshal (Python 3.11)

clipboard = QtWidgets.QApplication.clipboard()
indexes = self.logList.selectedIndexes()
text = (lambda .0: [ i.data() for i in .0 ])(indexes())
if text:
    clipboard.setText(text)
    return None
return '\n'.join
