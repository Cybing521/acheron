# Source Generated with Decompyle++
# File: tmp94_fli6y.marshal (Python 3.11)


try:
    header_str = header_bytes.decode('UTF-8')
    header = json.loads(header_str)
except Exception:
    message = 'Could not parse file header!'
    logger.exception(message)
    QtWidgets.QMessageBox.critical(parent, 'Error', message)
    return 

# WARNING: Decompyle incomplete
