# Source Generated with Decompyle++
# File: writer.pyc (Python 3.11)

import binascii
import ctypes
from dataclasses import fields
import datetime
import json
import logging
import os
from queue import Empty, Queue
import re
import struct
import subprocess
import sys
import threading
import time
from typing import Any, IO, Iterable, Optional, Protocol
import unicodedata
from asphodel.device_info import DeviceInfo
from compressor import open_compressor
from schedule import OutputConfig, ScheduleItem
logger = logging.getLogger(__name__)
UPLOAD_EXTENSION = '.upload'

class WriterStatusCallback(Protocol):
    
    def writer_file_started(self = None, filename = None, schedule_id = None, marked_for_upload = ('filename', str, 'schedule_id', str, 'marked_for_upload', bool, 'return', None)):
        pass

    
    def writer_file_finished(self = None, filename = None, schedule_id = None, marked_for_upload = ('filename', str, 'schedule_id', str, 'marked_for_upload', bool, 'return', None)):
        pass

    
    def writer_stopped(self = None, schedule_id = None, success = None):
        pass



def _get_valid_filename(s = None):
    b = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    s = b.decode('ascii')
    s = s.strip().replace(' ', '_')
    s = re.sub('[^-\\w.]', '', s)
    s = re.sub('[.]{2,}', '.', s)
    s = s.strip('.')
    return s


class StreamWriter:
    
    def __init__(self, logger, device_info, extra_info = None, schedule_item = None, default_output_config = None, writer_status_callback = ('logger', logging.LoggerAdapter, 'device_info', DeviceInfo, 'extra_info', dict, 'schedule_item', ScheduleItem, 'default_output_config', OutputConfig, 'writer_status_callback', WriterStatusCallback)):
        self.logger = logger
        self.device_info = device_info
        self.extra_info = extra_info
        self.schedule_item = schedule_item
        self.default_output_config = default_output_config
        self.writer_status_callback = writer_status_callback
    # WARNING: Decompyle incomplete

    
    def calc_filename_parts(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def create_header(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_filename(self = None, dt = None):
        if self.output_config.date_dir_structure:
            date_dir = dt.strftime('%Y_%m_%d')
        else:
            date_dir = ''
        directory = os.path.join(self.output_config.base_directory, date_dir, self.device_directory)
        os.makedirs(directory, exist_ok = True)
        if self.output_config.datetime_filename:
            base_name = dt.strftime('%Y%m%dT%H%MZ_') + self.base_name
        else:
            base_name = self.base_name
        base_name = os.path.join(directory, base_name)
        filename = base_name + '.apd'
        index = 1
    # WARNING: Decompyle incomplete

    
    def open_compressor(self = None, dt = None):
        filename = self.get_filename(dt)
        self.current_filename = filename
        (pipe, process) = open_compressor(filename, self.output_config.compression_level)
        self.compressor_pipe = pipe
        if process:
            self.compressor_lock
            self.compressors[filename] = process
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        pipe.write(self.header_bytes)
        if self.output_config.upload_marker:
            (path, name) = os.path.split(filename)
            uploadfilename = os.path.join(path, '.' + name + UPLOAD_EXTENSION)
            uploadfile = open(uploadfilename, 'w', encoding = 'ascii')
            uploadfile.write('in progress')
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        if sys.platform == 'win32':
            ctypes.windll.kernel32.SetFileAttributesW(uploadfilename, 2)
        
        try:
            self.writer_status_callback.writer_file_started(filename, self.schedule_item.id, self.output_config.upload_marker)
            return None
        except Exception:
            self.logger.exception('Exception in writer_file_started callback')
            return None


    
    def close_compressor(self = None):
        if self.compressor_pipe:
            self.compressor_pipe.close()
            self.compressor_pipe = None
            return None

    
    def mark_finished(self = None, filename = None):
        if filename:
            self.finished_queue.put(filename)
            return None

    
    def write(self = None, stream_packets = None):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.write_queue.put((b''.join(stream_packets), now))

    
    def calc_stop_time_target(self = None):
        t = None
        if self.collection_time_actual and self.schedule_item.duration:
            t = self.collection_time_actual + self.schedule_item.duration
        if self.schedule_item.stop_time:
            if t:
                t = min(t, self.schedule_item.stop_time)
            else:
                t = self.schedule_item.stop_time
        if self.schedule_item.failure_time:
            if t:
                t = min(t, self.schedule_item.failure_time)
            else:
                t = self.schedule_item.stop_time
        self.stop_time_target = t

    
    def calc_next_boundary(self = None, dt = None):
        if self.output_config.roll_over_interval:
            interval = self.output_config.roll_over_interval.total_seconds()
            seconds = (dt.hour * 60 + dt.minute) * 60 + dt.second
            partial = datetime.timedelta(seconds = seconds % interval, microseconds = dt.microsecond)
            boundary = (dt - partial) + datetime.timedelta(seconds = interval)
            return boundary
        return None.datetime.max

    
    def handle_write(self = None, stream_packets = None, dt = None):
        pass
    # WARNING: Decompyle incomplete

    
    def write_loop(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def monitor_loop(self = None):
        
        try:
            
            try:
                filename = self.finished_queue.get(True, 0.1)
                self.compressor_lock
                compressor = self.compressors.get(filename)
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                if compressor:
                                    ret_val = compressor.wait()
                                    if ret_val != 0:
                                        msg = 'Compressor exited with error {}'
                                        self.logger.warning(msg.format(ret_val))
                                    self.compressor_lock
                                    del self.compressors[filename]
                                    
                                    try:
                                        None(None, None)
                                    with None:
                                        if not None:
                                            
                                            try:
                                                
                                                try:
                                                    if self.output_config.upload_marker:
                                                        (path, name) = os.path.split(filename)
                                                        uploadfilename = os.path.join(path, '.' + name + UPLOAD_EXTENSION)
                                                        uploadfile = open(uploadfilename, 'r+', encoding = 'ascii')
                                                        uploadfile.seek(0)
                                                        uploadfile.truncate()
                                                        
                                                        try:
                                                            None(None, None)
                                                        with None:
                                                            if not None:
                                                                
                                                                try:
                                                                    
                                                                    try:
                                                                        
                                                                        try:
                                                                            self.writer_status_callback.writer_file_finished(filename, self.schedule_item.id, self.output_config.upload_marker)
                                                                            
                                                                            try:
                                                                                pass
                                                                            except Exception:
                                                                                self.logger.exception('Exception in writer_file_finished callback')
                                                                                
                                                                                try:
                                                                                    pass
                                                                                try:
                                                                                    
                                                                                    try:
                                                                                        pass
                                                                                    except Empty:
                                                                                        if self.write_loop_exited.is_set():
                                                                                            
                                                                                            try:
                                                                                                pass
                                                                                            except:
                                                                                                
                                                                                                try:
                                                                                                    continue
                                                                                                    self.compressor_lock
                                                                                                    for filename, compressor in self.compressors.items():
                                                                                                        ret_val = compressor.wait()
                                                                                                        msg = 'Uncollected compressor exited with code {}'
                                                                                                        self.logger.warning(msg.format(ret_val))
                                                                                                        self.writer_status_callback.writer_file_finished(filename, self.schedule_item.id, self.output_config.upload_marker)
                                                                                                        except Exception:
                                                                                                            self.logger.exception('Exception in writer_file_finished exit callback')
                                                                                                            continue
                                                                                                        self.compressors.clear()
                                                                                                        
                                                                                                        try:
                                                                                                            None(None, None)
                                                                                                            return None
                                                                                                            with None:
                                                                                                                if not None:
                                                                                                                    
                                                                                                                    try:
                                                                                                                        
                                                                                                                        try:
                                                                                                                            return None
                                                                                                                        except Exception:
                                                                                                                            self.logger.exception('Uncaught exception in monitor_loop')
                                                                                                                            return None





















    
    def close(self = None):
        self.is_finished.set()

    
    def join(self = None):
        self.write_thread.join()
        self.monitor_thread.join()

    
    def update(self = None, schedule_item = None):
        if self.schedule_item == schedule_item:
            return None
        if None.output_config != schedule_item.output_config:
            raise ValueError("Can't update output configuration while running")
        self.schedule_item = schedule_item
        self.collection_time_target = schedule_item.collection_time
        self.calc_stop_time_target()


