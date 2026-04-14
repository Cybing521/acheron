# Source Generated with Decompyle++
# File: tmpp7n4ywjc.marshal (Python 3.11)

b = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
s = b.decode('ascii')
s = s.strip().replace(' ', '_')
s = re.sub('[^-\\w.]', '', s)
s = re.sub('[.]{2,}', '.', s)
s = s.strip('.')
return s
