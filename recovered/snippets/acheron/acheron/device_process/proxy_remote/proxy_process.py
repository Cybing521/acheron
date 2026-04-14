# Source Generated with Decompyle++
# File: tmp5e_aj6ia.marshal (Python 3.11)

sys.stdout = open(os.devnull)
sys.stderr = open(os.devnull)
setup_remote_logging(log_queue)
device = None
device_logger = DeviceLoggerAdapter(logger, serial_number, proxy_string)
if sys.platform == 'win32':
    signal.signal(signal.SIGINT, signal.SIG_IGN)
else:
    os.setpgrp()
arg_strs = ffargs()
(lambda .0: pass# WARNING: Decompyle incomplete
)(ffkwargs.items()())
find_func_str = '{}({})'.format(find_func.__name__, ', '.join(arg_strs))
device_logger.debug('Proxy process starting with %s', find_func_str)
me = psutil.Process(os.getpid())
# WARNING: Decompyle incomplete
