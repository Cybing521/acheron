# Source Generated with Decompyle++
# File: tmpkv1qrngp.marshal (Python 3.11)

self.logger.debug('Stopping transmitting sockets')
self.lock
for listen_sock in self.listen_sockets:
    if listen_sock:
        self.selector.unregister(listen_sock)
    else:
        except KeyError:
            pass
        listen_sock.close()
    self.listen_sockets.clear()
    for channel_id, sockets in self.all_channel_sockets.items():
        for subchannel_index, connected_sock in sockets:
            self.selector.unregister(connected_sock)
        except KeyError:
            pass
        port = self.channel_ports[(channel_id, subchannel_index)]
        connected_sock.close()
        self.logger.info('Connection closed on %s', port)
        self.all_channel_sockets.clear()
        None(None, None)
        return None
        with None:
            if not None:
                pass
