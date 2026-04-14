# Source Generated with Decompyle++
# File: tmpi1tzbdp1.marshal (Python 3.11)

if self.suffix():
    s = text.rsplit(self.suffix(), 1)[0]
else:
    s = text
scaled_value = float(s)
value = (scaled_value - self.unit_formatter.conversion_offset) / self.unit_formatter.conversion_scale
return value
