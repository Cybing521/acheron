# Source Generated with Decompyle++
# File: select_subchannels.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtWidgets
from .ui.ui_select_subchannels import Ui_SelectSubchannelsDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class SelectSubchannelsDialog(Ui_SelectSubchannelsDialog, QtWidgets.QDialog):

    def __init__(self, names, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST parent
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_FAST names
        #   72 LOAD_FAST self
        #   74 STORE_ATTR names
        #   84 BUILD_MAP
        #   86 LOAD_FAST self
        #   88 STORE_ATTR subchannel_buttons
        #   98 LOAD_FAST self
        #  100 LOAD_METHOD setupUi
        #  122 LOAD_FAST self
        #  124 PRECALL
        #  128 CALL
        #  138 POP_TOP
        #  140 LOAD_FAST self
        #  142 LOAD_METHOD add_buttons
        #  164 PRECALL
        #  168 CALL
        #  178 POP_TOP
        #  180 LOAD_CONST None
        #  182 RETURN_VALUE
        pass

    def add_buttons(self):
        for channel_id, channel_name, subchannel_names in sorted(self.names):
            if len(subchannel_names) > 1:
                channel_label = QtWidgets.QLabel(channel_name, parent = self)
                self.verticalLayout.addWidget(channel_label)
                group_widget = QtWidgets.QWidget(parent = self)
                layout = QtWidgets.QVBoxLayout(group_widget)
                for i, subchannel_name in enumerate(subchannel_names):
                    check_box = QtWidgets.QCheckBox(subchannel_name, parent = group_widget)
                    self.subchannel_buttons[(channel_id, i)] = check_box
                    check_box.setChecked(False)
                    layout.addWidget(check_box)
                    self.verticalLayout.addWidget(group_widget)
                    check_box = QtWidgets.QCheckBox(subchannel_names[0], parent = self)
                    self.subchannel_buttons[(channel_id, 0)] = check_box
                    check_box.setChecked(False)
                    self.verticalLayout.addWidget(check_box)
                    return None

    def get_subchannels_list(self):
        selected_subchannels = []
        for index_tuple in sorted(self.subchannel_buttons.keys()):
            check_box = self.subchannel_buttons[index_tuple]
            if check_box.isChecked():
                selected_subchannels.append(index_tuple)
            return selected_subchannels
