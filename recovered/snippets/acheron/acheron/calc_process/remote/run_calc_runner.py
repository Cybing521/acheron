# Source Generated with Decompyle++
# File: tmpbfyxy6fc.marshal (Python 3.11)

sys.stdout = open(os.devnull)
sys.stderr = open(os.devnull)
handler = QueueHandler(log_queue)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
if sys.platform == 'win32':
    signal.signal(signal.SIGINT, signal.SIG_IGN)
else:
    os.setpgrp()
# WARNING: Decompyle incomplete
