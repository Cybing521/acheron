# Source Generated with Decompyle++
# File: download_firmware_dialog.pyc (Python 3.11)

import logging
from typing import Any, Optional
from PySide6 import QtCore, QtWidgets
from .ui.ui_download_firmware_dialog import Ui_DownloadFirmwareDialog
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class DownloadFirmwareDialog(Ui_DownloadFirmwareDialog, QtWidgets.QDialog):

    def __init__(self, parent):
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
        #   70 LOAD_FAST self
        #   72 LOAD_METHOD setupUi
        #   94 LOAD_FAST self
        #   96 PRECALL
        #  100 CALL
        #  110 POP_TOP
        #  112 LOAD_FAST self
        #  114 LOAD_METHOD extra_ui_setup
        #  136 PRECALL
        #  140 CALL
        #  150 POP_TOP
        #  152 LOAD_CONST None
        #  154 RETURN_VALUE
        pass

    def extra_ui_setup(self):
        self.board_button_group = QtWidgets.QButtonGroup(self)
        self.board_button_group.addButton(self.boardRadioButton)
        self.board_button_group.addButton(self.repoRadioButton)
        self.board_button_group = QtWidgets.QButtonGroup(self)
        self.board_button_group.addButton(self.branchRadioButton)
        self.board_button_group.addButton(self.commitRadioButton)
        self.boardRadioButton.setChecked(True)
        self.branchRadioButton.setChecked(True)
        self.boardRadioButton.toggled.connect(self.values_updated)
        self.repoRadioButton.toggled.connect(self.values_updated)
        self.branchRadioButton.toggled.connect(self.values_updated)
        self.commitRadioButton.toggled.connect(self.values_updated)
        self.boardName.textEdited.connect(self.values_updated)
        self.repoName.textEdited.connect(self.values_updated)
        self.branchName.textEdited.connect(self.values_updated)
        self.commitHash.textEdited.connect(self.values_updated)
        self.values_updated()

    def is_valid(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR boardRadioButton
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_FALSE to 144
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR boardName
        #   64 LOAD_METHOD text
        #   86 PRECALL
        #   90 CALL
        #  100 LOAD_METHOD strip
        #  122 PRECALL
        #  126 CALL
        #  136 POP_JUMP_FORWARD_IF_TRUE to 142
        #  138 LOAD_CONST False
        #  140 RETURN_VALUE
        #  142 JUMP_FORWARD to 234
        #  144 LOAD_FAST self
        #  146 LOAD_ATTR repoName
        #  156 LOAD_METHOD text
        #  178 PRECALL
        #  182 CALL
        #  192 LOAD_METHOD strip
        #  214 PRECALL
        #  218 CALL
        #  228 POP_JUMP_FORWARD_IF_TRUE to 234
        #  230 LOAD_CONST False
        #  232 RETURN_VALUE
        #  234 LOAD_FAST self
        #  236 LOAD_ATTR branchRadioButton
        #  246 LOAD_METHOD isChecked
        #  268 PRECALL
        #  272 CALL
        #  282 POP_JUMP_FORWARD_IF_FALSE to 376
        #  284 LOAD_FAST self
        #  286 LOAD_ATTR branchName
        #  296 LOAD_METHOD text
        #  318 PRECALL
        #  322 CALL
        #  332 LOAD_METHOD strip
        #  354 PRECALL
        #  358 CALL
        #  368 POP_JUMP_FORWARD_IF_TRUE to 374
        #  370 LOAD_CONST False
        #  372 RETURN_VALUE
        #  374 JUMP_FORWARD to 466
        #  376 LOAD_FAST self
        #  378 LOAD_ATTR commitHash
        #  388 LOAD_METHOD text
        #  410 PRECALL
        #  414 CALL
        #  424 LOAD_METHOD strip
        #  446 PRECALL
        #  450 CALL
        #  460 POP_JUMP_FORWARD_IF_TRUE to 466
        #  462 LOAD_CONST False
        #  464 RETURN_VALUE
        #  466 LOAD_CONST True
        #  468 RETURN_VALUE
        pass

    def done(self, r):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_FAST r
        #    6 POP_JUMP_FORWARD_IF_FALSE to 52
        #    8 LOAD_FAST self
        #   10 LOAD_METHOD is_valid
        #   32 PRECALL
        #   36 CALL
        #   46 POP_JUMP_FORWARD_IF_TRUE to 52
        #   48 LOAD_CONST None
        #   50 RETURN_VALUE
        #   52 LOAD_GLOBAL NULL + super
        #   64 PRECALL
        #   68 CALL
        #   78 LOAD_METHOD done
        #  100 LOAD_FAST r
        #  102 PRECALL
        #  106 CALL
        #  116 POP_TOP
        #  118 LOAD_CONST None
        #  120 RETURN_VALUE
        pass

    def values_updated(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR buttonBox
        #   14 LOAD_METHOD button
        #   36 LOAD_GLOBAL QtWidgets
        #   48 LOAD_ATTR QDialogButtonBox
        #   58 LOAD_ATTR StandardButton
        #   68 LOAD_ATTR Ok
        #   78 PRECALL
        #   82 CALL
        #   92 STORE_FAST ok_button
        #   94 LOAD_FAST self
        #   96 LOAD_METHOD is_valid
        #  118 PRECALL
        #  122 CALL
        #  132 POP_JUMP_FORWARD_IF_FALSE to 180
        #  134 LOAD_FAST ok_button
        #  136 LOAD_METHOD setEnabled
        #  158 LOAD_CONST True
        #  160 PRECALL
        #  164 CALL
        #  174 POP_TOP
        #  176 LOAD_CONST None
        #  178 RETURN_VALUE
        #  180 LOAD_FAST ok_button
        #  182 LOAD_METHOD setEnabled
        #  204 LOAD_CONST False
        #  206 PRECALL
        #  210 CALL
        #  220 POP_TOP
        #  222 LOAD_CONST None
        #  224 RETURN_VALUE
        pass

    def get_results(self):
        results = { }
        if self.boardRadioButton.isChecked():
            board_name = self.boardName.text().strip()
            board_rev = self.boardRev.value()
            results['board_info'] = (board_name, board_rev)
        else:
            results['repo'] = self.repoName.text().strip()
        if self.branchRadioButton.isChecked():
            results['branch'] = self.branchName.text().strip()
        else:
            results['commit'] = self.commitHash.text().strip()
        return results
