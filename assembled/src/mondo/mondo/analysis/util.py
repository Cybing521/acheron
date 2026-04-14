# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import binascii
import bisect
from dataclasses import dataclass, fields
import datetime
import json
import logging
import lzma
import operator
import os.path as os
import struct
from typing import cast, Iterable, Optional
import numpy
from PySide6 import QtCore, QtWidgets
import asphodel
from asphodel.device_info import DeviceInfo
import hyperborea.unit_preferences as hyperborea
from ..datetime_subset import DateTimeSubsetDialog
from ..psd_options import Chunk, PSDOptions, PSDOptionsDialog, MultiplePSDOptionsDialog
from ..select_subchannels import SelectSubchannelsDialog
from ..select_synchronous import SelectSynchronousDialog
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: UnitInfo = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class UnitInfo:

    ascii: str

    html: str

    utf8: str

    formatter: asphodel.AsphodelNativeUnitFormatter

def get_packdata_file(parent):
    settings = QtCore.QSettings()
    directory = settings.value('fileOpenDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
        else:
            directory = None
    if not directory:
        directory = ''
    caption = 'Open File'
    file_filter = 'Packed Data Files (*.apd);;All Files (*.*)'
    val = QtWidgets.QFileDialog.getOpenFileName(parent, caption, directory, file_filter)
    output_path = val[0]
    if output_path:
        output_dir = os.path.dirname(output_path)
        settings.setValue('fileOpenDirectory', output_dir)
        return output_path

def get_packdata_files(parent):
    settings = QtCore.QSettings()
    directory = settings.value('fileOpenDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
        else:
            directory = None
    if not directory:
        directory = ''
    caption = 'Open Files'
    file_filter = 'Packed Data Files (*.apd);;All Files (*.*)'
    val = QtWidgets.QFileDialog.getOpenFileNames(parent, caption, directory, file_filter)
    files = val[0]
    if files:
        output_dir = os.path.dirname(files[0])
        settings.setValue('fileOpenDirectory', output_dir)
        return sorted(files)

def decode_header(header_bytes, parent):
    try:
        header_str = header_bytes.decode('UTF-8')
        header = json.loads(header_str)
    except Exception:
        message = 'Could not parse file header!'
        logger.exception(message)
        QtWidgets.QMessageBox.critical(parent, 'Error', message)
        return 

def load_single_file(parent):
    filename = get_packdata_file(parent)

def load_batch(parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_CONST True
    #    4 STORE_FAST first_file
    #    6 BUILD_LIST
    #    8 STORE_FAST loaded_files
    #   10 BUILD_LIST
    #   12 STORE_FAST file_infos
    #   14 NOP
    #   16 LOAD_GLOBAL NULL + get_packdata_files
    #   28 LOAD_FAST parent
    #   30 PRECALL
    #   34 CALL
    #   44 STORE_FAST files
    #   46 LOAD_FAST files
    #   48 POP_JUMP_FORWARD_IF_TRUE to 62
    #   50 LOAD_FAST first_file
    #   52 POP_JUMP_FORWARD_IF_FALSE to 58
    #   54 LOAD_CONST None
    #   56 RETURN_VALUE
    #   58 BUILD_LIST
    #   60 STORE_FAST files
    #   62 LOAD_FAST files
    #   64 GET_ITER
    #   66 EXTENDED_ARG
    #   68 FOR_ITER to 1578
    #   70 STORE_FAST filename
    #   72 LOAD_FAST filename
    #   74 LOAD_FAST loaded_files
    #   76 CONTAINS_OP
    #   78 POP_JUMP_FORWARD_IF_FALSE to 242
    #   80 LOAD_CONST 'File {} already loaded! Skipping.'
    #   82 LOAD_METHOD format
    #  104 LOAD_FAST filename
    #  106 PRECALL
    #  110 CALL
    #  120 STORE_FAST message
    #  122 LOAD_GLOBAL logger
    #  134 LOAD_METHOD info
    #  156 LOAD_FAST message
    #  158 PRECALL
    #  162 CALL
    #  172 POP_TOP
    #  174 LOAD_GLOBAL QtWidgets
    #  186 LOAD_ATTR QMessageBox
    #  196 LOAD_METHOD information
    #  218 LOAD_FAST parent
    #  220 LOAD_CONST 'Already Loaded'
    #  222 LOAD_FAST message
    #  224 PRECALL
    #  228 CALL
    #  238 POP_TOP
    #  240 JUMP_BACKWARD to 66
    #  242 NOP
    #  244 LOAD_GLOBAL NULL + lzma
    #  256 LOAD_ATTR LZMAFile
    #  266 LOAD_FAST filename
    #  268 LOAD_CONST 'rb'
    #  270 PRECALL
    #  274 CALL
    #  284 BEFORE_WITH
    #  286 STORE_FAST f
    #  288 LOAD_GLOBAL NULL + struct
    #  300 LOAD_ATTR unpack
    #  310 LOAD_CONST '>dI'
    #  312 LOAD_FAST f
    #  314 LOAD_METHOD read
    #  336 LOAD_CONST 12
    #  338 PRECALL
    #  342 CALL
    #  352 PRECALL
    #  356 CALL
    #  366 STORE_FAST header_leader
    #  368 LOAD_GLOBAL datetime
    #  380 LOAD_ATTR datetime
    #  390 LOAD_METHOD fromtimestamp
    #  412 LOAD_FAST header_leader
    #  414 LOAD_CONST 0
    #  416 BINARY_SUBSCR
    #  426 LOAD_GLOBAL datetime
    #  438 LOAD_ATTR timezone
    # ... bytecode truncated ...
    pass

def choose_channel(header, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + set
    #   14 PRECALL
    #   18 CALL
    #   28 STORE_FAST channel_indexes
    #   30 LOAD_FAST header
    #   32 LOAD_CONST 'streams_to_activate'
    #   34 BINARY_SUBSCR
    #   44 GET_ITER
    #   46 FOR_ITER to 168
    #   48 STORE_FAST stream_id
    #   50 LOAD_FAST header
    #   52 LOAD_CONST 'streams'
    #   54 BINARY_SUBSCR
    #   64 LOAD_FAST stream_id
    #   66 BINARY_SUBSCR
    #   76 STORE_FAST stream
    #   78 LOAD_FAST stream
    #   80 LOAD_ATTR channel_index_list
    #   90 LOAD_CONST 0
    #   92 LOAD_FAST stream
    #   94 LOAD_ATTR channel_count
    #  104 BUILD_SLICE
    #  106 BINARY_SUBSCR
    #  116 GET_ITER
    #  118 FOR_ITER to 166
    #  120 STORE_FAST index
    #  122 LOAD_FAST channel_indexes
    #  124 LOAD_METHOD add
    #  146 LOAD_FAST index
    #  148 PRECALL
    #  152 CALL
    #  162 POP_TOP
    #  164 JUMP_BACKWARD to 118
    #  166 JUMP_BACKWARD to 46
    #  168 BUILD_LIST
    #  170 STORE_FAST channel_names
    #  172 BUILD_MAP
    #  174 STORE_FAST name_dict
    #  176 LOAD_GLOBAL NULL + sorted
    #  188 LOAD_FAST channel_indexes
    #  190 PRECALL
    #  194 CALL
    #  204 GET_ITER
    #  206 FOR_ITER to 370
    #  208 STORE_FAST channel_index
    #  210 LOAD_FAST header
    #  212 LOAD_CONST 'channels'
    #  214 BINARY_SUBSCR
    #  224 LOAD_FAST channel_index
    #  226 BINARY_SUBSCR
    #  236 STORE_FAST channel
    #  238 LOAD_FAST channel
    #  240 LOAD_ATTR name
    #  250 LOAD_CONST 0
    #  252 LOAD_FAST channel
    #  254 LOAD_ATTR name_length
    #  264 BUILD_SLICE
    #  266 BINARY_SUBSCR
    #  276 LOAD_METHOD decode
    #  298 LOAD_CONST 'UTF-8'
    #  300 PRECALL
    #  304 CALL
    #  314 STORE_FAST channel_name
    #  316 LOAD_FAST channel_names
    #  318 LOAD_METHOD append
    #  340 LOAD_FAST channel_name
    #  342 PRECALL
    #  346 CALL
    #  356 POP_TOP
    #  358 LOAD_FAST channel_index
    #  360 LOAD_FAST name_dict
    #  362 LOAD_FAST channel_name
    #  364 STORE_SUBSCR
    #  368 JUMP_BACKWARD to 206
    #  370 LOAD_GLOBAL QtWidgets
    #  382 LOAD_ATTR QInputDialog
    #  392 LOAD_METHOD getItem
    #  414 LOAD_FAST parent
    #  416 LOAD_CONST 'Select Channel'
    # ... bytecode truncated ...
    pass

def choose_synchronous_channels(header, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + SelectSynchronousDialog
    #   14 LOAD_FAST header
    #   16 LOAD_CONST 'streams'
    #   18 BINARY_SUBSCR
    #   28 LOAD_FAST header
    #   30 LOAD_CONST 'channels'
    #   32 BINARY_SUBSCR
    #   42 LOAD_FAST parent
    #   44 KW_NAMES
    #   46 PRECALL
    #   50 CALL
    #   60 STORE_FAST dialog
    #   62 LOAD_FAST dialog
    #   64 LOAD_METHOD exec
    #   86 PRECALL
    #   90 CALL
    #  100 STORE_FAST ret
    #  102 LOAD_FAST ret
    #  104 LOAD_CONST 0
    #  106 COMPARE_OP ==
    #  112 POP_JUMP_FORWARD_IF_FALSE to 118
    #  114 LOAD_CONST None
    #  116 RETURN_VALUE
    #  118 LOAD_FAST dialog
    #  120 LOAD_METHOD get_channel_list
    #  142 PRECALL
    #  146 CALL
    #  156 STORE_FAST channel_list
    #  158 LOAD_GLOBAL NULL + len
    #  170 LOAD_FAST channel_list
    #  172 PRECALL
    #  176 CALL
    #  186 LOAD_CONST 0
    #  188 COMPARE_OP ==
    #  194 POP_JUMP_FORWARD_IF_FALSE to 200
    #  196 LOAD_CONST None
    #  198 RETURN_VALUE
    #  200 LOAD_FAST channel_list
    #  202 RETURN_VALUE
    pass

class ChannelData:

    def __init__(self, stream, channel, channel_decoder):
        self.stream = stream
        self.channel = channel
        self.channel_decoder = channel_decoder
        self.samples = self.channel.samples
        self.subchannels = self.channel_decoder.subchannels
        if self.samples == 0 and self.subchannels == 0 or stream.rate == 0:
            raise ValueError('Invalid channel configuration')
        self.last_counter = -1
        self.lost_packet_list = []
        self.lost_packet_file_boundary_list = []
        self.file_boundary = False
        self.next_timestamp = 0
        self.allocated = 1000
        self.length = 0
        self.data = numpy.empty((self.allocated * self.samples, self.subchannels), dtype = numpy.double)
        self.indexes = numpy.empty((self.allocated,), dtype = numpy.uint64)
        self.timestamps = numpy.empty((self.allocated,), dtype = numpy.double)

    def set_file_boundary(self):
        self.file_boundary = True

    def set_next_timestamp(self, timestamp):
        self.next_timestamp = timestamp

    def trim(self):
        self.allocated = self.length
        self.data = self.data[0:self.length * self.samples]
        self.indexes = self.indexes[0:self.length]
        self.timestamps = self.timestamps[0:self.length]

    def decode_callback(self, counter, data, samples, subchannels):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR samples
        #   14 LOAD_FAST samples
        #   16 COMPARE_OP !=
        #   22 POP_JUMP_FORWARD_IF_FALSE to 54
        #   24 LOAD_GLOBAL NULL + ValueError
        #   36 LOAD_CONST 'Bad sample count in callback!'
        #   38 PRECALL
        #   42 CALL
        #   52 RAISE_VARARGS
        #   54 LOAD_FAST self
        #   56 LOAD_ATTR subchannels
        #   66 LOAD_FAST subchannels
        #   68 COMPARE_OP !=
        #   74 POP_JUMP_FORWARD_IF_FALSE to 106
        #   76 LOAD_GLOBAL NULL + ValueError
        #   88 LOAD_CONST 'Bad subchannel count in callback!'
        #   90 PRECALL
        #   94 CALL
        #  104 RAISE_VARARGS
        #  106 LOAD_FAST self
        #  108 LOAD_ATTR last_counter
        #  118 LOAD_CONST 1
        #  120 BINARY_OP +
        #  124 LOAD_FAST counter
        #  126 COMPARE_OP !=
        #  132 POP_JUMP_FORWARD_IF_FALSE to 304
        #  134 LOAD_FAST self
        #  136 LOAD_ATTR length
        #  146 LOAD_CONST 0
        #  148 COMPARE_OP !=
        #  154 POP_JUMP_FORWARD_IF_FALSE to 304
        #  156 LOAD_FAST self
        #  158 LOAD_ATTR last_counter
        #  168 LOAD_FAST counter
        #  170 LOAD_FAST self
        #  172 LOAD_ATTR length
        #  182 BUILD_TUPLE
        #  184 STORE_FAST lost_tuple
        #  186 LOAD_FAST self
        #  188 LOAD_ATTR lost_packet_list
        #  198 LOAD_METHOD append
        #  220 LOAD_FAST lost_tuple
        #  222 PRECALL
        #  226 CALL
        #  236 POP_TOP
        #  238 LOAD_FAST self
        #  240 LOAD_ATTR file_boundary
        #  250 POP_JUMP_FORWARD_IF_FALSE to 304
        #  252 LOAD_FAST self
        #  254 LOAD_ATTR lost_packet_file_boundary_list
        #  264 LOAD_METHOD append
        #  286 LOAD_FAST lost_tuple
        #  288 PRECALL
        #  292 CALL
        #  302 POP_TOP
        #  304 LOAD_FAST counter
        #  306 LOAD_FAST self
        #  308 STORE_ATTR last_counter
        #  318 LOAD_FAST self
        #  320 LOAD_ATTR length
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR allocated
        #  342 COMPARE_OP ==
        #  348 POP_JUMP_FORWARD_IF_FALSE to 796
        #  350 LOAD_FAST self
        #  352 LOAD_ATTR allocated
        #  362 LOAD_CONST 2
        #  364 BINARY_OP *
        #  368 LOAD_FAST self
        #  370 STORE_ATTR allocated
        #  380 LOAD_GLOBAL NULL + numpy
        #  392 LOAD_ATTR empty
        #  402 LOAD_FAST self
        #  404 LOAD_ATTR allocated
        #  414 LOAD_FAST self
        #  416 LOAD_ATTR samples
        #  426 BINARY_OP *
        #  430 LOAD_FAST self
        # ... bytecode truncated ...
        pass

def decode_batch(file_infos, header, channel_indexes, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL header
    #    2 RESUME
    #    4 BUILD_LIST
    #    6 STORE_FAST info_list
    #    8 LOAD_GLOBAL NULL + set
    #   20 LOAD_FAST channel_indexes
    #   22 PRECALL
    #   26 CALL
    #   36 STORE_FAST remaining_channels
    #   38 LOAD_DEREF header
    #   40 LOAD_CONST 'streams_to_activate'
    #   42 BINARY_SUBSCR
    #   52 GET_ITER
    #   54 FOR_ITER to 276
    #   56 STORE_FAST stream_id
    #   58 LOAD_DEREF header
    #   60 LOAD_CONST 'streams'
    #   62 BINARY_SUBSCR
    #   72 LOAD_FAST stream_id
    #   74 BINARY_SUBSCR
    #   84 STORE_FAST stream
    #   86 LOAD_FAST stream
    #   88 LOAD_ATTR channel_index_list
    #   98 LOAD_CONST 0
    #  100 LOAD_FAST stream
    #  102 LOAD_ATTR channel_count
    #  112 BUILD_SLICE
    #  114 BINARY_SUBSCR
    #  124 STORE_FAST indexes
    #  126 LOAD_CONST False
    #  128 STORE_FAST use_stream
    #  130 LOAD_FAST indexes
    #  132 GET_ITER
    #  134 FOR_ITER to 194
    #  136 STORE_FAST index
    #  138 LOAD_FAST index
    #  140 LOAD_FAST remaining_channels
    #  142 CONTAINS_OP
    #  144 POP_JUMP_FORWARD_IF_FALSE to 192
    #  146 LOAD_CONST True
    #  148 STORE_FAST use_stream
    #  150 LOAD_FAST remaining_channels
    #  152 LOAD_METHOD discard
    #  174 LOAD_FAST index
    #  176 PRECALL
    #  180 CALL
    #  190 POP_TOP
    #  192 JUMP_BACKWARD to 134
    #  194 LOAD_FAST use_stream
    #  196 POP_JUMP_FORWARD_IF_FALSE to 274
    #  198 LOAD_CLOSURE header
    #  200 BUILD_TUPLE
    #  202 LOAD_CONST <code object <listcomp> at 0x105abfa50, file "mondo\analysis\util.py", line 506>
    #  204 MAKE_FUNCTION closure
    #  206 LOAD_FAST indexes
    #  208 GET_ITER
    #  210 PRECALL
    #  214 CALL
    #  224 STORE_FAST channel_list
    #  226 LOAD_FAST info_list
    #  228 LOAD_METHOD append
    #  250 LOAD_FAST stream_id
    #  252 LOAD_FAST stream
    #  254 LOAD_FAST channel_list
    #  256 BUILD_TUPLE
    #  258 PRECALL
    #  262 CALL
    #  272 POP_TOP
    #  274 JUMP_BACKWARD to 54
    #  276 LOAD_GLOBAL asphodel
    #  288 LOAD_ATTR nativelib
    #  298 LOAD_METHOD create_device_decoder
    #  320 LOAD_FAST info_list
    #  322 LOAD_DEREF header
    #  324 LOAD_CONST 'stream_filler_bits'
    #  326 BINARY_SUBSCR
    #  336 LOAD_DEREF header
    #  338 LOAD_CONST 'stream_id_bits'
    #  340 BINARY_SUBSCR
    #  350 PRECALL
    # ... bytecode truncated ...
    pass

def get_datetime_subset(batch_info, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + sorted
    #   14 LOAD_FAST batch_info
    #   16 LOAD_METHOD items
    #   38 PRECALL
    #   42 CALL
    #   52 PRECALL
    #   56 CALL
    #   66 GET_ITER
    #   68 FOR_ITER to 556
    #   70 UNPACK_SEQUENCE
    #   74 STORE_FAST _channel_index
    #   76 STORE_FAST channel_data
    #   78 LOAD_FAST channel_data
    #   80 LOAD_ATTR channel_decoder
    #   90 LOAD_ATTR channel_name
    #  100 STORE_FAST channel_name
    #  102 LOAD_GLOBAL NULL + numpy
    #  114 LOAD_ATTR diff
    #  124 LOAD_FAST channel_data
    #  126 LOAD_ATTR timestamps
    #  136 PRECALL
    #  140 CALL
    #  150 STORE_FAST d
    #  152 LOAD_GLOBAL NULL + numpy
    #  164 LOAD_ATTR min
    #  174 LOAD_FAST d
    #  176 PRECALL
    #  180 CALL
    #  190 LOAD_CONST 0.0
    #  192 COMPARE_OP <
    #  198 POP_JUMP_FORWARD_IF_FALSE to 554
    #  200 LOAD_CONST 'Timestamps are not monotonic on channel {}! Continue?'
    #  202 STORE_FAST s
    #  204 LOAD_FAST s
    #  206 LOAD_METHOD format
    #  228 LOAD_FAST channel_name
    #  230 PRECALL
    #  234 CALL
    #  244 STORE_FAST message
    #  246 LOAD_GLOBAL logger
    #  258 LOAD_METHOD warning
    #  280 LOAD_FAST message
    #  282 PRECALL
    #  286 CALL
    #  296 POP_TOP
    #  298 LOAD_GLOBAL QtWidgets
    #  310 LOAD_ATTR QMessageBox
    #  320 LOAD_METHOD warning
    #  342 LOAD_FAST parent
    #  344 LOAD_CONST 'Warning'
    #  346 LOAD_FAST message
    #  348 LOAD_GLOBAL QtWidgets
    #  360 LOAD_ATTR QMessageBox
    #  370 LOAD_ATTR StandardButton
    #  380 LOAD_ATTR Yes
    #  390 LOAD_GLOBAL QtWidgets
    #  402 LOAD_ATTR QMessageBox
    #  412 LOAD_ATTR StandardButton
    #  422 LOAD_ATTR No
    #  432 BINARY_OP |
    #  436 LOAD_GLOBAL QtWidgets
    #  448 LOAD_ATTR QMessageBox
    #  458 LOAD_ATTR StandardButton
    #  468 LOAD_ATTR Yes
    #  478 KW_NAMES
    #  480 PRECALL
    #  484 CALL
    #  494 STORE_FAST ret
    #  496 LOAD_FAST ret
    #  498 LOAD_GLOBAL QtWidgets
    #  510 LOAD_ATTR QMessageBox
    #  520 LOAD_ATTR StandardButton
    #  530 LOAD_ATTR No
    #  540 COMPARE_OP ==
    #  546 POP_JUMP_FORWARD_IF_FALSE to 554
    #  548 POP_TOP
    #  550 LOAD_CONST None
    #  552 RETURN_VALUE
    #  554 JUMP_BACKWARD to 68
    # ... bytecode truncated ...
    pass

def warn_about_lost_packets(batch_info, parent, once):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + sorted
    #   14 LOAD_FAST batch_info
    #   16 LOAD_METHOD items
    #   38 PRECALL
    #   42 CALL
    #   52 PRECALL
    #   56 CALL
    #   66 GET_ITER
    #   68 EXTENDED_ARG
    #   70 FOR_ITER to 904
    #   72 UNPACK_SEQUENCE
    #   76 STORE_FAST _channel_index
    #   78 STORE_FAST channel_data
    #   80 LOAD_FAST channel_data
    #   82 LOAD_ATTR channel_decoder
    #   92 LOAD_ATTR channel_name
    #  102 STORE_FAST channel_name
    #  104 LOAD_GLOBAL NULL + len
    #  116 LOAD_FAST channel_data
    #  118 LOAD_ATTR timestamps
    #  128 PRECALL
    #  132 CALL
    #  142 LOAD_CONST 2
    #  144 COMPARE_OP <
    #  150 POP_JUMP_FORWARD_IF_FALSE to 154
    #  152 JUMP_BACKWARD to 68
    #  154 LOAD_CONST 0
    #  156 STORE_FAST lost_packets
    #  158 LOAD_CONST 0
    #  160 STORE_FAST lost_sections
    #  162 LOAD_FAST channel_data
    #  164 LOAD_ATTR lost_packet_list
    #  174 GET_ITER
    #  176 FOR_ITER to 226
    #  178 UNPACK_SEQUENCE
    #  182 STORE_FAST last
    #  184 STORE_FAST current
    #  186 STORE_FAST _i
    #  188 LOAD_FAST current
    #  190 LOAD_FAST last
    #  192 BINARY_OP -
    #  196 LOAD_CONST 1
    #  198 BINARY_OP -
    #  202 STORE_FAST packets_lost
    #  204 LOAD_FAST lost_packets
    #  206 LOAD_FAST packets_lost
    #  208 BINARY_OP +=
    #  212 STORE_FAST lost_packets
    #  214 LOAD_FAST lost_sections
    #  216 LOAD_CONST 1
    #  218 BINARY_OP +=
    #  222 STORE_FAST lost_sections
    #  224 JUMP_BACKWARD to 176
    #  226 LOAD_CONST 0
    #  228 STORE_FAST lost_packets_file_boundaries
    #  230 LOAD_CONST 0
    #  232 STORE_FAST lost_sections_file_boundaries
    #  234 LOAD_FAST channel_data
    #  236 LOAD_ATTR lost_packet_file_boundary_list
    #  246 GET_ITER
    #  248 FOR_ITER to 298
    #  250 UNPACK_SEQUENCE
    #  254 STORE_FAST last
    #  256 STORE_FAST current
    #  258 STORE_FAST _i
    #  260 LOAD_FAST current
    #  262 LOAD_FAST last
    #  264 BINARY_OP -
    #  268 LOAD_CONST 1
    #  270 BINARY_OP -
    #  274 STORE_FAST packets_lost
    #  276 LOAD_FAST lost_packets_file_boundaries
    #  278 LOAD_FAST packets_lost
    #  280 BINARY_OP +=
    #  284 STORE_FAST lost_packets_file_boundaries
    #  286 LOAD_FAST lost_sections_file_boundaries
    #  288 LOAD_CONST 1
    #  290 BINARY_OP +=
    #  294 STORE_FAST lost_sections_file_boundaries
    # ... bytecode truncated ...
    pass

def sequence_data(batch_info, parent, chunk, raw_units, unscaled_units):
    sequence_info = { }
    unit_info = { }
    for channel_index, channel_data in sorted(batch_info.items()):
        indexes = channel_data.indexes - channel_data.indexes[0]
        repeated_indexes = numpy.repeat(indexes.astype(numpy.double), channel_data.samples)
        fractional_section = numpy.array(range(channel_data.samples), dtype = numpy.double) / channel_data.samples
        fractional_indexes = numpy.tile(fractional_section, channel_data.length)
        orig_time = (repeated_indexes + fractional_indexes) / channel_data.stream.rate
        orig_data = channel_data.data
        if raw_units:
            unit_formatter = asphodel.nativelib.create_unit_formatter(channel_data.channel.unit_type, 0, 0, channel_data.channel.resolution, use_metric = True)
        elif unscaled_units:
            ch_min = 0
            ch_max = 0
        else:
            ch_min = numpy.nanmin(orig_data).item()
            ch_max = numpy.nanmax(orig_data).item()
        settings = QtCore.QSettings()
        unit_formatter = hyperborea.unit_preferences.create_unit_formatter(settings, channel_data.channel.unit_type, ch_min, ch_max, channel_data.channel.resolution)
        unit_info[channel_index] = UnitInfo(unit_formatter.unit_ascii, unit_formatter.unit_html, unit_formatter.unit_utf8, unit_formatter)
        orig_data = orig_data * unit_formatter.conversion_scale + unit_formatter.conversion_offset
        if chunk:
            chunk_list = []
            last_data_index = 0
            last_timestamp_index = 0
            for _x, _y, index in enumerate(channel_data.lost_packet_list):
                data_index = index * channel_data.samples
                new_data = orig_data[last_data_index:data_index]
                new_time = orig_time[last_data_index:data_index]
                start = channel_data.timestamps[last_timestamp_index]
                end = channel_data.timestamps[index - 1]
                last_data_index = data_index
                last_timestamp_index = index
                chunk_list.append((new_time, new_data, start, end))
                new_data = orig_data[last_data_index:]
                new_time = orig_time[last_data_index:]
                start = channel_data.timestamps[last_timestamp_index]
                end = channel_data.timestamps[-1]
                chunk_list.append((new_time, new_data, start, end))
                sequence_info[channel_index] = chunk_list
                nan_count = len(channel_data.lost_packet_list)
                new_shape = (orig_data.shape[0] + nan_count, orig_data.shape[1])
                new_data = numpy.empty(new_shape)
                nan_slice = numpy.full((), numpy.nan, dtype = numpy.double)
                new_time = numpy.empty((new_shape[0],))
                last = 0
                for _x, _y, index in enumerate(channel_data.lost_packet_list):
                    index *= channel_data.samples
                    new_data[last + i:index + i] = orig_data[last:index]
                    new_data[index + i] = nan_slice
                    new_time[last + i:index + i] = orig_time[last:index]
                    new_time[index + i] = orig_time[index - 1] + 1 / (channel_data.stream.rate * channel_data.samples)
                    last = index
                    new_data[last + nan_count:] = orig_data[last:]
                    new_time[last + nan_count:] = orig_time[last:]
                    start_time = channel_data.timestamps[0]
                    end_time = channel_data.timestamps[-1]
                    sequence_info[channel_index] = [
                        (new_time, new_data, start_time, end_time)]
                    return (sequence_info, unit_info)

def choose_subchannel(channel_data, allow_all, parent):
    options = list(channel_data.channel_decoder.subchannel_names)
    if len(options) == 1:
        return 0
    if None:
        options.insert(0, 'All Subchannels')
    (value, ok) = QtWidgets.QInputDialog.getItem(parent, 'Select Subchannel', 'Select Subchannel', options, 0, editable = False)
    if not ok:
        return None

    try:
        return channel_data.channel_decoder.subchannel_names.index(value)
    except ValueError:
        return -1

def choose_subchannels(header, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL header
    #    2 RESUME
    #    4 BUILD_LIST
    #    6 STORE_FAST info_list
    #    8 LOAD_GLOBAL NULL + set
    #   20 PRECALL
    #   24 CALL
    #   34 STORE_FAST channel_indexes
    #   36 LOAD_DEREF header
    #   38 LOAD_CONST 'streams_to_activate'
    #   40 BINARY_SUBSCR
    #   50 GET_ITER
    #   52 FOR_ITER to 254
    #   54 STORE_FAST stream_id
    #   56 LOAD_DEREF header
    #   58 LOAD_CONST 'streams'
    #   60 BINARY_SUBSCR
    #   70 LOAD_FAST stream_id
    #   72 BINARY_SUBSCR
    #   82 STORE_FAST stream
    #   84 LOAD_FAST stream
    #   86 LOAD_ATTR channel_index_list
    #   96 LOAD_CONST 0
    #   98 LOAD_FAST stream
    #  100 LOAD_ATTR channel_count
    #  110 BUILD_SLICE
    #  112 BINARY_SUBSCR
    #  122 STORE_FAST indexes
    #  124 LOAD_FAST indexes
    #  126 GET_ITER
    #  128 FOR_ITER to 176
    #  130 STORE_FAST index
    #  132 LOAD_FAST channel_indexes
    #  134 LOAD_METHOD add
    #  156 LOAD_FAST index
    #  158 PRECALL
    #  162 CALL
    #  172 POP_TOP
    #  174 JUMP_BACKWARD to 128
    #  176 LOAD_CLOSURE header
    #  178 BUILD_TUPLE
    #  180 LOAD_CONST <code object <listcomp> at 0x105ba4120, file "mondo\analysis\util.py", line 993>
    #  182 MAKE_FUNCTION closure
    #  184 LOAD_FAST indexes
    #  186 GET_ITER
    #  188 PRECALL
    #  192 CALL
    #  202 STORE_FAST channel_list
    #  204 LOAD_FAST info_list
    #  206 LOAD_METHOD append
    #  228 LOAD_FAST stream_id
    #  230 LOAD_FAST stream
    #  232 LOAD_FAST channel_list
    #  234 BUILD_TUPLE
    #  236 PRECALL
    #  240 CALL
    #  250 POP_TOP
    #  252 JUMP_BACKWARD to 52
    #  254 LOAD_GLOBAL asphodel
    #  266 LOAD_ATTR nativelib
    #  276 LOAD_METHOD create_device_decoder
    #  298 LOAD_FAST info_list
    #  300 LOAD_DEREF header
    #  302 LOAD_CONST 'stream_filler_bits'
    #  304 BINARY_SUBSCR
    #  314 LOAD_DEREF header
    #  316 LOAD_CONST 'stream_id_bits'
    #  318 BINARY_SUBSCR
    #  328 PRECALL
    #  332 CALL
    #  342 STORE_FAST decoder
    #  344 LOAD_GLOBAL NULL + set
    #  356 LOAD_FAST channel_indexes
    #  358 PRECALL
    #  362 CALL
    #  372 STORE_FAST remaining_channels
    #  374 BUILD_LIST
    #  376 STORE_FAST names
    #  378 NOP
    #  380 LOAD_FAST decoder
    # ... bytecode truncated ...
    pass

def get_contiguous_chunk(sequence, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + len
    #   14 LOAD_FAST sequence
    #   16 PRECALL
    #   20 CALL
    #   30 LOAD_CONST 1
    #   32 COMPARE_OP ==
    #   38 POP_JUMP_FORWARD_IF_FALSE to 56
    #   40 LOAD_FAST sequence
    #   42 LOAD_CONST 0
    #   44 BINARY_SUBSCR
    #   54 RETURN_VALUE
    #   56 BUILD_LIST
    #   58 STORE_FAST str_list
    #   60 BUILD_MAP
    #   62 STORE_FAST str_indexes
    #   64 LOAD_CONST 0
    #   66 STORE_FAST max_points
    #   68 LOAD_CONST 0
    #   70 STORE_FAST max_index
    #   72 LOAD_GLOBAL NULL + enumerate
    #   84 LOAD_FAST sequence
    #   86 PRECALL
    #   90 CALL
    #  100 GET_ITER
    #  102 FOR_ITER to 450
    #  104 UNPACK_SEQUENCE
    #  108 STORE_FAST i
    #  110 UNPACK_SEQUENCE
    #  114 STORE_FAST time
    #  116 STORE_FAST _data
    #  118 STORE_FAST start_time
    #  120 STORE_FAST _end_time
    #  122 LOAD_GLOBAL NULL + len
    #  134 LOAD_FAST time
    #  136 PRECALL
    #  140 CALL
    #  150 STORE_FAST points
    #  152 LOAD_FAST max_points
    #  154 LOAD_FAST points
    #  156 COMPARE_OP <
    #  162 POP_JUMP_FORWARD_IF_FALSE to 172
    #  164 LOAD_FAST points
    #  166 STORE_FAST max_points
    #  168 LOAD_FAST i
    #  170 STORE_FAST max_index
    #  172 LOAD_FAST time
    #  174 LOAD_CONST -1
    #  176 BINARY_SUBSCR
    #  186 LOAD_FAST time
    #  188 LOAD_CONST 0
    #  190 BINARY_SUBSCR
    #  200 BINARY_OP -
    #  204 STORE_FAST duration
    #  206 LOAD_GLOBAL datetime
    #  218 LOAD_ATTR datetime
    #  228 LOAD_METHOD fromtimestamp
    #  250 LOAD_FAST start_time
    #  252 LOAD_GLOBAL datetime
    #  264 LOAD_ATTR timezone
    #  274 LOAD_ATTR utc
    #  284 PRECALL
    #  288 CALL
    #  298 STORE_FAST start_dt
    #  300 LOAD_FAST start_dt
    #  302 LOAD_METHOD strftime
    #  324 LOAD_CONST '%Y-%m-%d %H:%M:%S (UTC)'
    #  326 PRECALL
    #  330 CALL
    #  340 STORE_FAST start_str
    #  342 LOAD_CONST '{} points ({} s), starting {}'
    #  344 LOAD_METHOD format
    #  366 LOAD_FAST points
    #  368 LOAD_FAST duration
    #  370 LOAD_FAST start_str
    #  372 PRECALL
    #  376 CALL
    #  386 STORE_FAST s
    #  388 LOAD_FAST s
    #  390 LOAD_FAST str_list
    # ... bytecode truncated ...
    pass

def get_psd_options(chunks_list, sampling_rate, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + PSDOptionsDialog
    #   14 LOAD_FAST chunks_list
    #   16 LOAD_FAST sampling_rate
    #   18 LOAD_FAST parent
    #   20 PRECALL
    #   24 CALL
    #   34 STORE_FAST dialog
    #   36 LOAD_FAST dialog
    #   38 LOAD_METHOD exec
    #   60 PRECALL
    #   64 CALL
    #   74 STORE_FAST ret
    #   76 LOAD_FAST ret
    #   78 LOAD_CONST 0
    #   80 COMPARE_OP ==
    #   86 POP_JUMP_FORWARD_IF_FALSE to 92
    #   88 LOAD_CONST None
    #   90 RETURN_VALUE
    #   92 LOAD_FAST dialog
    #   94 LOAD_METHOD get_options
    #  116 PRECALL
    #  120 CALL
    #  130 RETURN_VALUE
    pass

def get_multiple_psd_options(sections, parent):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + MultiplePSDOptionsDialog
    #   14 LOAD_FAST sections
    #   16 LOAD_FAST parent
    #   18 PRECALL
    #   22 CALL
    #   32 STORE_FAST dialog
    #   34 LOAD_FAST dialog
    #   36 LOAD_METHOD exec
    #   58 PRECALL
    #   62 CALL
    #   72 STORE_FAST ret
    #   74 LOAD_FAST ret
    #   76 LOAD_CONST 0
    #   78 COMPARE_OP ==
    #   84 POP_JUMP_FORWARD_IF_FALSE to 90
    #   86 LOAD_CONST None
    #   88 RETURN_VALUE
    #   90 LOAD_FAST dialog
    #   92 LOAD_METHOD get_options
    #  114 PRECALL
    #  118 CALL
    #  128 RETURN_VALUE
    pass
