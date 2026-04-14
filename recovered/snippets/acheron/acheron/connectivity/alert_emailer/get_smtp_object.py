# Source Generated with Decompyle++
# File: tmpkyr2v2oz.marshal (Python 3.11)

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
