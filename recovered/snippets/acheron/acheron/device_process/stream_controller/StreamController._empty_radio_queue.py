# Source Generated with Decompyle++
# File: tmp1xwp9bcw.marshal (Python 3.11)


try:
    message = self.radio_queue.get(False)
    message_type = message[0]
    if message_type == StreamControl.DO_ACTIVE_SCAN:
        serial_number = message[1]
        self.status_pipe_lock
        self.status_pipe.send((StreamStatus.ACTIVE_SCAN_DATA, serial_number, None))
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    if message_type == StreamControl.DO_RADIO_FUNCTION:
                        self.status_pipe_lock
                        self.status_pipe.send((StreamStatus.RADIO_FUNCTION_FINISHED, False, None))
                        
                        try:
                            None(None, None)
                        with None:
                            if not None:
                                
                                try:
                                    
                                    try:
                                        pass
                                    if message_type == StreamControl._REMOTE_INFO:
                                        pass
                                    elif message_type == StreamControl._REMOTE_CLOSED:
                                        pass
                                    else:
                                        self.logger.warning('Unknown radio message %s', message)

                                except Empty:
                                    return None
                                    continue






