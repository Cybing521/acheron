# Source Generated with Decompyle++
# File: select_synchronous.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtWidgets
import asphodel
from .ui.ui_select_synchronous import Ui_SelectSynchronousDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class SelectSynchronousDialog(Ui_SelectSynchronousDialog, QtWidgets.QDialog):

    def __init__(self, streams, channels, parent):
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
        #   70 LOAD_FAST streams
        #   72 LOAD_FAST self
        #   74 STORE_ATTR streams
        #   84 LOAD_FAST channels
        #   86 LOAD_FAST self
        #   88 STORE_ATTR channels
        #   98 BUILD_LIST
        #  100 LOAD_FAST self
        #  102 STORE_ATTR stream_buttons
        #  112 BUILD_LIST
        #  114 LOAD_FAST self
        #  116 STORE_ATTR channel_groups
        #  126 LOAD_FAST self
        #  128 LOAD_METHOD setupUi
        #  150 LOAD_FAST self
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_FAST self
        #  170 LOAD_METHOD add_buttons
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 LOAD_CONST None
        #  210 RETURN_VALUE
        pass

    def add_buttons(self):
        d = { }
        for stream_index, stream in enumerate(self.streams):
            stream_channels = stream.channel_index_list[:stream.channel_count]
            d[min(stream_channels)] = stream_index
            for _sort_key, stream_index in sorted(d.items()):
                stream = self.streams[stream_index]
                stream_channels = stream.channel_index_list[:stream.channel_count]
                if not stream_channels:
                    continue
                radio_button = QtWidgets.QRadioButton('Stream {}'.format(stream_index), parent = self)
                self.stream_buttons.append(radio_button)
                self.verticalLayout.addWidget(radio_button)
                group_widget = QtWidgets.QWidget(parent = self)
                layout = QtWidgets.QVBoxLayout(group_widget)
                channel_group = { }
                self.channel_groups.append(channel_group)
                for channel_index in sorted(stream_channels):
                    channel = self.channels[channel_index]
                    channel_name = channel.name.decode('utf-8')
                    check_box = QtWidgets.QCheckBox(channel_name, parent = group_widget)
                    channel_group[channel_index] = check_box
                    check_box.setChecked(False)
                    layout.addWidget(check_box)
                    self.verticalLayout.addWidget(group_widget)
                    group_widget.setEnabled(False)
                    radio_button.toggled.connect(group_widget.setEnabled)
                    self.stream_buttons[0].setChecked(True)
                    return None

    def get_channel_list(self):
        for i, stream_button in enumerate(self.stream_buttons):
            if stream_button.isChecked():
                indexes = set()
                for ch_index, check_box in self.channel_groups[i].items():
                    if check_box.isChecked():
                        indexes.add(ch_index)
                    
                    return None, sorted(indexes)
                    return []
