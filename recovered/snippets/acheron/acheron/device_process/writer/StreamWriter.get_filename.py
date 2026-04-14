# Source Generated with Decompyle++
# File: tmpjf1kswfs.marshal (Python 3.11)

if self.output_config.date_dir_structure:
    date_dir = dt.strftime('%Y_%m_%d')
else:
    date_dir = ''
directory = os.path.join(self.output_config.base_directory, date_dir, self.device_directory)
os.makedirs(directory, exist_ok = True)
if self.output_config.datetime_filename:
    base_name = dt.strftime('%Y%m%dT%H%MZ_') + self.base_name
else:
    base_name = self.base_name
base_name = os.path.join(directory, base_name)
filename = base_name + '.apd'
index = 1
# WARNING: Decompyle incomplete
