# Source Generated with Decompyle++
# File: tmp5nropcuk.marshal (Python 3.11)


def __init__(self = None):
    self.settings = QtCore.QSettings()

dark_mode = BoolProperty('DarkMode', True)
show_supplies = BoolProperty('ShowSupplies', False)
_base_dir = StringProperty('BasePath')

def get_base_dir(self = None):
    base_dir = self._base_dir
    if not base_dir:
        documents_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.DocumentsLocation)
        app_name = QtCore.QCoreApplication.applicationName()
        base_dir = os.path.join(documents_path, app_name + ' Data')
    return os.path.normpath(base_dir)


def set_base_dir(self = None, value = None):
    self._base_dir = value

base_dir = property(get_base_dir, set_base_dir)
_diskcache_dir = StringProperty('DiskCachePath')

def get_diskcache_dir(self = None):
    diskcache_dir = self._diskcache_dir
    if not diskcache_dir:
        cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
        app_name = QtCore.QCoreApplication.applicationName()
        diskcache_dir = os.path.join(cache_path, app_name + ' Cache')
    return os.path.normpath(diskcache_dir)


def set_diskcache_dir(self = None, value = None):
    self._diskcache_dir = value

diskcache_dir = property(get_diskcache_dir, set_diskcache_dir)
_firmware_dir = StringProperty('FirmwareCachePath')

def get_firmware_dir(self = None):
    firmware_dir = self._firmware_dir
    if not firmware_dir:
        cache_path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.CacheLocation)
        app_name = QtCore.QCoreApplication.applicationName()
        firmware_dir = os.path.join(cache_path, app_name + ' Firmware')
    return os.path.normpath(firmware_dir)


def set_firmware_dir(self = None, value = None):
    self._firmware_dir = value

firmware_dir = property(get_firmware_dir, set_firmware_dir)
firmware_root_dir = StringProperty('FirmwareRootDir')
auto_rgb = BoolProperty('AutoRGB', True)
downsample = BoolProperty('Downsample', True)
plot_mean = BoolProperty('PlotMean', False)
compression_level = IntProperty('CompressionLevel', 6)
archive_interval = IntProperty('ArchiveIntervalMinutes', 10)
modbus_enable = BoolProperty('ModbusEnable', False)
modbus_port = IntProperty('ModbusPort', 502)
upload_enabled = BoolProperty('Upload/Enabled', False)
s3_bucket = StringProperty('Upload/S3Bucket')
aws_region = StringProperty('Upload/AWSRegion')
upload_directory = StringProperty('Upload/Directory')
access_key_id = StringProperty('Upload/AccessKeyID')
secret_access_key = StringProperty('Upload/SecretAccessKey')
delete_original = BoolProperty('Upload/DeleteOriginal', False)
alert_email_enabled = BoolProperty('AlertEmail/Enabled', False)
alert_from_address = StringProperty('AlertEmail/FromAddress')
alert_to_address = StringProperty('AlertEmail/ToAddress')
alert_smtp_host = StringProperty('AlertEmail/SMTPHost')
alert_smtp_port = IntProperty('AlertEmail/SMTPPort', 587)
alert_security = StringProperty('AlertEmail/Security')
alert_use_auth = BoolProperty('AlertEmail/UseAuth', True)
alert_smtp_user = StringProperty('AlertEmail/SMTPUser')
alert_smtp_password = StringProperty('AlertEmail/SMTPPassword')
update_timer_interval = IntProperty('UpdateTimerInterval', 100)
graph_timer_interval = IntProperty('GraphTimerInterval', 100)
show_rf_test = BoolProperty('RFTest', False)
show_supplies = BoolProperty('ShowSupplies', False)
collapsed = BoolProperty('Collapsed', False)
closeable_tabs = BoolProperty('ClosableTabs', False)
automatic_rescan = BoolProperty('DialogAutomaticRescan', True)
background_active_scan = BoolProperty('BackgroundActiveScan', False)
initial_connect_usb = BoolProperty('InitialConnectUSB', True)
initial_connect_tcp = BoolProperty('InitialConnectTCP', False)
rescan_connect_usb = BoolProperty('RescanConnectUSB', False)
rescan_connect_tcp = BoolProperty('RescanConnectTCP', False)
disable_streaming = BoolProperty('DisableStreaming', False)
disable_archiving = BoolProperty('DisableArchiving', False)
socket_buffer_size = IntProperty('SocketBufferSize', 0)
event_upload_enabled = BoolProperty('EventUploadEnabled', True)
initial_serials = (lambda self = None: v = self.settings.value('InitialSerials')# WARNING: Decompyle incomplete
)()
