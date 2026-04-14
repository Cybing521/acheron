# Source Generated with Decompyle++
# File: tmpgwy6mq0z.marshal (Python 3.11)

sn_filtered = re.sub('[^\\d]', '', serial)

try:
    sn_int = int(sn_filtered)
except Exception:
    raise ValueError('Non-numeric serial number')

data = kwargs.copy()
data['serialNumber'] = sn_int
data['category'] = str(category)
data['description'] = str(description)
url = 'https://api.suprocktech.com/events/create'
response = requests.post(url, json = data)
response.raise_for_status()
