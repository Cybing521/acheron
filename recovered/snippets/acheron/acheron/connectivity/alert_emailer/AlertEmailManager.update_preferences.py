# Source Generated with Decompyle++
# File: tmpizidrdg0.marshal (Python 3.11)

if self.preferences.alert_email_enabled:
    
    try:
        self.email_settings = preferences_to_email_settings(self.preferences)
        validate_email_settings(self.email_settings)
        return None
    except Exception:
        logger.exception('Invalid email settings')
        self.email_settings = None
        return None
        self.email_settings = None
        return None

