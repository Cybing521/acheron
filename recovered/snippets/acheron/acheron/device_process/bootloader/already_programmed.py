# Source Generated with Decompyle++
# File: tmpkr65ar09.marshal (Python 3.11)

if device_info.supports_bootloader:
    return False
if None.get('build_info') != device_info.build_info:
    return False
if None.get('build_date') != device_info.build_date:
    return False
if None.get('application', False) is not True:
    return False
if None.get('bootloader', False) is not False:
    return False
