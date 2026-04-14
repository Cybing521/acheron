# Source Generated with Decompyle++
# File: tmppps06b73.marshal (Python 3.11)

import collections
import datetime
from dataclasses import dataclass
import email.message as email
import email.utils as email
import logging
import smtplib
import time
import threading
from typing import Callable, Optional
from device_logging import DeviceLoggerAdapter
from calc_process.types import Trigger
from core.preferences import Preferences
logger = logging.getLogger(__name__)
EmailCallback = Callable[([
    Optional[Exception]], None)]
AlertInfo = <NODE:12>()
EmailSettings = <NODE:12>()

def preferences_to_email_settings(preferences = None):
    return EmailSettings(from_address = preferences.alert_from_address, to_address = preferences.alert_to_address, smtp_host = preferences.alert_smtp_host, smtp_port = preferences.alert_smtp_port, security = preferences.alert_security.lower(), use_auth = preferences.alert_use_auth, smtp_user = preferences.alert_smtp_user, smtp_password = preferences.alert_smtp_password)


def validate_email_settings(email_settings = None):
    if email_settings.security not in ('', 'starttls', 'ssl'):
        raise ValueError(f'''unknown security setting "{email_settings.security}"''')
    if email_settings.from_address == '':
        raise ValueError('no email from address')
    if email_settings.to_address == '':
        raise ValueError('no email to address')


def _get_smtp_object(email_settings = None):
    security = email_settings.security
    if security == 'ssl':
        smtp_obj = smtplib.SMTP_SSL(host = email_settings.smtp_host, port = email_settings.smtp_port)
    else:
        smtp_obj = smtplib.SMTP(host = email_settings.smtp_host, port = email_settings.smtp_port)
    if security == 'starttls':
        smtp_obj.starttls()
    if email_settings.use_auth:
        smtp_obj.login(user = email_settings.smtp_user, password = email_settings.smtp_password)
    return smtp_obj


def send_test_email(email_settings = None):
    validate_email_settings(email_settings)
    msg = email.message.EmailMessage()
    msg['From'] = email_settings.from_address
    msg['To'] = email_settings.to_address
    msg['Subject'] = 'Alert test email'
    msg['Date'] = email.utils.formatdate()
    msg['Message-ID'] = email.utils.make_msgid()
    body = 'This is an email sent to test the alert email configuration.'
    msg.set_content(body)
    smtp_obj = _get_smtp_object(email_settings)
    
    try:
        smtp_obj.send_message(msg)
        smtp_obj.quit()
        return None
    except:
        smtp_obj.quit()



class AlertEmailManager:
    pass
# WARNING: Decompyle incomplete

