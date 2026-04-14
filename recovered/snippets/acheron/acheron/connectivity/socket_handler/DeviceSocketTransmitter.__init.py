# Source Generated with Decompyle++
# File: tmp4ltoncw9.marshal (Python 3.11)

self.socket_buffer_size = socket_buffer_size
self.channel_ports = channel_ports
self.selector = selector
self.logger = logger
self.lock = threading.Lock()
self.listen_sockets = set()
self.all_channel_sockets = { }
for channel_id, subchannel_index in channel_ports.items():
    port = None
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.setblocking(False)
    listen_sock.bind(('', port))
    listen_sock.listen()
    accept_cb = functools.partial(self._accept_ready, channel_id, subchannel_index, listen_sock)
    self.selector.register(listen_sock, selectors.EVENT_READ, accept_cb)
    self.logger.info(f'''Listening for connections on port {port}''')
    self.listen_sockets.add(listen_sock)
    except Exception:
        self.logger.exception('Error opening socket on port %s', port)
        continue
    return None
