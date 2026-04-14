# Source Generated with Decompyle++
# File: tmpdqx18i77.marshal (Python 3.11)

self.plotdata = { }
self._index = 0
if not setup_commands:
    self.append('import matplotlib')
    self.append('import numpy')
    self.append('from PySide6 import QtGui')
    self.append('')
    return None
None.extend(setup_commands)
self.append('')
self.append("plotdata = numpy.load(__file__ + '.npz')")
