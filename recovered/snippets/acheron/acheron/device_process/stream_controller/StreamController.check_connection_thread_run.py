# Source Generated with Decompyle++
# File: tmps6uci8xz.marshal (Python 3.11)

if self.disconnected.wait(timeout = 0.1):
    return None
if None.device_lock.acquire(blocking = False):
    
    try:
        self.device.echo_params(b'')
        
        try:
            pass
        except asphodel.AsphodelError:
            self.disconnected.set()
            self.ctrl_queue.put((StreamControl._WAKEUP,))
            self.status_pipe_lock
            self.status_pipe.send((StreamStatus.STREAMING_ERROR_DISCONNECT,))
            None(None, None)
        except:
            with None:
                if not None:
                    pass
            
            try:
                pass
            try:
                self.device_lock.release()
            except:
                self.device_lock.release()

            continue


