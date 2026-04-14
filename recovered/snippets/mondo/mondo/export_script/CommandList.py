# Source Generated with Decompyle++
# File: tmp9bptylq2.marshal (Python 3.11)


def __init__(self, setup_commands = (None,)):
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


def get_string(self, value):
    if isinstance(value, numpy.ndarray):
        i = 'array_{}'.format(self._index)
        value = self, self._index += 1, ._index
        return "plotdata['{}']".format(i)
    return None(value)


def output(self, scriptfile):
    datafile = scriptfile + '.npz'
    logger.debug('Writing script to {}'.format(scriptfile))
    f = open(scriptfile, 'wt', encoding = 'utf_8')
    for v in self:
        s = str(v)
        if s == 'fig.show()':
            s = 'plt.show()'
        f.write(s)
        f.write('\n')
        None(None, None)
    with None:
        if not None:
            pass
    logger.debug('Writing script data to {}'.format(datafile))
# WARNING: Decompyle incomplete

