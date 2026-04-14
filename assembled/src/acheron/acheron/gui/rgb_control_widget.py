# Source Generated with Decompyle++
# File: rgb_control_widget.pyc (Python 3.11)

import logging
from typing import Callable, Optional
from PySide6 import QtCore, QtWidgets
from ..core.update_func_limiter import UpdateFuncLimiter
from .ui.ui_rgb_control_widget import Ui_RGBControlWidget
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class RGBControlWidget(Ui_RGBControlWidget, QtWidgets.QWidget):

    def __init__(self, set_rgb, initial_values, parent):
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
        #   70 LOAD_CONST False
        #   72 LOAD_FAST self
        #   74 STORE_ATTR setting_color
        #   84 LOAD_GLOBAL NULL + UpdateFuncLimiter
        #   96 LOAD_FAST set_rgb
        #   98 LOAD_CONST 100
        #  100 LOAD_FAST self
        #  102 PRECALL
        #  106 CALL
        #  116 LOAD_FAST self
        #  118 STORE_ATTR updater
        #  128 LOAD_FAST self
        #  130 LOAD_METHOD setupUi
        #  152 LOAD_FAST self
        #  154 PRECALL
        #  158 CALL
        #  168 POP_TOP
        #  170 LOAD_FAST self
        #  172 LOAD_METHOD setup_callbacks
        #  194 PRECALL
        #  198 CALL
        #  208 POP_TOP
        #  210 LOAD_FAST self
        #  212 LOAD_METHOD set_values
        #  234 LOAD_FAST initial_values
        #  236 PRECALL
        #  240 CALL
        #  250 POP_TOP
        #  252 LOAD_CONST None
        #  254 RETURN_VALUE
        pass

    def setup_callbacks(self):
        self.buttons = {
            (255, 255, 255): self.whiteButton,
            (255, 0, 0): self.redButton,
            (0, 255, 0): self.greenButton,
            (0, 0, 255): self.blueButton,
            (0, 255, 255): self.cyanButton,
            (255, 0, 255): self.magentaButton,
            (255, 255, 0): self.yellowButton,
            (0, 0, 0): self.blackButton }
        self.whiteButton.clicked.connect(self.white_button_pressed)
        self.redButton.clicked.connect(self.red_button_pressed)
        self.greenButton.clicked.connect(self.green_button_pressed)
        self.blueButton.clicked.connect(self.blue_button_pressed)
        self.cyanButton.clicked.connect(self.cyan_button_pressed)
        self.magentaButton.clicked.connect(self.magenta_button_pressed)
        self.yellowButton.clicked.connect(self.yellow_button_pressed)
        self.blackButton.clicked.connect(self.black_button_pressed)
        self.redSlider.valueChanged.connect(self.color_changed)
        self.greenSlider.valueChanged.connect(self.color_changed)
        self.blueSlider.valueChanged.connect(self.color_changed)

    def white_button_pressed(self):
        self.set_color_from_button((255, 255, 255))

    def red_button_pressed(self):
        self.set_color_from_button((255, 0, 0))

    def green_button_pressed(self):
        self.set_color_from_button((0, 255, 0))

    def blue_button_pressed(self):
        self.set_color_from_button((0, 0, 255))

    def cyan_button_pressed(self):
        self.set_color_from_button((0, 255, 255))

    def magenta_button_pressed(self):
        self.set_color_from_button((255, 0, 255))

    def yellow_button_pressed(self):
        self.set_color_from_button((255, 255, 0))

    def black_button_pressed(self):
        self.set_color_from_button((0, 0, 0))

    def set_values(self, values):
        self.setting_color = True
        self.redSlider.setValue(values[0])
        self.greenSlider.setValue(values[1])
        self.blueSlider.setValue(values[2])
        for color, button in self.buttons.items():
            checked = color == tuple(values)
            button.setDown(checked)
            self.setting_color = False
            return None

    def set_color_from_button(self, values):
        self.set_values(values)
        self.updater.update(values)

    def color_changed(self):
        if not self.setting_color:
            values = (self.redSlider.value(), self.greenSlider.value(), self.blueSlider.value())
            self.set_values(values)
            self.updater.update(values)
            return None
