# Source Generated with Decompyle++
# File: tmpem5kfcsq.marshal (Python 3.11)

if self.preferences.upload_enabled:
    upload_options = {
        'base_dir': self.preferences.base_dir,
        's3_bucket': self.preferences.s3_bucket,
        'key_prefix': self.preferences.upload_directory,
        'access_key_id': self.preferences.access_key_id,
        'secret_access_key': self.preferences.secret_access_key,
        'aws_region': self.preferences.aws_region,
        'delete_after_upload': self.preferences.delete_original,
        'archive_interval': datetime.timedelta(minutes = self.preferences.archive_interval) }
else:
    upload_options = None
if upload_options == self.upload_options:
    return None
self.upload_options = None
if self.upload_manager:
    self.upload_manager.stop()
    self.background_join_deque.append(self.upload_manager.join)
    self.upload_manager = None
# WARNING: Decompyle incomplete
