# Source Generated with Decompyle++
# File: tmp79u4uypk.marshal (Python 3.11)

interval = datetime.timedelta(minutes = self.preferences.archive_interval)
output_config = OutputConfig(compression_level = self.preferences.compression_level, base_name = None, base_directory = self.preferences.base_dir, device_directory = True, date_dir_structure = True, datetime_filename = True, roll_over_interval = interval, upload_marker = self.preferences.upload_enabled)
stream_settings = StreamSettings(auto_rgb = self.preferences.auto_rgb, response_time = self.device_prefs.response_time, buffer_time = self.device_prefs.buffer_time, timeout = self.device_prefs.stream_timeout, default_output_config = output_config)
calc_settings = CalcSettings(channel_interval = self.preferences.update_timer_interval / 1000, plot_interval = self.preferences.graph_timer_interval / 1000, fft_interval = self.preferences.graph_timer_interval / 1000, downsample = self.preferences.downsample)
return (stream_settings, calc_settings)
