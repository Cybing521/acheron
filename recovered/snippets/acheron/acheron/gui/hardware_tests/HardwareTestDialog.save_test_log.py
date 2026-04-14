# Source Generated with Decompyle++
# File: tmpnyt524ac.marshal (Python 3.11)

dt = datetime.datetime.now(tz = datetime.timezone.utc)
dt_str = dt.strftime('%Y%m%dT%H%MZ_')
directory = os.path.join(self.preferences.base_dir, 'Hardware Tests')
base_name = os.path.join(directory, dt_str + self.controller.serial_number)
filename = base_name + '.txt'
index = 1
# WARNING: Decompyle incomplete
