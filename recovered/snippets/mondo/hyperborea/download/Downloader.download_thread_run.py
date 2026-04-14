# Source Generated with Decompyle++
# File: tmp3b8kty6r.marshal (Python 3.11)


try:
    r = requests.get(url, stream = True)
    r.raise_for_status()
    total_length_str = r.headers.get('content-length')
    written_bytes = 0
    if total_length_str:
        total_length = int(total_length_str)
    else:
        except ValueError:
            total_length = 0
        except:
            total_length = 0
        for chunk in r.iter_content(chunk_size = 4096):
            if chunk:
                file.write(chunk)
                written_bytes += len(chunk)
                self.update.emit(written_bytes, total_length)
            self.completed.emit(url, file)
            
            try:
                None(None, None)
                return None
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                return None
                            except Exception:
                                self.logger.exception('Error downloading file')
                                self.error.emit(file, 'Error downloading file')
                                return None




