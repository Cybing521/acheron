# Source Generated with Decompyle++
# File: tmp8yvxfmmx.marshal (Python 3.11)

if len(files) == 0:
    return None
for filename in None:
    logger.info('Marking file {}'.format(filename))
    mark_file_for_upload(filename)
    if self.upload_manager:
        self.upload_manager.rescan()
        return None
    return None
