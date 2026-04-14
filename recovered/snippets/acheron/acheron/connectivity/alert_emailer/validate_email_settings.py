# Source Generated with Decompyle++
# File: tmpdgc3ano6.marshal (Python 3.11)

if email_settings.security not in ('', 'starttls', 'ssl'):
    raise ValueError(f'''unknown security setting "{email_settings.security}"''')
if email_settings.from_address == '':
    raise ValueError('no email from address')
if email_settings.to_address == '':
    raise ValueError('no email to address')
