# Source Generated with Decompyle++
# File: tmpmasegtxb.marshal (Python 3.11)

import collections
import logging
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import asphodel
from core.dispatcher import Dispatcher
from core.preferences import Preferences
from ui.ui_tcp_scan_dialog import Ui_TCPScanDialog
logger = logging.getLogger(__name__)

class SortableTableWidgetItem(QtWidgets.QTableWidgetItem):
    pass
# WARNING: Decompyle incomplete

TableItems = collections.namedtuple('TableItems', [
    'serial_number',
    'tag1',
    'tag2',
    'board_info',
    'build_info',
    'build_date',
    'bootloader',
    'available'])

class RowInformation:
    
    def __init__(self = None, table_items = None):
        self.table_items = table_items
        self.device = None
        self.connected = False



class TCPScanDialog(QtWidgets.QDialog, Ui_TCPScanDialog):
    pass
# WARNING: Decompyle incomplete

