# Source Generated with Decompyle++
# File: tmp8yfultvy.marshal (Python 3.11)

results = {
    'hostname': self.hostname.text().strip(),
    'port': self.port.value() }
sn = self.serial.text().strip()
if len(sn) != 0:
    results['serial_number'] = sn
else:
    results['serial_number'] = None
return results
