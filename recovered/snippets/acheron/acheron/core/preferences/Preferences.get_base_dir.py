# Source Generated with Decompyle++
# File: tmp90lxwn3b.marshal (Python 3.11)

base_dir = self._base_dir
if not base_dir:
    documents_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
    app_name = QtCore.QCoreApplication.applicationName()
    base_dir = os.path.join(documents_path, app_name + ' Data')
return os.path.normpath(base_dir)
