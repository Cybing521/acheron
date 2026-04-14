# Source Generated with Decompyle++
# File: tmpmwccczt_.marshal (Python 3.11)

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

