# Source Generated with Decompyle++
# File: spectrogram.pyc (Python 3.11)

import logging
from PySide6 import QtWidgets
from . import util
from .. import export_script
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def spectrogram_analysis(parent):
    ret = util.load_batch(parent)
