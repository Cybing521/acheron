# Source Generated with Decompyle++
# File: change_stream_dialog.pyc (Python 3.11)

import logging
from typing import Optional
from PySide6 import QtWidgets
import asphodel
from .ui.ui_change_stream_dialog import Ui_ChangeStreamDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class ChangeStreamDialog(Ui_ChangeStreamDialog, QtWidgets.QDialog):

    def __init__(self, streams, channels, active_streams, parent):
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
        #   98 LOAD_FAST active_streams
        #  100 LOAD_FAST self
        #  102 STORE_ATTR active_streams
        #  112 BUILD_MAP
        #  114 LOAD_FAST self
        #  116 STORE_ATTR check_boxes
        #  126 LOAD_FAST self
        #  128 LOAD_METHOD setupUi
        #  150 LOAD_FAST self
        #  152 PRECALL
        #  156 CALL
        #  166 POP_TOP
        #  168 LOAD_FAST self
        #  170 LOAD_METHOD add_check_boxes
        #  192 PRECALL
        #  196 CALL
        #  206 POP_TOP
        #  208 LOAD_CONST None
        #  210 RETURN_VALUE
        pass

    def add_check_boxes(self):
        d = { }
        for index, stream in enumerate(self.streams):
            check_box = QtWidgets.QCheckBox(self)
            check_box.setChecked(index in self.active_streams)
            self.check_boxes[index] = check_box
            stream_channels = stream.channel_index_list[:stream.channel_count]
            channel_names = []
            for ch_index in stream_channels:
                channel = self.channels[ch_index]
                channel_names.append(channel.name.decode('utf-8'))
                stream_text = 'Stream {} ({})'.format(index, ', '.join(channel_names))
                check_box.setText(stream_text)
                d[min(stream_channels)] = check_box
                for ch_index in sorted(d.keys()):
                    check_box = d[ch_index]
                    self.verticalLayout.addWidget(check_box)
                    return None

    def get_new_stream_list(self):
        all_true = True
        stream_list = []
        for index in sorted(self.check_boxes.keys()):
            check_box = self.check_boxes[index]
            if check_box.isChecked():
                stream_list.append(index)
                continue
            all_true = False
            if all_true:
                return None
            return None
