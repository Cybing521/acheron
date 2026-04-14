# Source Generated with Decompyle++
# File: export_csv.pyc (Python 3.11)

import os.path as os
from PySide6 import QtGui, QtWidgets
from  import mondo_rc
from analysis.csv import get_csv_file

def _do_export(filename, labels, xdata, ydata):
    f = open(filename, 'w', encoding = 'utf-8')
    f.write(', '.join(labels))
    f.write('\n')
    for x, y in zip(xdata, ydata):
        f.write('{}, {}\n'.format(x, y))
        None(None, None)
        return None
        with None:
            if not None:
                pass


def add_export_csv_action(figure, labels, data):
    pass
# WARNING: Decompyle incomplete

