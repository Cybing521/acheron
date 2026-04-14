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
from datetime_subset import DateTimeSubsetDialog
from psd_options import Chunk, PSDOptions, PSDOptionsDialog, MultiplePSDOptionsDialog
from select_subchannels import SelectSubchannelsDialog
from select_synchronous import SelectSynchronousDialog
logger = logging.getLogger(__name__)
UnitInfo = <NODE:12>()

def get_packdata_file(parent = None):
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


def get_packdata_files(parent = None):
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


def decode_header(header_bytes = None, parent = None):
    
    try:
        header_str = header_bytes.decode('UTF-8')
        header = json.loads(header_str)
    except Exception:
        message = 'Could not parse file header!'
        logger.exception(message)
        QtWidgets.QMessageBox.critical(parent, 'Error', message)
        return 

# WARNING: Decompyle incomplete


def load_single_file(parent = None):
    """
    returns (file_infos, header) where file_infos is a sequence of tuples
    containing (filename, dt).
    * header is the dictionary loaded from the file's JSON data, with
      appropriate conversions applied to Asphodel struct data.
    * filename is the absolute path to the file location.
    * dt is the UTC datetime of the first packet in the file.
    """
    filename = get_packdata_file(parent)
# WARNING: Decompyle incomplete


def load_batch(parent = None):
    """
    returns (file_infos, header) where file_infos is a sequence of tuples
    containing (filename, dt).
    * header is the dictionary loaded from the file's JSON data, with
      appropriate conversions applied to Asphodel struct data.
    * filename is the absolute path to the file location.
    * dt is the UTC datetime of the first packet in the file.
    """
    first_file = True
    loaded_files = []
    file_infos = []
    files = get_packdata_files(parent)
    if not files:
        if first_file:
            return None
        files = None
    for filename in files:
        if filename in loaded_files:
            message = 'File {} already loaded! Skipping.'.format(filename)
            logger.info(message)
            QtWidgets.QMessageBox.information(parent, 'Already Loaded', message)
            continue
        f = lzma.LZMAFile(filename, 'rb')
        header_leader = struct.unpack('>dI', f.read(12))
        header_dt = datetime.datetime.fromtimestamp(header_leader[0], datetime.timezone.utc)
        header_bytes = f.read(header_leader[1])
        if len(header_bytes) == 0:
            message = 'Empty header in {}!'.format(filename)
            logger.error(message)
            QtWidgets.QMessageBox.critical(parent, 'Error', message)
            None(None, None)
            return None
        first_packet_timestamp = None.unpack('>d', f.read(8))[0]
        first_packet_dt = datetime.datetime.fromtimestamp(first_packet_timestamp, datetime.timezone.utc)
        if first_file:
            first_file = False
            first_header_bytes = header_bytes
            first_header_dt = header_dt
            header = decode_header(header_bytes, parent)
            if not header:
                None(None, None)
                return None
        if first_header_bytes != header_bytes or first_header_dt != header_dt:
            s = 'Headers do not match on {}!\n\nFiles must come from the same session.'
            message = s.format(filename)
            logger.error(message)
            QtWidgets.QMessageBox.critical(parent, 'Error', message)
            None(None, None)
            return None
        None.append((filename, first_packet_dt))
        loaded_files.append(filename)
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        message = 'Could not read header on {}!'.format(filename)
        logger.exception(message)
        QtWidgets.QMessageBox.critical(parent, 'Error', message)
        return None
    ret = QtWidgets.QMessageBox.question(parent, 'More Files?', 'Load more files for this batch?', buttons = QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, defaultButton = QtWidgets.QMessageBox.StandardButton.No)
    if ret != QtWidgets.QMessageBox.StandardButton.Yes:
        pass
    
    return (file_infos, header)


def choose_channel(header = None, parent = None):
    '''
    returns a channel index selected by the user.
    '''
    channel_indexes = set()
    for stream_id in header['streams_to_activate']:
        stream = header['streams'][stream_id]
        for index in stream.channel_index_list[0:stream.channel_count]:
            channel_indexes.add(index)
            channel_names = []
            name_dict = { }
            for channel_index in sorted(channel_indexes):
                channel = header['channels'][channel_index]
                channel_name = channel.name[0:channel.name_length].decode('UTF-8')
                channel_names.append(channel_name)
                name_dict[channel_name] = channel_index
                (value, ok) = QtWidgets.QInputDialog.getItem(parent, 'Select Channel', 'Select Channel', channel_names, 0, editable = False)
                if not ok:
                    return None
                return None[value]


def choose_synchronous_channels(header = None, parent = None):
    '''
    returns a sequence of channel indexes selected by the user, from a single
    stream.
    '''
    dialog = SelectSynchronousDialog(header['streams'], header['channels'], parent = parent)
    ret = dialog.exec()
    if ret == 0:
        return None
    channel_list = None.get_channel_list()
    if len(channel_list) == 0:
        return None


class ChannelData:
    
    def __init__(self = None, stream = None, channel = None, channel_decoder = ('stream', asphodel.AsphodelStreamInfo, 'channel', asphodel.AsphodelChannelInfo, 'channel_decoder', asphodel.AsphodelNativeChannelDecoder)):
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

    
    def set_file_boundary(self = None):
        self.file_boundary = True

    
    def set_next_timestamp(self = None, timestamp = None):
        self.next_timestamp = timestamp

    
    def trim(self = None):
        self.allocated = self.length
        self.data = self.data[0:self.length * self.samples]
        self.indexes = self.indexes[0:self.length]
        self.timestamps = self.timestamps[0:self.length]

    
    def decode_callback(self, counter = None, data = None, samples = None, subchannels = ('counter', int, 'data', list[float], 'samples', int, 'subchannels', int, 'return', None)):
        if self.samples != samples:
            raise ValueError('Bad sample count in callback!')
        if self.subchannels != subchannels:
            raise ValueError('Bad subchannel count in callback!')
        if self.last_counter + 1 != counter and self.length != 0:
            lost_tuple = (self.last_counter, counter, self.length)
            self.lost_packet_list.append(lost_tuple)
            if self.file_boundary:
                self.lost_packet_file_boundary_list.append(lost_tuple)
        self.last_counter = counter
        if self.length == self.allocated:
            self.allocated = self.allocated * 2
            new_data = numpy.empty((self.allocated * self.samples, self.subchannels), dtype = numpy.double)
            new_data[0:self.length * self.samples] = self.data
            self.data = new_data
            new_indexes = numpy.empty((self.allocated,), dtype = numpy.uint64)
            new_indexes[0:self.length] = self.indexes
            self.indexes = new_indexes
            new_timestamps = numpy.empty((self.allocated,), dtype = numpy.double)
            new_timestamps[0:self.length] = self.timestamps
            self.timestamps = new_timestamps
        d = numpy.array(data).reshape(samples, subchannels)
        self.indexes[self.length] = counter
        self.timestamps[self.length] = self.next_timestamp
        self.data[self.length * samples:(self.length + 1) * samples] = d
        if self.file_boundary:
            False = self, self.length += 1, .length
            return None
        return self, self.length += 1, .length



def decode_batch(file_infos = None, header = None, channel_indexes = None, parent = ('file_infos', list[tuple[(str, datetime.datetime)]], 'header', dict, 'channel_indexes', Iterable[int], 'parent', QtWidgets.QWidget, 'return', Optional[dict[(int, ChannelData)]])):
    '''
    returns a map with keys of channel indexes, values of ChannelData
    '''
    pass
# WARNING: Decompyle incomplete


def get_datetime_subset(batch_info = None, parent = None):
    '''
    filters data by datetime, provided by the user.
    '''
    for _channel_index, channel_data in sorted(batch_info.items()):
        channel_name = channel_data.channel_decoder.channel_name
        d = numpy.diff(channel_data.timestamps)
        if numpy.min(d) < 0:
            s = 'Timestamps are not monotonic on channel {}! Continue?'
            message = s.format(channel_name)
            logger.warning(message)
            ret = QtWidgets.QMessageBox.warning(parent, 'Warning', message, buttons = QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, defaultButton = QtWidgets.QMessageBox.StandardButton.Yes)
            if ret == QtWidgets.QMessageBox.StandardButton.No:
                return None
            starts = batch_info.values()()
            ends = batch_info.values()()
            start = datetime.datetime.fromtimestamp(numpy.floor(min(starts)), datetime.timezone.utc)
            end = datetime.datetime.fromtimestamp(numpy.ceil(max(ends)), datetime.timezone.utc)
            start_qdt = QtCore.QDateTime(start)
            end_qdt = QtCore.QDateTime(end)
            dialog = DateTimeSubsetDialog(start_qdt, end_qdt, parent)
            dialog_ret = dialog.exec()
            if dialog_ret == 0:
                return None
            if (lambda .0: [ d.timestamps[-1] for d in .0 ]).should_use_all():
                return batch_info
            (start_qdt, end_qdt) = (lambda .0: [ d.timestamps[0] for d in .0 ]).get_subset()
            utc = datetime.timezone.utc
            start = cast(datetime.datetime, start_qdt.toPython()).replace(tzinfo = utc).timestamp()
            end = cast(datetime.datetime, end_qdt.toPython()).replace(tzinfo = utc).timestamp()
            new_indexes = { }
            some_empty = False
            for channel_index, channel_data in batch_info.items():
                start_index = bisect.bisect_left(channel_data.timestamps, start)
                end_index = bisect.bisect_right(channel_data.timestamps, end)
                if start_index >= end_index:
                    some_empty = True
                new_indexes[channel_index] = (start_index, end_index)
                if some_empty:
                    message = 'No data is present within this interval on one or more channels.'
                    logger.warning(message)
                    QtWidgets.QMessageBox.warning(parent, 'Warning', message)
                    continue
    for channel_index, channel_data in batch_info.items():
        (start_index, end_index) = new_indexes[channel_index]
        if start_index >= end_index:
            start_index = 0
            end_index = 0
        data_start = start_index * channel_data.samples
        data_end = end_index * channel_data.samples
        channel_data.data = channel_data.data[data_start:data_end]
        channel_data.indexes = channel_data.indexes[start_index:end_index]
        channel_data.timestamps = channel_data.timestamps[start_index:end_index]
        
        def trim_list(lost_packet_list = None, start_index = None, end_index = None):
            new_lost_packet_list = []
            for last, current, index in lost_packet_list:
                if index > start_index and index < end_index:
                    new_lost_packet_list.append((last, current, index - start_index))
                return new_lost_packet_list

        channel_data.lost_packet_list = trim_list(channel_data.lost_packet_list, start_index, end_index)
        channel_data.lost_packet_file_boundary_list = trim_list(channel_data.lost_packet_file_boundary_list, start_index, end_index)
        channel_data.length = end_index - start_index
        channel_data.allocated = channel_data.length
        return batch_info


def warn_about_lost_packets(batch_info = None, parent = None, once = None):
