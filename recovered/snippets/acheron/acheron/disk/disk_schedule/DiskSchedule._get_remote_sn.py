# Source Generated with Decompyle++
# File: tmpwo4bd5e1.marshal (Python 3.11)

if len(serial) < 2:
    return None
matches = None.findall('\\d+', serial[-1])
return int(matches[-1]) if matches else None
