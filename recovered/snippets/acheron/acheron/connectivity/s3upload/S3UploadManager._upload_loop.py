# Source Generated with Decompyle++
# File: tmp67jlii9k.marshal (Python 3.11)


try:
    emitted_error = False
    if self.is_finished.is_set():
        return None
    
    try:
        self.s3_client.head_bucket(Bucket = self.s3_bucket)
        
        try:
            pass
        except Exception:
            if not emitted_error:
                emitted_error = True
                logger.exception('Error connecting to S3 bucket')
                self.error.emit()
            if self.is_finished.wait(20):
                
                try:
                    return None
                    
                    try:
                        continue
                        
                        try:
                            
                            try:
                                self.upload_lock
                                filename = self.upload_order.popleft()
                                self._do_upload(filename)
                                
                                try:
                                    None(None, None)
                                with None:
                                    if not None:
                                        
                                        try:
                                            
                                            try:
                                                
                                                try:
                                                    pass
                                                except IndexError:
                                                    if self.uploading:
                                                        self.uploading = False
                                                        self.rate_status.emit(False, 0)
                                                    time.sleep(0.1)
                                                    
                                                    try:
                                                        pass
                                                    try:
                                                        if self.is_finished.is_set():
                                                            return None
                                                    except Exception:
                                                        logger.exception('Uncaught exception in upload_loop')
                                                        self.stop()
                                                        self.error.emit()
                                                        return None












