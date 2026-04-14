# Source Generated with Decompyle++
# File: tmpglh32xcu.marshal (Python 3.11)

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
