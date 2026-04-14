# Source Generated with Decompyle++
# File: tmplg_dilgt.marshal (Python 3.11)

if not self.email_settings:
    return None

try:
    msg = self._create_message(alert_info, self.email_settings)
    smtp_obj = _get_smtp_object(self.email_settings)
    
    try:
        smtp_obj.send_message(msg)
        
        try:
            smtp_obj.quit()
        try:
            callback(None)
            return None
        except Exception:
            e = None
            callback(e)
            e = None
            del e
            return None
            e = None
            del e



