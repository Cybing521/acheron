# Source Generated with Decompyle++
# File: tmpnxzv0nf2.marshal (Python 3.11)


try:
    if not connected:
        self.disconnected.set()
        self.ctrl_queue.put((StreamControl._WAKEUP,))
        
        try:
            self.device.set_connect_callback(None)
            
            try:
                pass
            except asphodel.AsphodelError:
                
                try:
                    pass
                try:
                    self.status_pipe_lock
                    self.status_pipe.send((StreamStatus.STREAMING_ERROR_DISCONNECT,))
                    
                    try:
                        None(None, None)
                        return None
                        with None:
                            if not None:
                                
                                try:
                                    
                                    try:
                                        return None
                                        return None
                                    except Exception:
                                        self.logger.exception('Unhandled exception in connect_callback')
                                        return None







