# Source Generated with Decompyle++
# File: dark_mode.pyc (Python 3.11)

from PySide6 import QtCore, QtGui, QtWidgets
original_palette = None
current_setting = None

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def set_style(app, dark_mode):
    if current_setting == dark_mode:
        return None
    current_setting = None
    app.setStyle('Fusion')
