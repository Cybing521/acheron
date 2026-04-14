# Source Generated with Decompyle++
# File: tmpcpwbj3hj.marshal (Python 3.11)


try:
    
    try:
        filename = self.finished_queue.get(True, 0.1)
        self.compressor_lock
        compressor = self.compressors.get(filename)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        if compressor:
                            ret_val = compressor.wait()
                            if ret_val != 0:
                                msg = 'Compressor exited with error {}'
                                self.logger.warning(msg.format(ret_val))
                            self.compressor_lock
                            del self.compressors[filename]
                            
                            try:
                                None(None, None)
                            with None:
                                if not None:
                                    
                                    try:
                                        
                                        try:
                                            if self.output_config.upload_marker:
                                                (path, name) = os.path.split(filename)
                                                uploadfilename = os.path.join(path, '.' + name + UPLOAD_EXTENSION)
                                                uploadfile = open(uploadfilename, 'r+', encoding = 'ascii')
                                                uploadfile.seek(0)
                                                uploadfile.truncate()
                                                
                                                try:
                                                    None(None, None)
                                                with None:
                                                    if not None:
                                                        
                                                        try:
                                                            
                                                            try:
                                                                
                                                                try:
                                                                    self.writer_status_callback.writer_file_finished(filename, self.schedule_item.id, self.output_config.upload_marker)
                                                                    
                                                                    try:
                                                                        pass
                                                                    except Exception:
                                                                        self.logger.exception('Exception in writer_file_finished callback')
                                                                        
                                                                        try:
                                                                            pass
                                                                        try:
                                                                            
                                                                            try:
                                                                                pass
                                                                            except Empty:
                                                                                if self.write_loop_exited.is_set():
                                                                                    
                                                                                    try:
                                                                                        pass
                                                                                    except:
                                                                                        
                                                                                        try:
                                                                                            continue
                                                                                            self.compressor_lock
                                                                                            for filename, compressor in self.compressors.items():
                                                                                                ret_val = compressor.wait()
                                                                                                msg = 'Uncollected compressor exited with code {}'
                                                                                                self.logger.warning(msg.format(ret_val))
                                                                                                self.writer_status_callback.writer_file_finished(filename, self.schedule_item.id, self.output_config.upload_marker)
                                                                                                except Exception:
                                                                                                    self.logger.exception('Exception in writer_file_finished exit callback')
                                                                                                    continue
                                                                                                self.compressors.clear()
                                                                                                
                                                                                                try:
                                                                                                    None(None, None)
                                                                                                    return None
                                                                                                    with None:
                                                                                                        if not None:
                                                                                                            
                                                                                                            try:
                                                                                                                
                                                                                                                try:
                                                                                                                    return None
                                                                                                                except Exception:
                                                                                                                    self.logger.exception('Uncaught exception in monitor_loop')
                                                                                                                    return None




















