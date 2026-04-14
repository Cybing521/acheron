# Source Generated with Decompyle++
# File: tmps6fyxa9i.marshal (Python 3.11)

key = (channel_id, subchannel_index)

try:
    port = self.channel_ports[key]
    (connected_sock, _addr) = listen_sock.accept()
    self.logger.info('Accepted new connection on port %s', port)
    connected_sock.setblocking(False)
    connected_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
    if self.socket_buffer_size != 0:
        default_buffer_size = connected_sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        if self.socket_buffer_size > default_buffer_size:
            connected_sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.socket_buffer_size)
            new_buffer_size = connected_sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
            if new_buffer_size != self.socket_buffer_size:
                self.logger.warning('Socket buffer is %s not requested %s', new_buffer_size, self.socket_buffer_size)
            else:
                self.logger.debug('Socket buffer size is %s', new_buffer_size)
        else:
            self.logger.debug('Socket buffer size is OS default %s', default_buffer_size)
    close_cb = functools.partial(self._close_socket, channel_id, subchannel_index, connected_sock)
    self.selector.register(connected_sock, selectors.EVENT_READ, close_cb)
    self.lock
    channel_sockets = self.all_channel_sockets[channel_id]
except KeyError:
    channel_sockets = []
    self.all_channel_sockets[channel_id] = channel_sockets

channel_sockets.append((subchannel_index, connected_sock))

try:
    None(None, None)
    return None
    with None:
        if not None:
            
            try:
                
                try:
                    return None
                except OSError:
                    return None
                    except Exception:
                        self.logger.exception('Unhandled exception in _accept_ready()')
                        return None



