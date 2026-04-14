# Source Generated with Decompyle++
# File: tmpy4r4uygd.marshal (Python 3.11)


try:
    pipe = self.data_rx_pipe
    if self.finished.is_set():
        return None
    if None.poll(0.1):
        
        try:
            data = pipe.recv()
            
            try:
                pass
            except EOFError:
                
                try:
                    return None
                    
                    try:
                        self.handle_data(data)
                        continue
                    except Exception:
                        self.logger.exception('Unhandled exception in data_thread_run')
                        self.stop()
                        return None





