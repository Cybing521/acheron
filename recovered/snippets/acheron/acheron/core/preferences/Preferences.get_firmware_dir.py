# Source Generated with Decompyle++
# File: tmpa_7crd6t.marshal (Python 3.11)

firmware_dir = self._firmware_dir
if not firmware_dir:
    cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
    app_name = QtCore.QCoreApplication.applicationName()
    firmware_dir = os.path.join(cache_path, app_name + ' Firmware')
return os.path.normpath(firmware_dir)
