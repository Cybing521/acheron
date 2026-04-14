# Source Generated with Decompyle++
# File: tmpzkyzdrkx.marshal (Python 3.11)

handler = QueueHandler(log_queue)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
pyusb_logger = logging.getLogger('usb')
pyusb_logger.propagate = False
