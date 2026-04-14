# Source Generated with Decompyle++
# File: tmpnvkmavtc.marshal (Python 3.11)

setting_name = f'''Channel{channel_id}_{subchannel_index}_Port'''
port = read_int_setting(self.settings, setting_name, None)
return self._validate_port(port)
