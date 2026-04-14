# Source Generated with Decompyle++
# File: alert_emailer.pyc (Python 3.11)

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
from ..device_logging import DeviceLoggerAdapter
from ..calc_process.types import Trigger
from ..core.preferences import Preferences
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: EmailCallback = Callable[([
# INVALID FROM DECOMPILER:     Optional[Exception]], None)]
# INVALID FROM DECOMPILER: AlertInfo = <NODE:12>()
# INVALID FROM DECOMPILER: EmailSettings = <NODE:12>()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

@dataclass
class AlertInfo:

    serial_number: str

    display_name: str

    dt: datetime.datetime

@dataclass
class EmailSettings:

    from_address: str

    to_address: str

    smtp_host: str

    smtp_port: int

    security: str

    use_auth: bool

    smtp_user: str

    smtp_password: str

def preferences_to_email_settings(preferences):
    return EmailSettings(from_address = preferences.alert_from_address, to_address = preferences.alert_to_address, smtp_host = preferences.alert_smtp_host, smtp_port = preferences.alert_smtp_port, security = preferences.alert_security.lower(), use_auth = preferences.alert_use_auth, smtp_user = preferences.alert_smtp_user, smtp_password = preferences.alert_smtp_password)

def validate_email_settings(email_settings):
    if email_settings.security not in ('', 'starttls', 'ssl'):
        raise ValueError(f'''unknown security setting "{email_settings.security}"''')
    if email_settings.from_address == '':
        raise ValueError('no email from address')
    if email_settings.to_address == '':
        raise ValueError('no email to address')

def _get_smtp_object(email_settings):
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

def send_test_email(email_settings):
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

    def __init__(self, preferences):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 PRECALL
        #   56 CALL
        #   66 POP_TOP
        #   68 LOAD_FAST preferences
        #   70 LOAD_FAST self
        #   72 STORE_ATTR preferences
        #   82 LOAD_FAST self
        #   84 LOAD_METHOD update_preferences
        #  106 PRECALL
        #  110 CALL
        #  120 POP_TOP
        #  122 LOAD_FAST self
        #  124 POP_TOP
        #  126 BUILD_MAP
        #  128 LOAD_FAST self
        #  130 STORE_ATTR last_sent
        #  140 LOAD_GLOBAL NULL + threading
        #  152 LOAD_ATTR Event
        #  162 PRECALL
        #  166 CALL
        #  176 LOAD_FAST self
        #  178 STORE_ATTR is_finished
        #  188 LOAD_GLOBAL NULL + collections
        #  200 LOAD_ATTR deque
        #  210 PRECALL
        #  214 CALL
        #  224 LOAD_FAST self
        #  226 STORE_ATTR alerts
        #  236 LOAD_GLOBAL NULL + threading
        #  248 LOAD_ATTR Thread
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR _email_loop
        #  270 KW_NAMES
        #  272 PRECALL
        #  276 CALL
        #  286 LOAD_FAST self
        #  288 STORE_ATTR email_thread
        #  298 LOAD_FAST self
        #  300 LOAD_ATTR email_thread
        #  310 LOAD_METHOD start
        #  332 PRECALL
        #  336 CALL
        #  346 POP_TOP
        #  348 LOAD_CONST None
        #  350 RETURN_VALUE
        pass

    def update_preferences(self):
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

    def _create_message(self, alert_info, email_settings):
        if alert_info.display_name == alert_info.serial_number:
            name = alert_info.serial_number
        else:
            name = '{} ({})'.format(alert_info.display_name, alert_info.serial_number)
        msg = email.message.EmailMessage()
        msg['From'] = email_settings.from_address
        msg['To'] = email_settings.to_address
        msg['Subject'] = '[{}] Alert'.format(name)
        msg['Date'] = email.utils.format_datetime(alert_info.dt)
        msg['Message-ID'] = email.utils.make_msgid()
        timestr = alert_info.dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        lines = [
            f'''{name} experienced an alert condition at {timestr} with the following:''',
            '']
        for trigger, subchannel_name in alert_info.trigger_list:
            alert_type = trigger.limit_type.value
            s = f'''{alert_type} alert triggered on "{subchannel_name}".'''
            lines.append(s)
            body = '\n'.join(lines)
            msg.set_content(body)
            return msg

    def _do_email(self, alert_info, callback):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR email_settings
        #   14 POP_JUMP_FORWARD_IF_TRUE to 20
        #   16 LOAD_CONST None
        #   18 RETURN_VALUE
        #   20 NOP
        #   22 LOAD_FAST self
        #   24 LOAD_METHOD _create_message
        #   46 LOAD_FAST alert_info
        #   48 LOAD_FAST self
        #   50 LOAD_ATTR email_settings
        #   60 PRECALL
        #   64 CALL
        #   74 STORE_FAST msg
        #   76 LOAD_GLOBAL NULL + _get_smtp_object
        #   88 LOAD_FAST self
        #   90 LOAD_ATTR email_settings
        #  100 PRECALL
        #  104 CALL
        #  114 STORE_FAST smtp_obj
        #  116 NOP
        #  118 LOAD_FAST smtp_obj
        #  120 LOAD_METHOD send_message
        #  142 LOAD_FAST msg
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST smtp_obj
        #  162 LOAD_METHOD quit
        #  184 PRECALL
        #  188 CALL
        #  198 POP_TOP
        #  200 JUMP_FORWARD to 252
        #  202 PUSH_EXC_INFO
        #  204 LOAD_FAST smtp_obj
        #  206 LOAD_METHOD quit
        #  228 PRECALL
        #  232 CALL
        #  242 POP_TOP
        #  244 RERAISE
        #  246 COPY
        #  248 POP_EXCEPT
        #  250 RERAISE
        #  252 PUSH_NULL
        #  254 LOAD_FAST callback
        #  256 LOAD_CONST None
        #  258 PRECALL
        #  262 CALL
        #  272 POP_TOP
        #  274 LOAD_CONST None
        #  276 RETURN_VALUE
        #  278 PUSH_EXC_INFO
        #  280 LOAD_GLOBAL Exception
        #  292 CHECK_EXC_MATCH
        #  294 POP_JUMP_FORWARD_IF_FALSE to 340
        #  296 STORE_FAST e
        #  298 PUSH_NULL
        #  300 LOAD_FAST callback
        #  302 LOAD_FAST e
        #  304 PRECALL
        #  308 CALL
        #  318 POP_TOP
        #  320 POP_EXCEPT
        #  322 LOAD_CONST None
        #  324 STORE_FAST e
        #  326 DELETE_FAST e
        #  328 LOAD_CONST None
        #  330 RETURN_VALUE
        #  332 LOAD_CONST None
        #  334 STORE_FAST e
        #  336 DELETE_FAST e
        #  338 RERAISE
        #  340 RERAISE
        #  342 COPY
        #  344 POP_EXCEPT
        #  346 RERAISE
        pass

    def _email_loop(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 NOP
        #    4 LOAD_GLOBAL logger
        #   16 LOAD_METHOD debug
        #   38 LOAD_CONST 'Email loop started'
        #   40 PRECALL
        #   44 CALL
        #   54 POP_TOP
        #   56 NOP
        #   58 LOAD_FAST self
        #   60 LOAD_ATTR is_finished
        #   70 LOAD_METHOD is_set
        #   92 PRECALL
        #   96 CALL
        #  106 POP_JUMP_FORWARD_IF_FALSE to 112
        #  108 LOAD_CONST None
        #  110 RETURN_VALUE
        #  112 NOP
        #  114 LOAD_FAST self
        #  116 LOAD_ATTR alerts
        #  126 LOAD_METHOD popleft
        #  148 PRECALL
        #  152 CALL
        #  162 UNPACK_SEQUENCE
        #  166 STORE_FAST alert_tuple
        #  168 STORE_FAST callback
        #  170 JUMP_FORWARD to 244
        #  172 PUSH_EXC_INFO
        #  174 LOAD_GLOBAL IndexError
        #  186 CHECK_EXC_MATCH
        #  188 POP_JUMP_FORWARD_IF_FALSE to 236
        #  190 POP_TOP
        #  192 LOAD_GLOBAL NULL + time
        #  204 LOAD_ATTR sleep
        #  214 LOAD_CONST 0.1
        #  216 PRECALL
        #  220 CALL
        #  230 POP_TOP
        #  232 POP_EXCEPT
        #  234 JUMP_BACKWARD to 56
        #  236 RERAISE
        #  238 COPY
        #  240 POP_EXCEPT
        #  242 RERAISE
        #  244 LOAD_FAST self
        #  246 LOAD_METHOD _do_email
        #  268 LOAD_FAST alert_tuple
        #  270 LOAD_FAST callback
        #  272 PRECALL
        #  276 CALL
        #  286 POP_TOP
        #  288 JUMP_BACKWARD to 58
        #  290 PUSH_EXC_INFO
        #  292 LOAD_GLOBAL Exception
        #  304 CHECK_EXC_MATCH
        #  306 POP_JUMP_FORWARD_IF_FALSE to 408
        #  308 POP_TOP
        #  310 LOAD_GLOBAL logger
        #  322 LOAD_METHOD exception
        #  344 LOAD_CONST 'Uncaught exception in email_loop'
        #  346 PRECALL
        #  350 CALL
        #  360 POP_TOP
        #  362 LOAD_FAST self
        #  364 LOAD_METHOD stop
        #  386 PRECALL
        #  390 CALL
        #  400 POP_TOP
        #  402 POP_EXCEPT
        #  404 LOAD_CONST None
        #  406 RETURN_VALUE
        #  408 RERAISE
        #  410 COPY
        #  412 POP_EXCEPT
        #  414 RERAISE
        pass

    def send_alerts(self, device_logger, serial_number, display_name, trigger_list, callback):
        dt = datetime.datetime.now(tz = datetime.timezone.utc)
        last = self.last_sent.get(serial_number)

    def stop(self):
        self.is_finished.set()

    def join(self):
        self.email_thread.join()
