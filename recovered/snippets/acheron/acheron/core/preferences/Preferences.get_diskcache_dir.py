# Source Generated with Decompyle++
# File: tmpz2swljja.marshal (Python 3.11)

diskcache_dir = self._diskcache_dir
if not diskcache_dir:
    cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
    app_name = QtCore.QCoreApplication.applicationName()
    diskcache_dir = os.path.join(cache_path, app_name + ' Cache')
return os.path.normpath(diskcache_dir)
