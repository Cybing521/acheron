# Source Generated with Decompyle++
# File: tmppaww8_x4.marshal (Python 3.11)

scales = [
    (1, 'bit/s'),
    (1000, 'kbit/s'),
    (1e+06, 'Mbit/s'),
    (1e+09, 'Gbit/s')]
for factor, suffix in scales:
    if bitrate < factor * 1000:
        
        return None, f'''{bitrate / factor:.1f} {suffix}'''
    return f'''{bitrate / 1e+09:.3f} Gbit/s'''
