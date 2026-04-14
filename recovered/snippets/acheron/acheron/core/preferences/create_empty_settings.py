# Source Generated with Decompyle++
# File: tmpgrd9xno2.marshal (Python 3.11)

settings = QtCore.QSettings()
setting_keys = [
    'ArchiveIntervalMinutes',
    'DiskCachePath',
    'FirmwareCachePath',
    'FirmwareRootDir',
    'GraphTimerInterval',
    'InitialConnectTCP',
    'InitialConnectUSB',
    'InitialSerials',
    'RescanConnectTCP',
    'RescanConnectUSB',
    'RFTest',
    'UpdateTimerInterval']
for setting_key in setting_keys:
    value = settings.value(setting_key)
    if not value:
        settings.setValue(setting_key, '')
    return None
