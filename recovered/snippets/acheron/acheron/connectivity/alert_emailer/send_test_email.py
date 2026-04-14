# Source Generated with Decompyle++
# File: tmpjnxj6vv3.marshal (Python 3.11)

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

