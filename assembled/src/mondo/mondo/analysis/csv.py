# Source Generated with Decompyle++
# File: csv.pyc (Python 3.11)

import datetime
import functools
import logging
import math
import os.path as os
from typing import Optional
import numpy
from PySide6 import QtCore, QtWidgets
from . import util
logger = logging.getLogger(__name__)

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def get_csv_file(default_name, parent):
    settings = QtCore.QSettings()
    directory = settings.value('fileSaveDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
        else:
            directory = None
    if not directory:
        directory = ''
    file_and_dir = os.path.join(directory, default_name)
    caption = 'Save File'
    file_filter = 'Comma Seperated Value Files (*.csv);;All Files (*.*)'
    val = QtWidgets.QFileDialog.getSaveFileName(parent, caption, file_and_dir, file_filter)
    output_path = val[0]
    if output_path:
        output_dir = os.path.dirname(output_path)
        settings.setValue('fileSaveDirectory', output_dir)
        return output_path

def do_downsample(array, downsample_factor):
    pad_size = downsample_factor - array.size % downsample_factor
    if pad_size == downsample_factor:
        pad_size = 0
    padded_array = numpy.append(array, numpy.zeros(pad_size) * numpy.nan)
    reshaped = padded_array.reshape((-1, downsample_factor))
    result = numpy.nanmean(reshaped, axis = 1)
    return result

def csv_export(parent, downsample):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL header
    #    2 RESUME
    #    4 LOAD_GLOBAL NULL + util
    #   16 LOAD_ATTR load_batch
    #   26 LOAD_FAST parent
    #   28 PRECALL
    #   32 CALL
    #   42 STORE_FAST ret
    #   44 LOAD_FAST ret
    #   46 POP_JUMP_FORWARD_IF_NOT_NONE to 52
    #   48 LOAD_CONST None
    #   50 RETURN_VALUE
    #   52 LOAD_FAST ret
    #   54 UNPACK_SEQUENCE
    #   58 STORE_FAST file_infos
    #   60 STORE_DEREF header
    #   62 LOAD_FAST downsample
    #   64 POP_JUMP_FORWARD_IF_FALSE to 156
    #   66 LOAD_GLOBAL QtWidgets
    #   78 LOAD_ATTR QInputDialog
    #   88 LOAD_METHOD getInt
    #  110 LOAD_FAST parent
    #  112 LOAD_CONST 'Downsample Factor'
    #  114 LOAD_CONST 'Input downsample factor'
    #  116 LOAD_CONST 2
    #  118 LOAD_CONST 2
    #  120 LOAD_CONST 2147483647
    #  122 KW_NAMES
    #  124 PRECALL
    #  128 CALL
    #  138 UNPACK_SEQUENCE
    #  142 STORE_FAST downsample_factor
    #  144 STORE_FAST ok
    #  146 LOAD_FAST ok
    #  148 POP_JUMP_FORWARD_IF_TRUE to 154
    #  150 LOAD_CONST None
    #  152 RETURN_VALUE
    #  154 JUMP_FORWARD to 160
    #  156 LOAD_CONST 1
    #  158 STORE_FAST downsample_factor
    #  160 LOAD_GLOBAL NULL + util
    #  172 LOAD_ATTR choose_synchronous_channels
    #  182 LOAD_DEREF header
    #  184 LOAD_FAST parent
    #  186 PRECALL
    #  190 CALL
    #  200 STORE_FAST channel_indexes
    #  202 LOAD_FAST channel_indexes
    #  204 POP_JUMP_FORWARD_IF_NOT_NONE to 210
    #  206 LOAD_CONST None
    #  208 RETURN_VALUE
    #  210 LOAD_GLOBAL NULL + util
    #  222 LOAD_ATTR decode_batch
    #  232 LOAD_FAST file_infos
    #  234 LOAD_DEREF header
    #  236 LOAD_FAST channel_indexes
    #  238 LOAD_FAST parent
    #  240 PRECALL
    #  244 CALL
    #  254 STORE_FAST batch_info
    #  256 LOAD_FAST batch_info
    #  258 POP_JUMP_FORWARD_IF_NOT_NONE to 264
    #  260 LOAD_CONST None
    #  262 RETURN_VALUE
    #  264 LOAD_GLOBAL NULL + util
    #  276 LOAD_ATTR get_datetime_subset
    #  286 LOAD_FAST batch_info
    #  288 LOAD_FAST parent
    #  290 PRECALL
    #  294 CALL
    #  304 STORE_FAST batch_info
    #  306 LOAD_FAST batch_info
    #  308 POP_JUMP_FORWARD_IF_NOT_NONE to 314
    #  310 LOAD_CONST None
    #  312 RETURN_VALUE
    #  314 LOAD_GLOBAL NULL + util
    #  326 LOAD_ATTR warn_about_lost_packets
    #  336 LOAD_FAST batch_info
    #  338 LOAD_FAST parent
    #  340 LOAD_CONST True
    # ... bytecode truncated ...
    pass
