# Source Generated with Decompyle++
# File: tmpfi9l_ziu.marshal (Python 3.11)

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
